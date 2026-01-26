# 회원에 관한 crud를 구현.
# 부메뉴(sub)와 함께 run() 메서드를 진행함.
from webbrowser import register

from Member import login_user
import os

import os
from MemberService import MemberService

class MemberService: # 객체를 담당하는 클래스. 변수 MemberService() 생성자.
    def __init__(self, FILE_NAME = "members.txt"): # init class 생성시 필요한 것.
        self.FILE_NAME = FILE_NAME
        self.members = [] # 모든 회원이 들어있는 2차원 리스트 [id, pw, name]], [id, pw, name]
        self.ids = [] # 회원들의 아이디
        self.login_id = None # 회원들 로그인 (session 로그인 한 상태값 유지) (변하지 않는 값)
        # 로그아웃 상태는 None 으로 처리함.
        # 파일명을 생성을 안해서 각 함수 안에 self.save_members() 로 하지 않음.

    def run(self):
        # 부메뉴 (sub_menu) 구현 메서드 (함수)
        subrun = True
        while subrun:
            print("""
            -------------------------------
            1. 로그인
            2. 회원가입
            3. 회원정보수정
            4. 회원탈퇴
            5. 로그아웃

            9. 회원 서비스 종료
            """)

            subselect = input(">>>")

            if subselect == "1": # 프로그램 구동시 각 함수를 호출할 때 클래스 함수를 사용하면 self.login을 넣어줘야한다.
                self.login()
                print("로그인 메서드 호출")

            elif subselect == "2":
                self.register() # 프로그램 구동시 각 함수를 호출할 때 클래스 함수를 사용하면 self.register을 넣어줘야한다.
                print("회원가입 메서드 호츨")

            elif subselect == "3":
                self.modify() # 프로그램 구동시 각 함수를 호출할 때 클래스 함수를 사용하면 self.modify을 넣어줘야한다.
                print("회원수정 메서드 호출")

            elif subselect == "4":
                self.delete() # 프로그램 구동시 각 함수를 호출할 때 클래스 함수를 사용하면 self.delete을 넣어줘야한다.
                print("회원탈퇴 메서드 호출")

            elif subselect == "5":
                self.logout() # 프로그램 구동시 각 함수를 호출할 때 클래스 함수를 사용하면 self.logout을 넣어줘야한다.
                print("로그아웃 메서드 호출")

            elif subselect == "9":
                print("회원서비스종료")
                subrun = False

            else:
                print("잘못된 메뉴를 선택하였습니다.")
                print("다시 선택하세요.")


    # =============== 파일 로드 (읽기) =======================
    def load_members(self):  # 파일에서 메모리로 불러온다.
        if not os.path.exists(self.file_name):  # 맨위에 import os
            self.save_members()
            return

        self.members = []  # 메모리에 남은 값을 초기화
        with open(self.file_name, "r", encoding="utf-8") as f:
            for line in f:
                data = line.strip().split("|")
                data[4] = True if data[4] == "True" else False
                self.members.append(data)
                #                   Member객체에 .from_line() 메서드 실행
                #                               1줄을 가져와 클래스로 만듬
                #    members리스트 뒷부분에 추가

    # ============== 파일 저장 ================================
    def save_members(self):
        with open(self.file_name, "w", encoding="utf-8") as f:
            for member in self.members:
                    f.write(f"{member[0]}|{member[1]}|{member[2]}|{member[3]}|{member[4]}\n")

    # =============== 로그인 메서드===============================
    def login(self):
        print("로그인")
        uid = input("아이디 : ")

        if self.find_member(uid):
            print("이미 로그인 한 상태입니다.")
            return # def login 함수를 빠져나온다.

        user_id = input("아이디 :")
        user_pw = input("비밀번호 : ")

        for member in self.members:
            if member[0] == user_id and member[1] == user_pw:
                self.login_id = user_id  # 로그인 성공 시 ID 기록
                print(f"{member[2]}님 환영합니다!")
                return

        print("정보가 일치하지 않습니다.")

    # ==============회원 가입 메서드============================
    def register(self):
        print("\n회원가입")
        uid = input("아이디 : ")

        # 1. 중복 체크 (메모리 리스트 검색)
        found = self.find_member(uid)
        if found:
            print(f"이미 존재하는 아이디입니다. (기존 사용자: {found.name})")
            return

        # 2. 정보 입력
        pw = input("비밀번호 : ")
        name = input("이름 : ")
        role = "user"  # 사용자 권한 기본값

        # 3. 객체 생성 및 리스트에 추가 (이 단계가 '가입'의 전부)
        new_member = MemberService(uid, pw, name, role)
        self.members.append(new_member)

        print(f"\n{name}님, 가입이 완료되었습니다!")

    # ============= 회원 정보 수정 메서드======================
    def modify(self):
        if not self.login_id:  # 로그인 체크
            print("로그인 후 이용 가능합니다.")
            return

            # 현재 로그인한 회원의 위치(인덱스) 찾기
        idx = self.ids.index(self.login_id)

        print(f"\n[{self.login_id} 님의 정보 수정]")
        print("1. 비밀번호 변경 / 2. 이름 변경")
        menu = input("메뉴 선택 >>> ")

        if menu == "1":
            new_pw = input("새 비밀번호: ")
            self.members[idx][1] = new_pw
            print("비밀번호 수정 완료!")
        elif menu == "2":
            new_name = input("새 이름: ")
            self.members[idx][2] = new_name
            print("이름 수정 완료!")

        self.save_members()  # 변경사항 파일 저장

    # ============= 회원 탈퇴 메서드 ========================
    def delete(self):
        print("회원 탈퇴")

        if not self.login_id:
            print("로그인 후 이용가능합니다.")
            return

        confirm = input("정말로 탈퇴하시겠습니까? (y/n): ")
        if confirm.lower() == "y":
            idx = self.ids.index(self.login_id)

            # 리스트에서 완전히 제거 (중요!)
            self.members.pop(idx)
            self.ids.pop(idx)

            self.login_id = None  # 세션 초기화
            self.save_members()  # 파일 업데이트
            print("회원 정보가 완전히 삭제되었습니다.")

    # ============ 로그아웃 메서드 ==========================
    def logout(self):
        print("로그아웃")

        if not self.login_id:
            print("이미 로그아웃 상태입니다.")
            return

        print(f"{self.login_id}님, 로그아웃 되었습니다.")
        self.login_id = None  # 접속 상태 해제


    # 실행=============================================
    if __name__ == "main": # 여러파일을 호출하기 때문에 main() 일때만 main() 메서드를 실행.
        MemberService = MemberService()  # 위에서 만든 main() 함수를 실행한다.
        MemberService.run()