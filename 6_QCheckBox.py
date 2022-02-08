#Radiobox와 다른 점-> CheckBox는 복수선택이 가능해
import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800, 200, 300, 300)

        self.checkBox1 = QCheckBox("5일 이동평균선", self)
        self.checkBox1.move(10, 20)
        self.checkBox1.resize(150, 30)
        self.checkBox1.stateChanged.connect(self.checkBoxState) #statechange, 즉 사용자로부터 input이 오면 staechanged.connect로 보내줘

        self.checkBox2 = QCheckBox("20일 이동평균선", self)
        self.checkBox2.move(10, 50)
        self.checkBox2.resize(150, 30)
        self.checkBox2.stateChanged.connect(self.checkBoxState)

        self.checkBox3 = QCheckBox("60일 이동평균선", self)
        self.checkBox3.move(10, 80)
        self.checkBox3.resize(150, 30)
        self.checkBox3.stateChanged.connect(self.checkBoxState)

        self.statusBar = QStatusBar(self)
        self.setStatusBar(self.statusBar)

    def checkBoxState(self):
        msg = ""
        if self.checkBox1.isChecked() == True: #체크가 True면 출력/ #if문을 쓴 이유 -> 복수 체크가 가능해서
            msg += "5일 "
        if self.checkBox2.isChecked() == True:
            msg += "20일 "
        if self.checkBox3.isChecked() == True:
            msg += "60일 "
        self.statusBar.showMessage(msg)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()