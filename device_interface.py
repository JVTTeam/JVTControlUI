import serial

class SerialInterface:
    def __init__(self, port, baudrate=9600):
        self.port = port
        self.serial = serial.Serial(port, baudrate)
        self.serial.timeout = 0.5

    def readline(self):
        return self.serial.readline()

    def write(self, data):
        if isinstance(data, str):
            data = data.encode("ascii")
        self.serial.write(data)