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
    select = input("1~6번까지의 숫자를 입력하세요. : ") # 지역 변수(1회용이기 때문), 즉 while문 안에서만 변수를 사용함. while 문 밖에서 사용하면 사라짐.
    # select 는 while 문 안쪽에서만 사용할수 있는 1회용 변수 즉 지역변수라고 한다.
    # input은 키보드로 입려한 값을 문자열로 전달함.

    if select == "1":  #키보드로 입력한 값이 1이면
        print("게시글을 등록하세요")  # 게시글 등록용 코드 추카
        # 게시글의 번호는 프로세스가 자동 처리
        # 키보드로 게시글을 받아 변수에 넣는다.

        title =  input("게시글 제목 :")              # 게시글 제목
        content =  input("게시글 내용 :")            # 게시글 내용
        writer =  input("게시글 글쓴이 : ")          # 게시글 글쓴이
        pw = input("게시글 비밀번호 : ")              # 게시글 암호 # 수정 삭제용


        print(f"제목 : {title}, 내용 : {content} ")
        print(f"작성자 : {writer}, 암호 : {pw} ")
        print(f"저장하려면 y를 누르세요 ")
        choice = input("저장하려면 y를 누르세요 : ")

        if choice == "y":
            board_title.append(board_title)
            board_content.append(board_content)
            board_writer.append(board_writer)
            board_pw.append(board_number)


                # 제목의 리스트에서 인덱스를 추출하여 + 1한 값이 number.
                # if title in board_title :
                #      idx = board_title.index(board_title)
                #      board_number.append(idx+1)

                # 제목을 이용해서 번호를 생성하면 중복문제 문제발생
                # board_number 리스트의 길이를 활용하여 해결
            board_number = len(board_number) + 1

            board_number.append(board_number)
            board_hit.append(0)
            board_visitcount.append(0)

            print(f"{[board_number]}번의 게시글이 등록 되었습니다.")


        elif select == "2":
            print("게시글 전체 목록 출력합니다.")
            # 게시글 리스트 보기용 코드 추가.
            print("============================")
            print("번호\t 제목\t 작성자\t 조회수\t ")
            print("============================")

            if len(board_number) == 0:
                print("등록된 게시물이 없습니다.")
                continue  # while 문으로 다시 돌아간다.

            for i in range(len(board_number)): # 게시글의 갯수만큼 반복한다. (0부터 게시물 번호까지 인덱스 처리용.
                print(f"{board_number[i]}\t, {board_title[i]}\t, {board_writer[i]}\t, {board_visitcount[i]}\t ")
                #            번호                       제목               작성자                 조회수


        elif select == "3":
            print("게시글 자세히 보기입니다.")
            board_number = int(input("게시글 번호 : "))

        if board_number in board_pw: # 등록된 게시물의 유무 확인용
            print("게시물을 찾았습니다.")
            idx = board_number.index(board_number) # 리스트에서 게시물의 인덱스 값을 찾아온다.

            board_visitcount[idx] += 1  # 조회수 1 증가

            print("================================")
            print(f"번호 : {board_number[idx]}")
            print(f"제목 : {board_title[idx]}")
            print(f"내용 : {board_content[idx]}")
            print(f"작성자 : {board_writer[idx]}")
            print(f"조회수 : {board_visitcount[idx]}")
            print(f"좋아요 : {board_hit[idx]}")
            print("===============================")

            if input("좋아요 누르기(y) : ") == "y" :
                board_hit[idx] += 1
                print("좋아요가 눌러졌습니다.")

            else:
                print("아쉽습니다. 다음에 더 좋은 게시글이 될 것입니다.")

        else:
            print("해당번호의 게시글이 없습니다.")

    elif select == "4":
        print("게시글 수정합니다.")
        board_number = int(input("게시글 번호 : "))
        board_pw = input("비밀번호 : ")


        if board_number in board_number:
            print("해당 게시물의 내용이 수정되었습니다.")
            idx = board_pw.index(board_pw)
            # idx() 주소도 print를 많이 찍어봐야 알 수 있다.

            if board_pw[idx] == board_pw:
                board_title[idx] = input("새로운 제목을 입력하세요 : ")
                board_content[idx] = input("새로운 내용을 입력하세요 : ")
                print("게시글이 수정되었습니다.")

            else:
                print("암호가 틀렸습니다.")

        else:
            print("해당 게시물이 존재하지 않습니다.")



    elif select == "5":
        print("게시글 삭제합니다.")

        board_number[idx] = int(input("게시글 번호 : "))
        board_pw[idx] = input("새로운 암호 : ")

        if board_number[idx] in board_number:
            idx = board_pw.index(board_pw)

            if board_pw[idx] == pw:
                board_number.pop(idx)
                board_title.pop(idx)
                board_content.pop(idx)
                board_writer.pop(idx)
                board_pw.pop(idx)
                board_hit.pop(idx)
                board_visitcount.pop(idx)

                print("게시글이 삭제되었습니다.")

            else:
                print("암호가 틀렸습니다")
        else:
            print("게시글 번호가 없습니다")



    elif select == "6":
        print("[게시글 검색]")
        print("1. 제목으로 검색")
        print("2. 작성자로 검색")

        choice = input("선택 : ")

        found = False # 검색 결과 여부 확인

        if choice == "1":
            keyword = input("검색할 제목 키워드 : ").lower()

            print("번호\t제목\t작성자\t조회수")
            for i in range(len(board_number)):
                if keyword in board_title[i].lower():
                    print(f"{board_number[i]}\t{board_title[i]}\t{board_writer[i]}\t{board_visitcount[i]}")

                    found = True

        elif choice == "2":
            keyword = input("작성자 이름 : ").lower()

            print("번호\t제목\t작성자\t조회수")
            for i in range(len(board_number)):
                if keyword == board_writer[i].lower():
                    print(f"{board_number[i]}\t{board_title[i]}\t{board_writer[i]}\t{board_visitcount[i]}")

                    found = True

        else:
            print("잘못된 선택입니다.")

        if not found:
            print("검색 결과가 없습니다")
