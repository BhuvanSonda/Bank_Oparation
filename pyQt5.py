from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys

def on_click():
    print("Button clicked")

#create window
app = QApplication(sys.argv)

window=QMainWindow()
window.setGeometry(1200,250,500,500)
window.setWindowTitle("PyQt5")

# Lable=QtWidgets.QLabel(window)
# Lable.setText("This is Lable")
# Lable.move(50,50)

# Button=QtWidgets.QPushButton(window)
# Button.setText('click')
# Button.clicked.connect(on_click)

window.show()
sys.exit(app.exec_())