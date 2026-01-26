# 셀수 없이 많은 오류들..예외가 이것저것 날 것 같다.
# try 문 안에서 여러개의 오류를 처리

try:
    4/0
    a = [1, 2]
    print(a[3])
     # 이것을 실행하려면 finally 문 사용해야함.

# except ZeroDivisionError as e:
   # print(e)
   # print("0으로 나누어지는 예외가 발생함.")

# except IndexError as e:
   #  print(e)
   #  print("리스트 인덱스 범위 초과") # 만약에 위에 except 와 밑에 except 두개다 보고 싶다면 ????

except (ZeroDivisionError, IndexError) as e: # 한번에 어떠한 오류를 보고싶다면 이렇게 퉁 처리할 수 있다.
    print(e)
    print("0으로 나누었거나 리스트에 범위 초과 예외 발생")
    print("예외 발생 시 담당자에게 문의해주세요 : 전번")
