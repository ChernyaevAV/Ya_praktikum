# def find_smallest(arr):
#     smallest = arr[0]
#     smallest_idx = 0
#     for i in range(1, len(arr)):
#         if arr[i] < smallest:
#             smallest = arr[i]
#             smallest_idx = i
#     return smallest_idx
#
#
# def selection_sort(arr):
#     new_arr = []
#     for i in range(len(arr)):
#         smallest = find_smallest(arr)
#         new_arr.append(arr.pop(smallest))
#     return new_arr
#
#
# print(*selection_sort([5, 3, 6, 2, 10]))


letters = {
    2: 'abc',
    3: 'def',
    4: 'ghi',
    5: 'jkl',
    6: 'mno',
    7: 'pqrs',
    8: 'tuv',
    9: 'wxyz'
}

print(list(zip(letters[2], letters[3])))