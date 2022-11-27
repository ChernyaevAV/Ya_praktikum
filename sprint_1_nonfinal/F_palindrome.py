
def is_palindrome(line: str) -> bool:

    line = line.lower()
    new_line = ''
    for symbol in line:
        if symbol not in ' ,./!:;':
            new_line += symbol

    if new_line[:] != new_line[::-1]:
        return False
    return True


print(is_palindrome(input().strip()))


