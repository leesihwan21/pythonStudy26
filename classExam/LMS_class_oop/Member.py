# 파이썬에 oop를 적용해본다.
# oop 객체 지향 프로그래밍, Object-Oriented Programming
# 현실 세계의 '객체' 개념을 기반으로 데이터를 속성(데이터)과
# 행위(메서드)로 묶어 관리하고,

# 지금까지는 2차원 배열을 이용해서 인덱스로 데이터에 접근을 하는데, ex 리스트 [   ,    ,    ,  ]
# [0] 이곳에 무엇이 들어있는지 암기를 하고 [4]는 무엇이 들어갈 지 - > 이런것들을 생각을 했어야 했는데.
# 각각의 메모장에 한 줄로 되어있는 자료를 클래스로 만들면
# Member.name / Member.id / Member.pw 등으로 접근할 수 있다. -> 직관적이 됨. 근데 이것도 한두번이라 헷갈려서 꼬일수있다.

# Member.py는 개인의 객체 -> 변수와 게터(나오는값처리)/세터(입력값처리) 등을 담당함.
# -> 게터 : 값을 가져오는 것. 세터 : 값을 집어넣을 때 검증하는 것.
# MemberService.py는 CRUD용 메서드 들이 들어있는 모듈
# main은 주 실행 코드

# =========================================================================================================
# 면접시 물어보는 내용
# 직렬화, 역직렬화
# 직렬화(Serialization) : 객체 -> 저장 가능한 형태, 메모리에 있는 걸 파일에 저장하는 걸 직렬화
#       member.to_line() 이 직렬화

# 역직렬화(Deserialization) : 저장된 데이터를 -> 객체로 만들 떄 사용함. (@classmethod) 라고 했던 게 역직렬화
#       Member.from_line(line) 이 역직렬화 -> 한 줄로 데이터를 만드는 것.
# =========================================================================================================

# 회원 각각의 자료를 리스트가 아닌 변수에 담아 제공하려고 함.

class Member: # 클래스는 무조건 대문자로 시작해야함.
    def __init__(self, uid, pw, name, role = "user", active = True):
        self.id = uid           # id
        self.pw = pw            # pw
        self.name = name        # 이름
        self.role = role        # 권한
        self.active = active    # 활성화

# 이거는 무조건 맞춰야 함.
# 클래스는 무조건 대문자 사용해야 함.
# 얘를 호출하면 이름으로 쓸 수 있음. member.id, member.pw ,,,
# 사용방법 : member -> 변수 = Member(), 객체 -> 객체를 생성핳여 변수에 연결
# 이름 : Member.id
# 암호 : Member.pw

# 파일 저장용 문자열 변환 코드
    def to_line(self):
        return f"{self.id}|{self.pw}|{self.name}|{self.role}|{self.active}\n"

# 사용법 member = Member()
# member.to_line() -> kkw|1234|김기원|admin|True엔터
# 메모장에 기록용 -> kkw|1234|김기원|admin|True엔터

# 파일에서 불러온 내용 객체 처리
@classmethod # 객체 (self) 가 아니라, 클래스 자체를 (cls) 다루는 메서드라고 정의
def from_line(cls, line): # line : 메모장의 1줄 문자열
    uid, pw, name, role, active = line.strip().split("|")
    #      변수들에 넣는다.  <-  1줄 문자열에 엔터를 지우고 | 로 잘라서

    return cls(uid, pw, name, role, active) == "True"


