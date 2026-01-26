# main은 주실행 코드로 주메뉴를 담당한다.
# 외부 모듈을 호출해서 연동한다.
import MemberService # 회원관리용 클래스
import ScoreService # 성적관리용 클래스
import BoardService # 게시판관리용 클래스
import ItemService # 상품관리용 클래스


def main():
    run = True
    while run:
        print(f"""
=========================================
엠비씨 아카데미 lms 서비스 입니다.
1. 회원관리
2. 성적관리
3. 자료게시판
4. 교보재 관리
5. 교수 전용
6. 취업용 게시판

9. 종료
""")

        select = input(">>>")
        if select == "1":
            print("회원관리서비스로 진입합니다.")
            # 회원서비스 클래스 호출용 코드 추가.
            MemberService.MemberService().run() # 멤버서비스라는 인포트 안에 있는 멤버서버스 클래스 안에 있는 런 메서드를 실행해라.
            # import          클래스        메서드

            print("회원관리서비스를 종료합니다.")
            # 회원서비스 클래스 종료 호출용 코드

        elif select == "2":
            print("성적관리 서비스로 진입합니다.")
            # 성적관리 서비스 클래스 호출용 코드

            print("성적관리 서비스를 종료합니다.")
            # 성적관리 서비스 종료 호출용 코드

        elif select == "3":
            print("자료 게시판 서비스로 진입합니다.")
            # 자료 게시판 서비스 호출용 코드

            print("자료 게시판 서비스를 종료합니다.")

        elif select == "4":
            print("교보재 관리 서비스로 진입합니다.")
            # 교보재 관리 서비스 메서드 호출용 코드

            print("교보재 관리 서비스를 종료합니다.")
            # 교보재 관리 종료 호출용 코드

        elif select == "5":
            print("교수전용 서비스로 진입합니다.")
            # 교수전용 서비스 메서드 호출용 코드

            print("교수전용 서비스를 종료합니다.")
            # 교수전용 서비스 종료 호출용 코드
        elif select == "6":
            print("취업용 서비스로 진입합니다.")
            print("취업용 서비스를 종료합니다.")

        elif select == "9":
            print("엠비씨 lms 서비스를 종료합니다.")
            run = False

        else:
            print("잘못된 번호를 선택하였습니다.")
            print("다시 입력하세요.")


# 모듈 처리했을 떄 단점, 메인 주실행 코드인지 확인.
if __name__=="__main__": # 여러파일을 호출하기 때문에 main() 일때만 main() 메서드를 실행.
      main() # 위에서 만든 main() 함수를 실행한다.

