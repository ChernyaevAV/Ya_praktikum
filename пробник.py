def insertion_sort(array):
    for i in range(len(array)):
        item_to_insert = array[i]
        j = i
        while j > 0 and item_to_insert < array[j-1]:
            array[j] = array[j-1]
            j -= 1
        array[j] = item_to_insert
        print(f'step {i}, sorted {i+1} elements: {array}')


def insertion_sort2(array):
    for i in range(len(array)):
        item_to_insert = array[i]
        j = i
        while j > 0 and item_to_insert < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
            j -= 1
        print(f'step {i}, sorted {i+1} elements: {array}')


def select_sort(array):
    for i in range(len(array) - 1):
        for k in range(i+1, len(array)):
            if array[k] < array[i]:
                array[k], array[i] = array[i], array[k]
        print(f'step {i}, sorted {i+1} elements: {array}')


# insertion_sort([11, 2, 9, 7, 1])
# insertion_sort2([11, 2, 9, 7, 1])
select_sort([11, 2, 9, 7, 1])
