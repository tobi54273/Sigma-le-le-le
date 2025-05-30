from second_win import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from instr import *
from final_win import *
#app = QApplication([])
#win = QWidget()

#def heh():
#    pass


#win.setWindowTitle('Тест Руфье')
#win.move(600, 200)
#win.resize(900, 700)

#v_line1 = QVBoxLayout()


#win.setLayout(v_line1)
#class MainWin(QWidget):
#    def __init__(self):
#        text1 = QLabel('Добро пожаловать в прорамму по определению состояния здоровья!\n')
#        text2 = QLabel('Данное приложение позволит вам с помощью теста Руфье провести первичную диагностику вашего здоровья\n'+
#        'Проба Руфье представляет собой нагрузочный комплекс, предназначенный для оценки работоспособности сердца при физической нагрузке.\n'+
#        'У испытуемого, находящегося в положении лежа на спине в течение 6 мин, определяют частоту пульса за 10 секунд;\n'+
#       'затем в течение 40 секунд испытуемый выполняет 30 приседаний.\n'+
#       'После окончания нагрузки испытуемый ложится, и у него вновь подсчитывается число пульсаций за первые 15 секунд\n'+
#       'а потом за последние 15 секунд первой минуты периода восстановления.\n'+
#       'Важно! Если в процессе проведения испытания вы почувствуете себя плохо (появится головокружение, шум в\n'+
#       'ушах, сильная одышка и др.), то тест необходимо прервать и обратиться к врачу.')
#       super().__init__()
#but = QPushButton('Начать')
#v_line1.addWidget(text1, alignment = Qt.AlignCenter)
#v_line1.addWidget(text2, alignment = Qt.AlignCenter)
#v_line1.addWidget(but, alignment = Qt.AlignCenter)
#but.clicked.connect(heh)

#win.show()
#app.exec_()

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.set_appear()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)

    def next_click(self):
        self.tw = TestWin()
        self.hide()

    def initUI(self):
        self.btn_next = QPushButton(txt_next, self)
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)
        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.hello_text, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.instruction, alignment = Qt.AlignLeft) 
        self.layout_line.addWidget(self.btn_next, alignment = Qt.AlignCenter)
        self.setLayout (self.layout_line)

app = QApplication([])
mw = MainWin()
win = QWidget()
app.exec_()