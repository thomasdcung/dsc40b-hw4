import random


def knn_distance(arr, q, k):
    
    dists = [(abs(x - q), x) for x in arr]

    target_index = k - 1
    _quickselect(dists, 0, len(dists) - 1, target_index)

    distance, point = dists[target_index]
    return (distance, point)