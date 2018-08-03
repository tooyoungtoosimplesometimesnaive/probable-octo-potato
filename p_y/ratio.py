
def get_ratio(i, m, r):
    if i == 0:
        a = r // 1000000
        b = (r // 1000) % 1000
        c = r % 1000
        # print(str(a) + ',' + str(b) + ',' + str(c))
        if a * 2 == b and a * 3 == c:
            print(str(a) + ',' + str(b) + ',' + str(c))
    else:
        for k in range(1, 10):
            if (1 << k) & m == 0:
                get_ratio(i - 1, (1<<k) | m, 10 * r + k)


if __name__ == '__main__':
    get_ratio(9, 1, 0)

