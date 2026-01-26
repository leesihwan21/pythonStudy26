# 상품에 대한 CRUD를 구현해보자.

# C -> CREATE : 새상품 등록
# R -> READ : 상품 전체보기, 상품 전체목록
# R -> READ : 단일 상품 자세히 보기
# U -> UPDATE : 상품 수정
# D -> DELETE : 상품 품절

# 사용할 변수 글로벌 전역변수=====================================
run = True

item_names = ["노트북","뫼니터"] # 상품명
unit_prices = [120000, 400000] # 단가
quantity = [40,25] # 상품 수량
product_info = ["AI용 삼성노트북", "LG24인치 LED"] # 상품 정보
category = ["가전","잡화"] # 상품 분류
cat_num = [0] # 카테고리 분류 번호
#===========================================================

# 사용할 메서드(함수)
def new_item():
    print("new_item() 함수 호출 완료")
    print("새 상품 추가용 함수로 진입합니다.")
    # 새 상품 추가용 실행문....

    print(f"\n 상품 카테고리 선택 ")

    category_choice = input("카토고리 선택 : ")

    if category_choice == "9":
        return

    if cat_num == "1":
        print("교재")

    elif cat_num == "2":
        print("잡화")

    elif cat_num == "3":
        print("음식")

    elif cat_num == "4":
        print("패션")

    else:
        print("잘못된 카테고리 선택")
        return

    name = input("상품명 : ")
    price = int(input("상품 단가 : "))
    quantity = input("상품 수량 : ")
    product_info = input("상품 정보 : ")
    category = input("상품 분류 : ")

    item_names.append(name)
    unit_prices.append(price)
    quantity.append(quantity)
    product_info.append(product_info)
    category.append(category)
    cat_num.append(cat_num)

    print(f"상품 {name}이 성공적으로 등록되었씁니다. ")


def item_list():
    print("item_list() 함수 호출 완료")
    print("현재 판매중인 상품 리스트 입니다")
    # 리스트 출력용. for item in item_names:

    item_list()
    print("=============================")
    print("-" * 40)
    print("번호\t상품명\t가격\t수량\t카테고리")
    print("-" * 40)
    print("=============================")

    for i in range(len(item_names)):
        print(f"{item_names[i]}\t{unit_prices[i]}\t{quantity[i]}\t{category[i]}\t")
        print("-" * 40) # -> ??? 파이썬에서 문자열 뒤에 곱하기 기호를 쓰면, 해당 문자열을 반복, 40: 반복할 횟수, "-": 출력하고 싶은 문자(열)


def item_view():
    print("item_view() 함수 호출 완료")
    print("상품 자세히 보기")
    # 상품에 대한 상세 정보 표시

    idx = int(input("자세히 볼 상품 번호 : ")) -1
    if 0 <= idx < len(item_names):
        print(f"\n---{item_names[idx]} 상세 정보 ---")
        print(f"카테고리 : {category[idx]}")
        print(f"단가 : {unit_prices[idx]}")
        print(f"상품명 : {item_names[idx]}")
        print(f"수량 : {quantity[idx]}")
        print(f"선택한 상품 자세히보기에 들어왔습니다.")

    else:
        print("존재하지 않는 번호 입니다.")
        return

def item_update():
    print("item_update() 함수 호출 완료")
    print("상품 수정 하기")
    # 상품에 대한 수정 하기

    idx = int(input("상품 수정 할 번호 : ")) -1
    if 0 <= idx < len(item_names):
        print(f"\n---{item_names[idx]}---")
        item_names[idx] = input("새 상품 선택 : ")
        unit_prices[idx] = int(input("새 상품 가격 :"))
        quantity[idx] = int(input("새 상품 수량 : "))
        product_info[idx] = input("새 상품 정보 : ")
        category[idx] = input("새 상품 분류 : ")
        print(f"{item_names[idx]} 새 상품이 수정되었습니다.")

    else:
        print("잘못된번호")
        return

def item_delete():
    print("item_delete() 함수 호출 완료")
    print("상품 삭제 하기")
    # 상품 삭제

    idx = int(input("상품 삭제 할 번호 : ")) -1
    if 0 <= idx < len(item_names):
        print(f"\n---{item_names[idx]}---")
        item_names.pop(idx)   # pop() : 리스트에서 값을 꺼내서 삭제한다. 삭제된 값을 변수에 담아서 다른 곳에 활용할 수 있음.
        unit_prices.pop(idx)    # del() : 그냥 그 자리에서 데이터를 지워버린다. 삭제된 값이 무엇이엇는지 다시 확인할 방법이 없음.
        quantity.pop(idx)       # del() 을 사용하게 되면, 삭제된 지워진 데이터 값을 보고 싶을 때 지워진 데이터 값을 다시 꺼내서 보고싶을때
        product_info.pop(idx)   # 못 보기 떄문이다.
        category.pop(idx)
        print(f"{item_names[idx]} 상품이 삭제되었습니다. ")

    else:
        print("잘못된번호")
        return


def main_Menu():
    print("""
===================================
엠비씨 아카데미 쇼핑몰 입니다.
    
1. 상품 등록
2. 상품 리스트
3. 상품 자세히 보기
4. 상품 수정하기
5. 상품 삭제하기
    
9. 프로그램 종료
    """)

def item_add_menu():
    print("""
======== 상품 추가용 메뉴에 진입하였습니다 =========
1. 교재
2. 잡화
3. 음식
4. 패션

9. 종료
    """)


# 프로그램 주 실행문
while run:
    main_Menu() # 메인 메뉴 함수 호출하여 출력. print가 들어있으므로 출력함.

    select = input("숫자를 입력 : ")
    if select == "1":
        item_add_menu() # 아이템 추가용 함수
        new_item() # 아이템 추가용 코드


    elif select == "2":
        item_list()



    elif select == "3":
        item_view()



    elif select == "4":
        item_update()



    elif select == "5":
        item_delete()



    elif select == "9":
        run = False


    else:
        print("잘못된 숫자를 입력하였씁니다.")
        print("다시 입력하세요.")




