# ID: 79761153

def broken_search(nums, target) -> int:
    left = 0
    right = len(nums) - 1
    index = -1
    while left <= right:
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]:
            if nums[left] < target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        else:
            if nums[mid] < target < nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return index


def main():
    arr = list(map(int, input().strip().split()))
    target = int(input())
    print(broken_search(arr, target))


if __name__ == '__main__':
    main()


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6

    arr = [5, 1]
    assert broken_search(arr, 1) == 1

    arr = [3, 5, 6, 7, 9, 1, 2]
    assert broken_search(arr, 4) == -1

    arr = [1, 2, 3, 5, 6, 7, 9, 0]
    assert broken_search(arr, 3) == 2

    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]
    assert broken_search(arr, 1) == 0
