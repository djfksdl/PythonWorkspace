# 숫자형 자료형
print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1))


# 문자형 자료형
print('풍선')
print("나비")
print("ㅋㅋㅋㅋ")
print("ㅋ"*9) # 문자와 숫자를 섞어서 쓸 수 있다


# boolean형
print(5 > 10)
print(5 < 10)
print(True)
print(False)
print(not True)
print(not False)
print(not (5 > 10))


# 변수

# 애원동물을 소개해 주세요

animal = "고양이"
name = "보리"
age = 4
hobby = "산책"
is_adult = age >=3

print("우리집 강아지의 이름은 연탄이예요")
print("연탄이는 4살이며, 산책을 아주 좋아해요")
print("연탄이는 어른일까요? True")

print("우리집" + animal + "의 이름은" + name +" 예요")

hobby = "낮잠" # 변수는 맨위, 중간등 아무곳이나 설정 가능함!

print(name +"는 "+ str(age) +"살이며," +hobby+ "을 아주 좋아해요") # 정수형을 문자로 바꿀때 쓸때는 str()로 써줘야한다.
print(name ,"는 "+ str(age), "살이며,", hobby,  "을 아주 좋아해요") # +말고, ,도 되는데 무조건 뒤에 한칸 띄워야함
print(name +"는 어른일까요?" + str(is_adult)) # boolean형도 마찬가지로 감싸줘야 오류 안남

''' 작은 따옴표 3개를 쓰면 
이렇게 여러줄 문장이 주석처리가 된다'''


# 퀴즈

# 변수를 이용하여 다음 문장 출력하기
# 변수명
# : station

# 변수값
# : "사당", "신도림". "인천공함" 순서대로 입력

# 출력문장
# : xx행 열차가 들어오고 있습니다.

station = "사당"

print( station+ '행 열차가 들어오고 있습니다.')
station = "신도림"
print( station+ '행 열차가 들어오고 있습니다.')
station = "인천공항"
print( station+ '행 열차가 들어오고 있습니다.')