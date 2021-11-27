import time


print("Hello")
start_time = time.time()  # 초 단위로 현재 시간을 리턴하는 함수
print(start_time)

time.sleep(5)
print("...world!")
end_time = time.time()
print(end_time)

time_gap = end_time - start_time
print(f"Time elapsed: {time_gap:.4f}")
