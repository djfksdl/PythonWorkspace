# 예외처리 : 에러가 발생했을때 처리해주는거

# try:
#     print("나누기 전용 계산기 입니다")

#     nums = []
#     nums.append(int(input("첫번째 숫자를 입력하세요 : ")))
#     nums.append(int(input("두번째 숫자를 입력하세요 : ")))
#     # nums.append(int(nums[0]/nums[1])) 이렇게 하면 index어쩌고 에러가 나옴. 근데 그냥 한꺼번에 처리하고자 except만 쓰기

#     print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))

# except ValueError: # int가 아닌 값을 입력하였을떄
#     print("에러! 잘못된 값을 입력하였습니다")
# except ZeroDivisionError as err: # 0으로 나눌 수 없다
#     print(err)
# except Exception as err: # except만 써도 되는데 err메세지까지 출력하려면 err 써주기
#     print("알 수 없는 에러가 발생하였습니다")
#     print(err)


# 에러 발생시키기 
# try: 
#     print("한 자리 숫자 나누기 전용 계산기 입니다")
#     num1 = int(input("첫번째 숫자를 입력하세요 : "))
#     num2 = int(input("두번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise ValueError # raise를 통해 에러를 발생시킬 수 있음 = > 그럼 이후 문장은 실행되지 않고 밑에 예외처리 문장이 출력된다.
#     print("{0} / {1} = {2}".format(num1, num2, int(num1 /num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한자리 숫자만 입력하세요")


# 사용자 정의 예외처리 
# class BigNumberError(Exception):
#     # pass
#     # 메세지 넣고싶다하면 pass지우고
#     def __init__(self, msg): 
#         self.msg = msg
#     def __str__(self):
#         return self.msg
    
# try: 
#     print("한 자리 숫자 나누기 전용 계산기 입니다")
#     num1 = int(input("첫번째 숫자를 입력하세요 : "))
#     num2 = int(input("두번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise BigNumberError("입력값 : {0}, {1}".format(num1, num2)) # 사용자 정의 예외처리 / 메세지 쓰면 밑에 err로 출력
#     print("{0} / {1} = {2}".format(num1, num2, int(num1 /num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한자리 숫자만 입력하세요")
# except BigNumberError as err:
#     print("에러가 발생하였습니다. 한자리 숫자만 입력하세요")
#     print(err)

# # finally : 오류가 발생되건 잘 되건 무조건 실행됨
# finally : 
#     print("계산기를 이용해 주셔서 감사합니다.")


''' 퀴즈
동네에 항상 대기 손님이 있는 맛있는 치킨집이 있습니다. 
대기 손님의 치킨 요리 시간을 줄이고자 자동 주문 시스템을 제작하였습니다. 
시스템 코드를 확인하고 적절한 예외처리 구문을 넣으시오.

조건1 : 1보다 작거나 숫자가 아닌 입력값이 들어올 떄는 ValueError로 처리
        출력 메세지 : "잘못된 값을 입력하셨습니다. "
조건2 : 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정
        치킨 소진 시 사용자 정의 에러[SoldOutError]를 발생시키고 프로그램 종료
        출력 메세지 : "제고가 소진되어 더 이상 주문을 받지 않습니다. "
        
'''

chicken = 10
waiting = 1 # 홀 안에는 현재 만석. 대기번호 1부터 시작

class SoldOutError(Exception):
    pass
    

while(True):
    try : 
        print("[남은 치킨] : {0}" .format(chicken))
        order = int(input("치킨 몇 마리 주문하시겠습니까?"))
        if order > chicken :  # 남은 치킨보다 주문량이 많을 떄
            print("재료가 부족합니다")
        elif order <= 0 :
            raise ValueError
        else:
            print("[대기번호 {0}] {1}마리 주문이 완료 되었습니다."\
                .format(waiting, order))
            waiting += 1
            chicken -= order
        if chicken == 0:
            raise SoldOutError
    except ValueError:
        print("잘못된 값을 입력하셨습니다. ")

    except SoldOutError:
        print("제고가 소진되어 더이상 주문을 받지 않습니다.")
        break # while문 탈출(프로그램 종료)