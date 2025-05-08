#1. Breadth-First Search (BFS) Algorithm:
def bfs(graph, start):
    visited = set()  # Set to keep track of visited nodes
    queue = [start]  # List to act as a queue, initialized with the start node
    
    while queue:
        node = queue.pop(0)  # Dequeue the first element
        if node not in visited:
            print(node, end=" ")  # Print the node as we visit it
            visited.add(node)  # Mark the node as visited
            
            # Add all unvisited adjacent nodes to the queue
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Example graph (Undirected)
graph = {
    'S': ['A', 'B'],
    'A': ['S', 'C', 'D'],
    'B': ['S', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['A', 'B', 'E'],
    'E': ['B', 'D', 'F'],
    'F': ['C', 'E'],
}

# Run BFS starting from 'S'
bfs(graph, 'S')
print("\n")



# 2. Depth-First Search (DFS) Algorithm:
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()  # Initialize the visited set
    
    print(node, end=" ")  # Print the current node
    visited.add(node)  # Mark the current node as visited
    
    # Recursively visit all unvisited adjacent nodes
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Example graph (Undirected)
graph = {
    'S': ['A', 'B'],
    'A': ['S', 'C', 'D'],
    'B': ['S', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['A', 'B', 'E'],
    'E': ['B', 'D', 'F'],
    'F': ['C', 'E'],
}

# Run DFS starting from 'S'
dfs(graph, 'S')