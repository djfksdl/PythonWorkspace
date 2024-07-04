class Unit:
    def __init__(self):
        print("Unit 생성자")
    
class Flyable:
    def __init__(self) :
        print("Flyable 생성자")

# 1) 다중상속시 super사용
# class FlyableUnit(Unit, Flyable):
#     def __init__(self):
#         super().__init__()

# 2) 다중상속시 해결방안
class FlyableUnit(Flyable, Unit):
    def __init__(self):
        # super().__init__()
        Unit.__init__(self)
        Flyable.__init__(self)

# 드랍쉽
dropship = FlyableUnit() # (Unit, Flyable) 하면 Unit생성자에 대해 생성됨/ (Flyable, Unit) 하면 Fltable생성자에 대해 생성됨
# 2개 이상의 다중상속을 받을떄, super를 쓰면 맨 앞에 상속받는 클래스에 대해서만 입력함수가 호출이 된다.



