def sqrt(y, eps=10**(-5)):
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
    
    return num