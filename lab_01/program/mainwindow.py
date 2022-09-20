from design import Ui_MainWindow
from PyQt5 import QtWidgets


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Программа')

        self.pushButton.clicked.connect(self.show_success)

    def show_success(self):
        QtWidgets.QMessageBox.about(self, 'Успех', 'Вы нажали на кнопку!')
