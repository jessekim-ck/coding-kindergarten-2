def sqrt(y, eps=10**(-8)):

    # y가 1보다 크다고 상정하고 제곱근을 구할 예정
    # 따라서 y가 1보다 작다면 역수를 취해준다.
    if y < 0:
        raise RuntimeError("y should be bigger than 0.")
    elif y < 1:
        lt_one = True
        original_y = y
        y = 1 / y
    else:
        lt_one = False

    num = y  # 제곱근이 될 변수
    upper_bound = y  # 제곱근의 upper bound
    lower_bound = 0  # 제곱근의 lower bound

    # upper_bound와 lower_bound의 차이가 매우 작아질 때까지 반복
    while upper_bound - lower_bound >= eps:
        # num의 제곱이 y보다 크면, 제곱근은 지금의 num보다는 작다.
        if num**2 > y:
            upper_bound = num

        # num의 제곱이 y보다 작으면, 제곱근은 지금의 num보다는 크다.
        elif num**2 < y:
            lower_bound = num

        # num을 upper_bound와 lower_bound의 평균으로 업데이트
        num = (upper_bound + lower_bound) / 2

    # 원래 y가 1보다 작았다면, 역수의 제곱근에 원래 y를 곱해줘야 제곱근이 됨.
    if lt_one:
        num = num * original_y
    
    return num


print(sqrt(0.01))
print(sqrt(0.3))
print(sqrt(2))
print(sqrt(13))
print(sqrt(400))