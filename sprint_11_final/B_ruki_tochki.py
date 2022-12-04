# id: 76137558

from typing import List, Dict, Tuple


def get_key_count(keyboard: List[str]) -> Dict[str, int]:
    key_count = {}
    for item in keyboard:
        key_count[item] = key_count.get(item, 0) + 1
    return key_count


def get_key(keyboard: List[str], k: int) -> int:
    sum_balls = 0
    key_count = get_key_count(keyboard)
    for time in range(1, 10):
        time = str(time)
        if 0 < key_count.get(str(time), 0) <= k*2:
            sum_balls += 1

    return sum_balls


def read_input() -> Tuple[List[str], int]:
    k = int(input())
    keyboard = []
    for i in range(4):
       keyboard.extend(list(map(str, input().strip())))
    return keyboard, k


def main():
    keyboard, k = read_input()
    print(get_key(keyboard, k))


if __name__ == '__main__':
    main()
