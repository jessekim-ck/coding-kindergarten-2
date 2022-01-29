li = list()

try:
    li.remove(3)  # 에러 발생 => except로
    print("This code would not run!")
except Exception as e:
    print("Error occured!")
    print(e)

print("Fin.")
