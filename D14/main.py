import os
import time
import IPython.display
from IPython.core.display_functions import clear_output


class Grid:
    def __init__(self, width, height):
        self.grid = {i: {j: Air(i, j) for j in range(height + 1)} for i in range(width + 1)}
        self.part_one = False
        self.part_two = False
        self.boundaries = {
            "x": {
                "min": None,
                "max": None,
            },
            "y": {
                "min": None,
                "max": None,
            },
        }
        self.y_floor = 0
        self.sand_sources = []
        self.sand_grains = []
        self.resting_sand_grains = []
        self.rocks = []

    def create_rock_paths(self, scan):
        for i, line in enumerate(scan):
            prev_x = None
            prev_y = None
            for j, corner in enumerate(line):
                cur_x = int(corner.split(',')[0])
                cur_y = int(corner.split(',')[1])
                self.update_boundaries(cur_x, cur_y)
                if prev_x and prev_x != cur_x:
                    self.draw_path(prev_x, cur_x, cur_y, 'hor', Rock)
                elif prev_y and prev_y != cur_y:
                    self.draw_path(prev_y, cur_y, cur_x, 'ver', Rock)
                prev_x = cur_x
                prev_y = cur_y

    def update_boundaries(self, x, y):
        if self.boundaries['x']['min'] is None:
            self.boundaries['x']['min'] = x
        if self.boundaries['x']['max'] is None:
            self.boundaries['x']['max'] = x
        if self.boundaries['y']['min'] is None:
            self.boundaries['y']['min'] = y
        if self.boundaries['y']['max'] is None:
            self.boundaries['y']['max'] = y

        if x < self.boundaries['x']['min']:
            self.boundaries['x']['min'] = x
        if x > self.boundaries['x']['max']:
            self.boundaries['x']['max'] = x
        if y < self.boundaries['y']['min']:
            self.boundaries['y']['min'] = y
        if y > self.boundaries['y']['max']:
            self.boundaries['y']['max'] = y
            self.y_floor = y + 2

    def draw_path(self, point_a, point_b, axis, dir, obstacle):
        points = [point_a, point_b]
        start = min(points)
        end = max(points)
        if dir == 'hor':
            y = axis
            for x in range(start, end + 1):
                if isinstance(self.grid[x][y], Air):
                    # print(f"Placing horizontally at X: {x}")
                    self.grid[x][y] = obstacle(x, y)
                    self.rocks.append(self.grid[x][y])
                    # print(f"Horizontal line: placing {obstacle} at {x, y}")
        elif dir == 'ver':
            x = axis
            for y in range(start, end + 1):
                if isinstance(self.grid[x][y], Air):
                    # print(f"Placing vertically at Y: {y}")
                    self.grid[x][y] = obstacle(x, y)
                    self.rocks.append(self.grid[x][y])
                    # print(f"Vertical line: placing {obstacle} at {x, y}")
        else:
            print(f"Not a valid direction: {dir}")

    def add_sand_source(self, x, y):
        self.grid[x][y] = SandSpawner(x, y)
        self.update_boundaries(x, y)
        self.sand_sources.append(self.grid[x][y])

    def spawn_sand(self):
        for sand_source in self.sand_sources:
            x, y = sand_source.x, sand_source.y
            self.grid[x][y] = Sand(x, y)
            grid.sand_grains.append(self.grid[x][y])

    def move_sand(self):
        # self.sand_grains.sort(key=lambda grain: grain.y, reverse=True)
        for sand_grain in self.sand_grains:
            sand_grain.move()

    def check_part_one(self, grain):
        grains_at_rest = len(self.resting_sand_grains)
        total_grains = grains_at_rest + len(self.sand_grains)

        if grain.y == grid.boundaries['y']['max'] and not self.part_one:
            grid.part_one = True
            print(f"Part 1: Grain {total_grains} reached boundary, {grains_at_rest} came to rest before it")

    def check_part_two(self, grain):
        grains_at_rest = len(self.resting_sand_grains)
        total_grains = grains_at_rest + len(self.sand_grains)

        if grains_at_rest % 5000 == 0:
            print(f"Grains at rest: {grains_at_rest}")

        if grain.y == 0 and grain.x == 500 and not self.part_two:
            grid.part_two = True
            game_over(f"Part 2: Grain {total_grains} came to stop at (500, 0), {grains_at_rest} came to rest before it")


class Obstacle:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class SandSpawner(Obstacle):
    def __init__(self, x, y):
        super().__init__(x, y)

    def __str__(self):
        return '+'

    def __repr__(self):
        return '+'


class Sand(Obstacle):
    def __init__(self, x, y):
        super().__init__(x, y)

    def move(self):
        old_x, old_y = self.x, self.y
        new_x, new_y = None, None
        air_obj = None

        grid.check_part_one(self)

        if self.y + 1 < grid.y_floor:
            if isinstance(grid.grid[self.x][self.y + 1], Air):
                new_x, new_y = self.x, self.y + 1
                air_obj = grid.grid[new_x][new_y]
            elif isinstance(grid.grid[self.x - 1][self.y + 1], Air):
                new_x, new_y = self.x - 1, self.y + 1
                air_obj = grid.grid[new_x][new_y]
            elif isinstance(grid.grid[self.x + 1][self.y + 1], Air):
                new_x, new_y = self.x + 1, self.y + 1
                air_obj = grid.grid[new_x][new_y]
            else:
                grid.sand_grains.remove(self)
                grid.resting_sand_grains.append(self)
                grid.check_part_two(self)
                grid.spawn_sand()
        else:
            grid.sand_grains.remove(self)
            grid.resting_sand_grains.append(self)
            grid.check_part_two(self)
            grid.spawn_sand()

        if air_obj:
            # print(f"Grain @ {old_x, old_y} trying to move to {new_x, new_y}")
            grid.grid[old_x][old_y] = air_obj
            air_obj.x, air_obj.y = old_x, old_y
            grid.grid[new_x][new_y] = self
            self.x, self.y = new_x, new_y

    def __str__(self):
        return 'o'

    def __repr__(self):
        return 'o'


class Rock(Obstacle):
    def __init__(self, x, y):
        super().__init__(x, y)

    def __str__(self):
        return '#'

    def __repr__(self):
        return '#'


class Air(Obstacle):
    def __init__(self, x, y):
        super().__init__(x, y)

    def __str__(self):
        return '.'

    def __repr__(self):
        return '.'


def game_over(message):
    print(message)
    global game_active
    game_active = False


def output_grid():
    x_range = grid.boundaries['x']['min'] - 5, grid.boundaries['x']['max'] + 5
    y_range = grid.boundaries['y']['min'], grid.boundaries['y']['max'] + 5
    print(f"Drawing x: {x_range} and y: {y_range}")
    for y in range(y_range[0], y_range[1] + 1):
        row = ''
        for x in range(x_range[0], x_range[1] + 1):
            row += f"{grid.grid[x][y]}"
        print(row)


def game_loop():
    # output_grid()
    grid.move_sand()
    # time.sleep(0.1)
    # os.system("clear")


with open('input.txt') as data:
    sensor_scan = [line.strip().split(' -> ') for line in data.readlines()]

grid = Grid(1000, 1000)
grid.create_rock_paths(sensor_scan)
grid.add_sand_source(500, 0)

game_active = True
grid.spawn_sand()

while game_active:
    game_loop()
