# 세션에서 db 접속도 관리하자.
# 현재 세션으로 상태 관리를 하는데 차후에
# 프론트를 배우면 웹브라우져에서 세션을 처리한다.
# html + css + js : w3c 라고 부른다. 웹표준
# 차후에는 이곳이 db 관리하는 connection 영역이 될 것이다.

# 파이참에도 db를 관리하는 메뉴가 있다.
# 오른쪽 버튼을 보면 db 선택할 수 있다. -> mysql 워크벤치 대타용.

import pymysql # mysql 과 파이참이랑 돌릴 때 가져옴.
# pip install pymysql -> 터미널에서 설치 필수.
# 이거 지울 땐 uninstall 하면 지워짐.

class Session:
    login_member = None

    @staticmethod
    def get_connection(): # 데이터베이스에 연결용 코드
        print("get_connection() 메서드 호출 - mysql에 접속됩니다.")
        return pymysql.connect(
            host='localhost', # 다른 사람꺼 연결하겠다 192.168.0.xxx
            user='mbc',
            password='1234', # 본인의 비밀번호로 변경
            db='lms',
            charset='utf8mb4', # 한글지원용
            cursorclass=pymysql.cursors.DictCursor, # 커서클래스는 딕셔너리
            # 타입이다. 키 밸류 키 밸류를 객체화
            # dict 타입으로 처리함.
        )

    @classmethod
    def login(cls, member): # MemberService 에서 로그인시 객체를 담아야함
        cls.login_member = member

    @classmethod
    def logout(cls):
        cls.login_member = None


    @classmethod
    def is_login(cls):
        return cls.login_member is not None


    @classmethod
    def is_admin(cls):
        return cls.is_login() and cls.login_member.role == "admin"


    @classmethod
    def is_manager(cls):
        return cls.is_login() and cls.login_member.role == "manager"



