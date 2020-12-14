def insertionSort(arr):

    arr_len = len(arr)

    for i in range(1, arr_len):

        key = arr[i]

        while arr[i-1] > key and i > 0:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i = i - 1
    return arr


arr = [5, 2, 4, 6, 1, 3]
print(arr)

print(insertionSort(arr))
