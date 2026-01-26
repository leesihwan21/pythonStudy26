# 패키지 : 관련된 모듈 (*.py) 를 디렉토리로 묶어서 실행할 수 있게
# 대부분 하위폴더 아래쪽에 관련 파일들을 모아 관리한다.

#  main.py
# __init__.py (패키지관리용 : 이 패키지가 제공하는 API 목록), 패키지에서 init의 기능을 써야 됨.(그냥 필수로 생각하자)

# 2. -service 하위 디렉토리
# __init__.py (패키지관리용)
# --MemberService.py, crud 실행
# --ScoreService.py
# --BoardService.py

# 3. -domain 하위 디렉토리
# __init__.py (패키지관리용)
# --Member.py 객체
# --Score.py
# --Board.py
# -data 하위 디렉토리
# --member.txt, -> 실무에서는 이렇게 사용함. 근데 import를 쓸거냐 from을 쓸거냐 이 차이.
# --score.txt
# --board.txt

# __init__.py : 패키지와 관련된 설정이나 초기화 코드를 포함함.
# 패키지 변수 및 함수를 정의할 수 있다.
# 패키지 내 모듈을 미리 import 하면 하위 py 파일을 한 번에 import 할 수 있다.
from.graphic.render import render_test
#   . 현재 위치(디렉토리)  .. 은 상위 폴더(디렉토리)
#     폴더   .모듈        함수()


VERSION = 3.5 # 변수명을 대문자로 사용하면 상수처리,(변하지 않는 값)

def print_version_info():
    print(f"이 게임의 버전은 {VERSION} 입니다.")


# 패키지 초기화 : 패키지를 처음 불러올 때 -> import game
# 실행 되어야 되는 코드를 작성할 수 있다.
# 예를 들면 데이터베이스 접속용 코드(연결용) / 파일로드 코드
print("게임 패키지를 실행합니다.")
print("패키지 초기화중.........")
print("데이터베이스를 연결합니다......")
print("게임 접속완료 -> 메뉴를 출력합니다.")




