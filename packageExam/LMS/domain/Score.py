


class Score:

    def __init__(self, uid, kor, eng, mat): # 성적 과 관련한 초기값 설정. ex self 변수 안에 uid, kor, eng, mat....
        self.uid = uid
        self.kor = kor
        self.eng = eng
        self.mat = mat


    @property
    # @property 를 total 값이 변경되어도 avg를 호출하는 순간 실시간으로 계산된다.
    # 항상 최신 상태의 평균값을 유지하기 위해서 성적이나 숫자와 관련된 코드를 할 때 property라는 함수가 주로 사용된다.
    # 또한, 안전하다.
    def total(self): # 변수처럼 사용하기
        return self.kor + self.eng + self.mat # 각 영역의 점수들을 합친 점수

    @property
    def avg(self): # round 함수를 이용해서 self.total/3,2를 하게 되면????
        return round(self.total / 3, 2) # 소수점 셋째 자리에서 반올림하여 둘째 자리까지 표시한다. 라는 뜻.
    # 예를 들면? 출력. 83.33 점 (250 /3 = 83.3333...이 반올림 된다는 뜻이다)

    # 성적 등급 자동 계산 코드==============================================================================

    @property
    def grade(self): # 요것도 변수처럼 사용하기.
        if self.eng >= 90:
            return ("A")

        elif self.eng >= 80:
            return ("B")
        elif self.eng >= 70:
            return ("C")

        else:  # 70점 미만이면 모두 F 학점이라는 함수 else.
            return ("F")

    # ==================================================================================================

    def to_line(self): # 메모리에 있는 내용을 한 줄씩 가져옴.
        return f"{self.uid} {self.kor} {self.eng} {self.mat}\n"

    @classmethod
    def from_line(cls, line): # 역직렬화
        uid , kor, eng, mat = line.strip().split("|")
        return cls(uid, kor, eng, mat)
    # 클래스 메서드 함수를 사용함으로써 uid, kor, eng, mat 에 있는 내용을 strip와 split 처리함.
    # ==================================================================================================

