# 클래스 용도로 파일을 생성하면 대묹자로 시자하는 게 관례.

class FourCal:
    # pass # 아무 동작 안하고 그냥 넘어감.

    # 변수 선언부가 있어야 하기 때문에 - > __init__ 가 원래 있어야함.
    def __init__(self):
        self.first = 0 # 변수 2개 선언함.
        self.second = 0 # 변수 2개 선언함.
        # 이렇게 코드 짜면 취약한 코드.
        # init 안에 변수 기능들,,,,생성자..

    # 메서드 선언부가 있어야함.

    # 세터와 게터를 이용해서 구현함.
    def setdata(self,first,second): # setdata는 값을 집어 넣는다고 생각하면됨.
        # a.first와 a.second를 직접 가서 처리가 가능하지만,
        # 하지만 검증을 해서 값을 처리하는 것도 필요함.
        # 데이터를 넣는 메서드를 세터라고 한다.

        if first <= 0 :   ## if 문부터 무슨 뜻인지? 어떻게 해석할건지?
            self.first = 0 ## 첫번쨰 조건에서 0이 작거나 같으면, self.first 값은 0이다. 참
        else:
            self.first = first ## 그 밖의 나머지 ,,, 값들이 self.first 가 첫번째 값이다....

        if second <= 0 :  ##
            self.second = 0 ##
        else:
            self.second = second

        if second <= 0: self.second = second
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result # 결과값을 다시 반환한다. 결과값을 리턴한다.

    def div(self):
        result = self.first / self.second
        # 나누는 값이 0이면 컴퓨터는 오류를 발생시킨다. 왜? 컴퓨터는 0으로 못나누기 떄문에 오류를 발생한다.
        # 근데 컴퓨터는 사람이 아니기 때문에 그렇다.
        return result


a = FourCal()
# a.first = 100  # 객체 변수에 바로 입력됨.
# a.second = 200 # 프로패셔날한 개발자는 이렇게 안 씀. 클래스에서는. 변조가 될 수 있기 때문에 바로 찍어내는걸 안함. 위조.
a.setdata(-10,10)
result1 = a.add()
print(f"-10+10을 : add()메서드 실행결과 : {result1}")

a = FourCal()
# a.first = 100
# a.second = 200

# 위 방법은 개발자들이 취약한 코드라고 판단함. 왜? 위,변조가 될 수 있기 때문에.
# 파이썬 프로그램도 위변조가 가능하기 떄문, 조심해야함. 검증은 무조건 하는게 좋음.

a = FourCal()
# a 변수에 FourCal() 클래스를 연결한다.
type(a)
print(type(a))
# <class '__main__.FourCal'>
# __main__ -> 모듈의 이름을 담고 있는 파이썬 내장변수 ,
# 최상위 코드가 실행되는 환경의 이름 (주 실행코드임)
# 건물에는 무조건 1층 입구가 있듯이, 프로그램 실행은 main_메인으로 판단을 함.

# >>> class FourCal:    이거는 맨 위에다 class 위에다가 써놓아야 함. 왜? 순서대로 해야하기 떄문에. 초기값으로 생각.
# ...     def __init__(self, first, second):
# ...         self.first = first
# ...         self.second = second
# ...     def setdata(self, first, second):
# ...         self.first = first
# ...         self.second = second
# ...     def add(self):
# ...         result = self.first + self.second
# ...         return result
# ...     def mul(self):
# ...         result = self.first * self.second
# ...         return result
# ...     def sub(self):
# ...         result = self.first - self.second
# ...         return result
# ...     def div(self):
# ...         result = self.first / self.second
# ...         return result


class MoreFourCal(FourCal):  # 종속. 부모로부터 종속된다는 뜻.
    #              부모객체 (+, -, *, /)
    #  부모객체의 모든 기능을 사용하면서 추가, 메서드를 만든다.
    # ex 전화기 -> 1세대 -> 전화벨울림/전화받음/전화끊음
    # 2세대 -> 위 기능에 문자, 사진, 카카오톡,,기능들 추가
    # 3세대는 2세대에 있는 기능이 다 들어와서 상속을 받고 , DMB를 본다.(추가)
    def pow(self):
        result = self.first ** self.second  # ** 제곱
        # 부모의 추가 메서드 (제곱처리)
        return result

    def div(self):
        # 부모와 같은 메서드 명.
        if self.second == 0:
            # 나누는 뒷 값이 0이면 나눌 필요도 없이 0을 리턴한다. 반환한다.
            return 0
        else:
            return self.first / self.second  # 0이 아니면 둘이 나눔.


c = MoreFourCal()
c.add() # 부모의 메서드 활용. 더하기
c.pow() # 자식의 추가 메서드.

# 메서드 오버라이딩.(부모가 만든 메서드를 튜닝할 때)
 #d = FourCal()
# d.setdata(8,0) # 첫번째 값이 8, 두번쨰 값이 0이라서 타입오류가 나옴.
# result = d.div()
# print(result)

e = MoreFourCal()
e.setdata(9,0)
result = e.div()    # 부모에서 개선된 자식 div() 메서드를 실햄함. 그러면, 부모꺼는 사용하지 못함. 왜? 자식이 "오버라이딩"을 했으니까.
print(result)

# 클래스 변수(필드) : __init__ , 일반 메서드에 바깥쪽 변수라고 생각하면 됨.

class Family: # 웬만하면 전역변수 사용하지 말것. 왜? 데이터를 다 쉐어링 하기 떄문에.
    lastname = "김"

    # 각 함수에 사용될 메서드들이 들어있음.변수, 기능들,,,
print(Family.lastname)

a = Family()
b = Family()
a.lastname = "최"

print(a.lastname)
print(b.lastname)