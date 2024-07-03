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

if wraith2.clocking == True:
    print("{0}는 현재 클로킹 상태입니다. ".format(wraith2.name))

# 추가로 외부에서 변수를 만들어서 쓸 수 있다. wraith1은 없음. 그렇게 쓰면 오류남. 2만 만든거임. 확장된 변수는 확장한 객체에 대해서만 적용이 된다.  


# 메소드
# 3:53:17부터~