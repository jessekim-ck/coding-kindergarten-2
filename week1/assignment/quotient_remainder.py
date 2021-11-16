# x를 y로 나눈 몫과 나머지 구하기

x = 38
y = 5

quotient = 0
while True:
    if x - y >= 0:
        x = x - y
        quotient += 1
    else:
        break

print(f"{quotient}*{y} + {x}")
