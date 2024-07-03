# 표준 입출력
print("Python", "Java", sep=",") # sep로 사이에 어떻게 나눌지 설정할 수 있음
print("Python", "Java", sep=" vs ") 

# 2줄에 걸쳐서 나오는걸 한줄에 나오게 할 수 있다.
print("Python", "Java", sep="," , end="?")
print("무엇이 더 재밌을까요?")

# 에러처리
# import sys
# print("Python", "Java", file=sys.stdout)
# print("Python", "Java", file=sys.stderr)

# 출력 포멧
scores = {"수학" : 0, "영어" : 50, "코딩": 100}
for subject, scores in scores.items():
    # print(subject, scores)
    print(subject.ljust(8), str(scores).rjust(4), sep=":") # left, right 라는 뜻인데 8자리,4자리 공간을 만들고 왼쪽 정렬해서 표시해달라

# 은행 대기 순번표
# 001, 002, 003, ...
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3)) # 3크기만큼의 공간 확보하고 값을 집어 넣는데 값이 없으면 0을 채우라는 뜻 , zfill은 0을 채우는것이란 뜻

# 표준 입력
# answer = input("아무값이나 입력하세요 : ")
# print(type(answer)) # string으로 나온다
# print("입력하신 값은 " + answer + "입니다.")


# 다양한 출력 포멧
# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))

# 양수일 떈 + 로 표시, 음수일 떈 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

# 왼쪽 정렬하고, 빈칸을 _로 채움
print("{0:_<+10}".format(500))

# 3자리마다 ,를 찍어주기
print("{0:,}".format(10000000000))

# 3자리마다 ,를 찍어주기 + 부호도 붙이기
print("{0:+,}".format(-1000000000))

# 3자리마다 ,를 찍어주기 + 부호도 붙이기 + 자릿수 확보 + 빈자리는 ^ 표시로 채워주기 
print("{0:^<+30}".format(100000000000000))

# 소수점 출력
print("{0:f}".format(5/3))

# 소수점을 특정 자리수 까지만 표시(소수점 3째 자리에서 반올림)
print("{0:.2f}".format(5/3))

# 파일 입출력

# 쓰기
# score_file = open("score.txt", "w", encoding="utf8") # w는 쓰기용도(덮어쓰기)
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close() # 파일은 닫는거까지 해줘야함

# 수정하기
# score_file = open("score.txt", "a", encoding="utf8") # a는 이어쓰기용도(append)
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100") # write는 줄 바꿈이 안되서 임의로 해줘야함
# score_file.close() 


# 읽어오기
# score_file = open("score.txt" , "r" , encoding="utf8") # r = read
# print(score_file.read())
# score_file.close()

# 한줄씩 읽어오기
# score_file = open("score.txt" , "r" , encoding="utf8") # r = read
# print(score_file.readline() ,end="") # 줄별로 읽기, 한 줄 읽고 커서는 다음줄로 이동
# print(score_file.readline() ,end="") # end는 줄바꿈 안하고 싶으면 ""로 써주면 됨
# print(score_file.readline() ,end="")
# print(score_file.readline() ,end="")
# score_file.close()

# 파일이 몇줄인지 모를때 반복문으로 불러옴
# 방법1
# score_file = open("score.txt", "r", encoding="utf8")
# while True : 
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

# 방법2
# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines() # list형태로 저장
# for line in lines : 
#     print(line, end="")
# score_file.close()


# pickle
# 데이터를 파일 형태로 저장하는것
import pickle
# profile_file = open("profile.pickle", "wb") # w:쓰기 목적, b:binery 타입 /인코딩은 따로 안해도 됨
# profile = {"이름": "박명수", "나이" : 30, "취미": ["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
# profile_file.close()

# 읽어오기
# profile_file = open("profile.pickle", "rb") # r:읽기 목적, b:binery 타입 /인코딩은 따로 안해도 됨
# profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()


# with
# 더 간단하게 파일을 읽을 수 있음
# with open("profile.pickle","rb") as profile_file: # as뒤에 있는 변수로 저장해주고 열어버림. 그리고 자동 종료까지
#     print(pickle.load(profile_file))

# 파일 쓰기
# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")

# 파일 읽어오기
# with open("study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.read())

''' 퀴즈
당신의 회사에서는 매주 1회 작성해야하는 보고서가 있습니다. 
보고서는 항상 아래와 같은 형태로 출력되어야 합니다. 

- x 주차 주간보고 - 
부서 : 
이름 : 
업무 요약 : 

1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오

조건 : 파일 명은 '1주차.txt', '2주차.txt',... 와 같이 만듭니다.

'''

for i in range(1, 51):
    with open(str(i) + "주차.txt","w", encoding="utf8") as report_file:
        report_file.write("- {0}주차 주간보고 - ".format(i))
        report_file.write("\n부서 : ")
        report_file.write("\n이름: ")
        report_file.write("\n업무 요약: ")
