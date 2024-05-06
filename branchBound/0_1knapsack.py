class Item:
    def __init__(self, weight, profit, index):
        self.weight = weight
        self.profit = profit
        self.index = index
        self.ratio = profit / weight  # Calculate profit-to-weight ratio for each item

def knapsack_branch_bound(capacity, weights, profits):
    n = len(weights)
    items = []
    # Create Item objects for each item, calculating profit-to-weight ratio
    for i in range(n):
        items.append(Item(weights[i], profits[i], i))

    # Sort items based on their profit-to-weight ratio in descending order
    items.sort(key=lambda x: x.ratio, reverse=True)

    max_profit = 0
    max_profit_included = []  # Store profits of items included in the knapsack
    weights_included = []  # Store weights of items included in the knapsack

    # Calculate upper bound for the maximum possible profit
    def bound(u, current_weight, current_profit):
        if current_weight >= capacity:
            return 0
        max_bound = current_profit
        j = u + 1
        total_weight = current_weight
        # Greedily add items until capacity is reached
        while j < n and total_weight + items[j].weight <= capacity:
            total_weight += items[j].weight
            max_bound += items[j].profit
            j += 1
        # Add fraction of next item if capacity is not fully utilized
        if j < n:
            max_bound += (capacity - total_weight) * items[j].ratio
        return max_bound

    # Recursive function to explore all possible combinations of items
    def knapsack_recursive(u, current_weight, current_profit):
        nonlocal max_profit
        # Update max_profit and included items if a better solution is found
        if current_weight <= capacity and current_profit > max_profit:
            max_profit = current_profit
            max_profit_included.clear()
            weights_included.clear()
            for i in range(u):
                if items[i].index != -1:
                    max_profit_included.append(items[i].profit)
                    weights_included.append(items[i].weight)

        if u == n:
            return

        # Check if adding current item doesn't exceed capacity
        if current_weight + items[u].weight <= capacity:
            knapsack_recursive(u + 1, current_weight + items[u].weight, current_profit + items[u].profit)

        # If adding more items could potentially lead to a better solution, explore that branch
        if bound(u, current_weight, current_profit) >= max_profit:
            items[u].index = -1
            knapsack_recursive(u + 1, current_weight, current_profit)
            items[u].index = u  # Backtrack

    # Start the recursive search from the first item
    knapsack_recursive(0, 0, 0)
    return max_profit, max_profit_included, weights_included

def main():
    # Input number of items, their weights, profits, and knapsack capacity
    n = int(input("Enter the number of items: "))
    weights = []
    profits = []
    for i in range(n):
        weight, profit = map(int, input(f"Enter weight and profit for item {i+1}: ").split())
        weights.append(weight)
        profits.append(profit)
    capacity = int(input("Enter the capacity of the knapsack: "))

    # Find the maximum possible profit and the items included in the knapsack
    max_profit, max_profit_included, weights_included = knapsack_branch_bound(capacity, weights, profits)
    
    # Print the results
    print("Weights included:", " ".join(map(str, weights_included)))
    print("Profits included:", " ".join(map(str, max_profit_included)))
    print("Maximum possible profit:", max_profit)

if __name__ == "__main__":
    main()
