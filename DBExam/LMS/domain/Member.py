# oop 기반의 Member 객체용.

class Member:

    def __init__(self, id, uid, pw, name, role='user',active=True):
        self.id = id # db의 pk (기본키) -> 자동번호 생성
        self.uid = uid # 아이디
        self.pw = pw # 비밀번호
        self.name = name # 이름
        self.role = role # 권한
        self.active = active # 활성화 여부
        # 사용방법
        # member = Member("kkw","1234","김기원","user")
        # Member 객체를 member 변수에 넣음.

    @classmethod # self 대신에 cls 라는 객체를 사용함. (주소 대신 객체)
    def from_db(cls, row: dict):
        #            row: dict (딕셔너리 타입 명시) ,
        #     dict 는 없어도 되지만 있는게 낫다.
        if not row:
            return None

        return cls(# db에 있는 정보를 dict 타입으로 받아와 id에 넣음
            id=row.get('id'), # id : 2
            uid=row.get('uid'), # uid : kkw
            pw=row.get('password'), # db 컬럼명이 'pw'인 경우 : 1111
            name=row.get('name'), # name : 김기원
            role=row.get('role'), # role : admin
            active=bool(row.get('active')) # active : 1 bool 타입이니까 True로 변환.
        )


    def is_admin(self): # role 이 admin 인지 여부 확인.
        return self.role == "admin"

    def __str__(self): # member 객체를 문자열로 출력할 때 사용(테스트용)
        return f"{self.name} ({self.uid}) [{self.role}]"

