#사용자로부터 간단한 텍스트를 입력받을 때 사용
import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800, 400, 300, 150)

        # Label
        label = QLabel("종목코드", self) #이름
        label.move(20, 20)

        # LineEdit
        self.lineEdit = QLineEdit("", self) #input 받게 만드는거
        self.lineEdit.move(80, 20)
        self.lineEdit.textChanged.connect(self.lineEditChanged) #textchanged()=> lineeidt객체에서 텍스트가 변경될 때/ returnPressed() => 엔터 누를때

        # StatusBar
        self.statusBar = QStatusBar(self) #위젯생성
        self.setStatusBar(self.statusBar)

    def lineEditChanged(self): #밑에 숫자 입력하면 같이 나오는 위젯
        self.statusBar.showMessage(self.lineEdit.text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()