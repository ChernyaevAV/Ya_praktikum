def gen_bracket_seq(n, prefix, left=0, right=0):
    if left == n and right == n:
        print(prefix)
    else:
        if left < n:
            gen_bracket_seq(n, prefix + '(', left + 1, right)
        if right < left:
            gen_bracket_seq(n, prefix + ')', left, right + 1)


def main():
    n = int(input())
    gen_bracket_seq(n, prefix='')


if __name__ == '__main__':
    main()
