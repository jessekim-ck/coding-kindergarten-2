# https://www.acmicpc.net/problem/1110

n = int(input())

i = 0
_n = n
while True:
    i += 1
    if _n < 10:
        _n = _n*10 + _n
    else:
        _n = (_n%10)*10 + (_n%10 + _n//10)%10
    if _n == n:
        break
print(i)
