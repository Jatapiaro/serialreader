import serial

ser = serial.Serial(port='/dev/tty.usbmodem1431',
                    baudrate=9600)

try:
    ser.isOpen()
    print ("Reading open")
except:
    print ("Error")
    exit()


flag = 0
if ser.isOpen():
    while (1):
        if flag == 0:
            ser.readline()
            flag = 1
        else:
            value = str(ser.readline()).replace("\n", "")
            print (float(value))
else:
    print ("Error")