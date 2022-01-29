m = int(input())
n = int(input())

prime_numbers = list()
start_idx = None

for i in range(2, n + 1):
    flag = True
    for j in prime_numbers:
        if i % j == 0:
            flag = False
            break
    if flag:
        if start_idx is None and i >= m:
            start_idx = len(prime_numbers)
        prime_numbers.append(i)

if start_idx is None:
    print("-1")
    exit()

print(sum(prime_numbers[start_idx:]))
print(prime_numbers[start_idx])
