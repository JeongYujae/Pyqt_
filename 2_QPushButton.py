#내가 짠 코드가 아닌 것들은 모두 pyqt에서 자동생성되는 것-> 수정하거나 건들 필요 X
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
app = None

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        btn1 = QPushButton("닫기", self)
        btn1.move(20, 20) #()안은 좌표 -> qt designer 사용하면 좌표 지정은 필요 X
        btn1.clicked.connect(app.quit) #이건 QT가 만든것 닫는 app을 지정하여 '닫기' 누르면 꺼지게

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()