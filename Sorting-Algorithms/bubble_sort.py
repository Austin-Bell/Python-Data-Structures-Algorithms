# Helper function to swap items at indexes
def swap(arr, index_1, index_2):
    temp = arr[index_1]
    arr[index_1] = arr[index_2]
    arr[index_2] = temp


def bubble_sort(arr):
    for itm in arr:
        for idx in range(len(arr) - 1):
            if arr[idx] > arr[idx + 1]:
                swap(arr, idx, idx + 1)
