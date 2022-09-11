def quicksort(lst, start, stop):
    if stop - start > 0:
        pivot, left, right = lst[start], start, stop
        while left <= right:
            while lst[left] < pivot:
                left += 1
            while lst[right] > pivot:
                right -= 1
            if left <= right:
                lst[left], lst[right] = lst[right], lst[left]
                left += 1
                right -= 1
        quicksort(lst, start, right)
        quicksort(lst, left, stop)
    return lst