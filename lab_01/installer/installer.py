import os
import shutil
import subprocess
from PyQt5 import QtWidgets
from lab_01.installer.installer_view import Ui_Installer
from lab_01.config import KEY_FILE, get_serial_number


class Installer(QtWidgets.QDialog, Ui_Installer):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.__key: str = ""
        self.nextBtn.clicked.connect(self.__install_program)
        self.cancelBtn.clicked.connect(self.close)

    def __install_program(self):
        self.__save_serial_number()
        with open(KEY_FILE, 'w') as f:
            f.write(self.__key)

        install_command = f'pyinstaller --onefile --noconsole --clean --add-data "{KEY_FILE};." ./program/program.py'
        subprocess.call(install_command)
        shutil.copyfile('dist/program.exe', 'program.exe')

        shutil.rmtree('build')
        shutil.rmtree('dist')
        os.remove(KEY_FILE)


    def __save_serial_number(self):
        self.__key = get_serial_number()
