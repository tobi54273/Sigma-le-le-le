from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from instr import *
from second_win import *
class FinalWin(QWidget):
    def __init__(self, exp):
        super().__init__()
        self.exp = exp
        self.initUI()
        #self.connects()
        self.set_appear()
        self.show()

    def results(self):

        if  int(self.exp.age) < 7:
            self.index = 0
            return "нет данных для такого возраста"

        self.index = (4*(int(self.exp.rq1)+int(self.exp.rq2)+int(self.exp.rq3))-200)/10

        if int(self.exp.age) >= 15:
            if int(self.index) >= 15:
                return txt_res1
        elif int(self.index) < 15 and int(self.index) == 11:
            return txt_res2

        elif int(self.index) < 11 and int(self.index) == 6:
            return txt_res3

        elif int(self.index) < 6 and int(self.index) == 1:
            return txt_res4

        elif self.index<1:
            return txt_res5
    def next_click(self):
        self.tw = TestWin()
        self.hide()
    #def connects(self):
    #    self.btn_next.clicked.connect(self.next_click)
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width,win_height)
        self.move(win_x,win_y)
    def initUI(self):

        self.work_text = QLabel(txt_workheart + str(self.results()))
        self.index_text = QLabel(txt_index + str(self.index))
        self.vline = QVBoxLayout()
        self.l1 = QLabel("Индекс Руфье:")
        self.vline.addWidget(self.l1,alignment = Qt.AlignCenter)

        self.vline.addWidget(self.work_text,alignment = Qt.AlignCenter)
        self.l2 = QLabel("Работоспособность")
        self.vline.addWidget(self.l2,alignment = Qt.AlignCenter)

        self.vline.addWidget(self.index_text,alignment = Qt.AlignCenter)
        self.setLayout (self.vline)

        #self.work_text = QLabel(txt_workheart + str(self.results()))
        #self.index_text = QLabel(txt_index + str(self.index))
        #self.vline.addWidget(self.work_text,alignment = Qt.AlignCenter)

        print("ААААААААААААА")
        print(self.results())