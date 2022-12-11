def memorize(func):
    def wrapper(num):
        memory = {}
        res = memory.get(num)
        if res is None:
            res = func(num)
            memory[num] = res
        return res
    return wrapper


@memorize
def fibo(num):
    if num < 2:
        return 1
    fib1 = fib2 = 1
    for i in range(2, num):
        fib1, fib2 = fib2, fib1 + fib2
    return fib1 + fib2


def get_last_num(num, k):
    return num if len(str(num)) < k else num % (10 ** k)


def main():
    n, k = list(map(int, input().strip().split()))
    print(get_last_num(fibo(n), k))


if __name__ == '__main__':
    main()
