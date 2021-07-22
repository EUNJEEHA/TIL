# 알고리즘 특강

## 1. 자료구조와 알고리즘 소개

> 자료구조 == 요리 재료
>
> 알고리즘 == 요리 방법

### 1-1. 자료구조의 종류

* 단순 자료 구조 -> 파이썬
  * 정수
  * 실수
  * 문자
  * 문자열
* 선형 자료 구조 -> __암기!__
  * 리스트
  * 스텍
  * 큐
* 비선형 자료 구조 -> __암기!__
  * 트리
  * 그래프
* 파일 자료 구조 -> 파이썬
  * 순차 파일
  * 색인 파일
  * 직접 파일

### 1-2. 







## 2. 선형 자료 구조

### 2-1. 선형 리스트

* <다현 - 정연 - 쯔위 - 사나 - 지효> 순으로 데이터 생성

```python
katok = [] # 빈배열

katok.append(None) #빈칸 1개 확보
kLen = len(katok)
katok[kLen-1] = "다현" # 확보한 칸에 친구 입력

katok.append(None)
kLen = len(katok)
katok[kLen-1] = "정연"

katok.append(None)
kLen = len(katok)
katok[kLen-1] = "쯔위"

katok.append(None)
kLen = len(katok)
katok[kLen-1] = "사나"

katok.append(None)
kLen = len(katok)
katok[kLen-1] = "지효"

print(katok)
```

* 함수로 표현

```python
## 함수
def add_data(friend):
    katok.append(None)
    kLen = len(katok)
    katok[kLen - 1] = friend
    
add_data('다현')
add_data('정연')
add_data('쯔위')
add_data('사나')
add_data('지효')
```

* 데이터 추가

```python
def insert_data(position,friend):
    katok.append(None)
    kLen = len(katok)
    for i in range(kLen-1, position, -1):
        katok[i] = katok[i-1]
        katok[i-1] = None
    katok[position] = friend
    
insert_data(3,'미나')
print(katok)
```

* 데이터 삭제

```python
def delete_data(position):
    kLen = len(katok)
    katok[position] = None
    for i in range(position+1, kLen):
        katok[i-1] = katok[i]
        katok[i] = None
    del(katok[kLen-1])
    
delete_data(4)
print(katok)
```

* 사용자가 쓸 수 있도록 코딩

```python
## 함수
def add_data(friend):
    katok.append(None)
    kLen = len(katok)
    katok[kLen - 1] = friend

def insert_data(position,friend):
    katok.append(None)
    kLen = len(katok)
    for i in range(kLen-1, position, -1):
        katok[i] = katok[i-1]
        katok[i-1] = None
    katok[position] = friend

def delete_data(position):
    kLen = len(katok)
    katok[position] = None
    for i in range(position+1, kLen):
        katok[i-1] = katok[i]
        katok[i] = None
    del(katok[kLen-1])

## 전역
katok = []
select = -1 #1추가, 2삽입, 3삭제, 4종료

## 메인
while (select != 4):
    select = int(input('선택(1추가, 2삽입, 3삭제, 4종료)-->'))

    if (select == 1):
        data = input("추가할 친구->") #추가
        add_data(data)
        print(katok)
    elif (select == 2):
        data1 = int(input("삽입할 위치->")) #삽입
        data2 = input("삽입할 친구->")
        insert_data(data1,data2)
        print(katok)
    elif (select == 3):
        data = int(input("삭제할 위치->")) #삭제
        delete_data(data)
        print(katok)
    elif (select == 4):
        pass #종료
    else:
        print("잘못 입력!")
```





### 2-2. (단순)연결 리스트

* <다현 - 정연 - 쯔위 - 사나 - 지효> 순으로 데이터 생성 

```python
node1 = Node()
node1.data = '다현'

node2 = Node()
node2.data = '정연'
node1.link = node2

node3 = Node()
node3.data = '쯔위'
node2.link = node3

node4 = Node()
node4.data = '사나'
node3.link = node4

node5 = Node()
node5.data = '지효'
node4.link = node5

print(node1.data, end=' ')
print(node1.link.data, end=' ')
```

* class 선언

```python
class Node():
    def __init__(self):
        self.data = None
        self.link = None
        
current = node1
print(current.data, end=' ')
while(current.link != None):
    current = current.link
    print(current.data, end=' ')
```

* 노드(데이터) 삽입 

```python
newnode = Node()
newnode.data = '은지'
newnode.link = node2.link
node2.link = newnode
```

* 데이터 삭제

```python
node2.link = node3.link
del(node3)
```

* 사용자용 만들기

```python
## 함수
class Node() :  # 붕어빵 기계
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start):
    current = start
    print(current.data, end='  ')
    while current.link != None:
        current = current.link
        print(current.data, end='  ')
    print()

## 전역
memory = []
head, current, pre = None, None, None
# 데이터 집합 (실무 DB, 웹클롤링, 센서신호.....)
dataArray = ['다현', '정연', '쯔위', '사나', '지효']

## 메인
# 첫 노드
node = Node()
node.data = dataArray[0]
head = node
memory.append(node)
# 그외 노드
for data in dataArray[1:] : #['정연', '쯔위',...
    pre = node
    node = Node()
    node.data = data
    pre.link = node
    memory.append(node)

printNodes(head)
```

* 노드 삽입(맨 앞에)

```python
def insert_node(finddata,insertdata):
    global memory, head, current, pre
    if finddata == head.data:
        node = Node()
        node.data = insertdata
        node.link = head
        head = node
        return
```

* 노드 삽입(중간에)

```python
def insert_node(finddata,insertdata):
    global memory, head, current, pre
    if finddata == head.data:
        node = Node()
        node.data = insertdata
        node.link = head
        head = node
        return
    current = head
    while current.link != None!
        pre = current
        current = current.link
        if current.data == finddata:
            node = Node()
            node.data = insertdata
            node.link = current
            pre.link = node
            memory.append(node)
            return
```

* 노드 삽입(마지막에)

```python
```

* 삭제

```python
## 함수
class Node() :  # 붕어빵 기계
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start):
    current = start
    print(current.data, end='  ')
    while current.link != None:
        current = current.link
        print(current.data, end='  ')
    print()

def insert_node(findData, insertData) :
    global memory, head, current, pre
    if (findData == head.data) :
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        memory.append(node)
        return
    current = head
    while current.link != None :
        pre = current
        current = current.link
        if (current.data == findData) :
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            memory.append(node)
            return
    node = Node()
    node.data = insertData
    current.link = node
    memory.append(node)

def delete_node(delData) :
    global memory, head, current, pre
    if (head.data == delData) :
        current = head
        head = head.link
        del(current)
        return
    current = head
    while (current.link != None) :
        pre = current
        current = current.link
        if (current.data == delData) :
            pre.link = current.link
            del(current)
            return


## 전역
memory = []
head, current, pre = None, None, None
# 데이터 집합 (실무 DB, 웹클롤링, 센서신호.....)
dataArray = ['다현', '정연', '쯔위', '사나', '지효']

## 메인
# 첫 노드
node = Node()
node.data = dataArray[0]
head = node
memory.append(node)
# 그외 노드
for data in dataArray[1:] : #['정연', '쯔위',...
    pre = node
    node = Node()
    node.data = data
    pre.link = node
    memory.append(node)
printNodes(head)

insert_node('다현', '화사')
printNodes(head)
insert_node('사나', '솔라')
printNodes(head)
insert_node('재남', '문별')
printNodes(head)

delete_node('화사')
printNodes(head)
delete_node('사나')
printNodes(head)
delete_node('재남')
printNodes(head)
```

* 연결리스트 최종

```python
## 함수
class Node() :  # 붕어빵 기계
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start):
    current = start
    print(current.data, end='  ')
    while current.link != None:
        current = current.link
        print(current.data, end='  ')
    print()

def insert_node(findData, insertData) :
    global memory, head, current, pre
    if (findData == head.data) :
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        memory.append(node)
        return
    current = head
    while current.link != None :
        pre = current
        current = current.link
        if (current.data == findData) :
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            memory.append(node)
            return
    node = Node()
    node.data = insertData
    current.link = node
    memory.append(node)

def delete_node(delData) :
    global memory, head, current, pre
    if (head.data == delData) :
        current = head
        head = head.link
        del(current)
        return
    current = head
    while (current.link != None) :
        pre = current
        current = current.link
        if (current.data == delData) :
            pre.link = current.link
            del(current)
            return

def find_node(findData) :
    global memory, head, current, pre
    current = head
    if current.data == findData :
        return  current
    while current.link != None :
        current = current.link
        if current.data == findData:
            return current
    return Node() # 빈 노드 반환

## 전역
memory = []
head, current, pre = None, None, None
# 데이터 집합 (실무 DB, 웹클롤링, 센서신호.....)
dataArray = ['다현', '정연', '쯔위', '사나', '지효']

## 메인
# 첫 노드
node = Node()
node.data = dataArray[0]
head = node
memory.append(node)
# 그외 노드
for data in dataArray[1:] : #['정연', '쯔위',...
    pre = node
    node = Node()
    node.data = data
    pre.link = node
    memory.append(node)
printNodes(head)

insert_node('다현', '화사')
printNodes(head)
insert_node('사나', '솔라')
printNodes(head)
insert_node('재남', '문별')
printNodes(head)

delete_node('화사')
printNodes(head)
delete_node('사나')
printNodes(head)
delete_node('재남')
printNodes(head)

fNode = find_node('다현')
print(fNode.data)
fNode = find_node('지효')
print(fNode.data)
fNode = find_node('재남')
print(fNode.data)
```



### 2-3. 스텍





### 3-4. 큐







## 3. 비선형 자료구조

### 3-1. 트리





### 3-2. 그래프







## 4. 









## 5. 







