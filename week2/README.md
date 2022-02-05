# 2주차: 함수와 클래스

## 지난 주 복습하기
- 숫자 맞추기 게임!
- 이제 개발자가 되었으니, 깃헙 계정을 생성합니다.

## Function
프로그래밍의 정수는 DRY(Do not Repeat Yourself). 이를 위해 자주 사용하는 코드를 묶어놓은 것이 함수! 알고 있던 그 함수가 맞습니다.

함수의 구성 요소
- name: 미리 짜 놓은 함수를 호출하기 위한 이름입니다.
- parameter: 함수 결과값을 계산을 위해 필요한 값들입니다.
- statement: 함수 결과값을 계산식입니다.
- return: 함수의 결과값입니다.

```python
def name(parameter1, parameter2, ...):
    # some code statement
    return something
```

예를 들어, 다음과 같이 절댓값 함수를 정의할 수 있습니다.

```python
def absolute(number):
    if number >= 0:
        return number
    else:
        return -number
```

다음과 같이 함수의 결과값을 변수에 할당할 수 있습니다.

```python
minus_value = -3
abs_value = absolute(minus_value)
print(abs_value)  # 3
```

### Exercise
- 예제 1: 두 정수 x와 y를 입력받아 x가 크면 True를 출력하고, 그렇지 않으면 False를 출력하는 함수 만들기
- 예제 2: x를 y로 나눈 몫과 나머지를 출력하는 함수 만들기
- 예제 3: 입력받은 리스트의 홀수 원소만 담은 리스트를 출력하는 함수 만들기
- 예제 4: 입력받은 리스트의 짝수 원소만 담은 리스트를 출력하는 함수 만들기


## Class
클래스를 통해 나만의 자료형을 만들 수 있습니다. 자료형은 특정한 형식으로 데이터를 저장하고, 가공하기 위한 거푸집(틀)이라고 볼 수 있습니다. 저번에 배웠던 integer, string, list, dictionary 등 역시 이러한 자료형의 일종입니다. 즉, integer라는 틀이 있고, 이러한 틀을 통해 1, 4, 23, 100, ... 와 같은 객체들을 만드는 것입니다.

클래스의 구성 요소
- class name: 클래스를 호출하기 위한 이름입니다.
- class variable: 클래스의 객체들이 가지는 고유한 데이터. List의 elements를 생각하면 쉽습니다.
- class method: class variable들을 가공하기 위한 함수들. List의 append를 생각하면 쉽습니다.

```python
class Person:
    # 클래스의 생성자 메서드입니다.
    # 모든 클래스는 생성자 메서드를 가지며,
    # 생성자 메서드의 이름은 모두 __init__ 입니다.
    # 생성자 메서드는 객체가 생성될 때 자동으로 실행됩니다.
    def __init__(self, name, height, weight):
        # class variable들을 설정합니다.
        self._name = name
        self._height = height
        self._weight = weight

    # 새로운 메서드입니다.
    # 모든 메서드는 가장 처음에 self를 parameter로 받습니다.
    # self는 해당하는 객체를 가리킵니다.
    def greeting(self):
        print(f"Hello, my name is {self._name}.")
        print(f"My weight is {self._weight}kg.")
        print(f"My height is {self._height}cm.")

    def diet(self):
        self._weight = self._weight - 1

    def eat(self):
        self._weight = self._weight + 1


# 객체는 다음과 같이 생성할 수 있습니다.
# 파라미터로는 생성자(__init__) 메서드의 파라미터를 입력합니다.
jh = Person("Jaehyun Jeong", 160, 48)

# 다음과 같이 메서드를 호출할 수 있습니다. list.append()를 기억하시나요?
jh.greeting()
jh.diet()
jh.greeting()
jh.eat()
jh.greeting()
```

### Exercise
- 예제 1: 떡국 한 그릇 먹을 때마다 나이 한 살씩 먹기
- 예제 2: 학생 벌점 계산기 만들기. 인사하면 +1점, 욕하면 -1점, 학생을 때리면 -2점, 선생님을 때리면 -3점, 노벨상을 받으면 +2점

---
*E.O.D.*