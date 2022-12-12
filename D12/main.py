from heapq import heappop, heappush

class Node:
    def __init__(self, character, coordinates):
        self.height_char = character
        self.start = False
        self.end = False
        self.coordinates = coordinates
        self.height = None

    def get_height(self):
        if self.height_char == 'S':
            self.start = True
            self.height = 0
        elif self.height_char == 'E':
            self.end = True
            self.height = 25
        else:
            self.height = ord(self.height_char.lower()) - 97

    def get_neighbours(self, input_nodes):
        north = operate_tuples(self.coordinates, (0, -1))
        east = operate_tuples(self.coordinates, (1, 0))
        south = operate_tuples(self.coordinates, (0, 1))
        west = operate_tuples(self.coordinates, (-1, 0))
        potential_neighbours = [north, east, south, west]
        self.neighbour_nodes = []
        self.reachable_nodes = []
        for node in input_nodes:
            for potential_neighbour in potential_neighbours:
                if node.coordinates == potential_neighbour:
                    self.neighbour_nodes.append(node)
                    if node.height <= self.height + 1:
                        self.reachable_nodes.append(node)

        # print(f"node @ {self.coordinates} ({self.height_char}) surrounded by {[neighbour.coordinates for neighbour in self.neighbour_nodes]}\n can reach {[reachable.coordinates for reachable in self.reachable_nodes]}")

    def __str__(self):
        if self.start:
            return f"START: {self.height_char} at {self.coordinates} {self.height}m"
        elif self.end:
            return f"END: {self.height_char} at {self.coordinates} {self.height}m"
        return f"{self.height_char} at {self.coordinates} {self.height}m"

    def __repr__(self):
        if self.start:
            return f"START"
        elif self.end:
            return f"END"
        return f"{self.coordinates}"

    def __lt__(self, other):
        self == other


def operate_tuples(left: tuple, right: tuple):
    return left[0] + right[0], left[1] + right[1]


def create_nodes(heightmap):
    nodes = []
    for y, row in enumerate(heightmap):
        for x, char in enumerate(row):
            node = Node(char, (x, y))
            node.get_height()
            nodes.append(node)
    for node in nodes:
        node.get_neighbours(nodes)
        if node.start:
            start_node = node
        elif node.end:
            end_node = node
    return nodes, start_node, end_node


def dijkstra(graph, source, end):
    graph = graph
    visited = {vertex: False for vertex in graph}
    distance = {vertex: 99999 for vertex in graph}
    distance[source] = 0
    previous_nodes = {}

    pq = []

    heappush(pq, (0, source))

    while pq:
        current_distance, current = heappop(pq)
        visited[current] = True

        for neighbour in current.reachable_nodes:
            if not visited[neighbour]:
                new_distance = distance[current] + 1
                if new_distance < distance[neighbour]:
                    distance[neighbour] = new_distance
                    heappush(pq, (new_distance, neighbour))
                    previous_nodes[neighbour] = current
        if current == end_node:
            return previous_nodes, distance
    return previous_nodes, distance


with open('input.txt') as data:
    heightmap = [line.strip() for line in data.readlines()]

nodes, start_node, end_node = create_nodes(heightmap)

a_nodes = [node for node in nodes if node.height == 0]
print(a_nodes)

scenic_shortest = 99999
scenic_start = None
for node in a_nodes:
    previous, dist = dijkstra(nodes, node, end_node)
    if dist[end_node] < scenic_shortest:
        scenic_shortest = dist[end_node]
        scenic_start = node

previous, dist = dijkstra(nodes, start_node, end_node)
print(f"Distance from {start_node} to {end_node} is {dist[end_node]}")
print(f"Lowest scenic distance from {scenic_start} to {end_node} is {scenic_shortest}")

