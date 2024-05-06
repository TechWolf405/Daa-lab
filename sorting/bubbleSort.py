import random

# Function to perform bubble sort on the given array
def bubble_sort(arr, size):
    # Base case: if the size of the array is 1, it is already sorted
    if size == 1:
        return
    
    # Traverse through the size-1 elements of array 
    # (as last element will get automatically sorted, we don't need to perform sort on last elemnt)
    # and swap adjacent elements if they are in the wrong order
    for i in range(size-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]

    # Recursively call bubble_sort with a reduced size
    bubble_sort(arr, size-1)

# Input: Get the size of the array from the user
size = int(input("Enter size of array : "))

# Generate an array of random integers between 0 and 100 using list comprehension
arr = [random.randint(0, 100) for _ in range(size)]
print(f"\nArray : {arr}")

# Call the bubble_sort function to sort the array
bubble_sort(arr, size)

# Output: Display the sorted array
print(f"\nSorted Array : {arr}")
