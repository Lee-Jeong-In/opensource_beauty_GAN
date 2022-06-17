import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import NOMAKEUP

#form_class = uic.loadUiType("NOMAKEUP.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()


'''
    def initUI(self):
        # 버튼 클릭할때 연결되는 함수
        self.pushButton.clicked.connect(self.button_1)
        self.pushButton_2.clicked.connect(self.button_2)
        self.pushButton_3.clicked.connect(self.button_3)
        self.pushButton_4.clicked.connect(self.button_4)
        self.pushButton_5.clicked.connect(self.button_5)
        self.pushButton_6.clicked.connect(self.button_6)


    def button_1(self):
        pass

    def button_2(self):
        pass

    def button_3(self):
        pass

    def button_4(self):
        pass

    def button_5(self):
        pass

    def button_6(self):
        pass

        # 버튼 이미지 처리
        self.pushButton.setStyleSheet('border-image:url(imgs/01.jpg);border:0px;')
        self.pushButton_2.setStyleSheet('border-image:url(imgs/02.jpg);border:0px;')
        self.pushButton_3.setStyleSheet('border-image:url(imgs/03.jpg);border:0px;')
        self.pushButton_4.setStyleSheet('border-image:url(imgs/04.jpg);border:0px;')
        self.pushButton_5.setStyleSheet('border-image:url(imgs/05.jpg);border:0px;')
        self.pushButton_6.setStyleSheet('border-image:url(imgs/06.jpg);border:0px;')
'''

'''
class QtGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Appia Qt GUI")
        self.resize(700, 700)

        # 라벨 생성

        label1 = QLabel(self)
        label1.move(100, 100)

        # 이미지 관련 클래스 생성 및 이미지 불러오기

        #pixmap = QPixmap('imgs/01.jpg')
        # 이미지 관련 클래스와 라벨 연결
        #label1.setPixmap(pixmap)

        self.show()
'''

'''


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = QtGUI()
    app.exec_()
'''

    
