import sys
import random

from PyQt6.QtCore import QPoint
from PyQt6.QtGui import QPainter, QColor
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow

from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        MainWindow.setMinimumSize(QtCore.QSize(600, 600))
        MainWindow.setMaximumSize(QtCore.QSize(600, 600))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn.setGeometry(QtCore.QRect(10, 10, 131, 111))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.btn.setFont(font)
        self.btn.setStyleSheet("background-color: rgb(255, 218, 66);")
        self.btn.setObjectName("btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn.setText(_translate("MainWindow", "Кнопка"))


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.circles = []

        self.btn.setText('Клик')
        self.btn.clicked.connect(self.run)

    def run(self):
        self.circles.append([
            (
                random.randint(100, 500),
                random.randint(100, 500),
                random.randint(1, 100)
            ),
            (
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255)
            )
        ])
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        for el, color in self.circles:
            painter.setBrush(QColor(*color))
            painter.drawEllipse(QPoint(el[0], el[1]), el[2], el[2])


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
