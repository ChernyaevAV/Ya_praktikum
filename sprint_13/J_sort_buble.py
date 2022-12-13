def buble_sort(array):
    if array == sorted(array):
        print(*array)
        return
    for k in range(len(array)-1):
        count = 0
        for i in range(len(array) - 1 - k):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                count += 1
        if count == 0:
            return
        print(*array)


def main():
    _ = input()
    array = list(map(int, input().strip().split()))
    buble_sort(array)


if __name__ == '__main__':
    main()

# assert buble_sort([11, 2, 9, 7, 1]) == [1, 2, 7, 9, 11]
