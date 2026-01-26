# 이라고 치면 주석.
# 성적 처리용 프로그램을 개발해보자.

# C  CREATE : 성적입력
# R  READ : 성적보기
# U  UPDATE : 성적수정
# D  DELETE : 성적삭제

# 필요한 변수는??
sns = []                   # 학번
names = []                 # 이름
kors = []                 # 국어 점수
engs = []                  # 영어 점수
mats = []                 # 수학 점수
totals = []              # 총점 빈 배열
avgs = []                # 평균 빈 배열
grades = []              # 학점 빈 배열

# 성적 메뉴 구현
menu ="""
====================================
    mbc 아카데미 성적처리 프로그램
====================================

1. 성적입력
2. 성적보기
3. 성적수정
4. 성적삭제
5. 프로그램 종료

"""

run = True # 프로그램 실행 중이라고 생각하면 됨

while run: # run 변수가 false 처리 될 때까지 계속 반복한다라는 뜻.

    # : 아래는 들여쓰기 4칸 정도 처리
    # 들여쓰기를 진행ㅇ하면 하위 실행문 이다.
    # 가끔 빨간색 밑줄은 문법 오류일 수가 있어서 해결하고 진행.

    print(menu) # 콘솔창에 메뉴를 출력한다.
    select = input("(1~5) 값 입력 : ") # select 변수에 숫자를 넣는다.
    #               키보드로 입력받는 곳 앞쪽에 출력 메시지

    if select == "1": # 키보드로 입력한 숫자가 1이면, # = 는 값을 변수에 넣을 때 == 같은지 비교 동등비교
        print("학생 성적 입력하세요. ") # 1일 때 처리되는 부분
        sn = input("학번을 입력하세요 : ")
        name = input("이름을 입력하세요 : ")
        kor = int(input("국어 점수를 입력하세요 : "))
        eng = int(input("영어 점수를 입력하세요 : "))
        mat = int(input("수학 점수를 입력하세요 : ")) # 키보드를 이용한 점수 입력.
        #     키보드로 입력한 숫자는 문자로 인식됨으로 무조건 int()로 감싸 print할 때 계산용으로 바꿔준다.
        # 들어올 때는 문자로 받고, 나갈 때는 숫자로 나가기 때문에 int() 감싸준다.



        print("입력한 정보를 확인합니다. ")
        # print("학번 : " + sn)
        # print("이름 : " + name)
        # print("국어 : " + kor)
        # print("영어 : " + eng)
        # print("수학 : " + mat) # 키보드로 입력한 점수 확인
        # print에서 문자와 숫자가 같이 출력되려면 str() 숫자를 문자로 변경해야한다.
        # 그러나 f 포멧팅은 중괄호 안에 변수가 숫자든 문자든 상관없이 출력해준다.

        print(f"학번 : [sn], 이름 : [name], 국어 : [kor], 영어 : [eng], 수학 : [mat] ")


        if input("저장하려면 y : ") == "y": # 저장할 때 y 입력
            sns.append(sn)
            names.append(name)
            kors.append(kor)
            engs.append(eng)
            mats.append(mat) # 변수 뒤에 s는 배열(리스트) 라고 생각하면 됨.
                             # 변수. append() 배열 뒤에 (리스트)에 값이 추가된다 라고 생각하면 됨.

            total = kor + eng + mat
            totals.append(total) # 입력 후 저장 시 총점 계산하여 넣음.
            avgs.append(total / 3) # 입력 후 저장 시 평균 계산하여 넣음.
            # 미션 평균이 90이상이면 A, 80점 이상이면 B, 70점 이상이면 C, 나머지 F

            print("저장완료.")

        else:
            print("저장되지 않았습니다. ")
            print("처음부터 다시 입력하세요. ")




    elif select == "2":  # elif 는 1이 아닐 때 또 비교 # 키보드로 입력한 숫자가 2이면,,, # 2 일 때 처리되는 부분
        print("학생들의 성적을 출력합니다. ")
        print("==============================================================")
        print("[성적목록]")

        for i in range(len(sns)): # 리스트의 처음부터 끝까지 반복용
            #          len) -> sns 리스트의 길이를 가져옴. -> 5 (기본값)
            #    range(5) -> 0 ~ 5 까지 증가.
            # i in 5 -? i 값에 0 반복 1 반복 2 반복 3 반복 4 반복 5 끝.
            # 결론 : i 값이 인덱스로 사용함.

            # totals[i] = kors[i] + engs[i] + mats[i]
            # avgs[i] = totals[i] / 3
            # 오류 발생으로 주석 처리.  - > 인덱스 out of ragnge. 범위가 없다 공백이다라는 뜻.
            # 비어 있는 리스트는 주소가 없다.
            # 해결방법 : .append() 를 사용하면 빈 공백의 값도 같이 처리됨.
            # 처음부터 기초 데이터를 안쓰고 하는 방법. 문자를 숫자로 출력시킬 때 append를 다 때려박으면 꼬일 수 있다.


            totals.append(kors[i] + engs[i] + mats[i])
            avgs.append(totals[i] / 3)

            # grades 는 미션.


            print("-------------------------------------------------------------------------")
            print("학번 : " + sns[i] + "이름" + names[i])
            print("국어 : " + str(kors[i]) + "영어" + str(engs[i]) + "수학 : " + str(mats[i]))
            print("총점 : " + str(totals[i]) + "평균" + str(avgs[i]))
            print("-------------------------------------------------------------------------")

            # 프레임 틀, 워크 일한다.


    elif select == "3": # 3일 때 처리되는 부분
        print("학생 성적을 수정합니다. ")
        # 등록된 학생의 점수를 가져온다.
        # 학번을 이용하여 학생을 찾는다.
        sn = input("수정할 학번 : ")

        if sn in sns: # sns 는 학번이 들어있는 리스트 in 은 안에 있는지 확인.
            print("학번이 있습니다. ")
            idx = sns.index(sn) # 찾은 학번의 주소를 가져옴. idx는 index의 줄임말.
            print(f" 이름 : {names[idx]}, 국어 : {kors[idx]}, 영어 : {engs[idx]}, 수학 : {mats[idx]}")

        # 등록된 학생의 점수를 수정한다.
        # index 는 C,R,U,D 중에 R READ 전체보기, 1개만 보기의 주소를 불러오고 가지고 온다라는 뜻. idx.

            kors[idx] = int(input("수정할 국어 점수 : "))
            engs[idx] = int(input("수정할 영어 점수 : "))
            mats[idx] = int(input("수정할 수학 점수 : "))


            totals[idx] = int(input(kors[idx]) + input(engs[idx]) + input(mats[idx]))
            avgs[idx] = int(input(totals[idx]) / 3)
            grades = int(input(avgs[idx]))

        else:
            print("학번이 없습니다. ")
            print("처음으로 다시 돌아갑니다.")


    elif select == "4":
        print("학생 성적을 삭제합니다. ")
        sn = input("삭제할 학번 : ")

        if sn in sns:
            idx = sns.index(sn)
            print(f"{names[idx]} 학생의 정보를 삭제합니다. ")

            if input("정말 삭제할까요? (y) : ") == "y":
                print("삭제 완료되었습니다")
                sns.pop[idx]
                names.pop(idx)
                kors.pop(idx)
                engs.pop(idx)
                mats.pop(idx)
                totals.pop(idx)
                avgs.pop(idx)


            else:
                print("해당 학번이 없습니다.")


    elif select == "5":
        print("프로그램을 종료합니다")
        run = False


    else:
        print("1~5의 숫자만 허용합니다")
