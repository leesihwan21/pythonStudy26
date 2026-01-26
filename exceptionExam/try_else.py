# try_wlaw : try 문 수행 중 오류가 발생하면
# except 절을 처리하고
# 오류가 발생하지 않으면 else 로 수행된다.

try : # 성적 및 숫자와 관련된 코드 설계 할 떄 이 try_else 문장 사용하면 좋음.
    age = int(input("나이를 입력하세요"))

except : # except 에 클래스를 넣지 않으면 모든 예외라는 뜻을 가지고 있음.
    print("숫자만 입력하세요")

else: # 예외가 발생하지 않으면 처리되는 문장임.
    if age <= 18 :
        print("귀하는 미성년자 입니다.")
    else:
        print("환영합니다.")