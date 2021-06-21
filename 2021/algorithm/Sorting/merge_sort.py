def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[:mid]

    left_ = merge_sort(left)
    right_ = merge_sort(right)
    return merge_sort(left_, right_)