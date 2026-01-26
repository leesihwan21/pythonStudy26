import os

from packageExam.LMS.domain import Score
from packageExam.LMS.common import Session

FILE_PATH = "data/Score.txt"

class ScoreService:

    Scores = []

    # 파일 불러오기=================================================================================================
    @classmethod
    def load(cls):
        cls.Scores = []

        if not os.path.isfile(FILE_PATH):
            cls.save()
            return

        with open(FILE_PATH, "r", encoding="utf-8") as f:
            for line in f:
                print(line)
                cls.scores.append(Score.from_line(line))

    # 파일 저장하기================================================================================================
    @classmethod
    def save(cls): # 파일 저장
        with open(FILE_PATH, "w", encoding="utf-8") as f:
            for score in cls.scores:
                f.write(score.to_line())


    # 성적 메뉴===================================================================================================
    @classmethod
    def run(cls):
        if Session.login_member is None:
            print("로그인후 이용가능합니다.")
            return

        member = Session.login_member

        cls.save() # 저장된 파일 불러오기.

        while True:
            print("""\n====[성적관리]====""")

            if member.role in ("manager","admin"): # if member.role in ("manager","admin")
                print("1. 학생 성적 입력")

            print("내 성적 조회")

            if member.role == "admin": # if member.role == "admin": 회원 상태가 관리자이면?????
                print("뒤로가기") # print 돌아가기

            sel = input("메뉴 선택")

            if sel == "1" and member.role in ("manager","admin"): # if 문에서 1번을 선택시, 그리고 회원상태가 매니저나 관리자이면????
                cls.add_score() # 성적 입력한 내용 저장하기
            elif sel == "2": # 2번이면????
                cls.view_my_scsore() # 내 성적 조회를 할 수 있음.
            elif sel == "3" and member.role == "admin": # 3번 그리고 회원 상태가 관리자이면???
                cls.view_all() # 전체 목록을 조회할 수 있다.
            elif sel == "4": # 4번이면
                break

    # 성적 입력==================================================================================================
    @classmethod
    def add_score(cls):
        member = Session.login_member

        # 권한 체크
        if member.role not in ("manager","admin"): # 실무에서는 not in 을 많이 사용함. 왜냐하면, != 코드를 사용하게 되면
            # 지저분해지기 떄문에. 예를들면, if member.role != "admin" and member.role != "manager" and member.role != "staff":??
            # 이런식으로 문장이 길어지기 떄문에 , not in 을 사용함.
            # 무조건 != 로 하고 싶으면 최고 직급 직책만을 가진 사람만 볼 수 있게 할 수있도록 코드를 짤 수도 있다.
            print("성적 입력 권한이 없습니다.")
            return # 돌아가라.

        uid = input("아이디 : ")

        # 기존 성적 제거 (있으면 수정 개념)
        cls.scores = [s for s in cls.score if s.uid != uid] # != -> not 이 아니면이라는 뜻이랑 같음.
        # 기존 데이터의 중복을 방지하기 위한 핵심 로직....
        # 데이터 무결성을 위해 반드시 필요한 함수 로직. 만약 없을 시엔 중복으로 데이터가 될 수가 있어서.

        kor = int(input("국어 점수 : "))
        eng = int(input("영어 점수 : "))
        mat = int(input("수학 점수 : "))

        cls.scores.append(Score(uid, kor, eng, mat))
        cls.save()

        print("성적 입력 완료")

        # cls.scores = [s for s in cls.scores if s.uid != uid] -> 기존 성적 데이터 중복을 방지하기 위한로직
        # cls.scores.append(Score(uid, kor, eng, mat)) -> append를 이용해서 성적 데이터를 맨 뒤에 추가한다.

    # 성적 조회===================================================================================================
    @classmethod
    def view_my_scsore(cls):
        member = Session.login_member

        for score in cls.scores:
            if score.uid == member.uid:
                cls.print_score(score)
                return

            print("등록된 성적이 없습니다.")

    # 전체 성적 조회===============================================================================================
    @classmethod
    def view_all(cls):
        member = Session.login_member

        if member.role != "admin": # admin 관리자가 아니면. != -> not in
            print("관리자만 접근 가능합니다.")
            return

        print("\n[전체 성적 목록]")
        for s in cls.scores:
            cls.print_score(s)

    # 출력 공통 함수==============================================================================================????
    @staticmethod
    def print_score(score):
        print(f"ID:{score.uid} | 국어:{score.kor} | 영어:{score.eng} | 수학:{score.mat} "
              f"총점:{score.total} | 평균:{score.avg} | 등급:{score.grade}")
    # 인자를 자동으로 전달받지 않는다. 일반 함수처럼 작동하지만, 논리적으로 이 클래스와 관련이 있을 때 클래스 내부에 둔다.
    # 오직 score 객체의 정보만을 출력하고 있기 때문에 staticmethod 정적 메서드 함수가 적합하다.


# from packageExam.LMS.domain import Score
# from packageExam.LMS.common import Session

# file_path = "data/score.txt"

# class scoreservice
#       scores = []

# @classmethod
# def load(cls):
#     cls.scores()
#     if not os.path.exists(FILE_PAHT):
#       cls.save()
#       return
#     with open(FILE_PATH, "R", encdoing="utf-8") as f:
#           for line in f:
#               cls.score.append(scores.from_line(line))

# def save(cls):
#   with open(FILE_PATH, "W", encoding="utf-8") as f:
#       for score in cls.scores:
#           f.write(score.to_line())

# 성적메뉴
# @classmethod
# def run(cls):
#     if session.login_member is None:
#       print("로그인 후 이용")
#       return
#   Session.login_member()
#   print(f"{m.name}님 로그인 성공")
#   cls.save()
#   while True:
#       print("""성적메뉴""")
#       if member.role in ("manager"/"admin")
#           print("학생 성적 입력")
#       print("내 성적 조회")
#       if member.role == "admin":
#           print("돌아가기")

#       sel = input("선택")
#       if sel == "1" and member role in ("manager" / "admin")
#       cls.add_score()
#       elif sel == "2"
#           cls.view_my_scsore()
#       elif sel == "3" and member role == "admin"
#           cls.view_all_list()
#       elif sel == "4" : break

#============================================================================================



