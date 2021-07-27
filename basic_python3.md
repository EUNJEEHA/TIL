# BASIC_PYTHON3

## 1. if / for / while

### 1-1. 한 줄 comprehension

* 리스트 컴프리헨션

```python
# 1~5까지의 수를 제곱하여 출력
# 일반 for문
square = []
numbers = [1,2,3,4,5]
for number in numbers:
    square.append(number**2)
print(square)

# 컴프리헨션
numbers = [1,2,3,4,5]
square = [number**2 for number in numbers]
print(square)
```

```python
# 일반 for,if문
square = []
numbers = [1,2,3,4,5]
for number in numbers:
    if number >= 3:
        square.append(number**2)
print(square)

# 컴프리헨션
numbers = [1,2,3,4,5]
square = [number**2 for number in numbers if number >= 3]
print(square)
```

## 2. 입력과 출력

### 2-1. 기본 출력

* print() 함수 안에 문자열을 입력

```python
print("Hello World!")
```

* 두 문자열 사이의 구분값 설정 : sep

```python
print("Best", "python", "book", sep = "-:*:-")
```

* 두 문자열 연결 : +

```python
print("abce" + "efg")
```

* 문자열과 숫자는 더하기 연산자(+)로 연결할 수 없음

```python
name = "Tom"
ID_num = 789
print("name :", name + ", " + "ID_num : ", ID_num)
```

* 줄 바꿔서 출력하기 : \n

```python
print("Tom is my friend.\nHe is Korean.")
```

* 라인 끝 값 지정 : end

```python
print("Tom is my friend.", end = "")
print("He is Korean.")
```

### 2-2. 형식 지정 출력

* 나머지 연산자(%)를 이용

```python
name = "Tom"
age = 25
print("%s은 내 친구야. %i살이지." % (name,age))
```

* 형식 지졍 문자열 :  .format()

```python
animal0 = "cat"
animal1 = "dog"
animal2 = "fox"
print("animals : {0},{1},{2}".format(animal0,animal1,animal2))
```

* 순차적이라면, {N}에 N없이 {}만 써도 가능

```python
animal0 = "cat"
animal1 = "dog"
animal2 = "fox"
print("animals : {},{},{}".format(animal0,animal1,animal2))

# 신기하지만, 헷갈릴 수 있으니 실전에서는 꼭 숫자를 넣자!
```

* 문자 출력 위치 지정

```python
name = "Tom"
age = 10
a = 0.1234567891234
fmt_string = "String: {0}, Integer Number: {1}, Floating Number: {2}"
print(fmt_string.format(name,age,a))
```

* 숫자 출력 형식 지정

```python
a = 0.1234567891234
print("{0:.2f}, {0:.5f}".format(a))
```

### 2-3. input()

```python
myfruit = input("좋아하는 과일은?")
print("당신은 {}을 좋아하는 군요!".format(myfruit))

a = int(input("정사각형의 한 변의 길이는?"))
print("정사각형의 넓이는 {}입니다.".format(a**2))
```

## 3. 파일 읽고 쓰기





## 4. 







