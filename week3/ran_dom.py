import random


print(random.randint(1, 1000))  # 1 ~ 1000
print(random.random())  # 0 ~ 1


a = 0
b = 0
for _ in range(10000):
    if random.random() < 0.66:
        a += 1
    else:
        b += 1

print(a)
print(b)