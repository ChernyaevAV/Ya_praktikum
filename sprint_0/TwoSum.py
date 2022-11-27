from typing import List, Tuple, Optional


def two_sum(arr: List[int], target_sum: int) -> Optional[Tuple[int, int]]:
    for i in range(len(arr)):
        first_elem = arr[i]
        for j in range(i + 1, len(arr)):
            second_elem = arr[j]
            if first_elem + second_elem == target_sum:
                return first_elem, second_elem
    return None


def twosum_with_sort(arr: List[int], target_sum: int) -> Optional[Tuple[int, int]]:
    arr.sort()

    left = 0
    right = len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target_sum:
            return arr[left], arr[right]
        if current_sum < target_sum:
            left += 1
        else:
            right -= 1
    return None


def twosum_extra_ds(arr: List[int], target_sum: int) -> Optional[Tuple[int, int]]:
    previous = set()

    for first_elem in arr:
        second_elem = target_sum - first_elem
        if second_elem in previous:
            return first_elem, second_elem
        else:
            previous.add(first_elem)

    return None


def read_input() -> Tuple[List[int], int]:
    n = int(input())
    _arr = list(map(int, input().strip().split()))
    _target_sum = int(input())
    return _arr, _target_sum


def print_result(result: Optional[Tuple[int, int]]) -> None:
    if result is None:
        print(None)
    else:
        print(" ".join(map(str, result)))


arr, target_sum = read_input()
# print_result(two_sum(arr, target_sum))
# print_result(twosum_with_sort(arr, target_sum))
print_result(twosum_extra_ds(arr, target_sum))
