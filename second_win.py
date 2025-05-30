from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from instr import *
from final_win import *

class Experiment():
    def __init__ (self, age, res_quest1, res_quest2, res_quest3):
        self.age = age
        self.rq1 = res_quest1
        self.rq2 = res_quest2
        self.rq3 = res_quest3
class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.connects()
        self.set_appear()
        self.show()

    #def results(self):
        #self.index = (4*(int(self.exp.rq1)+int(self.exp.rq2)+int(self.exp.rq3))-200)/10
    def next_click(self):
        self.hide()
        self.exp = Experiment(self.agefield.text(),self.res_quest1.text(),self.res_quest2.text(),self.res_quest3.text())
        self.tw = FinalWin(self.exp)

    def timer_test(self):
        global time
        time = QTime(0,0,15)
        #time = time.addSecs(-1)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)
    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString('hh:mm:ss'))
        self.text_timer.setFont(QFont('Times', 36, QFont.Bold))
        self.text_timer.setStyleSheet('color: rgb(0,255,0)')

        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()
    
    def timer_sits(self):
        global time
        time = QTime(0,0,30)
        #time = time.addSecs(-1)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        #одно приседание в 1.5 секунды
        self.timer.start(1500)

    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString('hh:mm:ss')[6:8])
        self.text_timer.setFont(QFont('Times', 36, QFont.Bold))
        self.text_timer.setStyleSheet('color: rgb(255,0,0)')

        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()

    def timer_final(self):
        global time
        time = QTime(0,1,0)
        #time = time.addSecs(-1)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)
    def timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString('hh:mm:ss'))
        if int(time.toString('hh:mm:ss')[6:8]) >= 45:
            self.text_timer.setStyleSheet('color: rgb(0,255,0)')
        elif int(time.toString('hh:mm:ss')[6:8]) <= 15:
            self.text_timer.setStyleSheet('color: rgb(255,255,0)')
        else:
            self.text_timer.setStyleSheet('color: rgb(0,0,0)')

    def connects(self):
        self.final.clicked.connect(self.next_click)
        self.start_quest1.clicked.connect(self.timer_test)
        self.start_quest1.clicked.connect(self.timer_test)
        self.start_quest2.clicked.connect(self.timer_sits)
        self.start_quest3.clicked.connect(self.timer_final)

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width,win_height)
        self.move(win_x,win_y)
    def initUI(self):
        self.text_timer = QLabel(txt_timer)
        self.vline = QVBoxLayout()
        self.name = QLabel("Введите ФИО")
        self.namefield = QLineEdit("")
        self.age = QLabel("Полных лет:")
        self.agefield = QLineEdit("")
        self.quest1 = QLabel("Ложитесь на спину и замерьте пульс за 15 секунд. Нажмите кнопку 'Начать новый тест', чтобы запустить таймер. Результат запишите в окошко")
        self.start_quest1 = QPushButton("Начать новый тест",self)
        self.res_quest1 = QLineEdit("результат")
        self.quest2 = QLabel("Выполните 30 приседаний за 45 секунд. Для этого нажмите кнопку 'Начать делать приседания'")
        self.start_quest2 = QPushButton("Начать делать приседания",self)
        self.res_quest2 = QLineEdit("результат")
        self.quest3 = QLabel("Ложитесь на спину и замерьте пульс за первые 15 секунд минуты, затем за последние 15 секунд. Нажмите на кнопку 'Начать финальный тест'")
        self.start_quest3 = QPushButton("Начать финальный тест",self)
        self.res_quest3 = QLineEdit("результат")
        self.final = QPushButton("Отправить результаты",self)
        self.vline.addWidget(self.name,alignment = Qt.AlignLeft)
        self.vline.addWidget(self.namefield,alignment = Qt.AlignLeft)
        self.vline.addWidget(self.age,alignment = Qt.AlignLeft)
        self.vline.addWidget(self.agefield,alignment = Qt.AlignLeft)
        self.vline.addWidget(self.quest1,alignment = Qt.AlignLeft)
        self.vline.addWidget(self.start_quest1,alignment = Qt.AlignLeft)
        self.vline.addWidget(self.res_quest1,alignment = Qt.AlignLeft)
        self.vline.addWidget(self.quest2,alignment = Qt.AlignLeft)
        self.vline.addWidget(self.start_quest2,alignment = Qt.AlignLeft)
        self.vline.addWidget(self.res_quest2,alignment = Qt.AlignLeft)
        self.vline.addWidget(self.quest3,alignment = Qt.AlignLeft)
        self.vline.addWidget(self.start_quest3,alignment = Qt.AlignLeft)
        self.vline.addWidget(self.res_quest3,alignment = Qt.AlignLeft)
        self.vline.addWidget(self.final,alignment = Qt.AlignLeft)
        self.vline.addWidget(self.text_timer,alignment = Qt.AlignRight)
        self.setLayout (self.vline)