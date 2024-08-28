import numpy as np

class Node:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.closed = False
        self.is_obstacle = self.random_obstacle()
        self.parent = None
        self.cost = np.inf
        self.heuristic_cost = np.inf

    def random_obstacle(self):
        return np.random.rand() < 0.15

    def successors(self, node_map):
        next_nodes = []
        for (i, j) in np.array([[self.i, self.j+1], [self.i, self.j-1], [self.i+1, self.j], [self.i-1, self.j]]):
            if self.valid(i,j, node_map):
                #print(i, j, "valid")
                next_nodes.append(node_map[i][j])
        return next_nodes
    @staticmethod
    def valid(i, j, node_map):
        width = len(node_map)
        height = len(node_map[0])
        if i < 0 or j < 0 or i >= width or j >= height:
            return False
        if node_map[i][j].is_obstacle:
            return False
        return True

    def distance(self, position):
        x = position[0]
        y = position[1]
        return np.abs(self.i - x) + np.abs(self.j - y)
    
class Solver:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.node_map = [[None for _ in range(height)] for _ in range(width)]
        for i in range(width):
            for j in range(height):
                self.node_map[i][j] = Node(i, j)

    def solve(self, start_position, goal_position):
        list_of_nodes = []
        start_node = self.node_map[start_position[0]][start_position[1]]
        start_node.cost = 0
        start_node.heuristic_cost = start_node.distance(goal_position)
        list_of_nodes.append(start_node)
        while len(list_of_nodes) > 0:
            current_node = self.find_next_node(list_of_nodes)
            #print(current_node.i, current_node.j,"check cloed")
            list_of_nodes.remove(current_node)
            while current_node.closed:
                #print(current_node.i, current_node.j)
                current_node = self.find_next_node(list_of_nodes)
                #print(current_node.i, current_node.j,"check cloed")
                list_of_nodes.remove(current_node)
            if (current_node.i, current_node.j) == goal_position:
                return self.find_path(current_node)
            current_node.closed = True
            for successor in current_node.successors(self.node_map):
                if not successor.closed:
                    if  successor.heuristic_cost > current_node.cost + 1 + successor.distance(goal_position):
                        successor.cost = current_node.cost + 1
                        successor.heuristic_cost = successor.distance(goal_position) + successor.cost
                        successor.parent = current_node
                        list_of_nodes.append(successor)
                    
    def find_path(self, node):
        path = []
        while node.parent:
            path.append((node.i, node.j))
            node = node.parent
        path.append((node.i, node.j))
        path.reverse()
        return path
    
    def get_map(self, path):
        map = [[self.node_map[i][j].is_obstacle for j in range(self.height)] for i in range(self.width)]
        for (i, j) in path:
            map[i][j] = 2
        return map
    
    @staticmethod
    def find_next_node(list_of_nodes):
        current_node = list_of_nodes[0]
        if len(list_of_nodes) == 1:
            return current_node
        for node in list_of_nodes:
            if node.heuristic_cost < current_node.heuristic_cost:
                current_node = node
        return current_node
    
    def set_obstacles(self, obstacles_map):
        for i in range(self.width):
            for j in range(self.height):
                self.node_map[i][j].is_obstacle = obstacles_map[i][j]
