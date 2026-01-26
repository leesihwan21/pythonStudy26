import os

# from .testExam.LMS.common import Session
# from .testExam.LMS.domain import *


__all__ = ["MemberService", "BoardService", "ItemService", "ScoreService"]

from classExam.LMS_class_oop.Member import Member
from packageExam.LMS.common.Session import Session

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILE_PATH = os.path.join(BASE_DIR, "-", "data", "member.txt")

class MemberService:

    member = []

    #============================================================
    @classmethod
    def load(cls):
        cls.member = []

        if not os.path.exists(FILE_PATH):
            cls.save()
            return

        with open(FILE_PATH, "r", encoding="utf-8") as f:
            for line in cls.line:
                cls.members.append(Member.from_line(line))


    @classmethod
    def save(cls): # 파일 저장용
        with open(FILE_PATH, "w", encoding="utf-8") as f:
            for member in cls.members:
                f.write(member.to_line() + "\n")


    #==========================================================

    @classmethod
    def login(cls):
        print("\n[회원가입]")
        uid = input("아이디")
        pw = input("비밀번호")

        for member in cls.member:
            if member.uid == uid:
                print("비활성 계정입니다.")
                return

            if member.pw == pw:
                Session.login_member()
                print(f"{member.name} 님 로그인 성공 {member.role}")
                print(member)
                return


            else:
                print("비밀번호 틀림")

        else:
            print("존재하지 않는 아이디입니다.")

    #=========================================================

    @classmethod
    def logout(cls):

        if not Session.login_member():
            print("로그인 후 이용가능합니다.")
            return

        Session.logout()
        print("로그아웃 완료")

    #========================================================

    @classmethod
    def signup(cls):
        print("\n[회원가입]")
        uid = input("아이디 : ")

        if any(Member.uid == uid for member in cls.member):
            print("이미 존재하는 아이디 입니다.")
            return

        pw = input("비밀번호")
        name = input("이름")
        member = Member(uid, name, pw)
        cls.member.append(member)
        cls.save()

        print("회원가입 완료")

    #======================================================

    @classmethod
    def modify(cls):
        print("\n[내정보수정]")

        member = Session.login_member()

        uid = input("아이디:")

        if not Session.login_member():
            print("로그인 후 이용가능합니다.")
            return

        print("""
        [내 정보 수정]
        1. 이름 변경
        2. 비밀번호 변경
        3. 돌아가기
        """)

        sel = input("메뉴 선택")

        if sel == "1":
            print("새 이름 ")

        elif sel == "2":
            print("새 비밀번호 ")

        else:
            return

        print("내 정보수정완료")
        cls.save()

    #=================================================

    @classmethod
    def delete(cls):
        print("\n[회원탈퇴]")
        member = Session.login_member()

        if not Session.login_member():
            print("로그인 후 이용가능합니다.")
            return

        print("""
        [회원 탈퇴 메뉴]
        1. 완전 탈퇴
        2. 비활성화 계정
        3. 돌아가기
        """)

        sel = input("메뉸 선택")

        if sel == "1":
            Session.logout()
            cls.member.remove(member)
            cls.save()
            print("회원 완전 탈퇴")

        elif sel == "2":
            Session.logout()
            member.active = False
            cls.save()
            print("비활성화 완료")

    #===============================================

    @classmethod
    def is_admin(cls):

        if not Session.login() and Session.member.is_admin():
            print("관리자만 접근 가능합니다.")
            return


        while True:
            print("""
            [\n관리자 메뉴]
            1. 회원 전체 목록 조회
            2. 블랙리스트 처리
            3. 권한 변경
            4. 돌아가기
            """)

            sel = input("메뉴 선택")

            if sel == "1":
                cls.list_members()

            elif sel == "2":
                cls.black_member()

            elif sel == "3":
                cls.change_role()

            elif sel == "4":
                break


    # 추가기능들================================================

    @classmethod # 회원 리스트 보기 함수
    def list_member(cls):
        print("[회원 목록]")
        for member in cls.member:
            print(member)


    @classmethod # 회원 상태 변경 함수
    def change_member(cls):
        uid = input("대상 아이디:")

        for member in cls.member:
            if member.uid == uid:
                member.role = input("admin/manager/user")
                cls.save()
                print("권한 변경 완료")
                return

            print("회원 없음")

    @classmethod # 회원 블랙리스트 함수
    def black_member(cls):
        uid = input("대상 아이디:")
        for member in cls.member:
            if member.uid == uid:
                member.active = False
                cls.save()
                print("블랙 리스트 처리완료")
                return

            print("회원 없음")


    #======================================================







