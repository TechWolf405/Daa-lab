class Subset:
    def __init__(self, elements, cost):
        # Initialize Subset with elements and cost
        # Remove any element with value 0 from the elements list
        self.elements = [element for element in elements if element != 0]
        self.cost = cost

def minimum_cost_set_cover(sets, universe):
    # Determine the maximum element present in any subset
    max_elements = max(max(s.elements) for s in sets)
    
    # Initialize arrays to keep track of picked elements, result subsets, and uncovered elements
    picked = [False] * max_elements
    result = [False] * len(sets)
    uncovered = list(universe)
    
    # Initialize total cost
    total_cost = 0

    # Repeat until all elements are covered
    while uncovered:
        # Initialize minimum cost and best set index
        min_cost = float('inf')
        best_set = -1

        # Iterate through each subset
        for i, subset in enumerate(sets):
            # Count the number of uncovered elements in the subset
            count = sum(1 for element in subset.elements if not picked[element - 1])
            # Check if the subset covers any uncovered elements and has a lower cost
            if count > 0 and subset.cost < min_cost:
                min_cost = subset.cost
                best_set = i

        # Mark elements of the best set as picked
        for element in sets[best_set].elements:
            if not picked[element - 1]:
                picked[element - 1] = True
                uncovered.remove(element)

        # Add the best set to the result
        result[best_set] = True
        total_cost += min_cost

    # Print the minimum cost of set cover and the selected subsets
    print(f"Minimum cost of set cover: {total_cost}")
    print("Set Cover: {", end='')
    for i, val in enumerate(result):
        if val:
            print(f"S{i + 1}, ", end='')
    print("\b\b}")


# Example usage
sets = [
    Subset([4, 1, 3], 5),
    Subset([2, 5], 10),
    Subset([1, 4, 3, 2], 3)
]
universe = [1, 2, 3, 4, 5]
minimum_cost_set_cover(sets, universe)
