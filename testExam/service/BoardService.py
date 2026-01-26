FILE_PATH = "data/board.txt" # 게시판 텍스트 파일 저장 위치

import os

class  BoardService:

    boards = []


    # 게시판 파일 불러오기==========================================================================================
    @classmethod
    def load(cls):
        if not os.path.exists(FILE_PATH):
            return

        with open(FILE_PATH, "r", encoding="utf-8") as f:
            cls.boards = [Board.from_line(line) for line in f] # 이렇게?? 그냥 한줄로 이어서 쓰셨네.. 파일 불러올떄 역직렬화



    # 게시판 파일 저장==========================================================================================
    @classmethod
    def save(cls):
        with open(FILE_PATH, "w", encoding="utf-8") as f:
            for board in cls.boards:
                f.write(board.to_line() + "\n")


    # 게시판 파일 쓰기==========================================================================================
    @classmethod
    def write(cls):
        if not Session.login():
            print("로그인 후 이용가능합니다.")
            return

        title = input("제목")
        content = input("내용")

        writer = Session.login_member.uid
        # 게시글 작성자의 주소 Session 을 가지고 옴.

        no = len(cls.boards) + 1 # 게시글 번호 글 올린사람, 자동화 사용자가 일일이 번호를 입력할 필요없는 함수 로직. len(cls.boards) + 1
        # 리스트가 비어있지 않으면 마지막 항목의 no에 1을 더하고, 비어있으면 1 부여
        # no = cls.boards[-1].no + 1 if cls.boards else 1
        cls.boards.append(Board(no,title,content,writer))
        # .append를 이용해서 맨뒤에 추가

        cls.save() # 파일 저장
        print("게시글 등록완료")

    # 게시판 조회 하기========================================================================================
    @classmethod
    def list(cls):
        print("\n[게시글 목록]")
        print(f"no. 제목/내용/작성자")
        for board in cls.boards:
            if board.active:
                print(f"{board.no} | {board.title} | {board.content} | {board.writer}")

    # 게시글 삭제 하기========================================================================================
    @classmethod
    def delete(cls):

        if not Session.login():
            print("로그인 후 이용가능합니다.")
            return

        no = int(input("삭제할 글 번호 :"))

        for board in cls.boards:
            if board.no == no:
                if (Session.login_member.uid == board.writer or
                        Session.login_member.role == "admin"):
                    # 게시글 번호. 로그인 멤버 uid 와 게시글 작성자와 같으면
                    # 또는 로그인 한 멤버 권한이 관리자면 True.
                    board.active = False
                    cls.save()
                    print("삭제 완료")

                else:
                    print("권한 없음")
                    return

            print("게시글 없음")

    # run 메서드==============================================================================================
    @classmethod
    def run(cls):
        cls.load()

        while True:
            print("""
            [게시판]
            1. 글쓰기
            2. 글목록
            3. 글삭제
            0. 뒤로가기
            """)

            sel = input("메뉴 선택")

            if sel == "1":
                cls.write()

            elif sel == "2":
                cls.list()

            elif sel == "3":
                cls.delete()

            elif sel == "0":
                break