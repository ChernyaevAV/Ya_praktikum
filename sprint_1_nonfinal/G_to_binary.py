def to_binary(number: int) -> str:

    if number == 0:
        return 0

    binary_num = ''
    while number > 0:
        binary_num += str(number % 2)
        number //= 2
    return binary_num[::-1]


def read_input() -> int:
    return int(input().strip())


print(to_binary(read_input()))
