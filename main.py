import sys
import random

from PyQt6.QtCore import QPoint
from PyQt6.QtGui import QPainter, QColor
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.circles = []

        self.btn.setText('Клик')
        self.btn.clicked.connect(self.run)

    def run(self):
        self.circles.append(
            (
                random.randint(100, 500),
                random.randint(100, 500),
                random.randint(1, 100)
            )
        )
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QColor(255, 255, 0))
        for el in self.circles:
            painter.drawEllipse(QPoint(el[0], el[1]), el[2], el[2])


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
