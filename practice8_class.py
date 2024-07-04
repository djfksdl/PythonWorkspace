# class 3:38:00

# # 마린 : 공격 유닛, 군인. 총을 쓸 수 있음
# name = "마린" # 유닛의 이름
# hp = 40 # 유닛의 체력
# damage = 5 # 유닛의 공격력

# print("{0} 유닛이 생성되었습니다." .format(name))
# print("체력 {0}, 공격력 {1}\n" .format(hp, damage))


# # 탱크 : 공격 유닛, 탱크. 포를 쏠 수 있는데, 일반모드 / 시즈모드
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# tank2_name = "탱크"
# tank2_hp = 150
# tank2_damage = 35

# print("{0} 유닛이 생성되었습니다." .format(tank_name))
# print("체력 {0}, 공격력 {1}\n" .format(tank_hp, tank_damage))

# def attack(name, location, damage):
#     print("{0} :{1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format( name, location, damage))

# attack(name, "1시" , damage)
# attack(tank_name, "1시" , tank_damage)
# attack(tank2_name, "1시" , tank2_damage)

# 게임할때는 수십개가 나옴. -> 그래서 클래스라는 개념이 필요. 집합이라는 개념이라고 생각하면 됨

class Unit:
    def __init__(self, name , hp , damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다." .format(self.name))
        print("체력 {0}, 공격력 {1}\n" .format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
marine3 = Unit("탱크", 150, 35)

# __init__  = 생성자(객체(마린,탱크)가 만들어질떄 자동으로 호출되는 부분)
# 클래스로부터 만들어지는 것들을 '객체'라고 하고 
# 마린과 탱크는 Unit 클래스의 '인스턴스'라고 함
# 객체가 생성될떄는 기본적으로 init함수에 적용된 동일한 갯수만큼 값을 던져줘야함(self 제외하고)
# ex) 이렇게는 불가능
# marine3 = Unit("마린")
# marine3 = Unit("마린", 40)


# 멤버 변수 3:48:33
# 클래스 내에서 정의된 변수, 변수를 가지고 초기화할 수 있고, 쓸 수 있음. ex) self.hp , self,name, self.damage 등...

# 레이스 : 공중 유닛, 비행기. 클로킹(상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80, 5)
print("유닛이름 : {0}, 공격력 {1}" .format(wraith1.name, wraith1.damage))

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗음)
wraith2 = Unit("레이스", 80, 5)
wraith2.clocking = True

# if wraith1.clocking == True:
    # print("{0}는 현재 클로킹 상태입니다. ".format(wraith1.name))

if wraith2.clocking == True: # 오류남
    print("{0}는 현재 클로킹 상태입니다. ".format(wraith2.name))

# 추가로 외부에서 변수를 만들어서 쓸 수 있다. wraith1은 없음. 그렇게 쓰면 오류남. 2만 만든거임. 확장된 변수는 확장한 객체에 대해서만 적용이 된다.  


# 메소드 3:53:17
# 일반 유닛
class Unit2: 
    def __init__(self, name, hp, speed) :
        self.name = name
        self.hp = hp       
        self.speed = speed
        # self.damage = damage - 3줄 메딕떄문에 삭제
        # print("{0} 유닛이 생성되었습니다." .format(self.name))
        # print("체력 {0}, 공격력 {1}\n" .format(self.hp, self.damage))

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0}:{1} 방향으로 이동합니다.[속도 {2}]"\
            .format(self.name, location, self.speed)) 
            
# 상속
# 공격 유닛
class AttackUnit2(Unit2): # Unit2를 상속받음(인자 추가해주기)
    def __init__(self, name, hp , speed, damage ):
        # self.name = name # 우측name은 위()에서 전달 받은 인자를 의미
        # self.hp = hp
        Unit2.__init__(self, name, hp ,speed) # 상속받았기때문에 따로 정의해줄 필요가 없고, Unit2에서 만들어진 생성자를 호출해서 정의할 수 있다.
        self.damage = damage # 상속받지 않고 추가로 써준다.

    def attack(self, loacation): # 두번쨰 함수
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]" \
            .format(self.name, loacation, self.damage))

# self는 자기자신을 이야기함. 클래스 내에서 메소드 앞에서는 무조건 self를 적는다. self를 씀으로써 자기 자신의 변수에 접근할 수 있다.
# location은 self 가 없는데 attack의 전달받은 location을 의미

    def damaged(self, damage) :
        print("{0} : {1} 데미지를 입었습니다. " .format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다." .format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다." .format(self.name))

# 메딕 : 의무병 : damage가 없다 -> 부모로부터 공통부분만 상속받는다. 다른 유닛에만 damage를 추가한다.

# 파이어뱃 : 공격유닛, 화염 방사기.
firebat1 = AttackUnit2("파이어뱃", 50 , 0 ,16)
firebat1.attack("5시")

# 드랍쉽 : 공중 유닛, 수송기 . 마린 / 파이어뱃 /탱크 등을 수송 - dagame가 없다. 

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다.[ 속도 {2}]"\
              .format(name, location, self.flying_speed)) 
            
# 공중 공격 유닛 클래스
class FlyalbeAttackUnit(AttackUnit2, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit2.__init__(self, name, hp, 0 , damage) # 지상스피드는 필요없기 떄문에 0으로 초기화
        Flyable.__init__(self, flying_speed)

    def move(self, location): # 새롭게 move()를 재정의(오버라이딩)
        print("[공중유닛 이동]")
        self.fly(self.name, location) # fly함수를 통해서 정의

# 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사
valkyrie = FlyalbeAttackUnit("발키리", 200, 6,5)
valkyrie.fly(valkyrie.name , "3시")


# 공격 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)


# 다중상속 : 부모가 2이상이라 여러곳에서 상속을 받는다.


# 연산자 오버라이딩
# 벌쳐 : 지상 유닛, 기동성이 좋음
vulture = AttackUnit2("벌쳐", 80, 10, 20)

# 배틀 크르저 : 공중 유닛, 체력도 굉장히 좋음, 공격력도 좋음
battlecruiser = FlyalbeAttackUnit("배틀크루저", 500, 25, 3)

# 이렇게 하면 매번 공중인지 지상인지 구분을 해야함 -> 오버라이딩을 해서 공중이면 공중, 지상이면 지상의 속성을 쓸 수 있도록 하기 
# vulture.move("11시")
# battlecruiser.fly( battlecruiser , "9시")
vulture.move("11시")
battlecruiser.move( "9시") # self.name으로 이미 받기떄문에 location만 보내준다.


# pass
# 건물
# class BuildingUnit(Unit2):
#     def __init__(self, name, hp, speed):
#         pass

# # 서플라이 디폿 : 건물, 1개 건물당 8개 유닛 생성
# supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

# def game_start():
#     print("[알림] 새로운 게임을 시작합니다")

# def game_over():
#     pass # 아무것도 안하고 넘어간다

# game_start()
# game_over()


# super
class BuildingUnit(Unit2):
    def __init__(self, name, hp, location):
        # Unit2.__init__(self, name, hp, 0) 원래는 이렇게 썼는데, 
        super().__init__(name, hp, 0) # super를 써서 초기화할떄는 self를 쓰지 않는다. 근데 다중상속에서 문제 발생할 수 있음 -> practice9_class.py
        self.location = location

