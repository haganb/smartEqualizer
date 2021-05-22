# Importing Libraries
import serial
#import time
arduino = serial.Serial(port='COM1', baudrate=115200, timeout=.1)


def write_read(x):
    x = str(x)
    arduino.write(bytes(x, 'utf-8'))
    #time.sleep(0.05)
    data = arduino.readline()
    return data


#while True:
    # num = input("Enter a number: ")  # Taking input from user
    # value = write_read(num)
    #write_read("Proof of concept for serial comms")
    #write_read("\nSmart Equalizer\n") 
    # print(value)  # printing the value
    #for i in range(0, 8):
        #write_read(i)
       # time.sleep(5)