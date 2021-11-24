def quotient_remainder(x, y):
    _sum = 0
    n = 0
    while _sum < x - y:
        _sum += y
        n += 1
    return n, x - _sum

