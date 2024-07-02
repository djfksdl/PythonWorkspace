# 문자열
sentence = '나는 소년입니다'
print(sentence)

sentence2 = "파이썬은 쉬워요"
print(sentence2)

sentence3 = """
나는 소년이고, 
파이썬은 쉬워요
"""
print(sentence3)


# 슬라이싱
jumin = "990120-1234567"

print("성별 : " + jumin[7]) # 7번째 문자를 가져옴
print("연 : " + jumin[0 : 2]) # 0번째부터 2번째직전의 문자를 가져옴 = (0 , 1)
print("월 : " + jumin[2 : 4])
print("일 : " + jumin[4 : 6])

print("생년월일 : " + jumin[: 6]) # 처음부터 6 직전까지(맨처음부터 시작한다면 생략가능)
print("뒤 7자리 : " + jumin[7 :]) # 끝까지면 생략가능 : [ 7 : 14]
print("뒤 7자리 (뒤에서부터) " + jumin[ -7: ]) # 맨 뒷자리는 -1로 시작. 마찬가지로 생략가능 


# 문자열 처리 함수
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper()) # True : 0번째가 대문자인지 물어봄
print(len(python)) # length와 같이 길이를 알려줌
print(python.replace("Python", "Java"))

index = python.index("n") # n이 몇번째에 있는지
print(index) # 5
index = python.index("n" , index + 1) # n을 찾는데 (찾는거,start위치)라서 처음 찾은 n의 위치보다 +1한 다음위치부터 n을 찾을 수 있다.
print(index)


# find 함수 : 원하는 값 없을때 -1가 나옴. index는 오류남
print(python.find("n")) # 5

print(python.find("Java")) # -1
# print(python.index("Java")) # 오류남


# count함수 : n이 총 몇번 등장하는지 
print(python.count("n"))


# 문자열 포멧
print("a" + "b")
print("a", "b")

# 방법1 : % 사용
print("나는 %d살입니다." % 20) # 정수만 가능
print("나는 %s를 좋아해요." % "파이썬") # string(문자열)만 가능
print("Apple은 %c로 시작해요" % "A") # 한 글자만 가능

# %s는 정수,문자열,문자 다 가능
print("나는 %s살입니다." % 20)

# 여러개를 넣을때
print("나는 %s색과 %s색을 좋아해요" %("파란" , "빨간"))


# 방법2 : {}사용
print("나는 {}살입니다." .format(20))
print("나는 {}색과 {}색을 좋아해요" .format("파란" , "빨간"))
print("나는 {0}색과 {1}색을 좋아해요" .format("파란" , "빨간"))
print("나는 {1}색과 {0}색을 좋아해요" .format("파란" , "빨간"))


# 방법3 : {}, 변수 사용
print("나는 {age}살이며, {color}색을 좋아해요" .format(age = 20 , color = "빨간"))
print("나는 {age}살이며, {color}색을 좋아해요" .format(color = "빨간" , age = 20 ))


# 방법4 (v3.6이상~):
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")


# 탈출 문자
print("백문이 불여일견 백견이 불여일타")

# \n : 줄바꿈
print("백문이 불여일견\n백견이 불여일타")

# 저는 "나도 코딩입니다"
print("저는 '나도코딩'입니다.")
print('저는 "나도코딩"입니다.')
# 맨날 ""로 문자를 시작하다가 ''로 쓰기 싫어서 이때 쓰는게 탈출 문자다!: \ 활용
print("저는 \"나도코딩\" 입니다.")
print("저는 \'나도코딩\' 입니다.")

# \\ : 문장 내에서 하나의 \로 인식됨
print("C:\\PythonWorkspace")

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine") # 커서를 맨앞으로 이동해서 Red만큼을 Pine으로 다시 씀

# \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple")

# \t : 탭
print("Red\tApple")

# 퀴즈3
"""
사이트 별로 비밀번호를 만들어주는 프로그램을 작성하시오
예) http://naver.com

규칙1 : http://부분은 제외 => naver.com
규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
규칙3 : 남은 글자 중 처음 세자리 + 글자 개수 + 글자 내 'e'개수 + "!"로 구성

=> 생성된 비밀번호 :  nav 5 1 !
"""

print("퀴즈")

# 내가 푼 방법
url = "http://naver.com"

my_str = url[7:-4]
print(my_str)

three = my_str[0:3]
print(three)

index = len(my_str)
print(index)

cnt = my_str.count("e")
print(cnt)

print("생성된 비밀번호 : " + three + str(index) + str(cnt) + "!")


# 풀이
# url = "http://naver.com"
url = "http://google.com"

# 규칙1
my_str = url.replace("http://","")
print(my_str)

# 규칙2
my_str = my_str[:my_str.index(".")]
print(my_str)

# 규칙3
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print(password)


print("{0}의 비밀번호는 {1}입니다. " .format(url , password))


