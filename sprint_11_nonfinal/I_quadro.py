def is_power_of_four(number: int) -> bool:

    while number % 4 == 0:
        number //= 4

    if number == 1:
        return True
    return False


print(is_power_of_four(int(input())))
