def knapsack(val, wt, n, c):
    # Initialize a 2D array to store intermediate results
    k = [[0 for _ in range(c+1)] for _ in range(n+1)]
    
    # Populate the array using the dynamic programming approach
    for i in range(0, n+1):
        for w in range(0, c+1):
            # Base case: if there are no items or no capacity
            if i == 0 or w == 0:
                k[i][w] = 0
            # If the current item's weight is less than or equal to the current capacity
            elif wt[i] <= w:
                k[i][w] = max(val[i] + k[i-1][w-wt[i]], k[i-1][w])
            # If the current item cannot be included due to its weight
            else:
                k[i][w] = k[i-1][w]
    
    # Print the table with labels
    print(f"\nTable (k) - Rows: Items, Columns: Capacity\n")
    # Print column headers
    print(f"{'Capacity ':<8}", end="")
    for i in range(c+1):
        print(f"{i:<4}", end="")
    print("\n" + "-"*(8 + 4*(c+1)))

    # Print table content
    for i in range(n+1):
        print(f"Item {i:<4}", end="")
        for w in range(c+1):
            print(f"{k[i][w]:<4}", end="")
        print()

    print("\nMaximum value/profit :", k[n][c])
    print("Objects included in the knapsack are :\n")

    # Trace back to find the objects included in the knapsack
    i = n
    j = c
    max_weight = 0
    while i > 0 and j > 0:
        if k[i][j] == k[i-1][j]:
            print(f"{i} - not included.")
            i = i-1
        else:
            print(f"object {i} - was included in the knapsack.")
            max_weight = max_weight + wt[i]
            i = i-1
        j = j - wt[i]
    print(f"\nFinal weight of knapsack : {max_weight}")


# Get user input for knapsack parameters
capacity = int(input("Enter the capacity of the knapsack: "))
no_of_objects = int(input("Enter number of objects: "))
value = [0]
weight = [0]
for i in range(1, no_of_objects+1):
    wt = int(input(f"Enter the weight of object {i}: "))
    val = int(input("Enter its value/profit: "))
    weight.append(wt)
    value.append(val)

# Print input values
print(f"Weights = {weight}")
print(f"Profit = {value}")

# Call the knapsack function
knapsack(value, weight, no_of_objects, capacity)



# class Item:
#     def __init__(self, weight, value):
#         self.weight = weight
#         self.value = value




# def knapsack(weights, values, capacity):
#     n = len(weights)
#     dp = [[0] * (capacity + 1) for _ in range(n + 1)]

#     for i in range(1, n + 1):
#         for w in range(1, capacity + 1):
#             if weights[i - 1] <= w:
#                 dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
#             else:
#                 dp[i][w] = dp[i - 1][w]

#     return dp

# def constructList(dp, weights, values, capacity):
#     n = len(weights)
#     x = [0]*n
#     profit = dp[n][capacity]

#     for i in range(n,0,-1):
#         if profit in dp[i] and profit not in dp[i-1]:
#             x[i-1] = 1
#             profit = profit-values[i-1]

#     return x

# def main():
#     weights = [2, 3, 4, 5]
#     values = [1, 2, 5, 6]
#     items = [Item(5,6), Item(3,2), Item(4,5), Item(2, 1)]
#     items.sort(key = lambda x: x.weight)
#     for item in items:
#         print(item.weight)
#     capacity = 8
#     dp = knapsack(weights, values, capacity)
#     x = constructList(dp, weights, values, capacity)
#     print(x)

# if __name__=='__main__':
#     main()
