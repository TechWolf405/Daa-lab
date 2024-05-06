# formula to calculate cost of multiplying matrix

# C[i,j] = min { C[i,k] + C[k+1,j] + d(i-1)*d(k)*d(j)}...where i <= k < j

# Matrix Chain Multiplication using Dynamic Programming

# Function to print the tables
def printTables(matrix):
    print("\t", end="")
    for i in range(len(matrix[0])):
        print(i, end="\t")
    print()
    print("---------" * len(matrix))
    i = 0
    for row in matrix:
        print(i, end="\t")
        i += 1
        for element in row:
            print(element, end="\t")
        print()

# Function to print optimal parenthesization
def printParenthesis(i, j, bracket, matrix_names):
    if i == j:
        print(matrix_names[i - 1], end="")
        return
    print("(", end="")
    printParenthesis(i, bracket[i][j], bracket, matrix_names)
    printParenthesis(bracket[i][j] + 1, j, bracket, matrix_names)
    print(")", end="")

# Matrix Chain Multiplication function
def matrix_multiplication(n, p):
    global s, m
    # Initialize tables
    s = [[0 for _ in range(len(p))] for _ in range(len(p))]
    m = [[0 for _ in range(len(p))] for _ in range(len(p))]
    min = float('inf')
    
    # Loop for computing cost and optimal parenthesization
    for d in range(1, len(p) - 1):
        for i in range(1, len(p) - d):
            j = i + d
            min = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if q < min:
                    min = q
                    s[i][j] = k
            m[i][j] = min

    cost = m[1][len(p) - 1]

    # Print the cost matrix and K table
    print(f"\nCost matrix table (m) :")
    printTables(m)
    print()
    print(f"\nK Table (K value at which cost was minimum) :")
    printTables(s)

    print(f"\n\nOptimal Cost : {cost}")
    print("Optimal Parenthesization : ", end="")
    matrix_names = ['A', 'B', 'C', 'D', 'E']
    printParenthesis(1, len(p) - 1, s, matrix_names)
    print("\n")

# Get input for the number of matrices and their orders
orders = []
no_of_matrix = int(input("Enter the number of matrices : "))
print("Enter the orders of matrices :")
for i in range(no_of_matrix + 1):
    order = int(input(f"Order {i + 1} : "))
    orders.append(order)

# Call the matrix multiplication function
matrix_multiplication(n=no_of_matrix, p=orders)



