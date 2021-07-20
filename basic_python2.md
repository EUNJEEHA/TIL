# BASIC_PYTHON2

## 1. 변수

> 자료를 넣을 수 있는 상자인 변수

* 변수명 생성 규칙
  * 문자, 숫자, 밑줄 기호(_) 사용 가능
  * 숫자로 시작할 수 없다
  * 대소문자 구문
  * 공백 사용 불가
  * 예약어(Reserved word)는 변수명으로 사용 불가
* 상수(Constant variable)
  * 프로그래밍 언어에서 어떤 숫자를 변수에 할당한 후에 프로그램이 끝날 때까지 그 변수의 값을 변경하지 않고 사용하는 경우
  * 한 번 지정한 후 그 값이 변하지 않는 변수

## 2. 문자열

> 문자열은 문자의 나열을 의미하는데, 파이썬에서는 따옴표로 둘러싸인 문자의 집합

```python
string1 = "String Test 1"
string2 = 'String Test 2'
print(string1)
print(string2)
type(string1)
type(string2)
```

* 문자열에 큰 따옴표(")와 작은 따옴표(')를 모두 포함하고 싶거나, 문장을 여러 행을 넣고 싶거나, 입력한 그대로 출력하고 싶을 때

```python
long_string1 = '''[삼중 작은 따옴표를 사용한 예]
파이썬에는 삼중 작은 따옴표와 여러 행의 문자열을 입력할 수 있습니다.
큰 따옴표(")와 작은 따옴표(')도 입력할 수 있습니다.'''
```

* 더하기 연산자(+) : 문자열 끼리 연결

```python
a = 'Enjoy'
b = 'python!'
c = a + b
print(c)
```

* 곱하기 연산자(*) : 곱한 만큼 문자열을 반복

```python
print(a * 3)
```

## 3. 리스트(List)

> 숫자, 문자열, 불 데이터들을 묶어 놓은 것

* 리스트를 만들 때 각 항목의 데이터 타입은 같지 않아도 됨
* 항목은 콤마(,)로 구분
* 대괄호([])안에 아무것도 쓰지 않으면 빈 리스트가 만들어짐
* 학생의 국어, 영어, 수학, 과학 점수가 각각 95,90,85,80인 리스트

```python
student1 = [95, 90, 85, 80]
```

```python
type(studnet1)
```

```python
print(student1[0])  -> 95
print(student1[1])  -> 90
print(student1[2])  -> 85
print(student1[3])  -> 80
```

* 만약 N개의 항목이 있는 리스트 타입의 데이터가 있다면 인덱스 i의 범위는 __0부터 'N-1'__ 까지 임
* 마지막 항목은 '변수명 [-1]'로도 지정할 수 있음

```python
print(student1[-1])  -> 80
print(student1[-2])  -> 85
print(student1[-3])  -> 90
print(student1[-4])  -> 95
```

* 리스트 변경

```python
student1[1] = 100 #두번째 항목에 새로운 데이터 할당
print(student1)  -> [95, 100, 85 80]
```

* 리스트 중 일부 항목 가져오기
  * 리스트[i_start : i_end]
  * 리스트[i_start : i_end : i_step]
* 리스트에서 항목 삭제하기

```python
listdata = [0,1,2,3,4]
del listdata[3]
print(listdata)  -> [0,1,2,4]
```

* 리스트에서 항목의 존재 여부 확인하기

```python
listdata = [0,1,2,3,4]
print(4 in listdata)  -> True
print(8 in listdata)  -> False
```

* 리스트 메서드 활용하기 : __자료형(변수명).메서드이름()__

  ```python
  myf = ['j','r','l','m']
  ```

  * append() : 리스트 맨 끝에 새로운 항목 추가

    ```python
    myf.append('t')
    print(myf)  -> ['j','r','l','m','t']
    ```

  * insert() : 원하는 위치에 데이터 삽입

    ```python
    myf.insert(1,'p')
    print(myf)  -> ['j','p','r','l','m','t']
    ```

  * extend() : 맨 끝에 여러 개의 항목 추가

    ```python
    myf.extend('l','b')
    print(myf)  -> ['j','p','r','l','m','t','l','b']
    ```

  * remove() : 입력값과 첫 번째로 일치하는 항목을 삭제

    ```python
    myf.remove('l')
    print(myf)  -> ['j','p','r','m','t','l','b']
    ```

  * pop() : 마지막 항목을 제거한 후 반환

    ```python
    myf.pop()  -> 'b'
    ```

  * index() : 인자와 일치하는 첫 번째 항목의 위치를 반환

    ```python
    myf.index('r')   -> 2
    ```

  * count() : 인자와 일치하는 항목의 개수를 반환

    ```python
    myf.count('j')  -> 1
    ```

  * sort() : 숫자난 문자열로 구성된 리스트 항목을 순방향으로 정렬

  * reverse() : 리스트 항목을 끝에서 부터 역순으로 정렬

## 4. 튜플(Tuple)

> 리스트와 유사하게 데이터 여러 개를 하나로 묶는 데 이용.
>
> 튜플 데이터는 한 번 입력 혹은 생성하면 그 이후에는 항목을 변경할 수 없음.

```python
tuple1 = (1,2,3,4)
type(tuple1)
```

* 항목을 하나만 같은 튜플을 생성할 때는 항목을 입력한 후에 반드시 콤마(,)를 입력

```python
tuple3 = (9,)
tuple4 = 10,
```

* 튜플에서 메서드 활용하기

  * index()

    ```python
    tuple6 = ('a','b','c''d)
    tuple6.index('c')  -> 2
    ```

  * count()

    ```python
    tuple6 = ('a','b','c''d)
    tuple6.count('a')  -> 1
    ```

## 5. 딕셔너리(Dictionary)

> 키(key) : 값(value)

* 순서에 상관 없음

* 키 : 숫자, 문자열 / 값 : 어떤 데이터 형태도 가능

* 딕셔너리 추가하기

  ```python
  country = {"영국":"런던", "프랑스":"파리", "한국":"부산"}
  country["일본"] = "도쿄"
  ```

* 딕셔너리 변경하기

  ```python
  country= {"영국":"런던", "프랑스":"파리", "한국":"부산", "일본":"도쿄"}
  country["한국"] = "서울"
  ```

* 딕셔너리 삭제하기

  ```python
  del country ["영국"]
  ```

* 딕셔너리 메서드 활용하기

  * keys() : 키 전체를 리스트 형태로 반환

    ```python
    country= {"프랑스":"파리", "한국":"서울", "일본":"도쿄"}
    print(country.keys())  -> dict_keys(["프랑스", "한국", "일본"])
    ```

  * values() : 값 전체를 리스트 형태로 반환

    ```python
    print(country.values())  -> dict_values(["파리","서울","도쿄"])
    ```

  * items() : 카와 값의 쌍을 튜플 형태로 반환

    ```python
    print(country.items())  -> dict_items([("프랑스","파리"),("한국","서울"),("일본","도쿄")])
    ```

  * clear() : 딕셔너리의 모든 항목 삭제

    ```python
    print(country.clear())
    ```

  * update() : 새로운 딕셔너리 데이터 추가

    ```python
    newcountry = {"중국":"베이징"}
    print(country.update(newcountry))
    ```
