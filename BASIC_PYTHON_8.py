# <8. 객체와 클레스>

# 1. 클레스 선언과 객체 생성
# 객체 = 속성(변수) + 행위(함수)
# 클래스 = 붕어빵 틀 / 객체(인스턴스) = 틀에 크림을 넣어 만든 '크림 붕어빵
# 클래스명은 알파벳 대문자로 시작

class Bicycle:  #Bycicle 클래스 생성

    def __init__(self,wheel_size,color):  #객체 초기화
        self.wheel_size = wheel_size
        self.color = color

    def move(self,speed):
        print("자전거: 시속 {0}km로 전진".format(speed))

    def turn(self,direction):
        print("자전거: {0}회전".format(direction))

    def stop(self):
        print("자전거 {0} / {1} : 정지".format(self.wheel_size,self.color))

my_bicycle = Bicycle(26,"black")  #my_bicycle객체 생성, 속성값 지정

my_bicycle.move(110)
my_bicycle.turn("좌")
my_bicycle.stop()

# 2. 클래스를 구성하는 변수와 함수
# -클래스에서 사용하는 변수 :
# 클래스 변수(함수 밖에서 정의, 모든 객체가 사용 가능)/인스턴스 변수(클래스 내 함수 안에서 정의, self.변수명)
class Car():
    instance_count = 0  #클래스 변수

    def __init__(self,size,color):
        self.size = size  #인스턴스 변수
        self.color = color  #인스턴스 변수
        Car.instance_count = Car.instance_count + 1  #클래스 변수 이용
        print("자동차 객체의 수 : {0}".format(Car.instance_count))

    def move(self):
        print("자동차{0}/{1}가 움직입니다.".format(self.size,self.color))

car1 = Car("small","white")
car2 = Car("big","black")

#"instance_count"는 클래스 변수이기 때문에, 각 car1과 car2에 공통적으로 사용됨
print("car1객체를 사용하여 인스턴스 개수 확인 : {0}".format(car1.instance_count))
print("car2객체를 사용하여 인스턴스 개수 확인 : {0}".format(car2.instance_count))

#인스턴스 변수는 각 객체에서 별도로 관리
car1.move()
car2.move()

class Car2():
    count = 0

    def __init__(self,size,num):
        self.size = size  #인스턴스 변수
        self.count = num  #인스턴스 변수
        Car2.count = Car2.count + 1  #클래스 변수
        print("자동차 객체의 수 : Car2.count = {0}".format(Car2.count))
        print("인스턴스 변수 초기화 : self.count = {0}".format(self.count))

    def move(self):
        print("자동차{0}/{1}가 움직입니다.".format(self.size,self.size))

ca1 = Car2("big",20)
car2 = Car2("small",30)


# -클래스에서 사용하는 함수
# -인스턴스 매서드 : 각 객체에서 개별적으로 동작하는 함수
class Car():
    instance_count = 0

    #초기화 함수(인스턴스 매서드)
    def __init__(self,size,color):
        self.size = size
        self.color = color
        Car.instance_count = Car.instance_count + 1
        print("자동차 객체의 수 : {0}".format(Car.instance_count))

    #인스턴스 매서드
    def move(self,speed):
        self.speed = speed
        print("자동차{0}/{1}가".format(self.size,self.color),end="")
        print("시속 {0}km로 전진".format(speed))

    def auto_cruise(self):
        print("자율주행모드")
        self.move(self.speed)  #move()함수의 인자로 인스턴스 변수를 입력

car1 = Car("small","red")
car2 = Car("big","green")
car1.move(100)
car2.move(110)
car1.auto_cruise()
car2.auto_cruise()

# -정적 매서드 : 클래스나 객체와는 무관하게 독립적으로 함수를 만들고 싶을 때 이용(날짜, 시간 환율 등)
class Car():
    instance_count = 0

    def __init__(self,size,color):
        self.size = size
        self.color = color
        Car.instance_count = Car.instance_count + 1
        print("자동차 객체의 수 : {0}".format(Car.instance_count))

    @staticmethod  #정적 매서드
    def check_type(mode_code):
        if mode_code >= 20:
            print("이 차는 전기차입니다.")
        elif 10 < mode_code < 20:
            print("이 차는 가솔린차입니다.")
        else:
            print("이 차는 디젤차입니다.")

#객체나 self인자 없이 "클래스명.정적매서드명()"으로 사용
Car.check_type(35)
Car.check_type(13)

# -클래스 매서드 : 클래스 변수 사용, 첫 인자로 "cls"필요
class Car():
    instance_count = 0

    def __init__(self,size,color):
        self.size = size
        self.color = color
        Car.instance_count = Car.instance_count + 1

    @classmethod
    def count_instance(cls):
        print("자동차 객체의 개수 : {0}".format(cls.instance_count))

car1 = Car("small","red")
Car.count_instance()
car2 = Car("big","green")
Car.count_instance()

# 3. 객체와 클래스를 사용하는 이유 : 코드 작성과 관리가 편함
# 로봇의 속성 : 이름, 위치
# 로봇의 동작 : (위로) 한 칸 이동
class Robot():
    def __init__(self,name,pos):
        self.name = name
        self.pos = pos

    def move(self):
        self.pos = self.pos + 1
        print("{0} position {1}".format(self.name,self.pos))

robot1 = Robot("R1",0)
robot2 = Robot("R2",10)
robot1.move()
robot2.move()

# 4. 클래스 상속
# 부모 클래스 생성
class Bicycle:

    def __init__(self,wheel_size,color):
        self.wheel_size = wheel_size
        self.color = color

    def move(self,speed):
        print("자전거: 시속 {0}km로 전진".format(speed))

    def turn(self,direction):
        print("자전거: {0}회전".format(direction))

    def stop(self):
        print("자전거 {0} / {1} : 정지".format(self.wheel_size,self.color))

# 자식 클래스 생성
class FoldingBicycle(Bicycle):
    def __init__(self,wheel_size,color,state):
        Bicycle.__init__(self,wheel_size,color)
        self.state = state

    def fold(self):
        self.state = "folding"
        print("자전거 접기, state : {0}".format(self.state))

    def unfold(self):
        self.state = "unfolding"
        print("자전거 펴기, state : {0}".format(self.state))

my_bicycle1 = FoldingBicycle(25,"blue","folding")
my_bicycle1.move(120)  #부모 클래스의 함수 사용 가능
my_bicycle1.unfold()


#양궁 클래스 만들어 보기
import random
class Archery(): #양궁 클래스 생성
    def __init__(self,nation,name):
        self.nation = nation
        self.name = name

    def shoot(self):
        sum = 0
        print("{0}의 {1}선수가 화살을 쏩니다.".format(self.nation, self.name))
        for i in range(1, 4):
            score = random.randint(1,10)
            print(i,"번째 화살 : ",score,"점")
            sum = sum + score
        print("{0}의 {1}선수의 총점은 {2}점입니다.".format(self.nation,self.name,sum))

# class ShootOff(Archery):
#     def __init__(self,nation,name):
#         Archery.__init__(self,nation,name)
#         pass
#
#
ansan = Archery("Korea","Ansan")
ansan.shoot()

nakamura = Archery("Japan","Nakamura")
nakamura.shoot()


# if int(ansan.sum) > int(nakamura.sum):
#     print("승자는 {0}의 {1}선수입니다!!!".format(ansan.nation,ansan.name))
# elif int(ansan.sum) < int(nakamura.sum):
#     print("승자는 {0}의 {1}선수입니다!!!".format(nakamura.nation,nakamura.name))
# else:
#     print("두 선수 동점으로, shoot-off전으로 넘어갑니다!!")


