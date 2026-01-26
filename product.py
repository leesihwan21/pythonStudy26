# while 문 : run, subrun
# if 문 : 메뉴 선택, 판단용
# for 문 : 리스트에 있는 전체 내용 출력용
# for in 문 : 리스트에 있는 내용 인덱스 찾는 용(주소값)

# 상품
# C CREATE : 상품등록 (ids,pws,
# R READ : 상품보기, 상품 리스트, 상품 자세히보기, 장바구니 바로구매,,,
# U UPDATE : 상품수정,,,관리자(판매자만),,,
# D DELETE : 상품삭제(품절이면 재고 정리),,,Sold Out,,,

# 상품에 필요한 변수들,,
# product_id ,,, 상품 고유 ID
# name ,,, 상품명
# price ,,, 상품 가격
# stock ,,, 상품 재고


run = True  # main menu 메인 메뉴용 while.
# subRun = True   # 보조 메뉴용 while.

# 상품등록에 대한 리스트,,,
product_no = [1]  # 상품 번호
names = ["clothes", "shoes", "pants"]  # 상품명
prices = [0]  # 상품가격
stocks = [0]  # 상품재고
created_at = [0]  # 상품등록날짜
product_sns = ["1234", "2345", "3456"]  # 회원 ID
product_pws = ["0000", "1111", "2222"]  # 회원 비밀번호

# 상품보기에 대한 리스트,,,
ids = ["kkw"]  # ID
product_name = ["clothe", "shoe", "pant"]  # 상품명
product_price = [0]  # 상품가격
product_stock = [0]  # 상품재고수량
product_sales_status = []  # 상품판매상황
product_buy_now = [0]  # 그 상품 바로구매
product_Add_cart = [0]  # 그 상품 장바구니 담기
product_hit = [0]  # 그 상품에 대한 좋아요
product_visitcount = [0]  # 그 상품 조회수

# 상품수정에 대한 리스트,,,
product_revised_at = [0]  # 상품수정일
product_ID = [0]  # 상품 id
product_names = [0]  # 상품명
product_prices = [0]  # 상품가격

# 상품삭제에 대한 리스트,,,
product_IDs = [0]  # 상품을 삭제할 ID
product_is_active = [0]  # 상품에 대한 품절여부(True ; 판매중, False ; 품절.
product_deleted = [0]  # 상품에 대한 삭제일

product_Menu = """
===========================================
상품 메뉴에 오신 걸 환영합니다.

1. 상품 등록하기 
2. 상품 리스트 보기 
3. 상품 수정하기  
4. 상품 삭제하기  

9. 홈페이지 종료
===========================================
"""

product_submenu = """
-------------------------------------------

1. 상품 등록
2. 상품 보기
3. 상품 수정
4. 상품 삭제

9. 홈페이지 종료
-------------------------------------------
"""

run = True  # main menu 메인 메뉴용 while.
subrun = True  # 보조 메뉴용 while.

while run:
    print("Menu")  # 상품 메인메뉴 출력용
    select = input("1~4번까지의 숫자를 입력하세요.")  # 사용자가 주 메뉴 선택 값을 select 넣는다.

    if select == "1":
        print("상품등록메뉴입니다.")
        print("등록하고 싶은 상품을 등록하세요")
        subrun = True

        while subrun:  # 상품 부 메뉴 반복용.
            print("submenu")
            print("1. 신규 상품 등록")
            print("2. 메인 메뉴로 돌아가기")
            subselect = input("선택 : >>>")

            if subselect == "1":
                print("상품 등록 메뉴 창입니다.")


                product_enroll_writer = input("상품 등록한 사람 : ")
                product_no = input("상품번호 : ")
                product_name = input("상품명 : ")
                product_create_at = input("상품 등록일 : ")

                print(f"상품 작성자 : + {product_enroll_writer}, 상품 번호 :  + {product_no}, 상품명 :  + {product_name}")
                print("f상품을 등록하려면 y를 누르세요")
                choice = input(f" 상품을 등록하려면 y를 누르세요 : ")

                if choice == "y":
                    product_enroll_writer.append(product_enroll_writer)
                    product_no.append(product_no)
                    product_names.append(product_name)

                    product_no = len(product_no) + 1
                    #    상품 리스트에서 인덱스를 추출하여 +1 값이 product_number.
                    # product_no 리스트의 길이를 활용해서 해결.

                    product_visitcount.append(0)
                    product_hit.append(0)

                    print(f" 상품{[product_no]}, {[product_name]}, {[product_enroll_writer]}이 등록되었습니다.")

            elif subselect == "9":
                subrun = False
# =================================================================================================================

    elif select == "2":
        print("상품 보기 리스트 입니다.")
        # 상품 보기 리스트 코드 추가용.
        print("==========================================================")
        print("상품번호\n, 상품명\n, 상품 등록자\n, 상품 조회수\n, 상품 좋아요\n")
        print("==========================================================")


        if len(product_no) == 0:
            print("등록된 상품이 없습니다.")
            continue  # 다시 while문으로 돌아감.

        for i in range(len(product_no)):
            print(f"{product_no[i]}, {product_names[i]}, {product_enroll_writer[i]} ")


        if subselect == "1":
            print("상품 자세히 보기 입니다.")
            product_no = int(input("상품 번호 : "))
            product_name = input("상품명 : ")
            product_pw = input("비밀번호 설정 : ")

            idx = product_no.index(product_no)


            if product_no in product_no:
                print("등록된 상품을 찾았습니다.")
                print("해당 상품을 장바구니에 담을까요? y를 누르세요 ")
                print("해당 상품을 바로구매 할까요? y를 누르세요 ")
                idx = product_no.index(product_no)
                idx = product_name.index(product_name)
                idx = product_enroll_writer.index(product_enroll_writer)

                product_no[idx] += 1  # 상품 조회수 +1 씩 증가함.

                if input("해당 상품을 장바구니에 담기(y) ") == "y":
                   product_Add_cart.append(product_no)
                   product_visitcount.append(0)

                   product_Add_cart += 1 # 장바구니 1씩 증가

                else:
                    print("해당 상품을 바로구매 합니다. ")

            else:
                print("해당 상품이 구매완료 되었습니다. ")

                print("------------------------------------------------------")
                print(f"상품번호 : {product_no[idx]}")
                print(f"상품명 : {product_names[idx]}")
                print(f"상품 등록한 사람 : {product_enroll_writer[idx]}")
                print(f"상품 조회수 : {product_visitcount[idx]}")
                print(f"상품 좋아요 : {product_hit[idx]}")
                print(f"상품 장바구니 : {product_Add_cart[idx]}")
                print(f"상품 바로구매 : {product_buy_now[idx]}")
                print("------------------------------------------------------")

            if input("상품 조회수 누르기(y) ") == "y":
                product_visitcount += 1
                print("해당 상품 조회수 1이 증가하였습니다.")

            if input("상품 좋아요 누르기(y) ") == "y":
                product_no += 1
                print("상품 너무 좋아요")  # 해당 상품에 대한 소비자가 좋아요

            else:
                print("해당 상품은 더 좋은 상품으로 보답하겠습니다.")

        else:
            print("등록된 해당 상품번호가 존재하지 않습니다.")
# ===================================================================================================================

        if subselect == "2":
            print("상품 가격 보기 메뉴입니다.")
            product_price = int(input("상품명 : {clothes}, {shoes}, {pants}"))

            clothes = int(input("옷 가격 : 0"))
            shoes = int(input("신발 가격 : 1"))
            pants = int(input("바지 가격 : 2"))

            print("해당 상품이 있습니다.")

        else:
            print("해당 상품이 없습니다.")

            if product_name in product_name == 0:
                print("옷을 찾았습니다.")

            for i in range(len(product_price)):
                print(f"옷 : {clothes}, 신발 : {shoes}, 바지 : {pants}")

            for product_name in range(len(product_name)):
                print(product_no[i], product_price[i])


# =====================================================================================================================

    elif select == "3":
        print("해당 상품 수정하기 메뉴 입니다.")
        product_no = int(input("상품 번호 : "))
        product_name = input("상품명 : ")
        pws = input("비밀번호 : ")

        if product_no in product_no:
            print("해당 상품이 수정되었습니다.")
            idx = pws.index(pws)

            if pws in pws:
                product_no[idx] = input("새로운 상품번호를 입력하세요 : ")
                product_name[idx] = input("새로운 상품명을 입력하세요 : ")
                print("등록된 해당 상품이 수정되었습니다.")
                print("중복된 상품이 있습니다.")

            else:
                print("상품번호가 틀렸습니다.")

        else:
            print("등록된 해당 상품이 존재하지 않습니다.")

            if product_no in product_no:
                print("해당 상품이 있습니다.")
                idx = product_no.index(product_no)

            else:
                print("해당 상품번호가 없습니다.")


    elif select == "9":
        print("홈페이지 종료합니다.")
        run = False
# ====================================================================================================================


    elif select == "4":
        print("해당 상품 삭제 메뉴입니다.")

        product_no[idx] = int(input("해당 상품 번호 입력 : "))
        product_name[idx] = input("해당 상품명 입력 : ")
        product_pws[idx] = input("비밀번호 : ")

        product_no[idx] += 1

        if product_no in product_no:
            print("해당 상품이 삭제되었습니다.")
            product_no.pop(idx)
            product_name.pop(idx)
            product_pws.pop(idx)
            product_enroll_writer.pop(idx)

    elif select == "5":
        print("[재고 현황 조회]")
        print("1. 상품번호로 검색 : ")
        print("2. 상품명으로 검색 : ")
        choice = input("번호선택 : ")

        found = False # 재고 현황 조회 검색 결과 여부 확인

        if choice == "1": # 재고 현황 조회를 1번으로 검색했을 때
            keyword = input("상품번호 : ").lower()

            print("상품번호\n상품명\n")

            for i in range(len(product_no)):
                if keyword in product_name[i].lower():
                    print(f"{product_no[i]}\n, {product_name[i]}\n")

                    found = True # 재고 현황 조회 검색 결과가 참일때 있을때

        elif choice == "2": # 재고 현황 조회를 2번으로 검색했을 때
            keyword = input("상품명 : ").lower()
            for i in range(len(product_no)):
                if keyword in product_name[i].lower():
                    print(f"{product_no[i]}\n, {product_name[i]}\n")

                    found = True

                else:
                    print("해당 상품번호가 틀렸습니다.")

            else:
                print("상품명이 틀렸습니다.")

            if not found:
                print("검색 결과가 없습니다.")
                print("처음 페이지로 돌아갑니다.")
                run = False # 다시 돌아가기

    elif select == "9":
        print("해당 홈페이지 종료.")
        run = False

        if subselect == "9":
            print("해당 홈페이지 종료")
            subrun = False

# --------------------------------------------------------------------------------------------------------------------














