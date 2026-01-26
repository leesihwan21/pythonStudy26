# main.py는 앞으로 1번 파일이라고 생각하면 됨.
# 대부분 프로그래밍에서 1번이 되는 또는 시작이 되는 파일을 main 으로 만든다.
# 목표 : MBC 아카데미 LMS 프로그램을 만들어 보자.
# LMS는 학사관리 프로그램.
# 회원관리 : 시스템 담당자, 교수, 행정, 학생, 손님, 학부모
# 성적관리 : 교수가 성적등록, 수정
#           행정 담당자가 1년에 한 번, 학기마다 백업(먼저 옮기고 삭제한다
#           학생은 개인성적일람, 성적서 인쇄
#           손님은 학교 소개페이지 열람
#           학부모는 자녀 학사관리
# 게시판 : 회원제, 비회원제, 문의사항, Q&A

# while 문 : run, subrun
# if 문 : 메뉴 선택, 판단용
# for 문 : 리스트에 있는 전체 내용 출력용
# for in 문 : 리스트에 있는 내용 인덱스 찾는 용(주소값)


# 필요한 변수들
run = True # main menu 메인 메뉴용 while.
# subRun = True   # 보조 메뉴용 while.
session = None # 로그인 한 사용자의 인덱스(idx)를 기억하고 있는 것.

# 필요한 리스트
# 회원에 대한 리스트
sns = [1] # 회원에 대한 번호
ids = ["kkw"] # id에 대한 리스트
pws = ["1234"] # pw에 대한 리스트
groups = ["admin"] # 회원 등급 # admin, prof,,staff, stu,, parent
# admin (관리자), stu (학생), guest(손님) .....

# 성적에 대한 리스트
pythonScore = [] # 파이썬 점수들
dataBaseScore = []  # 데이터 베이스 점수들
wwwScore = [] # 프론트 점수들
totalsScore = [] # 총점들
avgScore = [] # 평균들
gradeScore = [] # 등급들
stuIdx = [] # 학생의 인덱스 (학번) <-> 회원의 번호 sns 과 연결

# 게시판에 대한 리스트
board_no = [] # 게시물의 번호
board_title = [] # 게시물 제목
board_content = [] # 게시물 내용
board_writer = [] # 게시물 글쓴이 -> 회원의 sns 와 연결이 되어야 함.
board_pw = [] #게시물 암호



#=================================================
#성적 데이터
#=================================================
dbScore = []
webScore = []

#================================================
#게시판 데이터

#================================================

# 메뉴 구성
mainMenu = """
==================================
엠비씨아카데미 LMS에 오신걸 환영합니다

1. 로그인(회원가입)
2. 성적관리
3. 게시판
4. 관리자 메뉴
9. 프로그램 종료

"""

memberMenu = """
-----------------------------------
회원관리 메뉴입니다.

1. 로그인
2. 회원가입

9. 뒤로가기

"""

scoreMenu = """
------------------------------------
성적관리 메뉴입니다.

1. 성적 입력(교수전용)
2. 성적 보기(개인용)

9. 뒤로가기
"""

boardMenu = """
------------------------------------
회원제 게시판 입니다.

1. 게시글 입력
2. 게시글 보기

9. 뒤로가기

"""

adminMenu = """
-------------------------------------
관리자 메뉴

1. 회원목록
2. 회원강제삭제

9. 뒤로가기

"""

while run:
    print(mainMenu) # 메인메뉴 출력용
    select = input(">>>") # 사용자가 주 메뉴 선택 값을 select 넣는다.

    if select == "1":
        print("로그인(회원가입)메뉴로 진입합니다.")
        subRun = True

        while subRun: # 부 메뉴 반복용.
            print(memberMenu) # 회원관리 메뉴 출력
            subselect = input(">>>") # 회원 부 메뉴 선택값을 subSelect 넣음.

            # -----------로그인 메뉴-------------------------------------------------------------------------------------

            if subselect == "1":
                print("로그인 메뉴로 진입합니다.")
                ids = input("회원 아이디 : ")
                pw = input("회원 비밀번호 : ")

                if ids in ids:
                    idx = ids.index(ids)
                    if pw in pws:
                        session = idx

                        print(f"로그인 성공/권한 : {groups[idx]}")
                        subRune = False

                    else:
                        print("비밀번호가 틀렸습니다.")

                else:
                    print("존재하지 않는 아이디 입니다.")

            # -----------------회원가입 메뉴------------------------------------------------------------------------------

            elif subselect == "2":
                print("회원가입 메뉴로 진입합니다.")
                print("회원가입")
                id = input("새 ID : ")

                if id in ids:
                    print("이미 존재하는 아이디 입니다.")
                    continue

                pw = input("비밀번호 : ")

                if pw in pw:
                    print("비밀번호 생성이 완료되었습니다.")

            # ================ROLE 분기==================================================================================

                if session is None:
                    print("회원 유형 선택")
                    print("1. 학생")
                    print("2. 학부모")

                    Role = input("선택")
                    if Role == "1":
                        role = "stu"

                    elif Role == "2":
                        role = "studentParent"

                    else:
                        print("1번으로 선택되었습니다.")

                elif groups(session) == "admin":
                    print("권한 선택")
                    print("1. 관리자(admin)")
                    print("2. 교수")
                    print("3. 학생")
                    print("4. 학부모")
                    print("5. 행정직원")

                    role_map = {"1" : "admin", "2" : "studentParent", "3" : "staff", "4" : "student", "5": "Prof"}

                    r = input("선택")
                    if r in role_map:
                        role = role_map[r]

                    else:
                        print("잘못된 선택입니다.")
                        continue

                else:
                    print("관리자만 회원을 관리 할 수 있습니다.")
                    continue

                sns.append(len(sns)+1)
                ids.append(ids)
                pws.append(pws)
                groups.append(role)

                print(f"회원가입이 완료되었습니다.(권한 : {role}")

            elif subselect == "9":
                subRun = False

        # =============================================================================================================
        # -----------------------------------------성적관리--------------------------------------------------------------

    elif select == "2":

        if session is None:
            print("로그인이 필요합니다.")
            continue

        subRun = True
        while subRun:
            print(scoreMenu)
            subselect = input(">>>")

        # --------------------------------------교수
            if subselect == "1":
                if groups[session] == "Prof":
                    print("교수만 성적 입력 가능")
                    continue

                sid = int(input("학생 번호 : "))
                py = int(input("Python : "))
                db = int(input("Database : "))
                web = int(input("Web : "))

                stuIdx.append(sid)
                pythonScore.append(py)
                dataBaseScore.append(db)
                wwwScore.append(web)

                print("성적 입력 완료")


        #-------------------------------------학생용

            elif subselect == "2":
                if groups[session] == "stu":
                    print("학생만 성적 조회 가능")
                    continue

                myNo = sns(session)
                #      코드를 만들어야 함. 데이터를 만들어야 함. 그래야지 구동시 성적입력에서 확인할 수 있다.

                if myNo in stuIdx:
                    i = stuIdx.index(myNo)
                    total = pythonScore[i] + dataBaseScore[i] + wwwScore[i]
                    avg = total / 3

                    print("Python :", pythonScore[i])
                    print("db :", dataBaseScore[i])
                    print("web :", wwwScore[i])
                    print("평균 :", avg)

                else:
                    print("등록된 성적이 없습니다.")

            elif subselect == "9":
                subRun = False



       # --------------------게시판-------------------------------------------------------------------------------

    elif select == "3":
        if session in None:
            print("로그인이 필요합니다.")
            continue

        subRun = True
        while subRun:
            print("boardMenu")
            sub = input(">>>")

            if sub == "1":
                title = input("제목 : ")
                content = input("내용 : ")

                board_no.append(len(board_no)+1)
                board_title.append(title)
                board_content.append(board_content)
                board_writer.append(board_writer)

                print("게시글 등록 완료되었습니다")

            elif sub == "2":
                print("번호\제목\작성자")
                for i in range(len(board_no)):
                    print(board_no[i], board_title[i], board_writer[i])

            elif sub == "9":
                subRun = False


        # -------------------------관리자 메뉴----------------------------------------------------------------------

    elif select == "4":
        if session in None or groups[session] != "admin":
            print("관리자만 접근 가능합니다.")
            continue

        subRun = True
        while subRun:
            print("adminMenu")
            sub = input(">>>")

            if sub == "1":
                print("번호\ID\권한")
                for i in range(len(ids)):
                    print("sns[i],ids[i],groups[i]")

            elif sub == "2":
                id = input("삭제할 ID : ")
                if id in ids:
                    i = ids.index(id)
                    sns.pop[i]
                    ids.pop(i)
                    pws.pop[i]
                    groups.pop(i)
                    print("삭제완료")

                else:
                    print("ID 없음")

            elif sub == "9":
                subRun = False


        # -------------------종료-----------------------------------------------------------------------------------

    elif select == "9":
        print("프로그램 종료")
        run = False

    else:
        print("잘못된 선택입니다.")