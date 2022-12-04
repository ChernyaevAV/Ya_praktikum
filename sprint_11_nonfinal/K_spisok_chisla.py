from typing import List, Tuple


def get_sum(number_list: List[int], k: int) -> List[int]:
    temp_str = ''
    for item in number_list:
        temp_str += str(item)
    temp = int(temp_str) + k
    result = []
    while temp > 0:
        result.append(temp % 10)
        temp //= 10
    return result[::-1]


def read_input() -> Tuple[List[int], int]:
    n = int(input())
    number_list = list(map(int, input().strip().split()))
    k = int(input())
    return number_list, k


number_list, k = read_input()
print(" ".join(map(str, get_sum(number_list, k))))