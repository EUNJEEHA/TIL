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









## 3. 





## 4. 







