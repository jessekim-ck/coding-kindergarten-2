# 1과 10000사이의 자연수 중 소수 구하기

prime_numbers = list()

for i in range(2, 10001):
    flag = True
    for j in prime_numbers:
        if i % j == 0:
            flag = False
            break
    if flag:
        prime_numbers.append(i)

print(prime_numbers)
