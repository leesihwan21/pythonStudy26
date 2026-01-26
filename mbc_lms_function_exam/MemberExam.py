# 회원관리 CRUD를 사용자 지정 함수로 만들어 보자.
# C CREATE : 회운가입
# R READ : 회원 리스트 관리자인경우 회원 암호 변경, 블래리스트 생성, 권한 부여
# R READ : 로그인 -> ID와 PW를 활용하여 로그인 상태 유지 session 이 필요함.
# U UPDATE : 회원 정보 수정
# D DELETE : 회원 탈퇴, 회원 비활성화


# 프로그램에서 사용될 변수들
# 전역변수 (global) : py 파일 안에서 전체적으로 사용되는 변수
# 지역변수 (local) : while이나 if for def 안에서 사용되는 변수

run = True # while 문에서 전체적으로 사용되는 변수(프로그램 구동중)
session = None # session 은 로그인 상태 저장용. -> 로그인 한 사용자의 리스트 인덱스 기억용(index, idx)

# 프로그램에서 사용될 리스트들 (더미 데이터), 더미 라는 뜻은 허수아비 가짜라는 뜻.

# sns = [1,2,3] # 회원 번호 오늘은 안해봄. 회원 삭제및 추가시 번호가 흔들릴 수 있음. index로만

ids = ["kkw","lhj","ljj"] # 회원 아이디
#        0     1     2
pws = ["1234","5678","8888"] # 회원 비밀번호
names = ["김기원","임효정","이재정"] # 회원 명, 사용자명
roles = ["admin","manager","user"] # 사용자 권한 (admin, manger, user)
active = [True,True,True] # 회원 사용중, 탈퇴, 블랙리스트 등.....
# 차후에는 파일처리로 변환 할 예정. txt.file

# 프로그램에서 사용될 함수들,  # def 함수 안에 코드 만들 것.


def member_add():
    # 회원 가입용 함수
    print("member_add 함수로 진입합니다.")
    # 회원가입에 필요한 기능을 넣음.
    print("회원가입메뉴에 진입하였습니다.")
    new_id = input("아이디 : ")
    # 키보드로 아이디를 입력한다.
    # 이미 아이디가 존재하면 다른 아이디로 입력하게 코드 설계
    if new_id in ids:
        # True 일 때
        print("이미 존재하는 아이디 입니다.")
        return # 빠져나옴. if 문 종료됨. 돌아가라

    else: # false 일 떄 ids에서 입력된 id가 없을 때 (중복된 아이디가 없을때)
        new_pw = input("비밀번호 : ")
        new_name = input("이름 : ")
        member_add_menu()
        role_set = input("권한선택 : ")
        if role_set == "1":
            new_role = "admin"


        elif role_set == "2":
            new_role = "manager"

        else:
            new_role = "user"

        print(f""" 입력된 정보를 확인하세요.
                  이름 : {new_name}, 암호 : {new_pw}
                  아읻 : {new_id}, 권한 : {new_role} """) # 쌍따옴표 3개일때 들여쓰기 할 필요 없음.!!

        # print("저장하려면 y를 누르세요 : ")
        save_select = input("저장하려면 y를 누르세요 : ")
        if save_select == "y":
            print("저장을 시작합니다.") # append를 이용해서 각 필요한 변수들을 뒤에다가 붙인다.
            ids.append(new_id)
            pws.append(new_pw)
            names.append(new_name)
            roles.append(new_name)
            active.append(True)   # 상태가 정상이면 참 True,. 거짓이면 False...라는 뜻.
            print("저장완료")

            # 차후에 로그인 함수를 추가 해봄.

        else:
            print("회원가입이 되지 않았습니다.")

    print("member_add 함수를 종료합니다.")
    # 회원 가입용 함수 종료

def member_login():
    # 가입된 회원을 확인하여 로그인 처리후 session 변수에 인덱스를 넣는다. -> 목적

    print("member_login 함수로 진입합니다.")
    # 로그인에 필요한 기능을 넣음.

    global session # 맨 위에 전역 변수로 지정한 내용을 활용하겠다.

    if session is not None: # 로그아웃 상태 session 에 이미 값이 있으면 != 가능. None이 아니면
        # if not None -> 싱글톤이라는 객체.가 있는지 비교하는 용. 객체??????? what???????
        # if session != None -> 숫자 비교할 떄 equal 이라는 값으로 사용.
        # 코드 설계시 밑줄 그어져 있는 거는 웬만하면 권장하지 않는다라는 얘기.
        # None 이라는 뜻이 not one 이라는 아무것도 없다라는 뜻임.
        # True 상태.

        print("이미 로그인 한 상태입니다.")
        print(f"로그인 한 사용자는 {names[session]} 님 로그인 되었습니다. ") # session 로그인한사람의 0번1번2번의 주소를가지고 있음.
        return   # 다시 되돌아가기.

    else:
        # False
        user_id = input("로그인 아이디 : ")
        user_pw = input("로그인 비밀번호 : ")

        if user_id in ids: #키보드로 받은 아이디를 아이디s 리스트에 있는지 확인한다면
            # True 있으면
            idx = ids.index(user_id) # 아이디에 해당하는 주소를 idx에 넣음.

            if not active[idx]: # 회원탈퇴인 상태 , 비활성화한 상태에 대한 코드 회원 활성화 상태인지를 확인하기 위해서 코드.
                # False
                # not 을 걸었으면 부정이 긍정으로 바뀜.
                print("비활성화, 회원탈퇴 된 계정입니다. ")
                return

            # True 참이면 비활성화, 회원탈퇴 된 계정이 아니다라는 얘기이다.
            # 암호 비교.
            if user_pw == pws[idx] : # 키보드로 넣은 암호와 리스트의 주소 암호가 일치한지 를 확인
                # id도 같고 활성화 상태이고 암호가 같다.
                session = idx # 로그인 상태로 완성외 됨. ??????
                # 글로벌 영역에 전역변수 session 값이 있는 상태. 로그인 사용자의 주소가 들어가 있음.

                print(f"{names[session]}님 환영합니다.")
                print(f"{roles[idx]}권한을 가지고 있습니다.")

            if roles[idx] == "admin":
                member_admin()

            else:
                print("비밀번호가 틀렸습니다.") # 비밀번호가 다르다 에서 끝.

        else:
            # False 없으면
            print("존재하지 않는 아이디 입니다. ")


    print("member_login 함수를 종료합니다.")
    # 회원 로그인용 함수 종료.

def member_admin():
    # 관리자가 로그인 했을 경우 할 수 있는 기능을 작성.
    print("member_admin 함수로 진입합니다.")
    # 다른 사용자(번호/id/권한,,추가 암호 변경 코드)


    global session # 전역변수로 사용가능하게.
    # 관리자 권한 체크 확인.


    print(f"회원 아이디 : {ids}, 회원 권한변경 : {roles}, 회원 상태 : {active}")
    # for 문 전체 회원 정보 목록
    for i in range(len("{ids}, {roles}, {active} ")):

        print(f"{ids[i]}, {roles[i]}, {active[i]}")

        menu = input("회원 아이디 : ")
        target_id = input("작업할 아이디 : ") # 작업할 회원 아이디 및 상태 변경할 아이디

        if menu == "1":
            print("회원 아이디 : ")
            if target_id in ids:
                idx = target_id.index(ids[i])

                print("새 비밀번호 : ")
                print(f"{target_id}님의 비밀번호가 변경되었습니다.")

        elif menu == "2":
            print("회원 아이디 : ")
            if target_id in ids:
                idx = target_id.index(ids[i])
                active[idx] = False # 상태변경 됨. 블랙처리
                print(f"{target_id}님의 블랙리스트로 처리변경 되었습니다.")

        elif menu == "3":
            print("회원 아이디 : ")
            idx = target_id.index(ids[i])

            print("1. admin, 2. manager, 3. user ")
            roles[idx] = input("새 권한 : ")

            print("권한이 변경되었습니다. ")

        else:
            print("잘못된 번호입니다.")
            return


    # 블랙리스트로 변환 -> active 를 False 처리
    # 권한 부여 -> 사용자의 권한을 변경 roles를 변경 (manage <-> user)

    print("member_admin 함수를 종료합니다.") # 관리자가 사용자 변경사항 종료.


def member_logout():
    # 회원 로스아웃으로 상태 변경 -> session 값을 None으로 변경
    print("member_logout 함수로 진입합니다.")
    # 로그인 상태인지 확인하고 session은 None 처리.

    global session # session 전역변수로 사용함.
    # 1. 로그인 상태인지 확인

    if  session is None: # 이미 None 이라는 뜻은 아니다. 없다라는 뜻을 내포하고 있으므로 같이 부정어를 사용할 수 없음. not 사용금지.
        print(f"{names}님이 로그아웃 되었습니다.") # 타입 에러 밟생, 함수에서 return을 사용했는데 아무 값도 돌려주지 않거나(None),
        # 변수에 값이 제대로 할당되지 않은 상태에서 str(문자열) 기능을 쓰려고 할 때도 이 메시지가 뜹니다.
        # **"코드가 좀 이상하니 확인해봐!"**라는 **경고(Warning)**의 의미입니다.
        # 해결책: 코드 맨 윗줄(ids, pws 정의하는 곳)에 session = None을 명시적으로 적어주세요.
        session = None

    else: # 이미 로그인 상태라면
        print("현재 로그인 상태입니다.") # 타입 에러 발생 (문법)

    print("member_logout 함수를 종료합니다.")
    # 로그아웃 함수 종료.

def member_modify():
    # 회원 정보 수정
    print("member_modify 함수로 진입합니다.")
    # 로그인 상태인지를 확인하고 자신의 정보를 확인 수정

    global session # 전역변수

    if session is None: # 만약 세션이 비어있다면 (로그인 안한 상태이면) 프린트에서 로그인 후에 이용가능하다는 출력을 사용할수 있음.
        print("로그인후 이용가능합니다.")
        session = None

    menu = input("선택 : ")

    print("\n 내정보수정")
    print("1. 이름 변경 : ")
    print("2. 비밀번호 변경 :")

    if menu == "1":
        names[session] = input("새 이름 : ")
        print("이름 변경 완료")

    elif menu == "2":
        pws[session] = input("새 비밀번호 : ")
        print("비밀번호 변경 완료")

    print("member_modify 함수를 종료합니다.")
    # 회원 정보 수정 종료

def member_delete():
    # 회원 탈퇴 및 비활성화 처리
    print("member_delete 함수로 진입합니다.")
    # 로그인 상태이지 확인하고 탈퇴는 pop, 비활성화 active를 False 처리.\

    global session

    if session is None:
        print("로그인 후 이용가능합니다.")
        return

    print("\n 회원 탈퇴")
    print("1. 회원 영구 탈퇴")
    print("2. 계정 비활성화")

    menu = input("선택 : ")

    if menu == "1":
        ids.pop(session) # 에러가 발생한 원인....(데이터 타입 충돌) pws는 원래 비밀번호들이 담긴 리스트. 근데,?
        pws.pop(session) # pws.index(...) 리스트에서 특정 값의 위치 숫자를 찾아주는 함수.
        names.pop(session) # pws 라는 변수에 리스트를 버리고 숫자를 넣어버리는 셈. 코드에서 다시 pws를 리스트처럼 쓰려고 하면, 컴퓨터는 인식하기를
        roles.pop(session) # 어? 아까 숫자로 바꿔놓고 왜 갑자기 리스트인 척해?라고 당황하며 에러를 내뿜는 것. -> 이를 해결방법:
        active.pop(session)
        session = None # 탈퇴했으니 로그아웃 처리한다는 뜻.
        print("회원 탈퇴 완료")

    elif menu == "2":
        active[session] = False
        session = None # 비활성화 했으니 로그아웃 처리
        print("계정이 비활성화 처리 되었습니다.")

    print("member_delete 함수를 종료합니다.")
    # 회원탈퇴 종료.

# ---------------------------------------기능에 대한 함수를 생성함.-----------------------------------


def mainmenu():
    print(f"""
======================================
엠비씨 아카데미 회원관리 프로그램

1. 회원가입
2. 로그인
3. 로그아웃
4. 회원보기
5. 회원수정
6. 회원탈퇴

9. 프로그램 종료

""")

# 메인메뉴용 함수 종료.

def member_add_menu():
    # 회원가입에서 사용할 메뉴
    print(f"""
=============회원권한을 확인하세요.================

1. 관리자
2. 일반사용자
3. 팀장

""")

# ---------------------------------메뉴 함수 종료.

# 프로그램 시작
while run:
    mainmenu() # 위에서 만든 메인 메뉴함수 실행

    print("mainmenu")
    select = input("1~6번까지 숫자를 입력하세요.")
    if select == "1":
        member_add()
        # 회원 가입용 함수

    elif select == "2":
        member_login()
        # 회원 로그인

    elif select == "3":
        member_logout()
        #회원로그아웃

    elif select == "4":
        member_modify()
        #회원정보 수정

    elif select == "5":
        member_delete()
        #회원탈퇴

    elif select == "9":
        run = False # while문 종료.

    else:
        print("잘못입력 하였습니다.")

    # 주 메뉴만 반복적으로 돌려사용하는 것.