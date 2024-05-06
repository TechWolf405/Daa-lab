from timeit import default_timer as timer
import random

total_swaps = 0
total_comparisons = 0

def printTime(s, e):
    time_taken = e - s
    print(f"Time taken : {time_taken}")

def arr_using_uid(roll):   
    r = roll
    arr = [r+(r+1)*i for i in range(10)]
    random.shuffle(arr)
    lower = 0
    upper = len(arr)-1

    return arr, lower, upper


def partition(arr, lb, ub):
    pivot = arr[lb]
    start = lb+1
    end = ub
    swaps = 0
    comparisons = 0

    while start <= end:
        while start <= end and arr[start] <= pivot:
            start += 1
            comparisons += 1
        
        while arr[end] > pivot:
            end -= 1
            comparisons += 1
        
        if start < end:
            arr[start], arr[end] = arr[end], arr[start]
            swaps += 1
    
    arr[lb], arr[end] = arr[end], arr[lb]
    swaps += 1

    return end, swaps , comparisons

def quic_sort(arr, lb, ub):
    global total_swaps, total_comparisons
    if lb<ub:
        loc, swaps, comparisons = partition(arr, lb, ub)
        quic_sort(arr, lb, loc-1)
        quic_sort(arr, loc+1, ub)

        total_swaps += swaps
        total_comparisons += comparisons


def merge(arr, lb, mid, ub):
    i = lb
    j = mid+1
    k = lb
    global total_swaps, total_comparisons
    brr = [0]*(ub+1)

    while i<=mid and j<=ub:
        if arr[i] < arr[j]:
            brr[k] = arr[i]
            i += 1
        else:
            brr[k] = arr[j]
            j += 1
            total_swaps += mid - i + 1
        total_comparisons += 1
        k += 1

    while i <= mid:
        brr[k] = arr[i]
        i += 1
        k += 1

    while j <= ub:
        brr[k] = arr[j]
        j += 1
        k += 1

    for index in range(lb, ub+1):
        arr[index] = brr[index]

def merge_sort(arr, lb, ub):
    global total_swaps, total_comparisons

    if lb<ub:
        mid = (lb + ub)//2
        merge_sort(arr, lb, mid)
        merge_sort(arr, mid+1, ub)
        merge(arr, lb, mid, ub)


def printArr(arr):
    print(f"Sorted array : {arr}")
    print(f"Total number of swaps required : {total_swaps}")
    print(f"Total number of comparisons required : {total_comparisons}")

def print_merge_sorting(arr, lb, ub):
    print(f"Array : {arr}")
    global total_swaps, total_comparisons 
    total_comparisons = 0
    total_swaps = 0
    start = timer()
    merge_sort(arr, lb, ub)
    end = timer()
    printArr(arr)
    printTime(start, end)

def print_quic_sorting(arr, lb, ub):
    print(f"Array : {arr}")
    global total_swaps, total_comparisons 
    total_comparisons = 0
    total_swaps = 0
    start = timer()
    quic_sort(arr, lb, ub)
    end = timer()
    printArr(arr)
    printTime(start, end)


while True:
    print("\n=======MERGE SORT AND QUICK SORT=========\n")
    user_arr = []
    best_arr = []
    worst_arr = []
    lb = 0
    ub = 0
    user_input = input("1. Input your choice of array\n2. Input array using roll no\nEnter your choice (1/2) : ")
    if user_input == '1':
        size = int(input("Enter the size(no of elements) in the array : "))
        for i in range(size):
            element = int(input(f"Enter element {i+1} : "))
            user_arr.append(element)
        lb = 0
        ub = len(user_arr) - 1
    elif user_input == '2':
        roll_no = int(input("Enter your roll no : "))
        user_arr, lb, ub = arr_using_uid(roll_no)
    else:
        print("Invalid choice\n")
        continue
    
    best_arr = sorted(user_arr)
    worst_arr = sorted(user_arr, reverse=True)
    choice = input("\n------ALGORITHM-----\n1. Merge sort \n2. Quick sort \nWhich algorithm you want to test? : ")
    if choice == '1':
        print("\n------MERGE SORT------")
        print("\nAverage Case - ")
        print_merge_sorting(user_arr, lb, ub)
        print("\nBest Case - ")
        print_merge_sorting(best_arr, lb, ub)
        print("\nWorst Case - ")
        print_merge_sorting(worst_arr, lb, ub)
    else:
        print("\n------QUICK SORT------")
        print("\nAverage Case - ")
        print_quic_sorting(user_arr, lb, ub)
        print("\nBest Case - ")
        print_quic_sorting(best_arr, lb, ub)
        print("\nWorst Case - ")
        print_quic_sorting(worst_arr, lb, ub)

    shall_exit = input("\nDo you want to go again? Enter 'Y' for YES or 'N' for NO : ").lower()
    if shall_exit == 'y':
        continue
    else:
        exit()