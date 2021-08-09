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

# 2. 구조적 데이터 표시와 처리에 강한 Pandas
# -구조적 데이터 생성하기
# Series를 활용한 데이터 생성
import pandas as pd
b1 = pd.Series([10,20,30,40,50])
print(b1)
print(b1.index)  #b1데이터의 인덱스 출력
print(b1.values)  #b1데이터의 value 출력

b2 = pd.Series(["a","b","c",1,2,3])
print(b2)  #문자열과 숫자가 혼합된 리스트도 인자로 사용 가능

b3 = pd.Series([np.nan,1,2,3])  #np.nan은 널값
print(b3)

index_date = ["2021-08-07","2021-08-08","2021-08-09"]
b4 = pd.Series([7,8,9], index=index_date)  #index 입력
print(b4)

b5 = pd.Series({"에어컨":18,"TV":25,"세탁기":12,"청소기":29})  #딕셔너리 사용
print(b5)

b6 = pd.date_range(start="2021-08-07",end="2021-08-15")  #date_range사용
print(b6)

b7 = pd.date_range(start="2021-08-07",periods=5)  #end대신에 periods사용
print(b7)

b8 = pd.date_range(start="2021-08-07",periods=5,freq="2D")  #이틀 간격으로 날짜 5개 생성
print(b8)

b9 = pd.date_range(start="2021-08-07",periods=5,freq="w")  #시작 요일 기준으로 일주일씩 증가하는 날짜 5개 생성
print(b9)

b10 = pd.date_range(start="2021-08-07",periods=5,freq="2BM")  #업무일 기준 2개월 월말 주기로 날짜 5개 생성
print(b10)

b11 = pd.date_range(start="2021-08-07",periods=4,freq="QS")  #분기 시작일 기준으로 날짜 4개 생성
print(b11)

b12 = pd.date_range(start="2021-08-07",periods=4,freq="AS")  #연도 첫 날 기준으로 1년 주기의 날짜 4개 생성
print(b12)

b13 = pd.date_range(start="2021-08-07 11:30",periods=4,freq="H")  #1시간 주기로 4개의 시간 생성
print(b13)

b14 = pd.date_range(start="2021-08-05 11:30",periods=9,freq="BH")  #업무시간 기준 1시간 주기로 9개의 시간 생성
print(b14)

b15 = pd.date_range(start="2021-08-05 11:30",periods=3,freq="30min")  #30분 주기로 3개의 시간 생성
print(b15)

b16 = pd.date_range(start="2021-08-05 11:30",periods=3,freq="10S")  #10초 주기로 3개의 시간 생성
print(b16)

index_date = pd.date_range(start="2021-08-07",periods=5)
b17 = pd.Series([7,8,9,10,11],index=index_date)
print(b17)


# DataFrame을 활용한 데이터 생성
c1 = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]])  #데이터 프레임 생성
print(c1)

num_list = np.array([[11,22,33],[44,55,66],[77,88,99]])  #numpy array사용하여 데이터프레임 생성
c2 = pd.DataFrame(num_list)
print(c2)

index_date = pd.date_range(start="2021-08-09",periods=3)  #인덱스와 컬럼 추가하여 데이터프레임 생성
col_list = ["영","일","이"]
c2 = pd.DataFrame(num_list,index=index_date,columns=col_list)
print(c2)

data_table = {"연도":["2015","2016","2016","2017","2017"],"지사":["한국","한국","미국","한국","미국"],"고객 수":[200,250,450,300,500]}
c3 = pd.DataFrame(data_table,columns=["연도","지사","고객 수"])  #딕셔너리 데이터를 이용하여 데이터프레임 생성
print(c3)
print(c3.index)
print(c3.columns)
print(c3.values)

# -데이터 연산
c4 = pd.Series([1,2,3,4,5])
c5 = pd.Series([10,20,30,40,50])
print(c4 + c5)  #Series끼리 사칙연산
print(c5 - c4)
print(c4 * c5)
print(c5 / c4)

c6 = pd.Series([1,2,3,4])
c7 = pd.Series([10,20,30,40,50])
print(c6 + c7)  #데이터 크기가 달라도 연산이 가능
print(c7 - c6)
print(c6 * c7)
print(c7 / c6)

data_list1 = {"A":[1,2,3,4,5],"B":[10,20,30,40,50],"C":[100,200,300,400,500]}
c8 = pd.DataFrame(data_list1)
data_list2 = {"A":[6,7,8],"B":[60,70,80],"C":[600,700,800]}
c9 = pd.DataFrame(data_list2)
print(c8 +c9)  #데이터프레임 형식의 데이터 크기가 달라도 연산 가능

table_data = {"연도":[2012,2013,2014,2015,2016],"봄":[256.5,264.3,215.9,223.3,312.8],"여름":[770.6,567.5,599.8,387.1,446.2],
"가을":[363.5,231.2,293.1,247.7,381.6],"겨울":[139.3,59.9,76.9,109.1,108.1]}
column_list = ["봄","여름","가을","겨울"]
index_list = ["2012","2013","2014","2015","2016"]
c10 = pd.DataFrame(table_data,index=index_list,columns=column_list)
print(c10)
print(c10.mean())  #각 열 기준 평균
print(c10.std())  #각 열 기준 표준편차
print(c10.mean(axis=1))  #각 행 기준 평균
print(c10.std(axis=1))  #각 행 기준 표준편차

print(c10.describe())  #각 열 기준 기초통계량
print(c10.T.describe())  #각 행 기준 기초통계량

# -데이터를 원하는 대로 선택하기
KTX_data = {"경부선":[39060,39896,42005,43621,41702,41266,32427],"호남선":[7313,6967,6873,6626,8675,10622,9228],
            "경전선":[3627,4168,4088,4424,4606,4984,5570],"전라선":[309,1771,1954,2244,3146,3945,5766],
            "동해선":[np.nan,np.nan,np.nan,np.nan,2395,3786,6667]}
col_data = ["경부선","호남선","경전선","전라선","동해선"]
ind_data = ["2011","2012","2013","2014","2015","2016","2017"]
df_KTX = pd.DataFrame(KTX_data,index=ind_data,columns=col_data)
print(df_KTX)
print(df_KTX.head())  #위에서 부터 5개의 데이터만 보기
print(df_KTX.tail())  #아래에서 부터 5개의 데이터만 보기
print(df_KTX[:1])  #특정 행 데이터 선택
print(df_KTX.loc["2013"])  #index를 지정했다면 index명으로 행 선택 가능
print(df_KTX.loc["2013":"2015"])  #index명으로 구간 설정도 가능
print(df_KTX["경부선"])  #하나의 열 선택
print(df_KTX[1:3]["전라선"])  #열과 행 선택

print(df_KTX.T)  #전치(transpose

print(df_KTX[["동해선","전라선","경부선","호남선","경전선"]])  #열의 순서를 지정

# -데이터 통합하기
# 세로 방향으로 통합하기
c11 = pd.DataFrame({"class1":[1,2,3,4],"class2":[10,20,30,40]})
print(c11)
c12 = pd.DataFrame({"class1":[5,6],"class2":[50,60]})
print(c12)
print(c11.append(c12))  #세로 방향으로 데이터 통합
print(c11.append(c12,ignore_index=True))  #기존 인덱스 순서를 이어서 통합

# 가로 방향으로 통합하기
c13 = pd.DataFrame({"class3":[100,200,300]})
print(c11.join(c13))

# 특정 열을 기준으로 통합하기
df_1 = pd.DataFrame({"A":[1,2,3,4],"B":[10,20,30,40],"C":[100,200,300,400]})
df_2 = pd.DataFrame({"C":[100,200,300,400],"D":[10,20,30,40],"E":[1,2,3,4]})
print(df_1.merge(df_2))  #C열을 기준으로 통합

df_3 = pd.DataFrame({"key":["A","B","C"],"left":[1,2,3]})
df_4 = pd.DataFrame({"key":["A","B","D"],"right":[4,5,6]})
print(df_3.merge(df_4,how="left",on="key"))  #왼쪽을 기준으로 통합
print(df_3.merge(df_4,how="right",on="key"))  #오른쪽을 기준으로 통합
print(df_3.merge(df_4,how="outer",on="key"))  #모든 데이터를 통합
print(df_3.merge(df_4,how="inner",on="key"))  #공통 데이터만 통합

# -데이터 파일을 읽고 쓰기

