from timeit import default_timer as timer
import random


def arr_using_uid(roll):   
    r = roll
    arr = [r+(r+1)*i for i in range(10)]
    random.shuffle(arr)
    return arr

def insertion_sort(arr):
    print(f"Array : {arr}")
    start  = timer()
    swap_count = 0
    comparison_count = 0
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i-1
        while j >= 0 and arr[j]>temp:
            arr[j+1] = arr[j]
            swap_count += 1
            j -= 1
        
        comparison_count += 1
        arr[j+1] = temp

    end = timer()
    total = (end - start)
    print(f"Sorted array : {arr}")
    print(f"Total number of swaps required : {swap_count}")
    print(f"Total number of comparisons required : {comparison_count}")
    print("Total time:- " + str(total))
           

def selection_sort(arr):
    print(f"Array : {arr}")
    start  = timer()
    swap_count = 0
    comparison_count = 0
    for i in range(len(arr)-1):
        min = i
        # j = i+1
        for j in range(i+1, len(arr)):
            if arr[j]<arr[min]:
                min = j

            comparison_count += 1
        
        if min != i:
            arr[i], arr[min] = arr[min], arr[i]
            swap_count += 1

    end = timer()
    total = (end - start)
    print(f"Sorted array : {arr}")
    print(f"Total number of swaps required : {swap_count}")
    print(f"Total number of comparisons required : {comparison_count}")
    print("Total time:- " + str(total))
    

while True:
    print("\n=======SELECTION SORT AND INSERTION SORT=========\n")
    user_arr = []
    best_arr = []
    worst_arr = []
    user_input = input("1. Input your choice of array\n2. Input array using roll no\nEnter your choice (1/2) : ")
    if user_input == '1':
        size = int(input("Enter the size(no of elements) in the array : "))
        for i in range(size):
            element = int(input(f"Enter element {i+1} : "))
            user_arr.append(element)
    elif user_input == '2':
        roll_no = int(input("Enter your roll no : "))
        user_arr = arr_using_uid(roll_no)
    else:
        print("Invalid choice\n")
        continue
    
    best_arr = sorted(user_arr)
    worst_arr = sorted(user_arr, reverse=True)
    choice = input("\n------ALGORITHM-----\n1. Insertion sort \n2. Selection sort \nWhich algorithm you want to test? : ")
    if choice == '1':
        print("\n------INSERTION SORT------")
        print("1. Average Case - ")
        insertion_sort(user_arr)
        print("\n2. Best Case -")
        insertion_sort(best_arr)
        print("\n3. Worst Case -")
        insertion_sort(worst_arr)
    else :
        print("\n------SELECTION SORT------")
        print("1. Average Case - ")
        selection_sort(user_arr)
        print("\n2. Best Case -")
        selection_sort(best_arr)
        print("\n3. Worst Case -")
        selection_sort(worst_arr)

    shall_exit = input("\nDo you want to go again? Enter 'Y' for YES or 'N' for NO : ").lower()
    if shall_exit == 'y':
        continue
    else:
        exit()

