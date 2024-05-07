def vertex_cover(graph):
    vertex_cover = set()  # Initialize an empty set to store the vertex cover

    # Iterate over all edges in the graph
    while graph:
        # Choose an arbitrary edge and add its vertices to the cover
        u, v = graph.pop()
        vertex_cover.add(u)
        vertex_cover.add(v)

        # Remove all edges incident to the chosen vertices
        to_remove = set()
        for edge in graph:
            if u in edge or v in edge:
                to_remove.add(edge)
        graph -= to_remove

    return vertex_cover

# Example usage
if __name__ == "__main__":
    # Example graph represented as a set of edges
    graph = {('A', 'B'), ('B', 'C'), ('B', 'D')}

    # Find the vertex cover using the approximation algorithm
    cover = vertex_cover(graph)
    print("Vertex cover:", cover)
