# id: 75971035

from typing import List, Optional


def get_nearest_null(homes_list: List[int]) -> List[int]:
    zero_idx: Optional[int] = None
    res: List[int] = [0] * len(homes_list)
    for idx, house_num in enumerate(homes_list):
        if house_num == 0:
            if zero_idx is None:
                res[0:idx] = res[0:idx][::-1]
            else:
                node_idx, rem = divmod(idx + zero_idx, 2)
                res[node_idx + 1: idx] = res[zero_idx + 1:node_idx + rem][::-1]
            zero_idx = idx
        else:
            res[idx] = idx + 1 if zero_idx is None else idx - zero_idx
    return res


def read_input() -> List[int]:
    n = int(input())
    homes_list = list(map(int, input().strip().split()))
    return homes_list


def main():
    homes_list = read_input()
    print(" ".join(map(str, get_nearest_null(homes_list))))


if __name__ == '__main__':
    main()

# assert get_nearest_null([0, 1, 4, 9, 0]) == [0, 1, 2, 1, 0]
# assert get_nearest_null([0, 7, 9, 4, 8, 20]) == [0, 1, 2, 3, 4, 5]
# assert get_nearest_null([0, 1]) == [0, 1]
# assert get_nearest_null([0, 2, 0]) == [0, 1, 0]
# assert get_nearest_null([0, 7, 9, 0, 8, 20]) == [0, 1, 1, 0, 1, 2]
# assert get_nearest_null([98, 0, 10, 77, 0, 59, 28, 0, 94]) == [1, 0, 1, 1, 0, 1, 1, 0, 1]
# assert get_nearest_null([5, 1, 7, 9, 2, 0]) == [5, 4, 3, 2, 1, 0]
