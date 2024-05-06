def partition(arr, lb, ub):
    pivot = arr[lb]
    start = lb + 1
    end = ub

    while start <= end:
        while start <= end and arr[start] <= pivot:
            start += 1

        while arr[end] > pivot:
            end -= 1

        if start < end:
            arr[start], arr[end] = arr[end], arr[start]

    arr[lb], arr[end] = arr[end], arr[lb]

    return end

def quick_sort(arr, lb, ub):
    if lb < ub:
        loc = partition(arr, lb, ub)
        quick_sort(arr, lb, loc - 1)
        quick_sort(arr, loc + 1, ub)

arr = [11, 10, 13, 14, 12]
lb = 0
ub = len(arr) - 1
quick_sort(arr, lb, ub)
print(arr)
