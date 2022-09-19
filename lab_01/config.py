import os
import sys

KEY_FILE = 'serial_number.key'


def get_serial_number():
    save_command = 'wmic bios get serialnumber'
    return os.popen(save_command).read().split()[1]


def get_resource_path(filename):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath('.')

    return os.path.join(base_path, filename)
