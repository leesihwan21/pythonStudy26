# 교보재에 관한 crud를 구현.
# 부메뉴(sub)와 함께 run() 메서드를 진행함.

class ItemService:
    def __init__(self): # 교보재 관리 함수 메서드 생성자. 초기값을 설정
        shopping = []
        cars = []
        music = []
        travel = [] #....

    def run(self):
        subrun = input(">>>")
        while subrun:
            print("""
            ---------------------------
            1. 로그인
            2. 회원가입
            3. 로그아웃
            4. 내 정보 보기
            5. 회원정보수정
            6. 회원탈퇴
            
            9. 교보재 관리 서비스 프로그램 종료
            """)

        subselect = input(">>>")
        if subselect == "1":
            print("로그인 메서드 함수 호출")

        elif subselect == "2":
            print("회원가입 메서드 함수 호출")

        elif subselect == "3":
            print("로그아웃 메서드 함수 호출")

        elif subselect == "4":
            print("내 정보보기 메서드 함수 호출")

        elif subselect == "5":
            print("회원정보수정 메서드 함수 호출")

        elif subselect == "6":
            print("회원탈퇴 메서드 함수 호출")

        elif subselect == "9":
            print("교보재 관리 서비스 프로그램 종료")
            subrun = False

        else:
            print("잘못된 메뉴로 진입하였습니다.")