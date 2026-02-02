# 주 실 행영역 (메인메뉴 등을 관리한다.)
from LMS.service import * # * 는 모든것들..셀수없이 많을 떄 사용함.
from LMS.common.session import Session

def main():
    # 프로그램 시작할 때 코드용. 주 메뉴 메서드 함수.
    MemberService.load() # MemberService.load() -> init에 서 생성해야함.

    run = True
    while run:
        print("""
        ==========================
        MBC 아카데미 관리 시스템
        ==========================
        1. 회원가입 2. 로그인 3. 로그아웃
        4. 회원관리
        5. 게시판 6. 성적관리 7. 상품몰
        9. 종료
        """)

        member = Session.login_member # 초기값이니까 None 처리됨.

        if member is None: # 로그인 안 된 상태
            print("로그인 후 이용가능합니다.")

        else:
            print(f"{member.name} 님 환영합니다.")

        sel = input("번호")

        if sel == "1":
            print("회원가입 서비스로 진입합니다.")
            MemberService.signup()

        elif sel == "2":
            print("로그인 서비스로 진입합니다.")
            MemberService.login()

        elif sel == "3":
            print("로그아웃 서비스로 진입합니다.")
            MemberService.logout()

        elif sel == "4":
            print("회원관리 서비스로 진입합니다.")

        elif sel == "5":
            print("게시판 서비스로 진입합니다.")
        elif sel == "6":
            print("성적관리 서비스로 진입합니다.")
        elif sel == "7":
            print("상품몰 서비스로 진입합니다.")
        elif sel == "9":
            print("LMS 서비스 프로그램 종료")
            run = False


# main() 메서드 종료.

if __name__ == "__main__": # 주실행문 시작.
    main()
