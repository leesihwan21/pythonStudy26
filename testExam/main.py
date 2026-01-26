from testExam.service import *
from testExam.common import Session


# from packageExam.testExam.LMS.service import *
# from packageExam.testExam.LMS.domain import Session

def main():
    MemberService.load()

    run = True
    while run:
        print("""
=====================================
엠비씨 아카데미 LMS 회원관리 프로그램입니다.
=====================================
1. 회원가입
2. 로그인
3. 로그아웃
4. 회원관리(내정보수정)
5. 게시판
6. 성적 관리
7. 상품몰
9. 종료      
""")

        member = Session.login_member()

        if member is None:
            print("현재 로그인 상태가 아닙니다")
        else:
            print(f"{member.name} 님 로그인 성공")


        sel = input("메뉴 선택")

        if sel == "1": MemberService.signup()

        elif sel == "2": MemberService.login()

        elif sel == "3": MemberService.logout()

        elif sel == "4": MemberService.admin_menu()

        elif sel == "5": BoardService.run()

        elif sel == "6": ScoreService.run()

        elif sel == "7": ItemService.run()

        elif sel == "9":
            print("프로그램 종료")
            run = False



if __name__ == "__main__": # 주실행문 프로그램 시작.
    main()