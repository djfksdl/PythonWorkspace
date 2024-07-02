# 리스트 []

# 지하철 칸 별로 10명, 20명, 30명 
subway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20, 30]
print(subway)

subway = ["유재석","조세호","박명수"]
print(subway)

# 조세호가 몇번째 타고 있는가? 
print(subway.index("조세호"))

# 하하가 다음 정류장에서 다음 칸에 탐
subway.append("하하")
print(subway)

# 정형돈이 유재석 - 조세호 사이 칸에 탐
subway.insert(1,"정형돈")
print(subway)

# 지하철에 있는 사람을 한명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인 
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬도 가능
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

# 순서 뒤집기 가능
num_list.reverse()
print(num_list)

# 모두 지우기 
num_list.clear()
print(num_list)

# 다양한 자료형 함께 사용 가능
mix_list = ["조세호", 20, True]
print(mix_list)

# 리스트 확장
num_list2 = [5,2,4,3,1,0]
num_list2.extend(mix_list)
print(num_list2)


# 사전 1:32:09
# {키: 벨류} 식으로 구성이 됨
cabinet = {3 : "유재석" , 100: "김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
# print(cabinet[5]) # 이렇게 하면 오류나고 프로그램 종료됨
print(cabinet.get(5)) # 이렇게 하면 None만 뜨고 정상적으로 작동된다.
print(cabinet.get(5, "사용가능")) # 이렇게 하면 None대신 뒤에 있는 값이 기본 디폴트 값으로 적용된다.
print("hi")

# 사전안에 값이 존재하는지 확인하는 방법
print(3 in cabinet) # True
print(5 in cabinet) # False

# 키 값은 숫자 뿐 아니라 문자형도 가능
cabinet2 = {"A-3" : "유재석" , "B-100" : "김태호"}
print(cabinet2["A-3"])
print(cabinet2["B-100"])

# 새 손님
print(cabinet2)
cabinet2["A-3"] = "김종국"
cabinet2["C-2"] = "조세호"
print(cabinet2)

# 간 손님
del cabinet2["A-3"]
print(cabinet2)

# key 들만 출력
print(cabinet2.keys())

# values 들만 출력
print(cabinet2.values())

# key, value쌍으로 출력
print(cabinet2.items())

# 목욕탕 폐점 - 모두 삭제
cabinet2.clear()
print(cabinet2)



# 튜플 - 속도가 리스트보다 빠른 대신 리스트처럼 내용 변경,추가를 할 수 없다 -> 변경되지 않는걸 사용할때 사용됨

menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

# menu.add("생선까스") - 아예 안됨

name = "김종국"
age = 20
hobby = "코딩"
print(name , age, hobby)

(name , age, hobby) = ("김종국" , 20 , "코딩")
print(name , age, hobby)


# 집합(set) 
# 중복 안됨, 순서 없음
my_set = {1,2,3,3,3} # 사전에서는 {키,벨류}로 사용했는데 set은 값만 쓰면 된다.
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 (java와 pytho을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# 합집합 (java도 할 수 있거나 python도 할 수 있는 개발자 : 순서가 보장되지 않음
print(java | python)
print(java.union(python))

# 차집합(java를 할 수 있지만 python은 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))

# python을 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

# java를 까먹음
java.remove("김태호")
print(java)


# 자료구조의 변경
menu = {"커피", "우유","주스"}
print(menu , type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu , type(menu))

# 퀴즈 
'''
당신의 학교에서는 파이썬 코딩 대회를 주최합니다. 
참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다. 
댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.

조건1: 편의상 댓글은 20명이 작성하였고 아이디는 1~20이라고 가정
조건2: 댓글 내용과 상관없이 무작위로 추첨하되 중복 불가
조건3: random 모듈의 suffle과 sample을 활용

출력 예제)
-- 당첨자 발표 --
치킨 당첨자 : 1
커피 당첨자 : [2 ,3, 4]
-- 축하합니다 --

# 활용 예제
from random import *
lst = [1,2,3,4,5]
print(lst)
shuffle(lst)
print(lst)
print(sample(lst,1)) # lst중에서 1개를 무작위로 뽑는것

'''

from random import *
users = range(1 , 21) # 1부터 20까지 숫자를 생성
print(type(users)) # range라고 type이 되는데 그럼 list에 있는 함수를 못씀
users = list(users) # 따라서 type변경
print(type(users))

print(users)
shuffle(users)
print(users)

winners = sample(users ,4)
print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}" .format(winners[0]))
print("커피 당첨자 : {0}" .format(winners[1:]))
print("-- 축하합니다 --")


