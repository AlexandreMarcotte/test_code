import serial
import threading
from time import sleep


class SerialReader(threading.Thread):
    def __init__(self):
        super().__init__()
        self.ser = serial.Serial('/dev/ttyACM1', 9600, timeout=0.5)

    def run(self):
        self.read()

    def read(self):
        while True:
            signal = self.ser.readline()
            print(int(signal))
            sleep(0.1)


if __name__ == '__main__':
    ser_reader = SerialReader()
    ser_reader.start()

