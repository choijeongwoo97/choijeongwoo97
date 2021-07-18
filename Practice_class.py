#class => 규약이나 틀
#구조
#명사 => attribute, property, instance 변수
#동사 => method

#class 클래스 이름:
    #명사(attribute)를 초기화
    #동사(behavior)를 정의

#class 정의와 호출

class SoccerPlayer: #class이름의 음절의 맨 앞은 대문자
    def shoot(self): #class의 맨 앞 인자는 무조건 self / 동사의 행동 정의
        print("슛을 날립니다.")
        print("슛~~")

    def pass_the_ball(self):
        print("패스를 합니다.")
        print("패스~~")

player = SoccerPlayer()

print(player.shoot())
print(player.pass_the_ball())

class SoccerPlayer:
    def __init__(self): #생성자 / 객체를 만들때 호출
        print(" 나 태어났어!!")

    def shoot(self):
        print("슛을 날립니다.")

player = SoccerPlayer()

class SoccerPlayer:
    def __init__(self, height, weight):
        print(" 나 태어났어!!")
        self.wow_height = height
        self.wow_weight = weight

    def shoot(self):
        print("슛을 날립니다.")

player1 = SoccerPlayer(height = 180, weight = 80)
print(player1.wow_height)
print(player1.wow_weight)

#상속 자식 class는 부모 class의 특징을 물려받는다

class Human: #부모 클래스
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def walk(self):
        print("걷는중!!")

h1 = Human(60, 170)

class Athelete(Human): #자식 클래스 1
    def __init__(self, weight, height, fat_rate):
        super().__init__(weight, height)
        self.fat_rate = fat_rate

    def workout(self):
        print("운동중!!")

h2 = Athelete(85, 180, 10)

print(h2.height)
print(h2.weight)
print(h2.fat_rate)
print(h2.walk())

class BasketballPlayer(Athelete): #자식 클래스 2

    def workout(self):
        print("농구를 한다!")

h3 = BasketballPlayer(80, 200, 10)
print(h3.workout())