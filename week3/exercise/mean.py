def mean(li):
    _length = 0
    _sum = 0
    for i in li:
        _length += 1
        _sum += i
    return _sum / _length


print(mean([1, 2, 3, 4, 5]))
