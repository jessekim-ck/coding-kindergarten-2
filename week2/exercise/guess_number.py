import random  # random 이라는 파이썬 내장 라이브러리를 임포트합니다.


random_number = random.randint(1, 100)  # 1에서 100 사이의 임의의 정수를 생성하여 저장합니다.

num = 101
while num != random_number:
    num = int(input("숫자를 입력하세요: "))
    if num < random_number:
        print("너무 작습니다.")
    elif num > random_number:
        print("너무 큽니다.")
    else:
        print("맞췄습니다.")
