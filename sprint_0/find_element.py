import time


def my_time_decorator(func):
    def wrapper(*args, **kwargs):
        time_start = time.perf_counter()
        print(func(*args, **kwargs), end=' ')
        time_finish = time.perf_counter()
        print(time_finish - time_start)
    return wrapper


@my_time_decorator
def find_element_linear(numbers, x):
    counter = 0
    for i in range(len(numbers)):
        counter += 1
        if numbers[i] == x:
            return i, counter
    return None


@my_time_decorator
def find_element_binary(numbers, item):
    left = 0
    right = len(numbers) - 1
    counter = 0

    while left <= right:
        counter += 1
        mid = (left + right) // 2
        guess = numbers[mid]
        if guess == item:
            return mid, counter
        if guess > item:
            right = mid - 1
        else:
            left = mid + 1
    return None


list_of_numbers = range(100000000)
X = 9056300

find_element_linear(list_of_numbers, X)
find_element_binary(list_of_numbers, X)
