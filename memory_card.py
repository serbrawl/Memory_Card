from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton, QGroupBox, QButtonGroup
from random import shuffle, randint

class Question():
    def __init__(self, question_, right_answer, wrong1, wrong2, wrong3):
        self.question_ = question_
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

q_list = list()
#q = Question('', '', '', '', '')              <- заготовка
q1 = Question('Какой национальности не существует?', 'Смурфы', 'Энцы', 'Чулымцы', 'Алеуты')
q2 = Question('Какая игра про выживание в кубическом мире?', 'Майнкрафт', 'Rust', 'World of Warcraft', 'Dota 2')
q3 = Question('Это оригинальный вопрос?', 'да', 'нет', 'наверное', 'не знаю')
q4 = Question('Сколько редкостей в бравл старс?', '6', '8', '7', '5')
q_list.append(q1)
q_list.append(q2)
q_list.append(q3)
q_list.append(q4)


def show_result():
    RadioGroupBox.hide()
    LabelGroupBox.show()
    button.setText('Следующий вопрос')

def show_question():
    LabelGroupBox.hide()
    RadioGroupBox.show()
    button.setText('Ответить')
    RadioButton.setExclusive(False)
    right_answer.setChecked(False)
    wrong1.setChecked(False)
    wrong2.setChecked(False)
    wrong3.setChecked(False)
    RadioButton.setExclusive(True)

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer) 
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question_) 
    lb_Correct.setText(q.right_answer) 
    show_question() 

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        main_win.score += 1
        print('Статистика\n-Правильных ответов:', main_win.score, '\nРейтинг:', main_win.score/main_win.total)
    elif answers[1].isChecked or answers[2].isChecked or answers[3].isChecked:
        show_correct('Неправильно!')
        print('Статистика\nРейтинг:', main_win.score/main_win.total)

def next_question():
    main_win.total += 1
    print('Статистика\n-Всего вопросов:', main_win.total, '\n-Правильных ответов:', main_win.score, '\nРейтинг:', main_win.score/main_win.total)
    main_win.cur_question = randint(0, len(q_list) -1)
    q = q_list[main_win.cur_question]
    ask(q)

def click_OK():
    if button.text() == 'Ответить':
        check_answer()
    else:
        next_question()


app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory Card')
main_win.resize(300, 200)

main_win.score = 0
main_win.total = 0

question = QLabel('Какой национальности не существует?')
RadioGroupBox = QGroupBox('Варианты ответов')
right_answer = QRadioButton('Смурфы')
wrong1 = QRadioButton('Энцы')
wrong2 = QRadioButton('Чулымцы')
wrong3 = QRadioButton('Алеуты')
button = QPushButton('Ответить')
answers = [right_answer, wrong1, wrong2, wrong3]
RadioButton = QButtonGroup()
RadioButton.addButton(right_answer)
RadioButton.addButton(wrong1)
RadioButton.addButton(wrong2)
RadioButton.addButton(wrong3)

layout_ans_h1 = QHBoxLayout()
layout_ans_v1 = QVBoxLayout()
layout_ans_v2 = QVBoxLayout()

layout_ans_v1.addWidget(right_answer)
layout_ans_v1.addWidget(wrong1)
layout_ans_v2.addWidget(wrong2)
layout_ans_v2.addWidget(wrong3)
layout_ans_h1.addLayout(layout_ans_v1)
layout_ans_h1.addLayout(layout_ans_v2)

RadioGroupBox.setLayout(layout_ans_h1)

h1_line = QHBoxLayout()
h2_line = QHBoxLayout()
h3_line = QHBoxLayout()
h1_line.addWidget(question, alignment =(Qt.AlignHCenter | Qt.AlignVCenter))
h2_line.addWidget(RadioGroupBox)
h3_line.addStretch(100)
h3_line.addWidget(button, stretch=200)
h3_line.addStretch(100)

v_line = QVBoxLayout()
v_line.addLayout(h1_line)
v_line.addLayout(h2_line)
v_line.addLayout(h3_line)
main_win.setLayout(v_line)
v_line.setSpacing(28)
RadioGroupBox.hide()

LabelGroupBox = QGroupBox()
lb_Result = QLabel('Правильно/Неправильно')
lb_Correct = QLabel('Правильный ответ')

layout_tot_h1 = QHBoxLayout()
layout_tot_v1 = QVBoxLayout()

layout_tot_v1.setSpacing(20)
layout_tot_h1.setSpacing(2000)
layout_tot_v1.addWidget(lb_Result)
layout_tot_v1.addWidget(lb_Correct, alignment= Qt.AlignHCenter)
layout_tot_h1.addLayout(layout_tot_v1)

LabelGroupBox.setLayout(layout_tot_h1)
h2_line.addWidget(LabelGroupBox)

button.clicked.connect(click_OK)

RadioGroupBox.show()
LabelGroupBox.hide()
next_question()
main_win.show()
app.exec_()
