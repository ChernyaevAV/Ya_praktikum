from typing import List


# def factorize(number: int) -> List[int]:
#     i = 2
#     res = []
#     while i * i <= number:
#         while number % i == 0:
#             res.append(i)
#             number //= i
#         i += 1
#     if number > 1:
#         res.append(number)
#     return res


def factorize2(number: int) -> List[int]:
    divisor = 2
    res = []
    while divisor <= number:
        if number % divisor == 0:
            res.append(divisor)
            number //= divisor
        else:
            divisor += 1

    return res


result = factorize2(int(input()))
print(" ".join(map(str, result)))
