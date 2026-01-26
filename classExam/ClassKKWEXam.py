# 클래스 공부해본다.
from http.cookiejar import Cookie

# ====================================================================================================================

result = 0 # 전역변수 글로벌
class  FourCal:

    def add(num):
        global result
        result += num
        return result
    # print(add(3))  # 맨 처음 펄스트 값 3
    # print(add(4))  # 세컨드 값 3+4 는 7

    result1 = 0
    result2 = 0

    def add1(num):
        global result1
        result1 += num
        return result1

    def add2(num):
        global result2
        result2 += num
        return result2
    # print(add(3))
    # print(add(4))

# ===================================================================================================================

class Calculator:
    def init (self,first,second): # 함수 초기값 설정, 변수, 기능들, ex 회원관리....회원아이디, 회원비번, 회원명, 기타등등...
        self.first = 0
        self.second = 0

# cal1 = Calculator() # calculator 클래스로 만든 별도의 계산기 cal1, cal2 (파이썬에서는 이것을 객체라고 부른다.) 객체라는 건
# object 라는 건데, 틀 안에 있는 객체 즉, 부모가 있으면 자식이 있다는 개념으로 알면 편하다.
# cal2 = Calculator()
# 클래스란 똑같은 무엇인가를 계속 반복적으로 만들어 낼 수 있는 "공장"과 같은 개념이다. 왜? 공장은 계속해서
# 찍어내니까. 똑같은ㅇ 제품을 똑같은 시간에 똑같은 행동과 이런 것들,,,,똑같은 장소에서,,,, 그러기 떄문에 다른 과자에는 아무런 영향이 없는
# 것과 마찬가지로 동일한 클래스로 만든 객체들은 서로 영향을 주지 않는다.
    def setdata(self,first,second): # setdata 는 def init 함수를 이용해서 값을 선언한 변수들을 setdata에 값을 넣어주는 기능을 함.
        self.first = first
        self.second = second

        if self.first <= 0:
            self.first = 0
        else:
            self.first = 0 # if 가 첫번째 값 0이면 참.

        if self.second <= 0:
            self.second = 0
        else:
            self.second = 0

        if second <= 0 : self.second = 0
        else:
            self.second = 0

    def add(self):
        result = self.first + self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def div(self):
        result = self.first / self.second
        return result

# =======================================

# a = FourCal()
#a.setdata(4,2)
# a.add()

class FourCal:
    def setdata(self,first,second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result
a = FourCal()
a.setdata(4,2)
a.add()



