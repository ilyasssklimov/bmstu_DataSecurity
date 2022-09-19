from PyQt5 import QtWidgets
import sys
sys.path.append('.')
sys.path.append('..')
from installer.installer import Installer


def main():
    app = QtWidgets.QApplication(sys.argv)
    installer = Installer()
    installer.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
