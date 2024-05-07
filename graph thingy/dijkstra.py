# Function to find the vertex with the minimum distance among the vertices that have not been visited yet
def min_distance(distances, visited):
    min_dist = float('infinity')  # Initialize the minimum distance to infinity
    min_vertex = None  # Initialize the vertex with the minimum distance
    for vertex, dist in enumerate(distances):  # Iterate through each vertex and its distance
        if not visited[vertex] and dist < min_dist:  # If the vertex is not visited and its distance is less than the current minimum distance
            min_dist = dist  # Update the minimum distance
            min_vertex = vertex  # Update the vertex with the minimum distance
    return min_vertex  # Return the vertex with the minimum distance

# Function to perform Dijkstra's algorithm to find the shortest distances from a source vertex to all other vertices in the graph
def dijkstra(graph, source):
    num_vertices = len(graph)  # Get the number of vertices in the graph
    distances = [float('infinity')] * num_vertices  # Initialize distances to all vertices as infinity
    distances[source] = 0  # Set the distance from the source vertex to itself as 0
    visited = [False] * num_vertices  # Initialize all vertices as not visited
    
    for _ in range(num_vertices):  # Iterate through all vertices
        current_vertex = min_distance(distances, visited)  # Find the vertex with the minimum distance among unvisited vertices
        visited[current_vertex] = True  # Mark the current vertex as visited
        
        # Update distances to neighboring vertices if a shorter path is found
        for neighbor, weight in enumerate(graph[current_vertex]):  # Iterate through neighbors of the current vertex
            if not visited[neighbor] and weight > 0:  # If the neighbor is not visited and there is a connection (weight > 0)
                new_distance = distances[current_vertex] + weight  # Calculate the new distance to the neighbor
                if new_distance < distances[neighbor]:  # If the new distance is shorter than the current distance to the neighbor
                    distances[neighbor] = new_distance  # Update the distance to the neighbor
    
    return distances  # Return the shortest distances from the source vertex to all other vertices

# Example graph representation
graph = [  
    [0, 10, 5, 0, 0],  
    [0, 0, 0, 1, 0],  
    [0, 3, 0, 9, 2],  
    [0, 0, 0, 0, 0],  
    [2, 0, 0, 6, 0],  
]  

# Source vertex
source = 0

# Run Dijkstra's algorithm
distances = dijkstra(graph, source)

# Print the distances from the source vertex
print("Vertex\tDistance from Source")
for vertex, distance in enumerate(distances):
    print(f"{vertex}\t{distance}")


# mannnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    visited = {node: False for node in graph}
    pq = [(0, start)]
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        if visited[current_node]:
            continue
        visited[current_node] = True
        for neighbor, weight in graph[current_node].items():
            if not visited[neighbor]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))
    return distances

graph = {
    'A': {'B': 4, 'E': 8},
    'B': {'A': 4, 'C': 8, 'E': 11},
    'C': {'B': 8, 'D': 7, 'G': 4, 'I': 2},
    'D': {'C': 7, 'G': 14, 'H': 9},
    'E': {'A': 8, 'B': 11, 'F': 1, 'I': 7},
    'F': {'E': 1, 'G': 2, 'I': 6},
    'G': {'C': 4, 'D': 14, 'F': 2, 'H': 10},
    'H': {'D': 9, 'G': 10},
    'I': {'C': 2, 'E': 7, 'F': 6}
}
start_node = 'A'

print(graph['A'].items())

shortest_distances = dijkstra(graph, start_node)
# for node, distance in shortest_distances.items():
#     print(f"{node} : {distance}")

# print(shortest_distances.keys())
# print(shortest_distances.values())
# for node, distance in shortest_distances.items():
#     print("To", node + ":", distance)