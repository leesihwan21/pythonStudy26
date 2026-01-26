from mbc_lms_function_exam.MemberExam import active


class Member:

    # member = Member ("id","pw", "name", "role")

    def __init__(self, uid, pw, name, role = "user", active = True): # 초기값을 설정해주기 위한 함수 __init__ Member 에 있는 리스트
        self.uid = uid # 아이디
        self.pw = pw # 비번
        self.name = name # 이름
        self.role = role # 권한 상태 확인 (admin / manager / user)
        self.active = active # 활성 / 비활성 유무

    def __str__(self): # print(member) 처리되는 용 (테스트용)
        status = "활성" if self.active else "비활성"
        return f"{self.uid} | {self.name} | {self.role} | {status}"
        # str 함수를 하는 이유는 str을 사용 안했을 시 print(member)로 출력했을 때 0x00000.... 나오기 떄문에
        # str 함수를 사용하면 문자열 그대로 처리한다는 뜻으로 사용함.

    def to_line(self): # 직렬화, 메모리에 있는 객체를 메모장으로 저장할 문자열로 변환
        return f"{self.uid}|{self.pw}|{self.name}|{self.role}|{self.active}"


    @staticmethod # 객체가 아니라 문자열로 처리. session.py에 @staticmethod 로 처리함
    def from_line(line: str): # 역직렬화 , 텍스트 파일에 저장되어 있는 문자열을 1줄씩 가로로 객체화(Member) 시킴.
        uid, pw, name, role, active = line.strip().split("|")
        return Member(uid, pw, name, role, active =(active == "True"))


    # 권한 상태 (role)==============================================================================================
    def is_admin(self):
        return self.role == "admin" # 지금 현재 객체가 admin??

    def is_manager(self):
        return self.role == "manager"  # 지금 현재 객체가 manager??

    # ============================================================================================================
    # def __init__(self, uid, pw, name, role = "True", active = True)
    #       self.role = role
    #       self.active = active
    #       self.uid = uid
    #       self.pw = pw
    #       self.name = name

    # def __str__(self):
    #     status = "활성" if self.active else "비활성"
    #     return f"{{self.uid} | {self.name} | {self.role} | {status}"

    # def to_line(line):
    #       return f"{self.uid}|{self.pw}|{self.name}|{self.role}|{self.active}"

    # @classmethod
    # def from_line(line : str):
    # uid, pw, name, role, active = line.strip().split("|")
    #   return Member(uid, pw, name, role, active = (active == "True"))

    # 권한상태
    # def is_admin(self):
    #      return self.role == "admin":
    # def is_manager(self):
    #      return self.role == "manager":
    # .