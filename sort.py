class Sort:
    def bubble_sort(arr):
        arr_len = len(arr)
        for i in range(arr_len):
            for j in range(0, arr_len-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

    def selection_sort(arr):
        arr_len = len(arr)
        for i in range(arr_len):
            min_index = i
            for j in range(min_index+1, arr_len):
                    if arr[min_index] > arr[j]:
                        min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]