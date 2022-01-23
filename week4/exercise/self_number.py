# https://www.acmicpc.net/problem/4673

def d(n):
    out = n
    for i in str(n):
        out += int(i)
    return out

a = 10000
self_numbers = list(range(1, a + 1))
for i in range(1, a + 1):
    n = d(i)
    try:
        self_numbers.remove(n)
    except:
        pass

for s in self_numbers:
    print(s)
