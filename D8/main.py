with open('input.txt', 'r') as input_data:
    height_map = [line.strip() for line in input_data.readlines()]

width = len(height_map[0])
height = len(height_map)
# print(width, height)
# Origin (0, 0) will be the top-left tree. Bottom right in a 10x10 grid then is (9, 9)

trees = []


class Tree:
    def __init__(self, x_cor, y_cor, tree_height):
        self.x = x_cor
        self.y = y_cor
        self.height = tree_height
        self.info = (self.x, self.y, self.height)
        self.scenic = None

    def __repr__(self):
        return f"({self.x}, {self.y}, {self.height}m)"

    def is_visible(self, tree_list):
        if self.x == 0 or self.y == 0 or self.x == width - 1 or self.y == height - 1:
            # print(f"Tree {self.info} visible because on border")
            return True
        trees_north = []
        trees_east = []
        trees_south = []
        trees_west = []
        for tree in tree_list:
            if tree.y == self.y:
                # East
                if tree.x > self.x:
                    trees_east.append(tree)
                # West
                elif tree.x < self.x:
                    trees_west.append(tree)
            elif tree.x == self.x:
                # North
                if tree.y < self.y:
                    trees_north.append(tree)
                # South
                elif tree.y > self.y:
                    trees_south.append(tree)

        north_visible = True
        for tree in trees_north:
            if self.height <= tree.height:
                north_visible = False
        if north_visible: return True

        east_visible = True
        for tree in trees_east:
            if self.height <= tree.height:
                east_visible = False
        if east_visible: return True

        south_visible = True
        for tree in trees_south:
            if self.height <= tree.height:
                south_visible = False
        if south_visible: return True

        west_visible = True
        for tree in trees_west:
            if self.height <= tree.height:
                west_visible = False
        if west_visible: return True

        return False

    def get_scenic(self, tree_list):
        trees_north = []
        trees_east = []
        trees_south = []
        trees_west = []

        for tree in tree_list:
            if tree.y == self.y:
                # East
                if tree.x > self.x:
                    trees_east.append(tree)
                # West
                elif tree.x < self.x:
                    trees_west.append(tree)
            elif tree.x == self.x:
                # North
                if tree.y < self.y:
                    trees_north.append(tree)
                # South
                elif tree.y > self.y:
                    trees_south.append(tree)

        trees_north.sort(key=lambda tree: tree.y, reverse=True)
        trees_east.sort(key=lambda tree: tree.x)
        trees_south.sort(key=lambda tree: tree.y)
        trees_west.sort(key=lambda tree: tree.x, reverse=True)

        north_view = 0
        east_view = 0
        west_view = 0
        south_view = 0

        for tree in trees_north:
            if tree.height >= self.height:
                north_view += 1
                break
            north_view += 1

        for tree in trees_east:
            if tree.height >= self.height:
                east_view += 1
                break
            east_view += 1

        for tree in trees_south:
            if tree.height >= self.height:
                south_view += 1
                break
            south_view += 1

        for tree in trees_west:
            if tree.height >= self.height:
                west_view += 1
                break
            west_view += 1

        self.scenic = north_view * east_view * south_view * west_view
        return self.scenic


def get_tree_at(x, y):
    for tree in trees:
        if tree.x == x and tree.y == y:
            return tree
    else:
        return None


# loop through map and create trees
for y in range(height):
    for x in range(width):
        # print(f"Treeheight at ({x}, {y}) is: {height_map[y][x]}")
        tree = Tree(x, y, height_map[y][x])
        trees.append(tree)

# Part 1
visible_trees = []
for tree in trees:
    if tree.is_visible(trees):
        visible_trees.append(tree)

print(f"{len(visible_trees)} visible trees.")

# Part 2
highest = 0
for tree in trees:
    value = tree.get_scenic(trees)
    if value > highest:
        highest = value

print(f"Highest scenic value is: {highest}")



