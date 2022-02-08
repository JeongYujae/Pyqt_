import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("1.ui")[0] #pyqt 파일을 불러오는거 -> 파이썬으로 하기 위해서

class MyWindow(QMainWindow, form_class): #-> 다중상속(이미 존재하는 코드, form_class도 위에 있음)/ 여기 class 코드들만 수정해야됨
    #MyWindows는 QMainWindow와 form_class로부터 다중상속을 받은 것을 확인할 수 있다.
    def __init__(self): #생성자 만들기
        super().__init__()
        self.setupUi(self) #만든건 아님 -> pyqt 에서 만든거라  바꾸면 안됨
        self.pushButton.clicked.connect(self.btn_clicked) #method/ 버튼을 눌렀을 때 -> self.btn_clicked에 연결해줌

    def btn_clicked(self):
        QMessageBox.about(self, "message", "clicked") #얘도 pyqt가 만든거임

if __name__ == "__main__": #파이썬을 실행시키면 제일 먼저 도는 부분 main이라서
    app = QApplication(sys.argv)
    #이벤트 루프를 생성하는 부분
    myWindow = MyWindow()
    myWindow.show()
    app.exec_() #이 프로그램 실행시키면 얘는 대기중 (24시간)-> 입력 받으면 돌림(이벤트를 받으면)