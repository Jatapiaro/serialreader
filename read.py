import serial
import requests

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
            v = float(value)
            url = "https://tinacos.herokuapp.com/containers/1/measures.json"

            payload = "{\n\t\"measure\": {\n\t\t\"height\": "+value+"\n\t}\n}"
            headers = {
                'content-type': "application/json",
                'cache-control': "no-cache",
                'postman-token': "57acf325-4021-c728-4e75-693c082dc459"
            }

            response = requests.request("POST", url, data=payload, headers=headers)
            print(response.text)
            print (v)
else:
    print ("Error")