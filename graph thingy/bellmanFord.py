def bellman_ford(graph, start):
    # Initialize distances for all vertices to infinity
    distances = {vertex: float('inf') for vertex in graph}
    # Set distance of start vertex to 0
    distances[start] = 0
    
    # Relax edges repeatedly |V| - 1 times
    for _ in range(len(graph) - 1):
        # Iterate through all vertices in the graph
        for u in graph:
            # Iterate through all neighboring vertices of u
            for v, weight in graph[u].items():
                # Relax the edge if a shorter path is found
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
                    
    # Check for negative cycles by relaxing edges one more time
    for u in graph:
        for v, weight in graph[u].items():
            # If a shorter path is found, it means there's a negative cycle
            if distances[u] + weight < distances[v]:
                print("Graph contains a negative cycle")
                return None
                
    # Return the shortest distances from the start vertex
    return distances

# Example graph representation as a dictionary
graph = {
    0: {1: 6, 2: 4, 3: 5},
    1: {4: -1},
    2: {1: -2, 4: 3},
    3: {2: -2, 5: -1},
    4: {5: 3},
    5: {}
}

# Source vertex
source = 0

# Run Bellman-Ford algorithm
distances = bellman_ford(graph, source)

# Print the distances from the source vertex
print("Vertex\tDistance from Source")
for vertex, distance in distances.items():
    print(f"{vertex}\t{distance}")


# mannnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
def bellman_ford(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0

    for _ in range(len(graph) - 1):
        for u in graph:
            for v, weight in graph[u].items():
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight

    for u in graph:
        for v, weight in graph[u].items():
            if distances[u] + weight < distances[v]:
                print("Graph contains a negative cycle")
                return None

    return distances

graph = {
    'A': {'B': 6, 'C': 4, 'D': 5},
    'B': {'E': -1},
    'C': {'B': -2, 'E': 3},
    'D': {'C': -2, 'F': -1},
    'E': {'F': 3},
    'F': {}
}

start_node = 'A'
shortest_distances = bellman_ford(graph, start_node)
if shortest_distances:
    print("Shortest distances from node", start_node + ":")
    for node, distance in shortest_distances.items():
        print("To", node + ":", distance)