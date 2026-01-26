# 회원관리용 더미 데이터를 텍스트 파일로 (메모장) 저장하여 관리해본다.
import os

# 회원관리용 더미데이터를 파일(메모장)로 저장하여 관리해보자.

# 회원관리 curd를 사용자 지정 함수로 만들어 보자.
# c : 회원가입
# r : 회원리스트 관리자인경우 회원암호 변경, 블랙리스트로생성, 권한 부여
# r : 로그인 id와 pw를 활용하여 로그인 상태 유지 session
# u : 회원정보 수정
# d : 회원탈퇴, 회원비활성화

# 프로그램에서 사용될 변수들
# 전역변수(global) -> py 파일 안에서 전체적으로 사용되는 변수
# 지역변수(local) -> while, if, for, def안에서 사용되는 변수
run = True  # while 에서 전체적으로 사용되는 변수(프로그램 구동)
session = None  # 로그인상태 저장용 -> 로그인한 사용자의 리스트 인덱스 기억용
FILE_NAME = "member.txt"  # 회원 정보를 저장할 메모장 파일명
members = ["kkw", "1234", "김기원", "admin", True] # 지금은 공백 이지만 조금 이따가 메모장에 있는 내용으 ㄹ가져와 리스트배열로 처리함.

# members 구조
# [아이디, 비밀번호, 이름, 권한, 활성화 여부]
# 변수 :  uid        pw       name       role       active
#  값 :  "kkw",,, "1234",,, "김기원",,,,"admin",,,,, "True",,,,,(활성화) 이런식으로 메모장에 한줄이 들어가있다.
# kkw|1234|김기원|admin|True 로 메모장에 저장될 예정. 파이프 shift 역슬래시 누르면 파이프 됨.
# [[           ],[               ], [                  ]]
#      0                1                    2 ...........

#[아이디, 비밀번호, 이름, 권한, 활성화여부]
#  0       1      2    3       4
#                [아이디, 비밀번호, 이름, 권한, 활성화여부]
#                                  [아이디, 비번, 이름,권한, 활성화여부]

# members[1][3] -> 두 번째 회원의 권한.
# kkw|1234|김기원|admin|True 로 메모장에 저장될 예정임.


# ===============파일저장====================================================================================

def save_members(): # 메모리상에 리스트를 파일로 저장한다. # members가 하는일은 2차원 배열.
    """
    members 2차원리스트 내용을 읽어서 members.txt 파일에 저장한다.
    """

    with open(FILE_NAME, "w", encoding = "utf-8") as f: # f 파일객체 , with는 close를 자기가 직접 처리함.
        # 대문자로 쓰는 애들은 상수처리시킨다.
        # 변하지 않는 값.
        #     상수    w = 덮어쓰기 한글처리용  파일객체(파일이 들어있는 변수)
        #            a = 추가용(append)
        # 메모리에 있는 리스트를 | 파이프로 연결하여 한줄로 저장한다.

        for member in members: # members 는 메모리에 있는 2차원 배열. member라는 곳에 하나씩 넣음. # f 포맷팅 문자열 한 번에 모두 다 받는다.
            line = f"{member[0]} | {member[1]} | {member[2]} | {member[3]} | {member[4]}\n"
            f.write(line) # f는 열린 파일.
            # save members() 함수 종료

#========================================================================================================

def load_member(): # txt 텍스트 메모장 파일 전체를 불러와 리스트로 만든다. 중간수정이 안됨.
    """
    members.txt 파일을 읽어서 members 파일에 저장한다.
    """

    global members
    members = [] # 기존 member 데이터 초기화

    # 파일이 없으면 새 파일을 생성(암기)
    if not os.path.exists(FILE_NAME): # 지금 디렉토리에 FILE_NAME 파일이 없으면
        # os.path 는 현재 위치, 현재 경로, -> os 는 내부 라이브러리지만 기본적으로 포함하지 않아 import를 해야함.
        save_members() # 빈 파일이 members.txt 로 생성함.
        return # 돌아가기. 함수를 빠져나와 main menu로 다싣 돌아감. return을 걸어놨기 때문에 else처리 함.

    # 있으면 파일을 열어서 한 줄씩 읽기를 해야함.
    with open(FILE_NAME, "r", encoding = "utf-8") as f:
        # 저장할 때 사용했던 "w" 대신 **"r"**을 사용함으로써,
        # 하드디스크에 저장된 members.txt 파일의 내용을 다시 파이썬의 **메모리(members 리스트)**로 불러올 준비를 하는 것입니다.
        # members.txt 읽기 전용       한글지원
        for line in f: # f 힘영역에 있는 파일 . kkw|1234|김기원|admin|true 를 line 변수에 넣는다.
            print(f"변조 전 데이터 : {line}") # kkw 1234 김기원 admin True

            # 줄끝에 enter 를 제거. | 파이프로 분류된 것을 리스트 해야함.
            data = line.strip().split("|") # strip 는 - > 맨 뒤에 있는 엔터를 제거시켜주는 기능.
            # split 는 -> | 기준으로 나눈다
            print(f"변조 후 데이터 : {data}")
            print("======================================================================")

            # 변조 후 데이터를 확인해보면 모두 다 문자열을 취급한다.
            # 문자열 True 블리언 타입 (True/False) 변환을 하기 위해서.
            data[4] = True if data[4] == "True" else False
            # 받은변수  넣을 값  데이터 4번째가 문자열 True 이면
            #                               아니면 False.
            # if data[4] == "True":
            #    data[4] = True
            # else:
            # data[4] = False
            print(f"변조 후 데이터 : {data}")
            print("======================================================================")

            # 맨 마지막에 members 를 리스트에 넣는다.
            members.append(data)
            # load_members() 함수 종료.

# 프로그램에서 사용할 메서드
def member_add():
    # 회원가입용 함수
    print("member_add 함수로 진입합니다.")
    # 회원가입에 필요한 기능을 넣음
    new_id = input("아이디 : ") # ex kkk
    # 아이디 중복 검사
    for member in members:
        if member[0] == new_id: # {member[0]}|{member[1]}|{member[2]}|{member[3]}|{member[4]}| -> member
            #                          0           1           2            3           4
            #                         id          pw         name         role        active
            print("이미 존재하는 아이디 입니다.")
            return # 돌아가기. 함수를 빠져나와 main menu로 다싣 돌아감. return을 걸어놨기 때문에 else처리 함.

    # else 처리없이 return으로 처리함.

    pw = input("비밀번호: ")
    name = input("이름 : ")

    # 권한 선택
    print("1. admin, 2. manager, 3. user.")
    roleSelect = input("권한 선택 ")

    role = "user" # 잘못  입력하면 user 권한으로 기본값
    if roleSelect == "1":
        role = "admin"
    elif roleSelect == "2":
        role = "manager"
    # if 문 위에 role = "user" 로 입력을 해놓았기 때문에 else 를 쓸 필요가 없다.
    # role = user 가 user 권한으로 기본값으로 설정된 상태이다.

    # ======== 입력 종료 ===============================================
    print(f"[입력정보확인] 아이디 : {new_id} 이름 : {name}, 권한 : {role}, 암호 : {pw}")
    # ======== 입력값 ==================================================
    # f 포맷팅을 해주었으면 그 다음에는 입력값을 확인할 정보를 확인해야함.

    save_confirm = input("정말로 저장하시겠습니까? (y/n) : ")

    if save_confirm == "y":
        # 저장 시작
        members.append([new_id, pw, name, role, True]) # 리스트로 만듬
        save_members() # 리스트를 파일에 저장
        print("회원가입완료")
        members.append([new_id, name, role, pw])
        save_members()

       # member_add() 함수 종료

    print("member_add 함수를 종료합니다.")


# 회원가입용 함수 종료

def member_login():
    # 가입된 회원을 확인하여 로그인 처리 후 session 변수에 인덱스를 넣음
    print("member_login 함수로 진입합니다.")
    # 로그인에 필요한 기능을 넣음
    global session # 전역변수로 생성한 값을 가져옴. (이미 로그인한 상태일수가????있고??? None 이면 로그인 안된상태...가 됨.)
    #                                               index가 있을거임
    print("\n(로그인)")
    uid = input("아이디: ")
    pw = input("비밀번호: ") # 키보드로 아이디와 비밀번호를 입력. 하고 변수에 넣음.

    # 회원목록에서 아이디를 찾아야함.
    for idx, member in enumerate(members): # enumerate 함수는 꼭 필요한 함수.
        #   enumerate() for 문은 반복문이잖아. 주소를 찾아올수있음(index)
        #   idx = 1차원 주소
        #   member -> 2차원 리스트
        #   멤버스에 있는 것들을 하나씩 꺼내와서 멤버, idx에 넣음. idx 에는 0(1차원 리스트), 멤버에는 리스트가 들어옴.
        #   idx 를 session 에 넣음. session 은 1차원 주소.

        if member[0] == uid: # 키보드로 입력한 uid와 리스트에 있는 값이 같으면, 아이디 찾음
            if not member[4] : # active 상태 확인 (False 이면) false = not 이니까
                print("로그인 할 수 없는 계정입니다.") # 블랙리스트/비활성화
                return # 로그인 중지.

            # 비밀번호 확인
            if member[1] == pw: # 키보드로 임력한 암호화 리스트 [1] 번에 암호가 같으면
                session = idx # 전역변수에 로그인 한 주소를 넣음.
                print(f"{member[2]} 님 로그인 성공 ")

        # 관리자일 경우 메뉴 호출
                if member[3] == "admin":
                    member_admin()
                return # for 문까지 빠져나옴. 로그인 멤버라는 함수를 종료한다.

            else:
                print("비밀번호가 틀렸습니다. 초기메뉴로 return 합니다. ")
                return
        else:
            print("존재하지 않는 아이디 입니다.")
            return
    # for문이랑 같은 line에서 출력. # for 문이 진행하면서 return에 없는 경우.

print("member_login 함수를 종료합니다.")

# 회원로그인용 함수 종료

def member_logout():
    # 회원 로그아웃으로 상태 변경 -> session 값을 None으로 변경
    print("member_logout 함수로 진입합니다.")
    # 로그인 상태인지를 확인하고 session을 None으로 변경

    # 로그아웃 기능 로직 생각해서 추가 해볼 것....
    # 로그아웃 기능의 작동원리 ....

    # 1. 로그인 중일 떄 session 변수에는 회원의 인덱스(index) 번호[1] 가 들어있음.
    # 2. 로그아웃 실행 : session 변수에 None을 대입함.
    # 따라서, 이후 프로그램에서 if session is not None: 조건을 체크할 때 "로그인 안 됨"으로 판단되어 다시 메뉴로 돌아가게 됨.

    global members
    session = None

    if session is not None:
        print("현재 로그인 상태가 아닙니다.")
        return

    user_name = members[session][1]  # 1번의 회원 상태를 가지고 옴.
    session = None

    save_members()  # 파일 저장 .
    print(f"{user_name} 님 로그아웃 되었습니다. ")

    # 추가 팁: 더 안전한 로그아웃
    # 로그아웃할 때 혹시나 변경된 데이터가 있을지 모르니,
    # save_members()를 한 번 호출해 주는 습관을 들이면 데이터 유실을 방지할 수 있어 더욱 안전합니다.
    # 이제 로그인 → 관리자 메뉴 → 권한 변경 → 로그아웃으로 이어지는 전체 흐름이 완성.

    print("member_logout 함수를 종료합니다.")
    # 로그아웃 함수를 종료

       # ===============================================================================================================


def member_admin():
    # 관리자가 로그인 했을 경우 할수 있는 기능을 작성
    print("member_admin 함수로 진입합니다.")
    # 다른 사용자 암호 변경 코드
    print("\n 관리자 메뉴")
    print("1. 비밀번호 변경")
    print("2. 블랙리스트 처리")
    print("3. 권한변경")
    print("4. 종료")

    menu = input("선택 : ")
    target_id = input("아이디 : ")

    if menu == "1":
        print("새 비밀번호 : ")
        print(f"{target_id} 님이 비밀번호가 변경되었습니다. ")

    elif menu == "2":
        print("블랙리스트 대상 : ")
        print(f"{target_id} 님이 블랙리스트로 변경되었습니다. ")

    elif menu == "3":
        new_role = input("권한 변경 : {admin/manager/user} ")
        members[target_id][3] = new_role # 권한 변경 할 번호 가정
        print(f"{target_id[3]} 님이 권한이 {new_role} 권한 변경 되었습니다. ")

    elif menu == "4": # 관리자가 비활성화 된 계정 회원을 다시 활성화 상태로 돌려주는 기능 추가.
        target_id = input("활성화 할 아이디 : ")

        # 회원 목록에서 아이디 찾기
        for idx, member in enumerate(members):
            if member[0] == target_id:
                target_idx = idx
                break

                # 아이디 존재여부 확인 후 상태 변경
                # 4번 인덱스가 상태값 (True -> 활성화, False -> 비활성화) 인 경우
            if member[target_id][4] == True or members[target_id][4] == "활성화":
                print(f"{target_id} 님은 이미 활성화 된 상태입니다. ")

            else:
                members[target_id][4] = True # 활성화 상태를 다시 비활성화 상태로 변경
                print(f"{target_id} 님의 계정이 성공적으로 비활성화 되었습니다.")
                save_members() # 변경된 내용을 파일에 다시 저장.

        print("관리자가 작업 완료하였습니다.")
        return # 돌아가기. if 문 함수에서 빠져나오기.

    print("대상 아이디가 없습니다.")

    # 블랙리스트로 변환 -> active를 False
    # 권한 부여 -> 사용자의 권한roles를 변경 (manage <-> user)

    print("member_admin 함수로 종료합니다.")

# 관리자가 사용자 변경사항 함수 종료

def member_modify():
    # 회원 정보 수정
    print("member_modify 함수로 진입합니다.")
    # 로그인 상태인지를 확인하고 자산의 정보를 확인하고 수정한다.

    global members
    session = None

    if session is None:
        print("로그인 후 이용가능합니다.")

    menu = input("선택: ")
    print("\n 내정보수정")
    print("1. 이름 변경 ")
    print("2. 비밀번호 변경")

    if menu == "1":
        members[session][2] = input("새 이름 :")
        print("이름이 변경되었습니다.")

    else:
        print("비밀번호가 변경되었습니다.")

    save_members()
    print("정보수정완료")

    print("member_modify 함수를 종료합니다.")
# 회원정보 수정 종료

def member_delete():
    # 회원 탈퇴 또는 회원 유휴등 처리
    print("member_delete 함수로 진입합니다.")
    # 로그인 상태인지를 확인하고 탈퇴는 pop, 유휴(active=False)

    global members
    session = None

    if session is None:
        print("로그인 후 이용가능합니다.")
        return

    print("\n회원탈퇴")
    print("1. 회원 영구 탈퇴")
    print("2. 비활성화 ")

    menu = input("선택 : ")

    if menu == "1":
        print("회원 영구 탈퇴되었습니다. ")
        # pop() 함수는 리스트에서 해당 데이터를 아예 삭제하고 꺼내버리는 기능
        # 문제 1 (데이터 삭제): members.pop(session)을 실행하는 순간, 해당 회원은 members 리스트에서 완전히 사라집니다.
        # 비활성화가 아니라 회원 탈퇴가 되어버리는 거죠.
        del members[session] # 해당 회원을 영구히 삭제시킨다라는 뜻.
        session = None

    elif menu == "2":
        print("계정이 비활성화 되었습니다. ")
        members.pop(session)[4] = False # False 는 계정 비활성화

    save_members() # 삭제된 상태로 파일을 갱신. -> members.txt 파일로 저장시킴.
    print("member_delete 함수를 종료합니다.")
# 회원탈퇴 종료

# --------------------- 기능에 대한 함수 생성 끝----------------

def main_menu():
    print(f"""
    ==== 엠비씨아카데미 회원관리 프로그램입니다======
    1. 회원가입    2. 로그인     3. 로그아웃
    4. 회원정보수정      5. 회원탈퇴
    9. 프로그램 종료
    """)
# 메인메뉴용 함수 종료

def member_add_menu():  # 회원가입에서 사용할 메뉴
    print(f"""
    ----- 회원권한을 확인하세요.---------
    1. 관리자    2. 팀장    3. 일반사용자 
    """)


# ------------------ 메뉴 함수 끝 ---------------------------

# 프로그램 시작!!!!

load_member() # 프로그램 시작 시 파일을 불러온다. (한 번만, 초기 리스트만 넘어오고 그 뒤로는 while 문이 돌아감.) -> 2차원 배열로 불러옴.(한번만)
print(members)
while run:  # 메인 프로그램 실행 코드
    main_menu()  # 위에서 만든 메인 메뉴함수를 실행

    if session == None: # 로그인 안 한 상태
        print("현재 비로그인 상태입니다. 로그인 하려면 2번을 누르세요.")
        print("회원이 아니면 1번을 누르세요.")
    else:
        print(f"{members[session][2]} 님 환영합니다. ")


    select = input(">>>")  # 키보드로 메뉴 선택

    if select == "1":  # 회원가입 코드
        member_add()  # 회원가입용 함수 호출

    elif select == "2":  # 로그인 메뉴 선택
        member_login()  # 로그인용 함수 호출

    elif select == "3":  # 로그아웃 메뉴 선택
        member_logout()  # 로그아웃 함수 호출

    elif select == "4":  # 회원정보 수정 선택
        member_modify()  # 회원정보 수정 함수 호출

    elif select == "5":  # 회원탈퇴 선택
        member_delete()  # 회원정보 삭제 함수 호출

    elif select == "9":  # 프로그램 종료 선택
        run = False

    else:
        print("잘못 입력하셨습니다.")


