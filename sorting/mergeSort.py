def merge(arr, lb, mid, ub):
    i = lb
    j = mid+1
    k = lb
    brr = [0]*(ub+1)

    while i<=mid and j<=ub:
        if arr[i] < arr[j]:
            brr[k] = arr[i]
            i += 1
        else:
            brr[k] = arr[j]
            j += 1
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
    if lb<ub:
        mid = (lb + ub)//2

        merge_sort(arr, lb, mid)
        merge_sort(arr, mid+1, ub)
        merge(arr, lb, mid, ub)


arr = [7, 5, 4, 3, 2, 1, 0]
lb = 0
ub = len(arr)-1
merge_sort(arr, lb, ub)
print(arr)