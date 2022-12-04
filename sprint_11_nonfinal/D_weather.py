from typing import List


def get_weather_randomness(temperatures: List[int]) -> int:

    if len(temperatures) == 1:
        return 1
    counter = 0
    if temperatures[0] > temperatures[1]:
        counter += 1
    if temperatures[-1] > temperatures[-2]:
        counter += 1

    for i in range(1, len(temperatures)-1):
        if (
                temperatures[i-1] < temperatures[i]
                and temperatures[i+1] < temperatures[i]
        ):
            counter += 1
    return counter


def read_input() -> List[int]:
    n = int(input())
    temperatures = list(map(int, input().strip().split()))
    return temperatures


temperatures = read_input()
print(get_weather_randomness(temperatures))