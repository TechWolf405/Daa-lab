

def insertion_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i -1
        while j>=0 and arr[j]>temp:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp
        

    return arr

arr = []
new_arr = []
arr = [1, 2, 9, 8, 3]
new_arr = insertion_sort(arr)
print(new_arr)

