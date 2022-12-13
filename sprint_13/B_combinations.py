def permute(buttons):
    num_letters = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    if len(buttons) == 1:
        return list(num_letters[buttons[0]])
    else:
        res = ['']
        for num in buttons:
            letters = num_letters.get(num, '')
            res = [prefix + letter for prefix in res for letter in letters]
        return res


def main():
    buttons = input().strip()
    print(*permute(buttons))


if __name__ == '__main__':
    main()
