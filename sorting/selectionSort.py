def selection_sort(arr):

    for i in range(0, len(arr)-1):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


arr = [7, 6, 8, 3, 5, 1] 
new_arr = selection_sort(arr)
print(new_arr)   