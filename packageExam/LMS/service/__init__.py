# 패키지용 초기값 및 기능을 관리하는 파일

from .MemberService import MemberService
from .BoardService import BoardService
from .ScoreService import ScoreService
from .ItemService import ItemService
from .OrderService import OrderService

__all__ = [
    "MemberService",
    "BoardService",
    "ScoreService",
    "ItemService",
    "OrderService"
]


# service 파일 생성 후 __init__.py 파이썬 파일을 만들고
# from .MemberService import MemberService
# from .BoardService import BoardService
# from .ScoreService import ScoreService
# from .ItemService import ItemService

# -> from 0000 import 0000 -> 해준다.
# 그 다음에 MemberService 코드 생성
# ScoreService 코드 생성 .... 쭉 진행 하면 된다.

# main 메뉴는 맨 마지막 순서에서 함수를 구현한다.
