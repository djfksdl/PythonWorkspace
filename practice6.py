# 함수

def open_account():
    print("새로운 계좌가 생성되었습니다.")

open_account()


# 전달값과 반환 값
def deposit(balance, money) : # 입금
    print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money): # 출금
    if balance >= money: # 잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은{0}원 입니다." .format(balance))
        return balance

def withdraw_night(balance , money) : #저녁에 출금
    commission = 100 # 수수료 100원
    return commission, balance - money -commission


balance = 0 # 잔액
balance = deposit(balance, 1000)
# balance = withdraw(balance, 2000)
# balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance, 500)
print("수수료 {0}원이며, 잔액은{1}원입니다.".format(commission, balance))


# 기본값
# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t주 사용언어 : {2}" \
#           .format(name, age, main_lang)) # 이렇게 하면 하나의 문장으로 인식됨

# 같은 학교 같은 학년 같은 반 같은 수업
def profile(name, age=17, main_lang="파이썬"):
    print("이름 : {0}\t나이 : {1}\t주 사용언어 : {2}" \
          .format(name, age, main_lang))

profile("유재석")
profile("김태호")


# 키워드 값
def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name="유재석", main_lang="파이썬", age=20)
profile(main_lang="자바", age=25, name="김태호")


# 가변 인자
# def profile(name, age, lan1, lan2, lan3, lan4, lan5):
#     print("이름: {0}\t 나이:{1}\t".format(name, age), end="") # 이문장 출력하고나서 줄바꿈 되는게 아니라 한칸 띄우고 계속 나온다는것!
#     print(lan1, lan2, lan3, lan4, lan5)

# profile("유재석", 20, "Python", "Java", "C", "C++", "C#")
# profile("김태호", 20, "Kotlin", "Swift", "C", "", "","")

def profile(name, age, *language): # 내가 원하는 만큼 쓰겠다 *
    print("이름: {0}\t 나이:{1}\t".format(name, age), end="") # 이문장 출력하고나서 줄바꿈 되는게 아니라 한칸 띄우고 계속 나온다는것!
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석", 20, "Python", "Java", "C", "C++", "C#")
profile("김태호", 20, "Kotlin", "Swift", "C")


# 지역변수와 전역변수
# 지역변수
# gun = 10
# def checkpoint(soldiers): # 경계근무
#     gun = 20 # 초기화를 지역변수로 초기화해줘야함. 안그럼 값 할당도 안되었는데 사용되었다고 오류남
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}" .format(gun))

# print("전체 총 : {0}".format(gun))
# checkpoint(2) # 2명이 경계 근무 나감
# print("남은 총 : {0}".format(gun))

# 전역변수 : 너무 많이 쓰면 복잡하니까 권장되진 않음
gun = 10
def checkpoint(soldiers): # 경계근무
    global gun # 전역 공간에 있는 gun을 사용하겠다
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}" .format(gun))

def checkpoint_ret(gun, soldiers): # 이렇게 쓰면 지역변수로써 쓸 수 있음
    gun = gun-soldiers
    print("[함수내] 남은 총 : {0}" .format(gun))
    return gun

print("전체 총 : {0}".format(gun))
# checkpoint(2) # 2명이 경계 근무 나감
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))

''' 퀴즈)
표준 체중을 구하는 프로그램을 작성하시오

* 표준 체중 : 각 개인의 키에 적당한 체중

(성별에 따른 공식)
 남자 : 키(m) X 키(m) X 22
 여자 : 키(m) X 키(m) X 21

조건1 : 표준 체중은 별도의 함수 내에서 계산
     * 함수명 : std_weight
     * 전달값 : 키(height) ,성별(gender)
조건2 : 표준 체중은 소수점 둘째자리까지 표시

(출력 예제)
키 175cm 남자의 표준 체중은 67.38kg입니다.

'''

def std_weight(height,gender): # 키 m 단위(실수) , 성별: 남자/여자
    if gender == "남자" :
        return  height*height*22
    else :
        return height*height*21

height = 175
gender= "남자"
weight = round(std_weight(height / 100, gender),2)
print("키 {0}cm {1}의 표준 체중은 {2}kg입니다." .format(height, gender, weight))