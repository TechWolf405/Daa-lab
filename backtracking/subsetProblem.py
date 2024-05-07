# Global variable to track if there exists at least one subset with the given sum
flag = False

# Function to print all subsets of a set with a sum equal to the given sum
def print_subset_sum(i, n, _set, target_sum, subset):
    global flag
    # If the target sum is achieved, print the subset and set the flag to True
    if target_sum == 0:
        flag = True
        print("[", end=" ")
        for element in subset:
            print(element, end=" ")
        print("]", end=" ")
        return
    
    # Base case: If all elements are traversed or target sum is not reached, return
    if i == n:
        return
    
    # Recur for next element without including current element in the subset
    print_subset_sum(i + 1, n, _set, target_sum, subset)
    
    # Recur for next element after including current element in the subset
    if _set[i] <= target_sum:
        subset.append(_set[i])
        print_subset_sum(i + 1, n, _set, target_sum - _set[i], subset)
        subset.pop()

# Driver code
if __name__ == "__main__":
    n = int(input("Enter number of elements : "))
    _set = []
    # Input elements of the set
    for i in range(n):
        num = int(input(f"Enter element {i+1} : "))
        _set.append(num)
    target_sum = int(input("Enter the sum : "))
    subset = []
    print("Output : ")
    # Call the function to print subsets with the given sum
    print_subset_sum(0, n, _set, target_sum, subset)
    print()
    # If no subset with the given sum is found, print a message
    if not flag:
        print("There is no such subset")


# manan Kher
def subset_sum_recursive(nums, k, index, current_sum, subset, all_subsets):
    if current_sum == k:
        all_subsets.append(subset[:])
        return
    
    if current_sum > k or index == len(nums):
        return
        
    
    subset.append(nums[index])
    subset_sum_recursive(nums, k, index + 1, current_sum + nums[index], subset, all_subsets)
    
    subset.pop()
    subset_sum_recursive(nums, k, index + 1, current_sum, subset, all_subsets)

def subset_sum(nums, k):
    all_subsets = []
    subset_sum_recursive(nums, k, 0, 0, [], all_subsets)
    return all_subsets

def main():
    nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    k = 150
    subsets = subset_sum(nums, k)
    for subset in subsets:
        print(subset)

if __name__=='__main__':
    main()