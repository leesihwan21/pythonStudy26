# 자료 게시판에 관한 crud를 구현.
# 부메뉴(sub)와 함께 run() 메서드를 진행함.

class BoardService:
    def __init__(self): # 자료 게시판용 함수 생성자. 초기값 지정 및 설정
        Board_num = [] #.... 자료 게시판과 관련한 변수들 생성해볼것. 필요한 것

    def run(self):
        subrun = True
        while subrun:
            print("""
            ------------------------------------
            1. 자료 게시글 등록
            2. 자료 게시글 리스트 보기
            3. 자료 게시글 자세히 보기
            4. 자료 게시글 수정하기
            5. 자료 게시글 삭제하기
            
            9. 자료 게시판 프로그램 종료
            """)

            subselect = input(">>>")
            if subselect == "1":
                print("자료 게시판 등록 메서드 호출")

            elif subselect == "2":
                print("자료 게시판 리스트 보기 메서드 호출")

            elif subselect == "3":
                print("자료 게시글 자세히 보기 메서드 호출")

            elif subselect == "4":
                print("자료 게시글 수정하기 메서드 호출")

            elif subselect == "5":
                print("자료 게시글 삭제하기 메서드 호출")

            elif subselect == "9":
                print("자료 게시판 프로그램 종료")
                subrun = False

            else:
                print("잘못된 메뉴에 진입하였습니다.")


