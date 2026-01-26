# 패키지용 초기값 및 기능을 관리하는 파일

from .Member import Member
from .Board import Board
from .Score import Score
from .Item import Item
from .Order import Order



__all__ = [
    "Member","Board","Score","Item","Order"
]


# domain 파일을 생성하고 init 파일을 만들고 init에서 먼저 from .... import 를 각각 객체들을 처리한다.

# __all__ = [각 객체를 담당하는 것들을 쌍따옴표로 처리한다.]
