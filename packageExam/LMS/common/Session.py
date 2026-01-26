# 로그인 상태 관리 클래스
# 현재 로그인 한 회원 (Member 객체) 을 보관
# 전역변수 대신 객체로 돌려사용함.
# 로그인, 로그아웃, 로그인여부, 관리자

# 이곳은 객체가 돌아다녀야 됨. @classmethod 로 함수 처리 필수

class Session:
    # def __init__(self) 필요없음
    # cls 로 Member를 활용하기 떄문

    login_member = None
    # 로그인을 했으면 login_member = Member()
    # 로그아웃을 했으면 login_member = None

    cart = [] # 장바구니 (Item 객체 저장하는 용)

    @classmethod
    def login(cls, member):
        cls.login_member = member
        cls.cart = []

    @classmethod
    def logout(cls):
        cls.login_member = None
        cls.cart = []

    @classmethod
    def is_login(cls):
        return cls.login_member is not None
        # cls : Member 객체         None 아니면 True


    @classmethod
    def is_admin(cls):
        # 현재 로그인 상태가 관리자 인지를 확인
        return cls.is_login() and cls.login_member_is.admin()
        #           True      and           Member().is_admin()
        #                                           True
        #                     and 는 둘 다 , True=True 처리함.

    @classmethod
    def is_manager(cls):
        # 현재 admin 관리자 상태인지
        return cls.is_login() and cls.login_member_is.manager()