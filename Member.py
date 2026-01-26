# 회원관리용 코드를 만든다.
# c -> 회원생성, 추가, 삽입
# r -> 관리자 일 경우 (전체 회원보기), 일반 회원일 경우 (로그인)
# u -> 관리자 일 경우 (회원 차단, 암호변경문의) 일반 회원일 경우 (내 정보 수정, 암호변경)
# d -> 회원 탈퇴, 회원 정보 삭제

# 메뉴 구현
run = True  # 프로그램 동작중을 관리하는 변수. False 처리하면 프로그램 종료
login_user = None

menu = """
======================================
     mbc 아카데미 회원 관리 프로그램
======================================
1. 회원가입
2. 로그인
3. 회원보기
4. 내 정보 수정
5. 프로그램 종료
"""



while run:
    print(menu)
    select = input("1~5 숫자 입력")

    #============================
    # 1. 회원가입
    #===========================

    if select == "1":
        print("회원가입")

        sn = input("사번")
        id = input("아이디")

        if id in id:
            print("이미 존재한는 아이디")
            continue

        pw = input("비밀번호")
        name = input("이름")
        email = input("이멜")
        admin = input("관리자")

        print("\n입력정보확인")
        print(f"이름:")
        print(f"아이디:")
        print(f"이메일:")

        if input("가입? (y/n): ") == "y":
            sn.append(sn)
            id.append(id)
            pw.append(pw)
            name.append(name)
            email.append(email)
            admin.append(admin)
            print("회원가입완료")

        else:
            print("회원가입완료")

        #===============================
        #2.로그인
        #===============================

    elif select == "2":
        print("로그인메뉴")

        id = input("아이디")
        pw = input("비밀번호")

        if id in id:
            idx = id.index(id)
            if pw[idx] == "pw":
                login_user = idx
                print(f"{name[idx]}님 로그인성공")

                if admin[idx]:
                    print("관리자 계정")

                else:
                    print("일반회원계정")
            else:
                print("비밀번호 틀림")

        else:
            print("존재하지 않는 아이디")


        #==============================
        #3.회우너보기
        #==============================
    elif select == "3":
        if login_user is None:
            print("로그인 후 이용 가능")
            continue

        #관리자
        if admin[login_user]:
            print("전제목록출력")
            for i in range(len(id)):
                print(f"{i+1}, {name[i]}, {email[i]}")

        else:
            #일반회원
            print("내정보")
            print(f"이름 : {login_user}")
            print(f"아이디: {admin}")
            print(f"이메일: {name}")

        #============================
        #4.내정보수정
        #============================
    elif select == "4":
        if login_user is None:
            print("로그인 후 이용 가능")
            continue

        print("내정수정")
        print("이름변경")
        print("이메일변경")
        print("비번 변경")

        choice = input("선택")

        if choice == "1":
            name[login_user] = input("새이름")
            print("이름변경완료")

        elif choice == "2":
            email[login_user] = input("새멜")
            print("이멜변경완료")

        elif choice == "3":
            pw[login_user] = input("새비번")
            print("비번변경완료")

        else:
            print("잘못된 선택")


        #===============================
        #5.종료
        #==============================

    elif select == "5":
        print("로그인 후 이용")
        run = False

    else:
        print("1~5 입력")
