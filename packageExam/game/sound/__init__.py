# __all__ 내장 변수

# __init__.py 파일이 있는 상태에서
# from game.sound import * (별 표시가 하위 모든 것)
#           패키지
# >> echo.echo_test()
# Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
# NameError: name 'echo' is not defined

# echo라는 이름이 정의 되지 않았다라는 오류가 나옴
# * 별표시를 사용하고 싶으면 2가지 해결방법
# 1. __init__.py 파일을 생성하지 말 것. (패키지가 아닌게 됨.)
# 2. __init__.py 이거 말고 - > __all__을 이용해서 제공할 것.

__all__ = ["echo"] # 변수에 리스트화 하여 모듈을 넣는다.
#          echo.py
# __all__ 이 의미하는 것은 sound 패키지 (디렉토리, 한 개의 방이라고 생각하면 됨) 하위 모듈을 import 할 목록.

# 이 때 착각하기 쉬운 것이
# from game.sound.echo import * 은 __all__ 에 상관 없이 import 됨.
#                 모듈
# from game.sound import * 는 패키지를 * 로 import 해서 __init__에 영향이 있다.
#           패키지


