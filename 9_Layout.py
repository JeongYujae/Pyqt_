import sys
from PyQt5.QtWidgets import *

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800, 200, 300, 300)

        self.textEdit = QTextEdit() #텍스트를 입력,수정할 수 있는 창
        self.pushButton= QPushButton('저장')

        layout = QVBoxLayout() #빈 박스 레이아웃 정하기
        layout.addWidget(self.textEdit)
        layout.addWidget(self.pushButton)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()