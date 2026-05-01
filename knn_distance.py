import random


def knn_distance(arr, q, k):

    dists = [(abs(x - q), x) for x in arr]

    target_index = k - 1
    _quickselect(dists, 0, len(dists) - 1, target_index)

    distance, point = dists[target_index]
    return (distance, point)


def _quickselect(arr, left, right, k):
    
    if left >= right:
        return

    pivot_index = random.randint(left, right)
    pivot_index = _partition(arr, left, right, pivot_index)

    if k == pivot_index:
        return
    elif k < pivot_index:
        _quickselect(arr, left, pivot_index - 1, k)
    else:
        _quickselect(arr, pivot_index + 1, right, k)


def _partition(arr, left, right, pivot_index):

    pivot_val = arr[pivot_index]
    
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]

    store = left
    for i in range(left, right):
        if arr[i] < pivot_val:
            arr[i], arr[store] = arr[store], arr[i]
            store += 1

    arr[store], arr[right] = arr[right], arr[store]
    return store
