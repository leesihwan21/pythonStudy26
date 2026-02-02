# Member 객체에 CRUD를 담당. 메뉴용 메서드 등을 넣어야 함.
import pymysql

from LMS.common import Session # __init__ 에 session이 비어있어서 빨간줄이 나옴.
from LMS.domain import Member

class MemberService:
    # 여기는 주소가 아닌 cls 클래스로 활용할거임. -> __init__ 메서드가 없다.

    @classmethod
    def load(cls): # db 에 연결 테스트 목적으로 생성함.
        conn = Session.get_connection() # LMS DB 를 가져옴. conn 이라는 변수에
        # 예외발생 가능 있음.
        try: # try문을 이용해서
            with conn.cursor() as cursor:  # db에서 가져온 객체 한 줄을 cursor 커서라고 부름.
                cursor.execute("select count(*) as cnt from members") # execute 실행한다.()
                #          수 나온 것을 cnt변수에 넣음  Member 테이블에서
                # Member 테이블에서 개수 나온것을 cnt 변수에 넣어라.
                # cursor.execute() sql 문 실행용.
                count = cursor.fetchone()['cnt'] # 딕셔너리 타입. dict cnt: 5 이런식으로..
                #             .fetchone() 1개의 결과가 나올때. readone
                #             .fetchall() 여러개의 결과가 나올때. readall
                #             .fetchmany(3) 3개의 결과만 보고싶을때. (최상위3개)
                print(f"시스템에 현재 등록된 회원수는 {count} 명 입니다. ")

        except: # 예외 발생 문구.
            print(f"MemberService.load() 메서드 오류발생..")

        finally: # 항상 출력되는 코드. try_except문 사용시 항상  finally 문 사용함.
            print(f"데이터베이스 접속종료")
            conn.close()


    @classmethod
    def login(cls):
        print("\n[로그인 메뉴]")

        uid = input("아이디 입력 : ")
        pw = input("비밀번호 입력 : ")

        conn = Session.get_connection()
        # print("Session.get_connection()" + conn)

        try:
            with conn.cursor() as cursor:
                sql = "SELECT * FROM members WHERE uid = %s AND password = %s"
                print("sql = " + sql)
                cursor.execute(sql,(uid,pw)) # 튜플은 1개여도 쉼표 필수.
                row = cursor.fetchone()
                # print("row = " + row[0])

                if row:
                    member = Member.from_db(row)

                    if not member.active:
                        print("비활성화 된 계정입니다. 관리자에게 문의하세요.")
                        return

                    Session.login(member)
                    print(f"{member.name} 님 로그인 성공 ({member.role})")

                else:
                    print("아이디 또는 비밀번호가 틀렸습니다.")

        except:
            print("MemberService.login() 메서드 오류발생..")

        finally:
            conn.close()


    @classmethod
    def logout(cls):
        # 1. 먼저 세션에 로그인 정보가 있는지 확인
        if not Session.logout():
            print("\n[알림] 현재 로그인 상태가 아닙니다.")
            return


        # 2. 세션의 로그인 정보 삭제
        Session.logout()
        print("\n[성공] 로그아웃 되었습니다. 안녕히 가세요.")


    @classmethod
    def signup(cls):
        print("\n[회원가입]")
        uid = input("아이디 : ")

        conn = Session.get_connection()
        try:
            with conn.cursor() as cursor:
                # 1. 중복 체크
                check_sql = "SELECT * FROM members WHERE uid = %s"
                cursor.execute(check_sql,(uid,)) # 튜플은 1개만 써도 쉼표, 필수.
                # print("cursor.fetchone() : " + cursor.fetchone()[0])
                if cursor.fetchone():
                    print("이미 존재하는 아이디 입니다.")
                    return

                pw = input("비밀번호 :")
                name = input("이름 : ")

                # 2. 데이터 삽입 -> mySQL 에 있는 데이터를 삽입.
                insert_sql = "INSERT INTO members (uid,password, name) VALUES (%s,%s,%s)"
                # check_sql = "SELECT * FROM members WHERE uid = %s" 와 insert_sql을 묶어서
                # 트랜젝션이라고 함.
                cursor.execute(insert_sql,(uid,pw, name))
                conn.commit() # connection 저장한다. 보관.
                print("회원가입 완료! 로그인 후 이용해주세요.")

        except Exception as e:
            conn.rollback()
            # 트랜젝션 : with 안쪽에 2개 이상의 sql 문이 둘다 true 일대는 commit()
            #                      2층 한개라도 오류가 발생하면 rollback()
            print(f"회원가입 오류: {e}")

        finally:
            conn.close()

    @classmethod
    def modify(cls):
        if not Session.login():
            print("로그인 후 이용가능합니다.")
            return

        member = Session.login_member
        print("\n[내 정보 수정]\n1. 이름 변경 2. 비밀번호 변경 3. 회원비활성 및 탈퇴 0 취소")

        sel = input("선택:")

        new_name = input("새 이름: ")
        new_pw = input("새 비밀번호: ")

        if sel == "1":
            new_name = input("새 이름: ")
        elif sel == "2":
            new_pw = input("새 비밀번호: ")
        elif sel == "3":
            print("회원 중지 및 탈퇴를 진행합니다.")

        else:
            return

        conn = Session.get_connection()
        try:
            with conn.cursor() as cursor:
                sql = "UPDATE members SET name = %s, password = %s WHERE id = %s"
                cursor.execute(sql,(new_name,new_pw, member.id))
                conn.commit()

            # 메모리 정보 동기화
            member.name = new_name
            member.password = new_pw
            print("정보 수정 완료")

        finally:
            conn.close()

    @classmethod
    def delete(cls):
        if not Session.login():
            return

        member = Session.login_member
        print("\n[회원탈퇴]\n1. 완전 탈퇴 2. 계정 비활성화")
        sel = input("선택: ")

        conn = Session.get_connection()
        try:
            with conn.cursor() as cursor:
                if sel == "1":
                    sql = "DELETE FROM members WHERE id = %s"
                    cursor.execute(sql,(member.id,))
                    print("회원 탈퇴 완료")
                elif sel == "2":
                    sql = "UPDATE members SET active = False WHERE id = %s"
                    cursor.execute(sql,(member.id,))
                    print("계정 비활성화")

                conn.commin()
                Session.logout()

        finally:
            conn.close()