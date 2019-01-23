import logging
# OpenBCI hardware module
from openbci.openbci_v3_interface import OpenBCIBoard
from time import sleep
from functools import partial


def print_openbci_data(sample, other=10):
    print('other', other)
    print(sample.aux_data)


def main():
    port = '/dev/ttyUSB0'  # if using Linux
    # (if encounter error: [Errno 13] could not open port /dev/ttyUSB0: Permission denied => see: https://askubuntu.com/questions/58119/changing-permissions-on-serial-port   then restart your computer
    # port = 'COM3'  # if using Windows
    # port = '/dev/tty.OpenBCI-DN008VTF'  # If using MAC?
    logging.basicConfig(filename="test.log", format='%(asctime)s - %(levelname)s : %(message)s', level=logging.DEBUG)
    logging.info('---------LOG START-------------')
    board = OpenBCIBoard(port=port, scaled_output=False, log=True)
    print("Board Instantiated")
    sleep(5)

    board.start_streaming(print_openbci_data)


if __name__ == '__main__':
    main()

