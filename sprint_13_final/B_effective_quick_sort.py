# ID: 79866754


def quicksort(array, start, end):
    if end - start > 1:
        p = partition(array, start, end)
        quicksort(array, start, p)
        quicksort(array, p + 1, end)


def partition(array, left, right):
    pivot = array[left]
    l = left + 1
    r = right - 1

    while True:
        while l <= r and array[l] <= pivot:
            l += 1
        while l <= r and array[r] >= pivot:
            r -= 1

        if l <= r:
            array[l], array[r] = array[r], array[l]
        else:
            array[left], array[r] = array[r], array[left]
            return r


def read_data():
    n = int(input())
    res = [(-int(completed), int(penalty), name)
           for name, completed, penalty
           in [input().strip().split() for _ in range(n)]]
    return res


def main():
    arr = read_data()
    quicksort(arr, 0, len(arr))

    for item in arr:
        print(item[-1])


if __name__ == '__main__':
    main()
