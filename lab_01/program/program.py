from PyQt5 import QtWidgets
import sys
sys.path.append('..')
from mainwindow import MainWindow
from lab_01.config import KEY_FILE, get_serial_number, get_resource_path


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()

    with open(get_resource_path(KEY_FILE)) as f:
        if f.read().strip() != get_serial_number():
            QtWidgets.QMessageBox.about(window, 'Ошибка',
                                        'Упс, Вы не можете пользоваться этим приложением, установите программу заново')
            return

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
