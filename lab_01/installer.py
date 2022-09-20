import os
import shutil
import subprocess
import sys
from PyQt5 import QtWidgets
from program.config import KEY_FILE, get_serial_number
from installer_view import Ui_Installer


class Installer(QtWidgets.QDialog, Ui_Installer):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.nextBtn.clicked.connect(self.__install_program)
        self.cancelBtn.clicked.connect(self.close)

    def __install_program(self):
        self.__save_serial_number()

        install_command = f'pyinstaller --onefile --clean --add-data "{KEY_FILE};." program/program.py'
        subprocess.call(install_command)

        shutil.copyfile(r'dist\program.exe', r'..\program.exe')
        self.__delete_tmp_files()

    @staticmethod
    def __save_serial_number():
        with open(KEY_FILE, 'w') as f:
            f.write(get_serial_number())

    @staticmethod
    def __delete_tmp_files():
        shutil.rmtree('build')
        shutil.rmtree('dist')
        os.remove('program.spec')
        os.remove(KEY_FILE)


def main():
    app = QtWidgets.QApplication(sys.argv)
    installer = Installer()
    installer.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
