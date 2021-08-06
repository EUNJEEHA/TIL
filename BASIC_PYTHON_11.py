# <11.데이터 분석을 위한 패키지>
# 1. 배열 데이터를 효과적으로 다루는 NumPy
# -배열 생성하기
#numpy를 "np"로 불러옴
import numpy as np
a1 = np.array([0,1,2,3,4])
print(a1)
print(a1.dtype)
a2 = np.array([0,1.2,4.56,7,8]) #정수,실수 섞여 있으면 실수로 나옴
print(a2)
print(a2.dtype)  #타입확인
a3 = np.array([[1,2,3],[4,5,6],[7,8,9]])  #다차원(2차원) 배열 생성
print(a3)
print(a3.dtype)

a4 = np.arange(10)  #arange로 범위 지정
print(a4)
a5 = np.arange(0,9,2)
print(a5)

a6 = np.arange(0,11,2).reshape(2,3)  #1차원 배열을 2차원의 행렬로 생성
print(a6)
print(a6.shape)

a7 = np.linspace(1,10,10)  #데이터 개수 지정하여 생성
print(a7)
a8 = np.linspace(0,np.pi,12)
print(a8)

a9 = np.zeros(10)  #모든 원소가 '0'
print(a9)
a10 = np.zeros((2,3))
print(a10)

a11 = np.ones(10)  #모든 원소가 '1'
print(a11)
a12 = np.ones((2,3))
print(a12)

a13 = np.eye(3)  #단위행렬
print(a13)

a14 = np.array(["1.5","0.64","5.6","3.9"])
print(a14.dtype)
a15 = a14.astype(float)  #데이터 타입 변환
print(a15.dtype)

a16 = np.random.rand(2,3) #2행3열에 0~1사이의 실수 난수 표현
print(a16)
a17 = np.random.rand(3,2,4) #2행4열을 총 3개 생성
print(a17)
a18 = np.random.randint(1,10,size=(2,5))  #2행5열에 1~10사이의 정수 난수 표현
print(a18)


# -배열의 연산
# 배열의 형태(shape)가 같다면 기본 연산 가능
a19 = np.array([1,2,3,4,5])
a20 = np.array([10,20,30,40,50])
print(a19 + a20)  #배열끼리 덧셈
print(a19 + 10)  #배열에 +10
print(a19 - a20)  #배열끼리 뺄셈
print(a19 * a20)  #배열끼리 곱셈
print(a19 / a20)  #배열끼리 나눗셈
print(a19 ** 2)  #배열 거듭제곱
print(a19 > 3)  #배열의 원소가 3보다 큰 지

print([a19.sum(), a19.mean()])  #배열의 합, 평균
print([a19.std(), a19.var])  #배열의 표준편차, 분산
print([a19.min(), a19.max()])  #배열의 최솟값, 최댓값
print([a19.cumsum(), a19.cumprod()])  #배열의 누적 합, 누적 곱

a21 = np.arange(1,5).reshape(2,2)
print(a21)
a22 = np.arange(5,9).reshape(2,2)
print(a22)
print(a21.dot(a22))  #a21과 a22 행렬 곱
print(a21.transpose())  #행렬a21의 전치 행렬
print(np.linalg.inv(a21))  #행렬a21의 역행렬
print(np.linalg.det(a21))  #행렬a21의 행렬식

# -배열의 인덱싱과 슬라이싱
a1 = np.array([0,1,2,3,4])
print(a1[0])  #배열에서 위치0의 원소 추출
print(a1[4])  #배열에서 위치4의 원소 추출
a1[3] = 5  #위치3의 원소값을 '5'로 변환
print(a1)

a6 = np.arange(0,11,2).reshape(2,3)
print(a6)
print(a6[0,2])  #0행2열 원소 추출
a6[1,1] = 9  #1행1열의 원소를 '9'로 변환
print(a6)
print(a6[1,])  #1행 원소들 추출
a6[0,] = [1,2,3]  #0행 원소들을 [1,2,3]값으로 변환
print(a6[0,])
print(a6[a6 > 7])  #배열 a6의 원소들 중에서 7보다 큰 값 추출

a1 = np.array([0,1,2,3,4])
print(a1[0:3])  #0부터 2까지 슬라이싱
print(a1[:2])  #0부터 1까지 슬라이싱
a1[:2] = [5,6]  #0부터 1까지의 값을 [5,6]으로 변환
print(a1)

a23 = np.arange(1,10).reshape(3,3)
print(a23)
print(a23[1:2, 0:1])
print(a23[:2, 1:])
print(a23[1][0:2])  #행을 1행으로 지정하고, 열을 슬라이싱
a23[1:2, 1:3] = [0, 0]
print(a23)

# 2. Pandas