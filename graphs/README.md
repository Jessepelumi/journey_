# Graph Data Structure

A **Graph** is a non-linear data structure consisting of **vertices** (nodes) connected by **edges**. It models pairwise relationships between objects.

## Real-world Examples

- Social networks (users as vertices, friendships as edges)
- Road networks (cities as vertices, roads as edges)
- Web pages (pages as vertices, hyperlinks as edges)
- Flight routes (airports as vertices, flights as edges)

## Key Terminology

- **Vertex (Node)**: A fundamental unit representing an entity
- **Edge**: A connection between two vertices
- **Degree**: Number of edges incident to a vertex
  - **In-degree**: Number of edges pointing to a vertex (directed graphs)
  - **Out-degree**: Number of edges pointing from a vertex (directed graphs)
- **Path**: A sequence of vertices connected by edges
- **Cycle**: A path that starts and ends at the same vertex
- **Connected Graph**: A graph where there's a path between every pair of vertices
- **Weight**: A value assigned to an edge (used in weighted graphs)

## Types of Graphs

### By Direction

| Type | Description |
|------|-------------|
| **Undirected** | Edges have no direction (bidirectional) |
| **Directed** | Edges have direction (arrows) — also called **Digraph** |

### By Weight

| Type | Description |
|------|-------------|
| **Unweighted** | All edges have equal weight (or no weight) |
| **Weighted** | Edges have associated values (e.g., distance, cost) |

### By Density

| Type | Description |
|------|-------------|
| **Sparse** | Few edges relative to vertices |
| **Dense** | Many edges relative to vertices |

## Graph Representations

### Adjacency Matrix
A 2D array where `matrix[i][j]` indicates an edge between vertices i and j.
- Space: **O(V²)**
- Good for dense graphs

### Adjacency List
A list where each vertex stores its connected neighbors.
- Space: **O(V + E)**
- Good for sparse graphs

## Common Operations

- **Add Vertex**: Insert a new vertex
- **Add Edge**: Connect two vertices
- **Remove Vertex**: Delete a vertex and its edges
- **Remove Edge**: Delete an edge
- **Search**: Find if a vertex exists
- **Get Neighbors**: Find all adjacent vertices
- **Get Edge Weight**: Retrieve weight of an edge (weighted graphs)

## Graph Traversals

### Depth First Search (DFS)
Explores as far as possible along each branch before backtracking.
- Uses a **stack** (or recursion)
- Time: **O(V + E)**

### Breadth First Search (BFS)
Explores all neighbors at the current depth before moving deeper.
- Uses a **queue**
- Time: **O(V + E)**

## Time Complexity

| Operation | Adjacency Matrix | Adjacency List |
|-----------|------------------|----------------|
| Add Vertex | O(V²) | O(1) |
| Add Edge | O(1) | O(1) |
| Remove Vertex | O(V²) | O(E) |
| Remove Edge | O(1) | O(1) |
| Search | O(V) | O(V) |
| Get Neighbors | O(V) | O(degree) |

## Common Algorithms

- **Dijks tra's Algorithm**: Shortest path in weighted graphs
- **Bellman-Ford**: Shortest path with negative weights
- **Floyd-Warshall**: All-pairs shortest path
- **Topological Sort**: Ordering in DAGs
- **BFS/DFS**: Traversal and search
- **Kruskal's/Prim's**: Minimum spanning tree