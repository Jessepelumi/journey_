# Implementation of Dijkstra's Algorithm

# Edge class
class Edge:
    def __init__(self, weight, start, target):
        self.weight = weight
        self.start = start
        self.target = target

# Node class
class Node:
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.predecesor = None
        self.neighbors = []
        self.min_dist = float("inf")

    def __lt__(self, other):
        return self.min_dist < other.min_dist
