def permute(string):
    permutation_list = []
    if len(string) == 1:
        return [string]
    else:
        for char in string:
            [permutation_list.append(char + a)
             for a in permute(string.replace(char, "", 1))]
    return permutation_list


def main():
    letters = {
        2: 'abc',
        3: 'def',
        4: 'ghi',
        5: 'jkl',
        6: 'mno',
        7: 'pqrs',
        8: 'tuv',
        9: 'wxyz'
    }
    buttons = list(map(int, list(input())))

    string = []
    for button in buttons:
        string.append(letters[button])
    print(permute(string))


if __name__ == '__main__':
    main()
