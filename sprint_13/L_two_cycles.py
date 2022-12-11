from typing import List, Tuple


def read_input() -> Tuple[List[int], int]:
    _ = input()
    nums_list = list(map(int, input().strip().split()))
    price = int(input())
    return nums_list, price


def get_cycle(arr, price, left, right):
    if right <= left:
        return -1
    mid = (left + right) // 2
    if price <= arr[mid] and (arr[mid - 1] < price or mid == 0):
        return mid + 1
    elif price <= arr[mid]:
        return get_cycle(arr, price, left, mid)
    else:
        return get_cycle(arr, price, mid + 1, right)


def main():
    nums_list, price = read_input()
    left, right = 0, len(nums_list)
    day1 = get_cycle(nums_list, price, left, right)
    day2 = get_cycle(nums_list, price*2, left, right)
    print(day1, day2)


if __name__ == '__main__':
    main()
