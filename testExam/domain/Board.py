

class Board:

    def __init__(self, no, title, name, content, write, active = True):
        self.no = no
        self.title = title
        self.name = name
        self.content = content
        self.write = write
        self.active = active

    # 파일용 직렬화=============================================================================
    def to_line(self):
        return f"{self.no},{self.title},{self.name},{self.content},{self.write},{self.active}"

    # 텍스트 .txt 에 있는 파일용 역직렬화
    @staticmethod # staticmethod 를 사용하는 이유는 텍스트에 있는 파일 내용을 문자열로 그대로 받기 위해서
    def from_line(line):
        no,title,name,content,write,active = line.strip().split(",")
        return Board(no,title,name,content,write,active)