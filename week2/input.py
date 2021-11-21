
input_string = input("글자를 입력해주세요: ")
print(input_string)
print()

input_maybe_number = input("숫자를 입력해주세요: ")
print(input_maybe_number)
print(type(input_maybe_number))  # input으로 들어온 값은 string data type으로 저장됩니다.
print()

input_number = input("숫자를 입력해주세요: ")
input_number = int(input_number)  # string type의 숫자를 integer type으로 만들어줍니다.
print(input_number)
print(type(input_number))
