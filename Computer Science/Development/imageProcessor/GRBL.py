import time
import serial

class SerialObj:
    def __init__(self, portName):
        self.serialObj = serial.Serial() #creates a serial object from serial (pySerial) library
        self.serialObj.port = portName   #default to "COM3" in windows (I think)
        self.serialObj.baudrate = 115200
        self.serialObj.parity = 'N'      #no parity bit
        self.serialObj.bytesize = 8
        self.serialObj.stopbits = 1
        self.serialObj.timeout = 5       #wait for 5 sec before timeout

        self.serialObj.open()   #begin serial communication
        time.sleep(2)           #sleep 2 sec to allow for arduino/serial port to initialize

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback): 
        self.serialObj.close()  #end serial communication when object is out of scope

    def write(self, strInput):
        self.serialObj.write(strInput.encode('utf-8') + b"\r\n")    #string is encoded into byte-form and appended with a return and newline\
        print(strInput)
        time.sleep(.5)

    def read(self):
        while self.serialObj.inWaiting() > 0:      
            print(self.serialObj.readline().decode('ascii')) 