# <9. 문자열과 텍스트 파일 데이터 다루기>

# 1. 문자열 다루기
# -문자열 분리하기
str1 = "배구 축구 야구 높이뛰기 도마"
print(str1.split())

print("배구 축구 야구 높이뛰기 도마".split()) #띄어쓰기와 개행문자 기준으로 분리

print("배구,축구,야구,높이뛰기,도마".split(",")) #쉼표 기준으로 분리

print("배구,축구,야구,높이뛰기,도마".split(",",maxsplit=2)) #쉼표 2개까지만 분리

phone_number = "+82-01-2345-6789" #국내전화번호만 분리하기
print(phone_number.split("-",maxsplit=1)[1])
print("국내전화번호 : {0}".format(phone_number.split("-",maxsplit=1)[1]))


# -필요없는 문자열 삭제하기
str2 = "    아이스 카페라떼  "
print(str2.strip()) #띄어쓰기와 개행문자 삭제

print("아아아아이스 카페라떼아아아".strip("아"))

str2_1 = "아아아떼떼떼이스 카페라떼떼떼아아아".strip("아")
print(str2_1.strip("떼"))

print("아아아떼떼떼이스 카페라떼떼떼아아아".strip("아떼")) #한 번에 두 문자 삭제 가능

print("아아아떼떼떼이스아떼 카페라떼떼떼아아아".strip("아떼")) #중간에 있는 글자는 삭제 불가

print("아아아떼떼떼이스 카페라떼떼떼아아아".lstrip("아떼")) #왼쪽만 삭제

print("아아아떼떼떼이스 카페라떼떼떼아아아".rstrip("아떼")) #오른쪽만 삭제

sports = " 배구   ,  축구,  야구  , 높이뛰기   ,    도마 " #쉼표와 띄어쓰기가 엉망진창
sportz = sports.split(",") #쉼표 기준으로 분리
print(sportz)
sportx = [] #빈 리스트 생성
for sport in sportz: #반복문으로 하나씩 가져와서 공백제거하고 리스트에 추가
    sporty = sport.strip(" ")
    sportx.append(sporty)
print(sportx)


# -문자열 연결하기 (리스트의 항목을 하나의 문자열로 연결)
list1 = ["세계","최고의","배구","선수","김연경"]
print(" ".join(list1))
print("*^_^*".join(list1))


# -문자열 찾기
print("배구 축구 야구 높이뛰기 도마".find("높이뛰기"))
print("파이썬은 재밌어. 근데 파이썬은 가끔 어려워".find("파이썬",5)) #위치 5부터 "파이썬" 찾기

print("파이썬이 나온 횟수는? {0}".format("파이썬은 재밌어. 근데 파이썬은 가끔 어려워".count("파이썬")))

print("파이썬은 재밌어. 근데 파이썬은 가끔 어려워".startswith("파"))
print("파이썬은 재밌어. 근데 파이썬은 가끔 어려워".startswith("파",13))

print("파이썬은 재밌어. 근데 파이썬은 가끔 어려워".endswith("워"))
print("파이썬은 재밌어. 근데 파이썬은 가끔 어려워".endswith("썬",13,15))


# -문자열 바꾸기
print("파이썬은 재밌어. 근데 파이썬은 가끔 어려워".replace("파이썬","개발")) #파이썬->개발
print("파이썬은 재밌어. 근데 파이썬은 가끔 어려워".replace("파이썬","개발",1))
print("파이썬은 재밌어. 근데 파이썬은 가끔 어려워".replace("가끔","")) #가끔->""


# -문자열의 구성 확인하기
print("안녕하세요방가방가".isalpha()) #문자만
print("1234567890".isdigit()) #숫자만
print("안녕하세요123방가방가".isalnum()) #문자또는 숫자만
print("안녕하세요 123 방가방가".isalnum()) #띄어쓰기X
print("   ".isspace()) #공백만
print("HELLO EVERYBODY".isupper()) #대문자만
print("hello everybody".islower()) #소문자만


# -대소문자로 변경하기
print("python is easy to learn".upper())
print("python is easy to learn".lower())


# 2. 텍스트파일의 데이터를 읽고 처리하기
with open(file="coffeeShopSales.txt",mode="r",encoding="utf8") as file:
    header = file.readline()
    header_list = header.split()
    print(header_list)

    espresso = []
    americano = []
    cafelatte = []
    cappucino = []

    for line in file:
        data_list = line.split()
        espresso.append(int(data_list[1]))
        americano.append(int(data_list[2]))
        cafelatte.append(int(data_list[3]))
        cappucino.append(int(data_list[4]))

print("{0} : {1}".format(header_list[1],espresso))
print("{0} : {1}".format(header_list[2],americano))
print("{0} : {1}".format(header_list[3],cafelatte))
print("{0} : {1}".format(header_list[4],cappucino))

total_sum = [sum(espresso),sum(americano),sum(cafelatte),sum(cappucino)]
total_mean = [sum(espresso)/len(espresso),sum(americano)/len(americano),sum(cafelatte)/len(cafelatte),sum(cappucino)/len(cappucino)]

for i in range(0,5):
    print("[{0}] 판매량".format(header_list[i+1]))
    print("- 나흘 전체 : {0}, 하루 평균 : {1}".format(total_sum[i],total_mean[i]))