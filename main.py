from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget,
                    QHBoxLayout, QVBoxLayout,
                    QLabel, QPushButton, QLineEdit)
from config import *
from test import TestWindow


class MainWindow(QWidget):
    def __init__(self, title=TXT_TITLE):
        super().__init__()
        self.title = title
        self.set_ui()
        self.config_win()
        # self.connections()
        self.show()

    def set_ui(self):
        # widgets
        self.hello_txt =  QLabel(TXT_HELLO)
        self.instructions_txt =  QLabel(TXT_INSTRUCTIONS)
        self.btn_next = QPushButton(TXT_BTN)
        #layout
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.hello_txt, alignment=Qt.AlignCenter)
        self.main_layout.addWidget(self.instructions_txt, alignment=Qt.AlignLeft)
        self.main_layout.addWidget(self.btn_next, alignment=Qt.AlignCenter)

        self.setLayout(self.main_layout)

    def config_win(self):
        self.resize(WIN_WIDTH, WIN_HEIGHT)
        self.move(WIN_X, WIN_Y)
        self.setWindowTitle(self.title)

    # def connections(self):
    #     self.btn_next.clicked.connect(self.next_window)
    
    # def next_window(self):
    #     new_window = TestWindow()
    #     self.hide()

app = QApplication([])
main_window = MainWindow()


app.exec_()
