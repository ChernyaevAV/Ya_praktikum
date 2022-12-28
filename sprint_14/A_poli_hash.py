def horner_hash(base, modul, data_string):
    res = 0
    for char in data_string:
        res = (res * base + ord(char)) % modul
    return res


def read_data():
    base = int(input())
    modul = int(input())
    data_string = input()
    return base, modul, data_string


def main():
    base, modul, data_string = read_data()
    print(horner_hash(base, modul, data_string))


if __name__ == '__main__':
    main()
