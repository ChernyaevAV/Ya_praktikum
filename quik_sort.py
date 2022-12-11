from random import sample


def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


arr = [10, 5, 2, -5, 0, 23, -10, 30]
arr2 = sample(range(0, 100), 100)
# print(arr2)
# print(quick_sort(arr2))

assert quick_sort(arr2) == list(range(0, 100))

