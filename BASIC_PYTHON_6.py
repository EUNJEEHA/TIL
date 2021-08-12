# <입력과 출력>
# 1. 화면 출력
# -기본출력 : print()
print("Oh My God! Python!")
print("Oh", "My", "God!", "Python!",sep="^-^")  #구분자 설정
print("Oh My God! Python!","It's too hard!")  #띄어쓰기
print("Oh My God! Python!" + "It's too hard!")  #붙여쓰기
print("Oh My God! Python!\nIt's too hard!")  #개행문자로 줄 바꾸기
print("Oh My God! Python!",end=" ")  #줄 바꿈 없애기
print("It's too hard!")

# -형식 지정 출력
nation = "한국"
print("저는 %s 사람입니다." %nation)

r = 3
PI = 3.14159265358979
print("반지름 : %d, 원주율 : %f" %(r,PI))

ani = "강아지"
hobby = "달리기"
print("저는 {0}를 좋아하고 취미는 {1}입니다.".format(ani,hobby))

# 2. 키보드 입력 : input()
# like = input("가장 좋아하는 과일은?")
# print("과일 중에서 {0}를 가장 좋아하는군요!".format(like))

# a = input("정사각형의 한 변의 길이는?")  #결과가 문자열로 나오기 때문에 연산할 때는 숫자형으로 바꾸기
# print(int(a)**2)

# 3. 파일 읽고 쓰기
file = open(file="coffeeShopSales.txt",mode="r",encoding="utf8")  #파일 읽기 기본형
print(file.read())
file.close()

with open(file="coffeeShopSales.txt",mode="r",encoding="utf8") as file:  #with as 사용
    print(file.read())

with open(file = "coffeeShopSales.txt",mode="r",encoding="utf8") as file:  #readlines(), for문 사용
    for line in file.readlines():
        print(line,end="")

with open(file = "coffeeShopSales.txt",mode="r",encoding="utf8") as file:
    for line in file.readlines():
        date = line.strip().split("   ")
        print(date)

with open(file = "coffeeShopSales.txt",mode="r",encoding="utf8") as file:  #그냥 file 사용
    for line in file:
        print(line,end="")

with open(file="myfile.txt",mode="w",encoding="utf8") as file:
    file.write("line one\n")
    file.write("line two")

countries = {"국가": "대한민국","수도":"서울","지역":"아시아"},\
            {"국가":"일본","수도":"동경","지역":"아시아"},\
            {"국가": "중국","수도":"베이징","지역":"아시아"}
with open(file="myfile.txt",mode="w",encoding="utf8") as file:
    for country in countries:
        line = "국가:{국가},수도:{수도},지역:{지역}\n".format(**country)
        file.write(line)

# with open(file="myfile.txt",mode="x",encoding="utf8") as file:  # x = w의 안전모드. 같은 파일이 있을 경우 에러 발생
    file.write("새로운 데이터")

with open(file="myfile.txt",mode="a",encoding="utf8") as file:  # 같은 파일이 있을 경우 끝 부분 부터 이어짐
    file.write("\n새로운 데이터")
























