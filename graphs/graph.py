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
        if v not in self.dict:
            return []

        visited = set()
        queue = deque([v]) # double ended queue (O(1) pop operation)
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
        # Time complexity: O(V+E) -> V (no. of vertices), E (no. of edges)
        # Space O(V)

    def dfs(self, v):
        if v not in self.dict:
            return []
        
        visited = set()
        stack = [v]
        result = []

        visited.add(v)

        while stack:
            current = stack.pop()

            if current not in visited:
                visited.add(current)
                result.append(current)

                for n in self.dict[current]:
                    stack.append(n)

        return result
        # Time complexity: O(V+E) -> V (no. of vertices), E (no. of edges)
        # Space O(V)

    # Topological sort
    # Helper function
    def topological_sort_helper(self, v, visited: list, stack: list):
        visited.append(v)

        for n in self.dict[v]:
            if n not in visited:
                self.topological_sort_helper(n, visited, stack)

        stack.insert(0, v)

    def topological_sort(self):
        visited = []
        stack = []

        for k in self.dict:
            if k not in visited:
                self.topological_sort_helper(k, visited, stack)

        return stack
    
    # Single Source Shortest Path Problems
    # BFS
    # Dijkstra's Algorithm
    # Bellman Ford Algorithm

    # BFS SSSP
    def bfs(self, start, end):
        queue = deque([start])
        parent_map = {start: None}

        while queue:
            node = queue.popleft()

            if node == end:
                path = []
                while node is not None:
                    path.append(node)
                    node = parent_map[node]
                return path[::-1]

            for adjacent in self.dict.get(node, []):
                if adjacent not in parent_map:
                    parent_map[adjacent] = node
                    queue.append(adjacent)

        return None

# Usage
graph = Graph()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_vertex("D")
graph.add_edge("D", "C")
graph.add_edge("D", "B")

# graph.remove_vertex("B")

result = graph.bfs("A")

print(result)
print(graph.topological_sort())
print(graph.dict)
