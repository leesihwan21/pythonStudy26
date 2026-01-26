# 모듈 학습하기.
# 모듈은 파이썬 파일로 만든 것을 연동하여 프로그램으로 처리한다.
# 실무에서는 파일 한 개로 모두 만들어 제공하는 것이 아니라
# 각각 기능이 있는 파일을 빼서 클래스화 하고 메서드로 동작한다.

# Main.py -> __name__ (__main__) 주 실행코드와 서비스를 연결하는 주메뉴와 메서드 -> c,r,u,d
# MemberService.py -> __name__ (MemberService) 회원관리하는 클래스와 메서드 -> c,r,u,d
# ScoreService.py -> __name__ (ScoreService) 성적관리하는 클래스와 메서드 -> c,r,u,d
# BoardService.py -> __name__ (BoardService) 게시판을 관리하는 클래스와 메서드 -> c,r,u,d
# ItemService.py -> __name__ (ItemService) 상품을 관리하는 클래스와 메서드 -> c,r,u,d
# CartService.py -> __name__ (CartService) 장바구니를 관리하는 클래스와 메서드 -> c,r,u,d

# 파이썬 확장자 .py로 만든 파이썬 파일은 모두 모듈로 처리가능하다.

def add(a,b):
    return a+b

def sub(a,b):
    return a-b


# print(add(1,4))
# print(sub(4,2))
# 터미널에 python을 실행하고
# import를 mod1을 했더니
# 바로 print문이 실행된다.
# 당연한 결과이다.
# 근데 main에서 실행하면 ???
# mod1. py에서 print 2개가 실행되고
# main.py에서 print 2개가 실행된다.
# main에서는 add와 sub함수만 호출해서 사용하려고만 했다.
# 이 때는 if 문으로 실행을 조절해야한다.

if __name__ == '__main__': # 호출당하는 놈이 실행 안되게끔 하려면 요놈을 기억하면된다.
    # 클래스나 모듈이 호출된 자신이 main 역할인지를 확인하기 위해서 if문을 사용함.
    print(add(3,4))
    print(sub(5,4))
    print(type(__name__)) # >>> type(__name__), class 'str' 타입으로 나옴.

print(__name__) # mod1 으로 터미널에서 나옴.