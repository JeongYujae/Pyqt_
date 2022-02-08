import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()
#마찬가지로 숫자들 -> 좌표 
    def setupUI(self):
        self.setGeometry(800, 400, 300, 150)

        textLabel = QLabel("Message: ", self) # ㅇ항상 'Message'를 출력하는 객체는 textlabel로 항상 바인딩한다
        textLabel.move(20, 20)

        self.label = QLabel("", self) #버튼이 클릭되었습니다와 같은 메시지 출력은 self.label로 바인딩/ 'QLabel에' 텍스트를 띄울거야! 
        self.label.move(80, 20) # move->객체의 출력 위치 지정
        self.label.resize(150, 30) #크기 조정 가능

        btn1 = QPushButton("Click", self) #버튼 1 click 버튼
        btn1.move(20, 60)
        btn1.clicked.connect(self.btn1_clicked)


        btn2 = QPushButton("Clear", self) #버튼 2 clear 버튼
        btn2.move(140, 60)
        btn2.clicked.connect(self.btn2_clicked)

    def btn1_clicked(self):
        self.label.setText("버튼이 클릭되었습니다.") #텍스트 설정/ 임의로 당연히 변경 가능

    def btn2_clicked(self):
        self.label.clear() #텍스트 지워지기

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()