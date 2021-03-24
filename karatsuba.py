
def Karatsuba(x, y):
    if x < 10 and y < 10:
        return x * y

    max_len = max(len(str(x)), len(str(y)))
    half_len = round(max_len / 2)

    a = x // 10 ** half_len
    b = x % 10 ** half_len
    c = y // 10 ** half_len
    d = y % 10 ** half_len
    ac = Karatsuba(a, c)
    bd = Karatsuba(b, d)
    adbc = Karatsuba(a + b, c + d) - ac - bd

    return (10 ** (2 * half_len)) * ac + (10 ** half_len) * adbc + bd
