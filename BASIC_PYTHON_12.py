import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# <선 그래프>
data1 = [10,14,19,20,25]
plt.plot(data1)

# 2차원 선 그래프
x = np.arange(-4.5,5,0.5)
y = 2 * x ** 2
print([x,y])
plt.plot(x,y)

# 한 그래프 창에 여러 그래프 그리기
x = np.arange(-4.5,5,0.5)
y1 = 2 * x ** 2
y2 = 5 * x + 30
y3 = 4 * x ** 2 + 10
plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)
plt.plot(x,y1,x,y2,x,y3)

# 새로운 그래프 창에 그리기
plt.plot(x,y1)
plt.show()
plt.figure()
plt.plot(x,y2)
plt.show()

# 지정된 번호의 그래프 창에 그래프 그리기
x = np.arange(-5,5,0.1)
y1 = x ** 2 -2
y2 = 20 * np.cos(x) ** 2

plt.figure(1)
plt.plot(x,y1)

plt.figure(2)
plt.plot(x,y2)

plt.figure(1)
plt.plot(x,y2)

plt.figure(2)
plt.clf()
plt.plot(x,y1)

plt.show()

# 하나의 그래프 창에 영역을 나누어 그리기
x = np.arange(0,10,0.1)
y1 = 0.3 * (x-5) **2 + 1
y2 = -1.5 * x + 3
y3 = np.sin(x) ** 2
y4 = 10 * np.exp(-x) + 1

plt.subplot(2,2,1)
plt.plot(x,y1)

plt.subplot(2,2,2)
plt.plot(x,y2)

plt.subplot(2,2,3)
plt.plot(x,y3)

plt.subplot(2,2,4)
plt.plot(x,y4)

plt.show()

# 그래프의 출력 범위 지정하기
x = np.linspace(-4,4,100)
y1 = x ** 3
y2 = 10 * x**2 -2

plt.plot(x,y1,x,y2)
plt.xlim(-1,1)
plt.ylim(-3,3)
plt.show()

# 그래프 꾸미기
x = np.arange(0,5,1)
y1 = x
y2 = x + 1
y3 = x + 2
y4 = x + 3
plt.plot(x,y1,x,y2,x,y3,x,y4) # 기본 선 색
plt.plot(x,y1,"m",x,y2,"y",x,y3,"k",x,y4,"c")  # 선 색 정하기
plt.plot(x,y1,"-",x,y2,"--",x,y3,":",x,y4,"-.")  # 선 스타일 정하기
plt.plot(x,y1,"o",x,y2,"^",x,y3,"s",x,y4,"d")  # 마커 정하기
plt.plot(x,y1,">--r",x,y2,"s-g",x,y3,"d:b",x,y4,"-.Xc")  #옆삼각형/빨간색, 사각형/직선/초록색, 다이아/점선/파랑, 혼합,엑스.청록
plt.show()

# 라벨, 제목, 격자, 범례, 문자열 표시
x = np.arange(-4.5,5,0.5)
y = 2 * x ** 3

plt.plot(x,y)
plt.xlabel("x_axis")  # x축 라벨
plt.ylabel("y_axis")  # y축 라벨
plt.title("Graph title")  # 제목
plt.grid()  # 격자
plt.show()

x = np.arange(0,5,1)
y1 = x
y2 = x + 1
y3 = x + 2
y4 = x + 3

plt.plot(x,y1,">--r",x,y2,"s-g",x,y3,"d:b",x,y4,"-.Xc")
plt.legend(["data1","data2","data3","data4"], loc="lower right")  # 범례
plt.xlabel("x_axis")  # x축 라벨
plt.ylabel("y_axis")  # y축 라벨
plt.title("Graph title")  # 제목
plt.grid()  # 격자
plt.show()

# 한글 폰트 설정 (맑은 고딕)
import matplotlib
matplotlib.rcParams["font.family"] = "Malgun Gothic"
matplotlib.rcParams["axes.unicode_minus"] = False

plt.plot(x,y1,">--r",x,y2,"s-g",x,y3,"d:b",x,y4,"-.Xc")
plt.legend(["데이터1","데이터2","데이터3","데이터4"])  # 범례
plt.xlabel("x축")  # x축 라벨
plt.ylabel("y축")  # y축 라벨
plt.title("그래프 제목")  # 제목
plt.grid()  # 격자
plt.show()

plt.plot(x,y1,">--r",x,y2,"s-g",x,y3,"d:b",x,y4,"-.Xc")
plt.text(0,6,"문자열 출력1")
plt.text(0,5,"문자열 출력2")
plt.text(3,1,"문자열 출력3")
plt.text(3,0,"문자열 출력4")
plt.show()

# <산점도>
height = [165,177,160,180,185,155,172]
weight = [62,67,55,74,90,43,64]

plt.scatter(height,weight,s=500,c="r")
plt.xlabel = "Height(cm)"
plt.ylabel = "Weight(kg)"
plt.title = "Height & Weight"
plt.grid()
plt.show()

size = 100 * np.arange(1,8)
colors = ["r","g","b","c","m","k","y"]
plt.scatter(height,weight,s=size,c=colors)
plt.show()

city = ["서울","인천","대전","대구","울산","부산","광주"]
lat = [37.56,37.45,36.35,35.87,35.53,35.18,35.16]
lon = [126.97,126.70,127.38,128.60,129.31,129.07,126.85]
pop_den = [16154,2751,2839,2790,1099,4454,2995]
size = np.array(pop_den) * 0.2
colors = ["r","g","b","c","m","k","y"]

plt.scatter(lat,lon,s=size,c=colors,alpha=0.5)
plt.xlabel = "경도"
plt.ylabel = "위도"
plt.title = "지역별 인구 밀도(2017)"

for x,y,name in zip(lat,lon,city):
    plt.text(x,y,name)
plt.show()

# <막대 그래프>
member_IDs = ["m_01","m_02","m_03","m_04"]
before_ex = [27,35,40,33]
after_ex = [30,38,42,37]

n_data = len(member_IDs)
index = np.arange(n_data)
colors = ["r","g","b","m"]
plt.bar(index,before_ex,tick_label=member_IDs,color=colors,width=0.6)
plt.show()

colors = ["r","g","b","m"]
plt.barh(index,before_ex,color=colors,tick_label=member_IDs)
plt.show()

barwidth = 0.4
plt.bar(index,before_ex,width=barwidth,color="c",align="edge",label="before")
plt.bar(index+barwidth,after_ex,width=barwidth,color="m",align="edge",label="after")
plt.xticks(index+barwidth, member_IDs)
plt.legend(loc="upper left")
plt.xlabel("회원ID")
plt.ylabel("윗몸일으키기 횟수")
plt.title("운동 시작 전과 후의 근지구력(복근) 변화 비교")
plt.show()

# <히스토그램>
math = [75,82,84,83,90,86,85,92,72,71,100,87,81,76,94,78,81,60,79,69,74,87,82,68,79]
plt.hist(math)
plt.show()

plt.hist(math,bins=8)
plt.title("수학 시험의 히스토그램")
plt.xlabel("시험점수")
plt.ylabel("도수(frequency)")
plt.grid()
plt.show()

# <파이 그래프>
plt.figure(figsize=(5,5))  # 그래프 너비, 높이 비율이 같도록
fruit = ["사과","바나나","딸기","오렌지","포도"]
result = [7,6,3,2,2]
explode_value = (0.1,0,0,0,0)
plt.pie(result,labels=fruit,autopct="%.1f%%",startangle=90,counterclock=False,shadow=True,explode=explode_value)
plt.show()

# <그래프 저장하기>
plt.figure(figsize=(5,5))  # 그래프 너비, 높이 비율이 같도록
fruit = ["사과","바나나","딸기","오렌지","포도"]
result = [7,6,3,2,2]
explode_value = (0.1,0,0,0,0)
plt.pie(result,labels=fruit,autopct="%.1f%%",startangle=90,counterclock=False,shadow=True,explode=explode_value)
plt.savefig("C:\\Users\\USER\Desktop\DS\project1\\first_figsave.png",dpi=100)
plt.show()

# <판다스로 그래프 그리기>
s1 = pd.Series([1,2,3,4,5,6,7,8,9,10], index=pd.date_range("2021-09-01",periods=10))
s1.plot(grid=True)
plt.show()

df_rain = pd.read_csv("C:\\Users\\USER\\Desktop\\DS\\sea_rain1.csv", index_col="연도")
print(df_rain)
rain_plot = df_rain.plot(grid=True, style=["r--*","g-o","b:*","m-.p"])
rain_plot.set_xlabel("연도")
rain_plot.set_ylabel("강수량")
rain_plot.set_title("연간 강수량")
plt.show()

year = [2006,2008,2010,2012,2014,2016]
area = [26.2,27.8,28.5,31.7,33.5,33.2]
table = {"연도":year, "주거면적":area}
df_area = pd.DataFrame(table,columns=["연도","주거면적"])
print(df_area)
area_plot = df_area.plot(x="연도",y="주거면적",grid=True,title="연도별 1인당 주거면적")
plt.show()

# <pandas의 산점도>
temperature = [25.2,27.4,22.9,26.2,29.5,33.1,30.4,36.1,34.4,29.1]
Ice_cream_sales = [236500,357500,203500,365200,446600,574200,453200,675400,598400,463100]
dict_data = {"기온":temperature, "아이스크림 판매량":Ice_cream_sales}
df_ice_cream = pd.DataFrame(dict_data,columns=["기온","아이스크림 판매량"])
print(df_ice_cream)
ice_cream_plot = df_ice_cream.plot(x="기온", y="아이스크림 판매량", grid=True, title = "최고 기온과 아이스크림 판매량", kind="scatter")
plt.show()

# <pandas의 막대 그래프>
grade_num = [5,14,12,3]
students = ["A","B","C","D"]
df_grade = pd.DataFrame(grade_num,index=students,columns=["Student"])
print(df_grade)
grade_bar = df_grade.plot.bar(grid=True)
grade_bar.set_xlabel("학점")
grade_bar.set_ylabel("학생수")
grade_bar.set_title("학점별 학생 수 막대 그래프")
plt.show()

# <pandas의 파이 그래프>
fruit = ["사과","바나나","딸기","오렌지","포도"]
result = [7,6,3,2,2]
explode_value = (0.1,0,0,0,0)
df_fruit = pd.Series(result,index=fruit,name="선택한 학생수")
print(df_fruit)
fruit_pie = df_fruit.plot.pie(explode=explode_value, startangle=90, counterclock=False,autopct="%.1f%%",shadow=True,table=True)
fruit_pie.set_title("과일 선호도 조사 결과")
fruit_pie.set_ylabel("")
plt.savefig("C:\\Users\\USER\Desktop\DS\project1\\second_figsave.png",dpi=200)
plt.show()



