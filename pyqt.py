from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def window():
    app=QApplication(sys.argv)
    win=QMainWindow()
    win.setGeometry(220,220,300,300)
    win.setWindowTitle("First PyQt5 app")
    label=QtWidgets.QLabel(win)
    label.setText("Hello World")
    label.move(115,115)
    win.show()
    sys.exit(app.exec_())
window()