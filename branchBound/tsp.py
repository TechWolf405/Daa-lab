import numpy as np

def tsp(adj_matrix):
    n = len(adj_matrix)
    min_path = []
    min_weight = float('inf')

    def calculate_path_weight(path):
        weight = 0
        for i in range(n - 1):
            weight += adj_matrix[path[i]][path[i+1]]
        weight += adj_matrix[path[-1]][path[0]]
        return weight

    def calculate_lower_bound(path):
        lb = 0
        for i in range(n):
            if i not in path:
                lb += min(adj_matrix[i][j] for j in range(n) if j not in path)
        return lb

    def branch_and_bound(current_vertex, remaining_vertices, current_path, current_weight):
        nonlocal min_path, min_weight

        if len(remaining_vertices) == 0:
            current_weight += adj_matrix[current_vertex][current_path[0]]
            if current_weight < min_weight:
                min_weight = current_weight
                min_path = current_path[:]
            return

        for v in remaining_vertices:
            new_remaining = [vertex for vertex in remaining_vertices if vertex != v]
            new_path = current_path + [v]
            new_weight = current_weight + adj_matrix[current_vertex][v]
            lb = calculate_lower_bound(new_path)

            if lb + new_weight < min_weight:
                branch_and_bound(v, new_remaining, new_path, new_weight)

    branch_and_bound(0, list(range(1, n)), [0], 0)
    return min_path, min_weight

# Example usage
adj_matrix = np.array([[0, 10, 15, 20],
                        [10, 0, 35, 25],
                        [15, 35, 0, 30],
                        [20, 25, 30, 0]])

optimal_path, optimal_distance = tsp(adj_matrix)
print("Optimal Path:", optimal_path)
print("Optimal Distance:", optimal_distance)