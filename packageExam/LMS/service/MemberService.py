import os

from packageExam.LMS.common import Session
from packageExam.LMS.common import *
from packageExam.LMS.domain import * # 별표는 __init__.py 에 있는 저장된 내용을 __all__ 에 가져옴.

# 상위폴더에 있는 폴더 모듈        클래스

# 회원 데이터 파일 경로
# FILE_PATH = "../data/members.txt" # ".." 은 최상위 폴더, .은 상위폴더
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILE_PATH = os.path.join(BASE_DIR, "-", "data", "member.txt")

class MemberService: # 회원관련된 비즈니스 로직 담당하는 클래스, CRUD를 담당함.

    #============================================================
    @classmethod
    def load(cls):

        cls.member = []

        if not os.path.exists(FILE_PATH):
            # try:
            #  os.makedirs(os.path.dirname(cls.FILE_PATH), exist_ok=True)
            #  with open(cls.FILE_PATH, "w", encoding="utf-8") as f:
            #  pass # 빈 파일 생성
            #  print(f"새로운 데이터 파일을 생성했습니다: {cls.FILE_PATH}")
            #  except OSError as e:
            #  print(f"폴더나 파일을 생성하는 중 오류가 발생했습니다: {e}")
            cls.save()
            return

    # try:
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            for line in cls.line:
                #try:
                    # Member 객체 생성 시도
                    # member = Member.from_line(line)
                    # cls.members.append(member_obj)

                # except (ValueError, IndexError) as e:
                # 데이터 형식이 잘못된 경우 (예: 'kkw|1234' 처럼 데이터가 부족할 때)
                # print(f"[데이터 오류] {line_num}행 형식이 잘못되었습니다: {line}")
                # print(f"상세 내용: {e}")

                # except Exception as e:
                # 기타 예상치 못한 개별 데이터 오류
                # print(f"[알 수 없는 오류] {line_num}행에서 문제가 발생했습니다: {e}")
                cls.members.append(Member.from_line(line))

    # except IOError as e:
    #             # 파일 읽기 자체에 실패한 경우 (권한 문제 등)
    #         print(f"파일을 읽는 도중 시스템 오류가 발생했습니다: {e}")

    # except FileNotFoundError:
    #         print("파일을 찾을 수 없습니다.")
    # except Exception as e:
    #         # 예상치 못한 다른 모든 에러 처리
    #         print(f"데이터를 불러오는 중 알 수 없는 오류가 발생했습니다: {e}")



    @classmethod
    def save(cls): # 파일 저장용

    # try:

        with open(FILE_PATH, "w", encoding="utf-8") as f:
            for member in cls.members:
                f.write(member.to_line() + "\n")
                # print("데이터가 성공적으로 저장되었습니다.")

    #     except PermissionError:
    #         print(f"오류: {self.FILE_PATH} 파일이 다른 프로그램에서 사용 중입니다.")

    #     except OSError as e:
    #         print(f"시스템 오류로 저장에 실패했습니다: {e}")

    #     except Exception as e:
    #         print(f"예상치 못한 오류 발생: {e}")


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








