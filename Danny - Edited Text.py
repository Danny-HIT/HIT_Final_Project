#Daniel#
#8 electrodes senario#

import time
import datetime
import csv
from io import StringIO
import io

print("Edit the text file for a shorter one") #Print
time.sleep(2) #delay
timestr = datetime.datetime.now().strftime("%d/%m/%y - %H:%M:%S") #set a time
print("Rewriting the text at" ,timestr)
filenamestr = "Ready Raw Data - " + str(datetime.datetime.now().date()) + ' ' + str(datetime.datetime.now().time()).replace(':', '.') + '.txt'#Name the file
time.sleep(2) #delay
with open('Text Raw Data - 2021-09-30 13.50.57.6663776.txt', "r") as f:
    file_contents = f.read()
    file_contents = file_contents.replace("208 7","")
    file_contents = file_contents.replace("     ","  ")
    file_contents = file_contents.replace("    ","  ")
    file_contents = file_contents.replace("   ","  ")
a=open('wdw.txt',"w+") #Creating the file
a.write(file_contents)

