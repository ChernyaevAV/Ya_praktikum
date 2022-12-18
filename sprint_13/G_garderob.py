
def counting_sort(array, k):
    counted_values = [0] * k
    for value in array:
        counted_values[value] += 1

    index = 0
    for value in range(k):
        for amount in range(1, counted_values[value]+1):
            array[index] = value
            index += 1
    return array


def main():
    k = int(input())
    unsorted_list = list(map(int, input().strip().split()))
    print(*counting_sort(unsorted_list, 3))


if __name__ == '__main__':
    main()
