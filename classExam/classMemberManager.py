# 클래스 (class) 를 활용한 회원관리 c,r,u,d 를 구현해보자.
from prompt_toolkit.key_binding.bindings.named_commands import self_insert

# ============================================================================

run = True  # while 에서 전체적으로 사용되는 변수(프로그램 구동)
session = None  # 로그인상태 저장용 -> 로그인한 사용자의 리스트 인덱스 기억용
FILE_NAME = "member.txt"  # 회원 정보를 저장할 메모장 파일명
members = ["kkw", "1234", "김기원", "admin", True]

# =============================================================================

import os

class MemberManager: # 객체를 담당하는 클래스. 사용법은 변수는 = membermanager() 생성.

    # class score,,class board,, 성적관리 게시판 이런 것들도 한번 코드 init 해서 해볼것.

    # 프로그램이 시작될 때, 파일을 미리 읽어오거나 데이터베이스(DB)에 연결하는 등 준비 작업을 자동으로 수행하게 할 때 사용함.
    # init 를 쓸 때 / 안 쓸 떄 차이점.
    # ex p = person("철수") 한줄로 끝. / p = person, p.name = 철수 두줄이 필요함.
    # 필수 데이터가 즉 변수가 없으면 에러를 내서 실수 방지 / 데이터(변수, 값)를 입력을 깜빡해도 객체는 만들어짐. (위험함)

    def __init__(self,filename="members.txt"): # 객체 생성 시, 만드는 기본값을 만드는 생성자. 초기값.(클래스 만들떈 init 필수)
        # 클래스에서 self 는 객체의 주소를 가지고 있음.
        # 클래스 함수 사용시 init 앞뒤로 언더바__ 두개 씩 붙여야
        # 초기화 함수로 작동함.. ?? 꼭 붙여야하나? # 클래스 함수 초기값 설정.
        self.filename = filename # 객체에 파일이름을 넣는다. # members.txt
        self.members = [] # 객체에 members. 리스트를 만든다. 2차원 배열.
        self.session = None # 객체에 session 변수를 로그인 상태 값 유지. 기본값으로 None 처리함. 정수타입
        self.load_members() # 아래에 선언된 메서드를 호출한다. load.member 를 호출함.


        # ========파일 로드(읽기)===========
    def load_members(self): # 앞으로 만들 메서드는 괄호안에 self가 필수. 왜? 객체에 있는 주소이기 때문에
        # __init__ 안에 넣었는지 그 이유가 무엇인지 이해가는지? 프로그램 실행과 동시에 데이터를 불러오기 위함)
        self.members = [] # 빈 배열로 생성. 왜? -> 이전에 리스트가 남아있을 수 있기 때문에...만약이라는 전제조건을 생각해야함.

        if not os.path.exists(self.filename):  # 동일 디렉토리에 파일명이 없으면. members.txt. 가 없으면.
            self.save.members() # save.members를 호출함. (open() 이라는 걸 이용해서 파일생성 할 수 있음.
            return # 함수를 빠져나와라. def load_members 함수를 빠져나와라.

        with open(self.filename, "r", encoding="utf-8") as f: # 이 문장 -> with 는 알아서 close 해줌. open은 파일을 여는것.
            # self.는 객체 초기값 self.filename = members.txt utf 한글처리 필수. f 라는 변수에 넣어라.
            for line in f: # 이 문장도 해석 -> f 변수에 잇는 파일 객체를 줄 단위로 반복하기 위해서. for 문을 사용함.
                line = line.strip() # 엔터제거
                if not line:
                    continue
                data = line.split()("|") # -> 이 문장 -> | 파이프를 기준으로 잘라 -> 1차원 리스트로 생성.
                # ["kkw","1234","김기원","admin","True"] 1차원 리스트 생성. True 라는 값이 문자열로 처리됨.
                # 리스트 5번째 값이 문자열로 True이면 불타입 True로 변경 아니면 False. 쌍따옴표를 없애줘라.
                data[4] = True if data[4] == "True" else False
                self.members.append(data) # -> 2차원 배열로 만든 members 맨뒤에 추가해라. for 문 종료시까지 append 추가해라.


        # ========파일 저장save============
    def save_members(self): # members 2차원 리스트 값을 파일로 덮어쓴다.
        # 파일에다가는 수정이 안되고 한꺼번에 다 불러와서 덮어쓴다. (중간수정도 불가능)
        # r, w, a -> read, write, add. 읽기 덮어쓰기 마지막에 추가용.

        with open(self.filename, "w", encoding="utf-8") as f:
            #  members.txt       덮어쓰기    한글처리 -> f 라는 변수에 넣어라.
            for member in self.members: # for 문. 메모리에 있는 members 2차원 리스트를 1줄씩 가져와
                # m 변수에 넣어라.
                # ["kkw","1234","김기원","admin","True"] = m. -> kkw | 1234 | 김기원 | admin | True > write 저장.
                # for 문 종료시까지.
                f.write(f"{members[0]},{members[1]},{members[2]},{members[3]},{members[4]}\n")


        # =========회원 가입==============
    def member_add(self): # self는 클래스의 객체 주소.
        print("회원가입 함수로 진입합니다.")
        print("\n 메뉴 선택")
        user_id = input("아이디 : ") # 키보드로 입력한 값을 uid 변수에 넣음.

        for member in self.members: # for 문.  load.member까지되어있는애들. 2차원 배열인 members에 1차원 리스트를 가져와 (1줄)
            if member[0] == user_id: # [0,1,2,3,4] -> 이 전체를 0번지라고 함. member 라는 변수안에. (uid, pw, name, role, active)
                print("이미 존재하는 아이디입니다.")
                return # def member add 라는 함수를 빠져나온다.
                # continue 를 하면 다시 for문으로 돌아감. break skip pass .... 어떤 결과가 나오는지 실험 해볼 것.
                # 중복 아이디가 없으면 아래쪽 코드 실행이 됨. return이 걸리지 않아서.-> else문 처리해도됨. -> 이렇게 해도 되나 들여쓰기가 필수.

            pw = input("비밀번호 : ")
            name = input("이름 : ")
            print("1. admin, 2. manager, 3. user")
            role = input("선택 : ")
            r = "user"
            if r == "1":
                role = "admin"
            elif r == "2":
                role = "manager"

            # 여기까지가 변수에 입력완료.
            self.members.append([user_id, pw, name, role, True])
            # 메모리에 있는 2차원 리스트 멤버스 뒤에 추가하는 것. .append()
            self.save.members() # 파일로 저장
            print("회원가입완료")

        # ============로그인================
    def member_login(self): # 함수는 self라는 걸 안씀, #  메서드는 self 함수를 사용함. 왜? 객체 주소이기 떄문에
        print("\n 메뉴 선택")
        user_id = input("아이디:")
        pw = input("비밀번호:")

        # enumerate() -> 2차원 배열을 인덱스와 리스트를 추출한다.
        for idx, member in enumerate(self.members):
            # i 값이 인덱스, m 이 member.
            # for 문 중에 같은 아이디가 있으면
            if member[0] == user_id: # m 0번에 uid,
                if not member[4]: # 4번에 active가 펄스냐.? 펄스가 아니면?
                    # active가 False 인지를 확인함.
                    print("비활성화된 계정입니다.")
                    return # def member login 함수를 빠져나와라.


            if member[1] == pw: # active가 True이면 m에 1번주소가 패스워드를 물어봄.
                self.session = idx # m 1번이 맞으면 session 에 인덱스를 넣어라. 회원의 주소.
                # 그럼 로그인 성공.
                print(f"{member[2]} 님 로그인 성공 ({member[3]})")

                if member[3] == "admin": # 관리자이면 m 3번주소가 member admin 메서드를 호출한다.
                    # 관리자 메뉴.
                    self.member_admin() # 메서드를 호출한다.
                    self.load.members()
                    return # member login 메서드를 빠져나온다.

            else: # 패스워드가 False 이면, 비밀번호 오류.
                print("비밀번호가 틀렸습니다.")
                return # def member login 함수를 빠져나온다.

            print("존재하지 않는 아이디입니다.") # for문이 return이 안걸리면 여기까지 온다.

        # ==============관리자,admin=============

    def member_admin(self): # 로그인 시 admin = role 이면 진입.
        print("\n관리자 메뉴 창")
        print("1. 비밀번호 변경")
        print("2. 블랙리스트")
        print("3. 권한변경")
        print("4. 종료")

        user_id = input("아이디:") # 아이디 찾는 용
        menu = input("선택:") # 관리자 메뉴 선택용

        for member in self.members: # members 에 2차원 배열을 반복함.
            if menu[0] == user_id: # 대상 아이디를 찾으면 menu에 0번이 uid와 같으면
                if menu == "1": # 1번이 비밀번호 변경
                    member[1] = input("비밀번호 :")
            elif menu == "2": # 2번이 블랙리스트
                member[4] = False # member 4번주소가 True가 아니면 False 처리함.(블랙리스트 처리함)
            elif menu == "3": # 3번이 권한변경
                member[3] == input("1. admin, 2. manager, 3. user")
                self.save_members() # self 에 save member 파일로 저장.
                print("관리자 작업 완료")

            print("존재하지 않는 아이디 입니다.")


        # =============로그아웃=================
    def member_logout(self):
        print("로그아웃 메뉴 입니다.")
        self.session = None # session에 있는 인덱스를 None 처리함.

        print("로그아웃 완료")


        # ==========내 정보 수정================

    def member_modify(self):
        print("회원정보수정")


        if session is None: # 현재 세션에 값이 None 이면 로그인 안했다는 얘기. 그래서 로그인이 필요하다.
            print("로그인 후 이용가능")
            return # def member modify 메서드를 빠져나온다.

        menu = input("회원정보수정 선택:")
        print("1. 비밀번호 변경:")
        print("2. 이름 변경:")

        menu = input("선택:")
        if menu == "1": # 1번을 누르면 비번변경
            self.members[self.session[2]] = input("새이름:")
            # 2차원배열     로그인 인덱스[] 2번은 안쪽에 있는 주소       암호필드
        elif menu == "2": # 2번을 누르면 이름변경
            self.members[self.session[1]] = input("새비밀번호:")
            # 2차원배열       로그인 인덱스[]         이름필드

        self.save.members() # self 안에 save.members 파일에 저장한다.
        print("회워정보수정완료")

     # ==========회원 탈퇴==============

    def member_delete(self):
        print("회원탈퇴메뉴")

        if session is None:
            print("로그인 후 이용가능")
            return

        print("\n 탈퇴")
        print("1. 영구탈퇴")
        print("2. 비활성화")

        menu = input("선택")

        if menu == "1":
            self.members.pop(self.session) # pop 쓰면 완전탈퇴 영구탈퇴
        elif menu == "2":
            self.members[self.session][4] = False
            self.session = None
            self.save_members() # 저장. 파일로 저장
            self.load.members() # load는 파일에 있는 걸 불러오는 건데 이것을 여기에다가 해야할지,
            # 아니면 while 문에서 사용할지 생각해야함.
            print("탈퇴완료")


        # ============ 기능에 대한 함수 생성=================

    def main_menu(self): # self 클래스를 활용한 회원관리 프로그램 코드 주 메뉴
        print(f"""
        ==== 엠비씨아카데미 회원관리(Class를 활용한, self) 프로그램입니다======
        1. 회원가입    2. 로그인     3. 로그아웃
        4. 회원정보수정      5. 회원탈퇴
        9. 프로그램 종료
        """)

    # 메인메뉴용 함수 종료

    def member_add_menu(self):  # 회원가입에서 사용할 메뉴
        print(f"""
        ----- 회원권한을 확인하세요.---------
        1. 관리자    2. 팀장    3. 일반사용자 
        """)

        # ============= 메뉴 함수 종료===================

    # =============== 주실행===============================
def run(self):
    while True:
        main_menu()
        menu = input(">>>")

        if menu == "1":
            self.member_add()
        elif menu == "2":
            self.member_login()
        elif menu == "3":
            self.member_logout()
        elif menu == "4":
            self.member_modify()
        elif menu == "5":
            self.member_delete()
        elif menu == "9":
            break


    # =============프로그램 시작==========================
app = MemberManager() # 가장 중요한 포인트 (지금까지 만든 클래스를 객체로 만들고 실행)
app.run() # 객체에 있는 .run() 메서드를 실행한다. 그러면 def run 메서드가 실행이 된다.