# ID: 77924009


def evaluate(a, b, expression):
    exp_dict = {
        '+': a + b,
        '-': a - b,
        '*': a * b,
        '/': a // b if b != 0 else None,
    }

    return exp_dict[expression]


def calculate(exp_str: str) -> [int, str]:
    exp_str = exp_str.split()
    operations = '+-*/'
    stack = []
    result = None
    expression = None
    for elem in exp_str:
        if elem not in operations:
            stack.append(elem)

        else:
            b = int(stack.pop())
            a = int(stack.pop())
            expression = elem
            result = evaluate(a, b, expression)
            stack.append(result)
    if expression is None:
        return int(''.join(stack.pop()))
    return result


def main():
    exp_str = input().strip()
    print(calculate(exp_str))


if __name__ == '__main__':
    main()

    # assert calculate('2 1 + 3 *') == 9
    # assert calculate('7 2 + 4 * 2 +') == 38
    # assert calculate('123') == 123
    # assert calculate('123 2') == 2
    # assert calculate('2 1 2 / *') == 0
