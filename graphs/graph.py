# Graph implementation using adjacency list

from collections import deque

class Graph:
    def __init__(self, dict=None):
        if dict is None:
            dict = {}
        self.dict = dict

    # Add vertex
    def add_vertex(self, v):
        if v not in self.dict:
            self.dict[v] = []
            return True
        return False

    # Add edge
    def add_edge(self, v1, v2):
        if v1 not in self.dict:
            self.add_vertex(v1)
        if v2 not in self.dict:
            self.add_vertex(v2)
        if v2 not in self.dict[v1]:
            self.dict[v1].append(v2)
        if v1 not in self.dict[v2]:
            self.dict[v2].append(v1)

    # Remove edge
    def remove_edge(self, v1, v2):
        remove = False

        if v1 in self.dict and v2 in self.dict[v1]:
            self.dict[v1].remove(v2)
            remove = True
        if v2 in self.dict and v1 in self.dict[v2]:
            self.dict[v2].remove(v1)
            remove = True

        return remove
    
    # Remove vertex
    def remove_vertex(self, v):
        if v not in self.dict:
            return False
        
        for n in self.dict[v]:
            self.dict[n].remove(v)

        del self.dict[v]

        return True
    
    # Graph traversal
    def bfs(self, v):
        visited = set()
        queue = deque([v])
        result = []

        visited.add(v)

        while queue:
            current = queue.popleft()
            result.append(current)

            for n in self.dict[current]:
                if n not in visited:
                    visited.add(n)
                    queue.append(n)

        return result
    

# Usage
graph = Graph()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_edge("A", "B")

graph.remove_vertex("B")

print(graph.dict)
