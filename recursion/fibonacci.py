# Function to calculate the nth Fibonacci number using recursion
def fib(n):
    # Base case: if n is 0 or 1, return 0
    if n <= 1:
        return 0
    # Base case: if n is 2, return 1
    if n == 2:
        return 1
    
    # Recursive case: return the sum of the (n-2)th and (n-1)th Fibonacci numbers
    return fib(n-2) + fib(n-1)

# Function to print the terms and corresponding Fibonacci numbers
def print_fib(arr, terms):
    print("\tTerms\tfibonacci number")
    # Iterate through the array and print each term and its Fibonacci number
    for n in range(len(arr)):
        print("\t", n+1, "\t", arr[n])

# Input: Get the number of terms from the user
terms = int(input("Enter the number of terms you want to print : "))

# Initialize an empty array to store Fibonacci numbers
arr = []

# Generate Fibonacci numbers for the specified number of terms
for i in range(1, terms+1):
    # Append the Fibonacci number for the current term to the array
    arr.append(fib(i))

# Output: Display the terms and corresponding Fibonacci numbers
print_fib(arr, terms)
