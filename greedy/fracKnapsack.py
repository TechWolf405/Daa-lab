class Item:
    def __init__(self, index, weight, value):
        self.index = index
        self.weight = weight
        self.value = value
        self.ratio = value / weight

def fractional_knapsack(weights, values, capacity):
    n = len(weights)
    items = [Item(i, weights[i], values[i]) for i in range(n)]
    
    items.sort(key=lambda x: x.ratio, reverse=True)
    
    max_value = 0
    x = [0] * n
    
    for item in items:
        if capacity >= item.weight:
            x[item.index] = 1
            max_value += item.value
            capacity -= item.weight
        else:
            fraction = capacity / item.weight
            x[item.index] = fraction
            max_value += fraction * item.value
            break
    
    return max_value, x

def main():
    weights = [2, 3, 5, 7, 1, 4, 1]
    values = [10, 5, 15, 7, 6, 18, 3]
    capacity = 15
    max_value, x = fractional_knapsack(weights, values, capacity)
    print("Maximum value achievable:", max_value)
    print("Fractional knapsack array:", x)

if __name__=='__main__':
    main()