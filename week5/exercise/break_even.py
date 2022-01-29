a, b, c = input().split(" ")
a, b, c = int(a), int(b), int(c)

if c == b:
    print("-1")
    exit()

x = int(a/(c - b))
if x < 0:
    print("-1")
else:
    print(x + 1)