

class Parent:
    def __init__(self):
        self._a = "a"
    
    def say_hello(self):
        print("hello!")


class Child(Parent):
    def __init__(self):
        super().__init__()

child = Child()

child.say_hello()  # 상속된 메서드
print(child._a)  # 상속된 클래스 변수
