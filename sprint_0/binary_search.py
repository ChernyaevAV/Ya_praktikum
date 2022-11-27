import sys
import datetime


def binary_search(same_list, item):
    time_start = datetime.datetime.now()
    sys.stdout.write(time_start.strftime("%Y-%m-%d %H:%M:%S"),)
    sys.stdout.write("\n")
    low = 0
    high = len(same_list) - 1
    count = 0

    while low <= high:
        count += 1

        mid = (low + high) // 2
        guess = same_list[mid]
        if guess == item:
            time_finish = datetime.datetime.now()
            sys.stdout.write(time_finish.strftime("%Y-%m-%d %H:%M:%S"))
            sys.stdout.write("\n")
            sys.stdout.write(str(time_finish - time_start))
            sys.stdout.write("\n")
            return mid, count
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = range(100000000)
print(binary_search(my_list, 150001))