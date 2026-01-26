# 비회원용 게시판을 만들어보자.

# C  CREATE : 게시글 등록, 게시글 생성
# R  READ : 게시글 전체보기(리스트 배열), 게시글 1개만 보기(자세히보기)
# U  UPDATE : 게시글 수정
# D  DELETE : 게시글 삭제


# 필요한 변수들,,,,what...

run = True # while 문 프로그램 구동중일 때 사용함. (그냥 기본으로 사용함)

board_number = [] # 중복되지 않은 유일한 고유한 값, 공백있으면 null 있으면 안됨. # 전역 변수(프로그램 전반적으로 사용가능하게 한 변수) # , 전체적으로 사용할 수 있는 변수들
board_title = [] # 게시글 제목           # 전역 변수, 전체적으로 사용할 수 있는 변수들
board_content = [] # 게시글 내용        # 전역 변수, 전체적으로 사용할 수 있는 변수들
board_writer = [] # 게시글 글쓴이         # 전역 변수, 전체적으로 사용할 수 있는 변수들
board_pw = [] # 게시글 암호 # 수정 삭제용       # 전역 변수, 전체적으로 사용할 수 있는 변수들
board_hit = [] # 좋아요                    # 전역 변수, 전체적으로 사용할 수 있는 변수들
board_visitcount = [] # 게시글 조회수         # 전역 변수, 전체적으로 사용할 수 있는 변수들


# 게시글 구현해보기
menu = """
============================================
        mbc 아카데미 비회원 게시글
============================================

1. 게시글 등록
2. 게시글 리스트 보기
3. 게시글 자세히 보기
4. 게시글 수정하기
5. 게시글 삭제하기
6. 게시판 프로그램 종료

"""

while run:
    print(menu)
    select = input("1~6번까지의 숫자를 입력하세요")

    if select == "1":
        board_title.append(board_title)
        board_content.append(board_content)
        board_writer.append(board_writer)
        board_pw.append(board_pw)

        board_number = len(board_number) + 1
        board_hit = [0]
        board_visitcount = [0]


        print(f"{[board_number]}번의 게시물 등록이 완료되었습니다.")

    elif select == "2":
        print("게시물 전체 목록 보기입니다.")
        print("-------------------------")
        print("번호\t 제목\t 작성자\t 조회수\t")

        if len(board_number) == 0:
            print("등록된 게시물이 없습니다.")
            continue

        for i in range(len(board_number)):
            print(f"{board_number[i]}, {board_title[i]}, {board_writer[i]}, {board_visitcount[i]}]")
            #           번호                제목                작성자                조회수

    elif select == "3":
        print("게시물 자세히 보기입니다.")
        board_number = int(input("게시물 번호 : "))
        board_number = int(input(board_number + 1))

    if board_number in board_pw:
        print("해당 게시물을 찾았습니다.")
        idx = board_number.index(board_number)

        board_visitcount[idx] += 1

        print(f"번호 : {board_number[idx]}")
        print(f"제목 : {board_title[idx]}")
        print(f"내용 : {board_content[idx]}")
        print(f"작성자 : {board_writer[idx]}")
        print(f"조회수 : {board_visitcount[idx]}")
        print(f"좋아요 : {board_hit[idx]}")

        if input("좋아요 누르면 y를 누르세요. : ") == "y":
            board_hit[idx] += 1
            print("좋아요 +1")

        else:
            print("다음에 더 좋은 게시글이 될 것입니다. ")

    else:
        print("해당 게시글이 존재하지 않습니다.")






