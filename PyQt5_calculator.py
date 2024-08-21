from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


def one():
    concate("1")
def two():
    concate("2")
def three():
    concate("3")

def four():
    concate("4")
def five():
    concate("5")
def six():
    concate("6")

def seven():
    concate("7")

def eight():
    concate("8")

def nine():
    concate("9")

def zero():
    concate("0")

def add():
    concate("+")
def sub():
    concate("-")
def mul():
    concate("*")
def div():
    concate("/")
def point():
    concate(".")
def eql():
    concate("=")

global Num
Num=""

def concate(a):
    global Num
    if a=="=":
        ans=(eval(Num))
      
        Num=""
    else:
        Num+=a

class window():
    def Win(self):
        app = QApplication(sys.argv)
        self=QMainWindow()
        self.setWindowTitle("Calculator")
        self.setGeometry(1200,250,500,500)

        window.gui(self)
        self.show()
        sys.exit(app.exec_())

    def gui(self):
        central_widget=QWidget()
        self.setCentralWidget(central_widget)

        btn1=QPushButton(self)
        btn1.setText("1")
        btn1.clicked.connect(one)
        

        btn2=QPushButton(self)
        btn2.setText("2")
        btn2.clicked.connect(two)

        btn3=QPushButton(self)
        btn3.setText("3")
        btn3.clicked.connect(three)

        btn11=QPushButton(self)
        btn11.setText("+")
        btn11.clicked.connect(add)


        btn4=QPushButton(self)
        btn4.setText("4")
        btn4.clicked.connect(four)

        btn5=QPushButton(self)
        btn5.setText("5")
        btn5.clicked.connect(five)

        btn6=QPushButton(self)
        btn6.setText("6")
        btn6.clicked.connect(six)

        btn22=QPushButton(self)
        btn22.setText("-")
        btn22.clicked.connect(sub)

        btn7=QPushButton(self)
        btn7.setText("7")
        btn7.clicked.connect(seven)

        btn8=QPushButton(self)
        btn8.setText("8")
        btn8.clicked.connect(eight)

        btn9=QPushButton(self)
        btn9.setText("9")
        btn9.clicked.connect(nine)

        btn33=QPushButton(self)
        btn33.setText("*")
        btn33.clicked.connect(mul)

        btn0=QPushButton(self)
        btn0.setText("0")
        btn0.clicked.connect(seven)

        btn_=QPushButton(self)
        btn_.setText(".")
        btn_.clicked.connect(point)

        btn__=QPushButton(self)
        btn__.setText("=")
        btn__.clicked.connect(eql)

        btn44=QPushButton(self)
        btn44.setText("/")
        btn44.clicked.connect(div)


        hbox=QGridLayout()
        hbox.addWidget(btn1,0,0)
        hbox.addWidget(btn2,0,1)
        hbox.addWidget(btn3,0,2)
        hbox.addWidget(btn11,0,3)


        hbox.addWidget(btn4,1,0)
        hbox.addWidget(btn5,1,1)
        hbox.addWidget(btn6,1,2)
        hbox.addWidget(btn22,1,3)


        hbox.addWidget(btn7,2,0)
        hbox.addWidget(btn8,2,1)
        hbox.addWidget(btn9,2,2)
        hbox.addWidget(btn33,2,3)

        hbox.addWidget(btn0,3,0)
        hbox.addWidget(btn_,3,1)
        hbox.addWidget(btn__,3,2)
        hbox.addWidget(btn44,3,3)


        
        
        central_widget.setLayout(hbox)

win=window()
win.Win()