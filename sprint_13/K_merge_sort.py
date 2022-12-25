def merge(arr, lf, mid, rg):
    left = arr[lf:mid]
    right = arr[mid:rg]
    k = lf
    i = j = 0
    while lf + i < mid and mid + j < rg:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    if lf + i < mid:
        while k < rg:
            arr[k] = left[i]
            i += 1
            k += 1

    else:
        while k < rg:
            arr[k] = right[j]
            j += 1
            k += 1
    return arr


def merge_sort(array, left, right) -> None:
    if right - left > 1:
        mid = (left + right) // 2
        merge_sort(array, left, mid)
        merge_sort(array, mid, right)
        return merge(array, left, mid, right)


def main():
    _ = input()
    n = int(input())
    unsort_array = list(map(int, input().strip().split()))
    merge_sort(unsort_array, 0, n)


def test():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    expected = [1, 2, 4, 9, 10, 11]
    assert b == expected
    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0, 6)
    print(c)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected


if __name__ == '__main__':
    main()
