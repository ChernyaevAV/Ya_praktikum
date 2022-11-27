# a,b = map(int, input().split())
# print(a+b)


# with open('input.txt', 'r') as in_file:
#     a, b = map(int, in_file.readline().split())
#     with open('output.txt', 'w') as out_file:
#         out_file.write(str(a + b))

import sys

len_array = int(sys.stdin.readline().strip())
array1 = sys.stdin.readline().strip().split()
array2 = sys.stdin.readline().strip().split()

result = []
for i in range(len_array):
    result.append(array1[i])
    result.append(array2[i])

print(*result)




