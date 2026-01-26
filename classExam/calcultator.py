# 클래스는 주로 같은 내용에 변수 및 메서드를 모아서 처리하는 용도.
# 인스턴스(Instance) : 객체를 복제해서 같은 변수나 메서드를 찍어내는 효과.
# LMS 프로그램을 지금처럼 콘솔에 출력하면 1인용인데,
# 클래스로 콘솔에 출력하면 다인용(여러명)이 접근해서 사용할 수도 있다. - > FLASK, FastAPI - > 웽 서버

# 변수 선언 할 때 글로벌(global) 영역에 선언하면 session -> 데이터 및 값, 자료를 공용으로 사용함.(공유)
# 클래스가 아닌 일반 사항으로 처리하면 1명이 로그인 하면
# 다른 사람이 접속할 떄 이미 로그인 한 상태가 됨.

result = 0 # result 는 결과값 이라는 영문.
result2 = 0

def add(number):            # 함수 생성 -> number를 받아서
    global result           # 전역변수를 가져와 0값을 가지고 있음
    result += number        # result = result + number
    return result           # return은 결과를 내보냄.
# add() 함수 만듬 끝.

def add2(number):           # 함수명만 다름.
    global result2
    result2 = result + number    # result += number
    return result2

print(add(5))
print(add2(9))      # 5 더하기 9는 14.
print(add(2))
print(add2(4))     # -> 5 더하기 2 는 7, 7 더하기 4는 11.
# 글로벌 영역에 있는 result, result2를 공유함.
# 단점은 혼자 프로그램을 사용하지 않으면?
# 여러명이 add() 함수를 사용하려면 여러명 만큼 함수와 변수를 생성해야함.


