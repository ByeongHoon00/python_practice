class BigNumberError(Exception):
    # pass
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return self.msg


try:
    print("한 자리 숫자 나누기 전용 계산기 입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 :"))
    num2 = int(input("두 번째 숫자를 입력하세요 :"))
    if num1 >= 10 or num2 >= 10:
        # raise ValueError # raise를 이용해 에러를 발생시킴
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2)) # 사용자가 정의한 예외처리
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))

except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
except BigNumberError as err:
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
    print(err)
finally: # 에러가 일어나드 일어나지 않든 처리 후 프로그램이 종료되지 않고 finally구문이 실행된다.
    print("계산기를 이용해 주셔서 감사합니다.")