#5
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


#6
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


# cd 10str\ 16str
def main(arr):
    r4 = int(arr[2][1]) & 0b111
    r3 = int(arr[1][1]) & 0b1
    r1 = int(arr[0][1]) & 0b1111
    res = (r4 << 7) | (r3 << 6) | (r1 << 0)
    return res


# tr 16str\ 10str
def main(number):
    num = int(number, 16)
    g1 = (num >> 0) & 0b11111111
    g2 = (num >> 8) & 0b111
    g3 = (num >> 11) & 0b111111
    result = (g2 << 23) | (g3 << 17) | (g1 << 9)
    return str(result)


# tr 10str \ 10str
def main(s):
    i = int(s)
    L1 = 0b11111111 & i
    L3 = 0b11 & (i >> 17)
    L4 = 0b111111111 & (i >> 19)
    result = (L4 << 19) | (L3 << 8) | L1
    return str(result)


# cd slovar 10str\ 10str
def main(n):
    s1 = int(n['S1'])
    s2 = int(n['S2'])
    s3 = int(n['S3'])
    s4 = int(n['S4'])
    s5 = int(n['S5'])
    s6 = int(n['S6'])
    r = (((s6 << 5) | s5) << 10) | s4
    r = (((r << 5) | s3) << 1) | s2
    return str((r << 2) | s1)


# tr int\ 10str
def main(num):
    v1 = (num >> 0) & 0b111111
    v2 = (num >> 6) & 0b1
    v3 = (num >> 7) & 0b111111
    result = int((v1 << 7) | (v2 << 6) | (v3 << 0))
    return str(result)


# dc 10str\ kort int
def main(x):
    x = int(x)
    b1 = x & 0b1
    b3 = (x >> 11) & 0b11
    b4 = (x >> 13) & 0b1111_1
    b5 = (x >> 18) & 0b1111
    result = (b1, b3, b4, b5)
    return result


# cd slov int \ 10str
def encode(fields):
    mask1 = 2 ** 9 - 1
    mask2 = (2 ** 5 - 1) << 9
    mask4 = (2 ** 11 - 1) << 15
    mask5 = (2 ** 8 - 1) << 25
    mask6 = (2 ** 2 - 1) << 33
    n1 = fields.get('N1', 0) & mask1
    n2 = (fields.get('N2', 0) << 9) & mask2
    n4 = (fields.get('N4', 0) << 15) & mask4
    n5 = (fields.get('N5', 0) << 25) & mask5
    n6 = (fields.get('N6', 0) << 33) & mask6
    encoded = n1 | n2 | n4 | n5 | n6
    return str(encoded)


def main(fields):
    return encode(fields)


# cd slov 10 str\ 16str
def main(d):
    d1 = bin(int(d['Q1']))[2:].zfill(8)
    d2 = bin(int(d['Q2']))[2:].zfill(2)
    d3 = bin(int(d['Q3']))[2:].zfill(5)
    d4 = bin(int(d['Q4']))[2:].zfill(4)
    d5 = bin(int(d['Q5']))[2:].zfill(1)
    d6 = bin(int(d['Q6']))[2:].zfill(6)
    return (hex(int(d6 + d5 + d4 + d3 + d2 + d1, 2)))


# 88888888888
# -1 \ 0 spisok par
def main(x):
    x = x.replace('.do', '') \
        .replace('.end', '') \
        .replace('<:', '') \
        .replace('variable', '') \
        .replace('list', '') \
        .replace('(', '') \
        .replace(')', '') \
        .replace('\n', '') \
        .replace(' ', '')
    x_parts = x.split(';:>')
    x_parts.pop(-1)
    x_parts1 = [i.split('<-') for i in x_parts]
    result = []
    for i in x_parts1:
        result.append((i[0], i[1].split(';')))
    return result


# slovar
def main(x):
    x = x.replace('(', '') \
        .replace(')', '') \
        .replace('var', '') \
        .replace('\n', '') \
        .replace(' ', '') \
        .replace('|', '')
    x_parts = x.split(';,')
    x_parts.pop(-1)
    x_parts1 = [i.split('::=') for i in x_parts]
    result = {}
    for i in x_parts1:
        result[i[0]] = i[1]
    return result
#1000000
class MealyError(Exception):
    pass


class StateMachine:
    def __init__(self):
        self.state = 'A'

    def spin(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        if self.state == 'C':
            self.state = 'D'
            return 4
        if self.state == 'D':
            self.state = 'E'
            return 5
        if self.state == 'B':
            self.state = 'E'
            return 3
        if self.state == 'E':
            self.state = 'F'
            return 6
        raise MealyError('spin')

    def punch(self):
        if self.state == 'B':
            self.state = 'C'
            return 1
        if self.state == 'E':
            self.state = 'A'
            return 7
        if self.state == 'F':
            self.state = 'G'
            return 9
        raise MealyError('punch')

    def stand(self):
        if self.state == 'B':
            self.state = 'G'
            return 2
        if self.state == 'E':
            self.state = 'G'
            return 8
        raise MealyError('stand')


def main():
    return StateMachine()


def raises(func, error):
    output = None
    try:
        output = func()
    except Exception as e:
        assert type(e) == error
    assert output is None


def test():
    o = main()
    assert o.spin() == 0
    assert o.punch() == 1
    assert o.spin() == 4
    assert o.spin() == 5
    assert o.punch() == 7
    assert o.spin() == 0
    assert o.spin() == 3
    assert o.spin() == 6
    assert o.punch() == 9
    o = main()
    assert o.spin() == 0
    assert o.stand() == 2
    o = main()
    assert o.spin() == 0
    assert o.spin() == 3
    assert o.stand() == 8
    raises(lambda: o.stand(), MealyError)
    raises(lambda: o.punch(), MealyError)
    raises(lambda: o.spin(), MealyError)
