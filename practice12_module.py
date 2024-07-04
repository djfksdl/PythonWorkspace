# 모듈은 불러오려는 파일과 같은 경로에 있거나 파이썬 라이브러리들이 모여있는 파일에 모듈이 있어야 모듈 사용이 가능하다. 

# 1. 모듈 사용
# import theater_module
# theater_module.price(3) # 3명이서 영화 보러 갔을떄 가격
# theater_module.price_morning(4) # 4명이서 조조 할인 영화 보러갔을떄
# theater_module.price_soldier(5) # 5명의 군인이 영화 보러갔을떄


# 2. 모듈 명이 길때 별명 설정
# import theater_module as mv
# mv.price(3) # 3명이서 영화 보러 갔을떄 가격
# mv.price_morning(4) # 4명이서 조조 할인 영화 보러갔을떄
# mv.price_soldier(5) # 5명의 군인이 영화 보러갔을떄

# 3. 모듈에 있는 모든 함수를 쓰겠다
# from theater_module import *
# price(3)
# price_morning(4)
# price_soldier(5)

# 4. 모듈에 있는 부분 함수만 사용
# from theater_module import price, price_morning
# price(3)
# price_morning(6)
# price_soldier(5) 이건 쓴다고 안했기 떄문에 오류남

# 5. 모듈에 있는 부분 함수에 별명 설정
# from theater_module import price_soldier as price
# price(5)


# 패키지 : 모듈 여러개 모여있는것
# import travel.thailand
# import travel.thailand.ThailandPackage # 오류남. 이런식으로는 사용 불가능 -> from import에서는 가능하다
# trip_to = travel.thailand.TailandPackage()
# trip_to.detail()

# from import 에서는 모듈, 패키지, 클래스 함수등 모두 쓸 수 있다. 
# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# 파일에서 모듈을 import해도 됨
# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()


# __all__
# # from random import * 
# from travel import * # 오류남. *은 모든걸 가져오겠다는건데 ,공개범위를 설정해줘야함. travel에서 비공개 공개 설정을 할 수 있다 .-> init에서 __all__설정하기
# trip_to = vietnam.VietnamPackage()
# trip_to = thailand.TailandPackage() 
# trip_to.detail()


# 패키지 모듈 위치
# import inspect
# import random
# print(inspect.getfile(random)) # 이 파일이 어디에 있는지 알 수 있다
# print(inspect.getfile(thailand))


# pip install
# https://pypi.org/
# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())

# pip list를 터미널에 입력하면 설치되어있는 패키지 내용에 대해서 볼 수 있다. 
# pip show beautifulsoup4 터미널에 입력하면 관련 정보 볼 수 있다. 
# pip install --upgrade beautifulsoup4 하면 버전 업그레이드도 할 수 있다. 
# pip uninstall beautifulsoup4 하면 버전 업그레이드도 할 수 있다. 


# 내장함수 : 이미 내장되어있어서 import따로 안해도 쓸 수 있다. 
# input : 사용자 입력을 받는 함수 
# language = input("무슨 언어를 좋아하세요?")
# print("{0}은 아주 좋은 언어 입니다!".format(language))

# dir : 어떤 객체를 넘겨줬을때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
# print(dir())
import random # 외장함수
# print(dir()) # random이 추가가 됨

# import pickle
# print(dir()) # pickle도 추가됨

# print(dir(random)) # random모듈내에서 쓸수 있는걸 보여줌

# lst = [1,2,3]
# print(dir(lst))

# name = "lee"
# print(dir(name))

# google에 list of python builtins 검색하면 쓸 수 있는 함수를 볼 수 있음


# 외장 함수: import해서 사용해야함
# google에서 list of python modules 검색하면 외장함수 목록을 볼 수 있다. 

# glob : 경로내의 폴더/ 파일 목록 조회 (윈도우 dir)
import glob
print(glob.glob("*.py")) # 확장자가 py인 모든 파일

# os : 운영체제에서 제공하는 기본 기능
import os
# print(os.getcwd()) # 현재 디렉토리

# folder = "sample_dir"

# if os.path.exists(folder): 
#     print("이미 존재하는 폴더 입니다.")
#     os.rmdir(folder)
#     print(folder, "폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder) # 폴더 생성
#     print(folder, "폴더를 생성하였습니다. ")

# print(os.listdir())

# time : 시간 관련 함수
import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))

import datetime
print("오늘 날짜는 ", datetime.date.today())

# timedelta : 두 날짜 사이의 간격
today = datetime.date.today() # 오늘 날짜 저장
td = datetime.timedelta(days=100) # 100일 저장
print("우리가 만난지 100일은 ", today + td) # 오늘부터 100일 후


''' 퀴즈
프로젝트 내에 나만의 시그니처를 남기는 모듈을 만드시오

조건 : 모듈 파일명은 byme.py로 작성

(모듈 사용 예제)
import byme
byme.sign()

(출력예제)
이 프로그램은 나도코딩에 의해 만들어졌습니다. 
유튜브 : http://youtube.com
이메일 : nadocoding@gmail.com

'''
import byme
byme.sign()


