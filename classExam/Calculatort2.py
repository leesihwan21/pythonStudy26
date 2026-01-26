# 영어 대문자를 사용하면 개발자들은 클래스로 알아먹음.
# 클래스는 대부분 파일명을 대문자로 만드는게 관례이다.
# 클래스는 인스턴스를 목적으로 만든다.

class Calculator:  # 파일명과 클래스명도 대문자로 똑같이 .
    # : 콜론으로 끝나기 때문에 들여쓰기가 중요함.

    # 내부에 함수(메서드)를 생성한다.
    def init (self):
        # 초기화 메서드 라고 생각하면됨. init self
        # 클래스 선언 시 기본적으로 실행되는 문법.
        self.result = 0 # 클래스가 생성되면서 변수를 생성함.

    def add(self, num):
        self.result += num # result = result + num
        return self.result

    def sub(self, num):
        self.result -= num # result = result - num
        return self.result

    def multiply(self, num):
        self.result *= num # result = result * num, 곱하기
        return self.result

    def divide(self, num):
        self.result /= num # result = result / num, 나누기
        return self.result


# class 선언 메서드 종료.
    # class는 일반적으로 부품이라고 생각하면됨.
        # crud가 class 안쪽에 들어가야함. 들여쓰기가 되어야함.
            # class 를 만들때 초기값 설정.
            # 회원을 클래스로 만들었으면 사용할 변수들 있어야함.
            # sns, ids, pws, names,,,
            # self ?? 그냥 주소임.
            # self.ids, self.pws, self.names, self.sns,,,etc
            # init 은 초기화(변수를)시켜준다는 뜻.

cal1 = Calculator() # 100번지라는 주소를 self로 씀
# 변수에 객체를 연결함.
cal2 = Calculator() # 101번지라는 주소를 self로 씀.
# 클래스를 사용하려면 변수에 연결해야함. (스택영역과 힘 영역에 연결)
# 이 떄 사용하는 주소가 self. 임.
# 객체(인스턴스) 생성과 변수 연결(self) 끝.


# 객체. 메서드(값) self로 연결된 주소의 객체를 찾아서
# .add(5) 실행한다. -> 메서드 실행 후 결과를 받음.
kkwresult = cal1.add(5)
print(kkwresult)

ksbresult = cal2.add(7)
print(ksbresult)

print(cal1.sub(10))
print(cal2.mul(9))
print(cal2.div(9))