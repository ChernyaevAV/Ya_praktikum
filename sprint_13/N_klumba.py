
def get_coord_klumb(coord_klumb):
    coord_klumb = sorted(coord_klumb)
    left = coord_klumb[0][0]
    right = coord_klumb[0][1]
    res = [[left, right]]
    for i in range(1, len(coord_klumb)):
        if res[-1][0] <= coord_klumb[i][0] <= res[-1][1]:
            if res[-1][1] < coord_klumb[i][1]:
                res[0][1] = coord_klumb[i][1]
        else:
            res.append([coord_klumb[i][0], coord_klumb[i][1]])
    return res


def pprint(array):
    for item in array:
        print(*item)


def main():
    n = int(input())
    klumbs_coord = [list(map(int, input().strip().split())) for _ in range(n)]
    pprint(get_coord_klumb(klumbs_coord))


if __name__ == '__main__':
    main()
