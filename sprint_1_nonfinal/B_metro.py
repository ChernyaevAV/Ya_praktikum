def check_parity(a: int, b: int, c: int) -> bool:
    return (all(item % 2 == 0 for item in (a, b, c))
            or all(item % 2 != 0 for item in (a, b, c)))


def print_result(result: bool) -> None:
    if result:
        print("WIN")
    else:
        print("FAIL")


a, b, c = map(int, input().strip().split())
print_result(check_parity(a, b, c))
