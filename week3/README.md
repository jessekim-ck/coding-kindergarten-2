# 파이썬 3주차

## 지난 주 복습하기
- 리스트의 평균값 구하는 함수 만들기!
- next 메서드를 실행할 때마다 피보나치 수열의 다음 수를 프린트하는 클래스 만들기!

## 파일 I/O
파이썬으로 파일을 읽고 쓸 수 있습니다!

파이썬에서 파일을 읽을 때는 세 가지의 모드가 있습니다.
- write: 파일을 처음부터 다시 씁니다. "w" 로 표기합니다.
- read: 파일을 읽습니다. 파일을 수정할 수 없습니다. "r" 로 표기합니다.
- append: 파일의 끝에 새로운 텍스트를 추가합니다. "a" 로 표기합니다.

파이썬에서 파일을 읽을 때는 통상적으로 다음과 같은 context manager를 사용합니다. I/O 작업이 끝나면 할당된 메모리를 해제하기 위함입니다.
```python
with open(FILENAME, MODE) as f:
    lines = f.readlines()
    f.write("some texts to write.")
```

다음과 같이 새로운 파일을 쓸 수 있습니다.

```python
with open("test.txt", "w") as f:
    f.write("Hello, world!\n")
    f.write("My name is Jesse Kim.")
```

다음과 같이 파일에 텍스트를 추가할 수 있습니다.

```python
with open("test.txt", "a") as f:
    f.write("I love coffee.")
```

다음과 같이 파일을 읽을 수 있습니다.

```python
with open("test.txt", "r") as f:
    lines = f.readlines()
    print(lines)
```

다음과 같이 기존의 파일을 덮어쓸 수 있습니다.

```python
with open("test.txt", "w") as f:
    f.write("This would overwite file.")
```

### Exercise
- 예제 1: 정지용 시인의 시, <호수>를 파이썬으로 써 봅시다. 줄 나눔에 유의하세요!


> 호수  
> 
> 얼굴 하나야  
> 손바닥 둘로  
> 푹 가리지만  
>   
> 보고 싶은 마음  
> 호수만 하니  
> 눈 감을 수 밖에  
> 
> -정지용-

## 라이브러리
개발자들은 이타적인 존재라서, 여러가지 기능들을 만들어 다른 사람들이 쓸 수 있게 세상에 공개합니다. 이를 간단하게 불러와 사용할 수 있습니다!

### 내장 라이브러리: time, datetime, random

```python
import time

time.sleep(5)
print(time.time())
```

```python
import datetime

today = datetime.date.today()
print(today.year)
print(today.month)
print(today.day)
print(today.weekday())
```

```python
import random

print(random.randint(1, 100))
print(random.random())
```

### 외장 라이브러리: openpyxl
외부 라이브러리는 다음과 같이 다운로드할 수 있습니다.
`pip` 는 `Package Installer for Python` 입니다. 이러한 라이브러리를 다운로드받고, 관리해주는 프로그램이라고 생각하면 됩니다!

```bash
pip install LIBRARY_NAME
```

[openpyxl](https://openpyxl.readthedocs.io/en/stable/)은 파이썬에서 엑셀 파일을 읽고, 쓰고, 가공하기 위한 외부 라이브러리입니다.
다음과 같이 다운로드할 수 있습니다.

```bash
pip install openpyxl
```

세상에는 수많은 라이브러리들이 있고, 필요에 따라 검색하고, 익히고, 응용하는 것이 핵심입니다. 원하는 게 있으면 구글에 검색하고, 괜찮아보이는 라이브러리를 선택한 후, documentation을 읽고, 이리저리 테스트해본 후 사용해봐야 합니다!

### Exercise
- 예제 1: 파이썬으로 이메일을 보내봅시다! `jessekim.ck.94@gmail.com` 으로 아무 말이나 보내보세요!

---
*E.O.D.*