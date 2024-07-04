# 모듈 : 필요한것들끼리 묶음처럼 만들어진 파일같은것 ex) 자동차 바퀴만 교체 에서 바퀴가 모듈/ 부품만 갈면 유지보수 쉽고 수정이 좋다
# 함수나 클래스를 담고 있는것 : 모듈. 확장자가 py다 

# 일반가격
def price(people):
    print("{0}명 가격은 {1}원 입니다. ".format(people, people * 10000))

# 조조할인 가격
def price_morning(people):
    print("{0}명 조조 할인 가격은 {1}원입니다." .format(people, people* 6000))

# 군인 할인 가격
def price_soldier(people):
    print("{0}명 군인 할인 가격은 {1}원입니다." .format(people, people* 4000))
