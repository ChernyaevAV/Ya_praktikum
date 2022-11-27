from typing import List, Tuple


def transpon_matrix(n: int, m: int, matrix: List[List[int]]) -> List[List[int]]:
    trans_matrix = [[0 for j in range(n)] for i in range(m)]
    for i in range(n):
        for j in range(m):
            trans_matrix[j][i] = matrix[i][j]
    return trans_matrix


def read_input() -> Tuple[int, int, List[List[int]]]:
    n = int(input())
    m = int(input())
    matrix = [[0]*m]*n
    for i in range(n):
        matrix[i] = list(map(int, input().strip().split()))
    return n, m, matrix


def pprint(m: int, trans_matrix: List[List[int]]) -> None:
    for i in range(m):
        print(*trans_matrix[i])


def main():
    n, m, matrix = read_input()
    trans_matrix = transpon_matrix(n, m, matrix)
    pprint(m, trans_matrix)


if __name__ == '__main__':
    main()
