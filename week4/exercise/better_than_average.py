# https://www.acmicpc.net/problem/4344

n = int(input())

for _ in range(n):
    _input = input().split(" ")
    num_students = int(_input[0])
    
    upper_bound = 100*num_students  # 총점의 최댓값
    lower_bound = 0  # 총점의 최솟값
    inside_band = list()
    
    c = 0
    for s in _input[1:]:
        s = int(s)
        lower_bound += s
        upper_bound = upper_bound - 100 + s
        print(lower_bound, upper_bound)
        if s > upper_bound / num_students:
            c += 1  # 얜 무조건 넘음
        elif s < lower_bound / num_students:
            pass  # 얜 무조건 못 넘음
        else:
            inside_band.append(s)  # 얜 다시 봐야 함
    
    avg = lower_bound / num_students
    print(avg)
    for s in inside_band:
        if s > avg:
            c += 1
            
    print(f"{(c/num_students)*100:.3f}%")