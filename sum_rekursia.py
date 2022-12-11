def sum_with_rekursiv(array):
    if len(array) == 0:
        return 0
    return array[0] + sum_with_rekursiv(array[1:])


array = range(11)
print(sum_with_rekursiv(array))
