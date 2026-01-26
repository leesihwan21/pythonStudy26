
import os

from Member import Member


class MemberService:
    def __init__(self, file_name="members.txt"):
    # 클래스가 생성할때 초기값 관리
        self.file_name = file_name
        self.members = []  # 회원들을 리스트로 만들어 Member()객체를 담는다.
        self.session = None # 로그인상태를 담당(members의 인덱스 보관용)
        self.load_members() # 아래쪽에 메서드 호출

    def run(self):
        # 부메뉴 (sub_menu) 구현 메서드 (함수)
        subrun = True
        while subrun:
            print("""
========= 안녕하세요. 엠비씨 아카데미 LMS 회원관리 프로그램에 오신걸 환영합니다. ==============
            
            1. 로그인
            2. 회원가입
            3. 회원정보수정
            4. 회원탈퇴
            5. 로그아웃

            9. 회원 서비스 종료
====================================================================================            
            """)

            subselect = input(">>>")

            if subselect == "1":  # 프로그램 구동시 각 함수를 호출할 때 클래스 함수를 사용하면 self.login을 넣어줘야한다.
                self.member_login()
                print("로그인 메서드 호출")

            elif subselect == "2":
                self.member_add()  # 프로그램 구동시 각 함수를 호출할 때 클래스 함수를 사용하면 self.register을 넣어줘야한다.
                print("회원가입 메서드 호츨")

            elif subselect == "3":
                self.member_modify()  # 프로그램 구동시 각 함수를 호출할 때 클래스 함수를 사용하면 self.modify을 넣어줘야한다.
                print("회원정보수정 메서드 호출")

            elif subselect == "4":
                self.member_delete()  # 프로그램 구동시 각 함수를 호출할 때 클래스 함수를 사용하면 self.delete을 넣어줘야한다.
                print("회원탈퇴 메서드 호출")

            elif subselect == "5":
                self.member_logout()  # 프로그램 구동시 각 함수를 호출할 때 클래스 함수를 사용하면 self.logout을 넣어줘야한다.
                print("로그아웃 메서드 호출")

            elif subselect == "9":
                print("회원서비스종료")
                subrun = False

            else:
                print("잘못된 메뉴를 선택하였습니다.")
                print("다시 선택하세요.")

    # =============== 파일 로드 (읽기) =======================
    def load_members(self):
        self.members = []

        if not os.path.exists(self.file_name):
            self.save_members()
            return

        with open(self.file_name, "r", encoding="utf-8") as f:
            for line in f:
                data = line.strip().split("|")
                data[4] = True if data[4] == "True" else False
                self.members.append(data)

    # ============== 파일 저장 ==============================

    def save_members(self):  # 파일에서 메모리로 불러온다.
        def save_members(self):
            with open(self.file_name, "w", encoding="utf-8") as f:
                for m in self.members:
                    f.write(f"{m[0]}|{m[1]}|{m[2]}|{m[3]}|{m[4]}\n")

    # =============== 로그인 메서드===========================
    def member_login(self):
        print("\n[로그인]")
        uid = input("아이디 : ")
        pw = input("비밀번호 : ")

        for i, m in enumerate(self.members):
            if m[0] == uid:
                if not m[4]:
                    print("비활성화된 계정입니다.")
                    return

                if m[1] == pw:
                    self.session = i
                    print(f"{m[2]}님 로그인 성공 ({m[3]})")

                    if m[3] == "admin":
                        self.member_admin()
                    return
                else:
                    print("비밀번호 오류")
                    return

        print("존재하지 않는 아이디")

    # ==============회원 가입 메서드========================
    def member_add(self):
        print("\n[회원가입]")
        uid = input("아이디 : ")

        for m in self.members:
            if m[0] == uid:
                print("이미 존재하는 아이디입니다.")
                return

        pw = input("비밀번호 : ")
        name = input("이름 : ")

        print("1.admin  2.manager  3.user")
        r = input("권한 선택 : ")

        role = "user"
        if r == "1":
            role = "admin"
        elif r == "2":
            role = "manager"

        self.members.append([uid, pw, name, role, True])
        self.save_members()
        print("회원가입 완료")

    # ============= 회원 정보 수정 메서드==================
    def member_modify(self):
        print("\n[관리자 메뉴]")
        print("1. 비밀번호 변경")
        print("2. 블랙리스트")
        print("3. 권한 변경")
        print("0. 종료")

        sel = input("선택 : ")
        uid = input("대상 아이디 : ")

        for m in self.members:
            if m[0] == uid:
                if sel == "1":
                    m[1] = input("새 비밀번호 : ")
                elif sel == "2":
                    m[4] = False
                elif sel == "3":
                    m[3] = input("admin / manager / user : ")

                self.save_members()
                print("관리자 작업 완료")
                return

        print("대상 회원 없음")

    # ============= 회원 탈퇴 메서드 =====================
    def member_delete(self):
        if self.session is None:
            print("로그인 필요")
            return

        print("\n[회원 탈퇴]")
        print("1. 완전 탈퇴")
        print("2. 계정 비활성화")

        sel = input("선택 : ")

        if sel == "1":
            self.members.pop(self.session)
        elif sel == "2":
            self.members[self.session][4] = False

        self.session = None
        self.save_members()
        print("처리 완료")
# ===================================================================

    def member_admin(self):
        # role = "admin"에 진입 가능한 메서드
        subrun = True
        while subrun:
            print("\n[관리자 메뉴]")
            print("1. 회원 리스트 조회")
            print("2. 비밀번호 변경")
            print("3. 블랙리스트 처리")
            print("4. 권한 변경")
            print("9. 종료")

            sel = input("선택 : ")

            # 회원 목록 보기
            if sel == "1":
                self.show_member_list()

            # 비밀번호 변경
            elif sel == "2":
                uid = input("대상 아이디 : ")
                member = self.find_member(uid)
                if member:
                    member.pw = input("새 비밀번호 : ")
                    self.save_members()
                    print("비밀번호 변경 완료")
                else:
                    print("회원 없음")

            # 블랙리스트
            elif sel == "3":
                uid = input("대상 아이디 : ")
                member = self.find_member(uid)
                if member:
                    member.active = False
                    self.save_members()
                    print("블랙리스트 처리 완료")
                else:
                    print("회원 없음")

            # 권한 변경
            elif sel == "4":
                uid = input("대상 아이디 : ")
                member = self.find_member(uid)
                if member:
                    member.role = input("admin / manager / user : ")
                    self.save_members()
                    print("권한 변경 완료")
                else:
                    print("회원 없음")

            elif sel == "9":
                subrun = False

    def show_member_list(self):
        # 관리자가 볼수 있는 회원 리스트
        print("\n[회원 목록]")
        print("-" * 60)
        print(f"{'ID':10} {'이름':10} {'권한':10} {'상태'}")
        print("-" * 60)

        for member in self.members:
            # members 리스트에 있는 객체를 하나씩 가져와 member에 넣음
            status = "활성" if member.active else "비활성"
            # member.active == True면 status변수에 "활성"을 넣고 아니면 "비활성"
            print(f"{member.id:10} {member.name:10} {member.role:10} {status}")
            #                                                     "활성 " , "비활성"
            print("-" * 60)

