#8 electrodes senario#

import serial
import time
import datetime
import struct

port = "COM8" #Change N ("COMN") to the correct number AFTER conecting the device
ser = serial.Serial(port,460800) #Defines a connection
print("The port", ser.port, "made a connection") #Prints which port works
time.sleep(2) #delay
timestr = datetime.datetime.now().strftime("%d/%m/%y - %H:%M:%S") #set a time
print("Creating a new file Text Raw Data at" ,timestr)
time.sleep(2) #delay
filenamestr = "Text Raw Data - " + str(datetime.datetime.now().date()) + ' ' + str(datetime.datetime.now().time()).replace(':', '.') + '.txt'#Name the file
a=open(filenamestr,"w+") #Creating the file
a.write(" ") #writes space for better organization
while True:
    data = ser.readline(1) #(!for list() or int.from_bytes only!) - Change
    #the value inside the readline() to print and write in a file. Relevant values - 1-128.
    RawData = struct.unpack("B", data)[0] #Makign a struct from the data as unsigned char (integer) format
    print(RawData) #prints data in console - not needed for the whole operation
    if RawData == 128: #if 128 is found, replace with a new term
        RawData = "\n"
    a.write(str(RawData)+" ") #writes the data
    a.flush() # flushes the internal buffer
