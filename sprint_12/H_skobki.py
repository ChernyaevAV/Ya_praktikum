def is_correct_bracket_seq(string) -> bool:
    open_bracket = '[({'
    closed_bracket = '])}'
    valid_bracket = ['()', '{}', '[]']
    stack = []

    if not len(string):
        return True
    for char in string:
        if char in open_bracket:
            stack.append(char)
        if char in closed_bracket:
            if len(stack) > 0 and stack[-1] + char in valid_bracket:
                stack.pop()
            else:
                return False
    if len(stack):
        return False
    return True


def main():
    string = input()
    print(is_correct_bracket_seq(string))


if __name__ == '__main__':
    main()

    assert is_correct_bracket_seq('{[()]}') is True
    assert is_correct_bracket_seq('()') is True
    assert is_correct_bracket_seq(')(') is False
    assert is_correct_bracket_seq('(') is False
    assert is_correct_bracket_seq('') is True
    assert is_correct_bracket_seq('()[]') is True
    assert is_correct_bracket_seq('[]()}{') is False
