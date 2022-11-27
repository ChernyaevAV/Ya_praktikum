import sys

home_addreses = [0, 1, 4, 9, 2]

right_null = home_addreses[:]

print(*right_null)

for item in right_null:
    sys.stdout.write(str(item) + ' ')
