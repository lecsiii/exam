# Задание 5
import math


def main(x):
    sum = 0
    n = len(x)
    x = [0] + x
    for i in range(1, n + 1):
        a = 41 * x[n + 1 - math.ceil(i / 4)] ** 2
        b = 77 * x[n + 1 - math.ceil(i / 4)] ** 3
        sum += 60 * (a - b) ** 6
    return 2 * sum


# Задание 6
def php(x, left, right):
    if x[4] == 'PHP':
        return right
    return left


def year_1(x, left, right):
    if x[0] == 1999:
        return left
    return right


def year_2(x, left, middle, right):
    if x[1] == 1988:
        return left
    if x[1] == 2006:
        return middle
    return right


def main(x):
    if x[2] == 'SHEN':
        if x[3] == 'MASK':
            return year_1(x, php(x, 0, 1), 2)
        if x[3] == 'JULIA':
            return 3
    else:
        if x[3] == 'MASK':
            return php(x, 4, 5)
        if x[3] == 'JULIA':
            return php(x, year_2(x, 6, 7, 8), year_1(x, 9, 10))


# 7
# decode 10str \ kort 10str
def main(s):
    i = int(s)
    c1 = 0b1111111 & i
    c2 = 0b1111111111 & (i >> 7)
    c3 = 0b11 & (i >> 17)
    c5 = 0b111111111 & (i >> 27)
    return tuple(map(str, (c1, c2, c3, c5)))


# docode 16str \ kort 10str
def main(num):
    num = int(num, 16)
    x6 = str((num >> 20) & 0b1)
    x5 = str((num >> 17) & 0b111)
    x3 = str((num >> 6) & 0b1111)
    x2 = str((num >> 1) & 0b11111)
    x1 = str((num >> 0) & 0b1)
    return (x1, x2, x3, x5, x6)


# dc int \ kort int
def main(n):
    n = int(n)
    A = ((int(n) >> 0) & int(
        (32 - (8 - 0 + 1)) * '0' + (8 - 0 + 1) * '1',
        2))
    B = ((int(n) >> 9) & int(
        (32 - (15 - 9 + 1)) * '0' + (15 - 9 + 1) * '1',
        2))  # << b[3]
    C = ((int(n) >> 16) & int(
        (32 - (16 - 16 + 1)) * '0' + (16 - 16 + 1) * '1',
        2))  # << b[3]
    D = ((int(n) >> 17) & int(
        (32 - (25 - 17 + 1)) * '0' + (25 - 17 + 1) * '1',
        2))
    E = ((int(n) >> 26) & int(
        (32 - (29 - 26 + 1)) * '0' + (29 - 26 + 1) * '1',
        2))
    ans = (A, B, C, D, E)
    return ans


# tr 16str\ int
def main(num):
    num = int(num, 16)
    x5 = (num >> 29) & 0b11111
    x4 = (num >> 24) & 0b11111
    x3 = (num >> 14) & 0b1111111111
    x2 = (num >> 10) & 0b1111
    x1 = (num >> 0) & 0b1111111111
    res = (x1 << 24) | (x5 << 19) | (x3 << 9) | (x4 << 4) | (x2 << 0)
    return int(res)


# cd kort int\ 16str
def main(x):
    x = [i for i in x]
    e1 = 0b0000_0000_0
    e2 = x[0] & 0b1111_1111_1
    e3 = x[1] & 0b11
    e4 = x[2] & 0b11
    result = e1 | (e2 << 9) | (e3 << 18) | (e4 << 20)
    return str(hex(result))

