import colonyCounter
import imageCapture
import outputData

#for Degubbing
from gpiozero import LED, Button
import time
button1 = Button(18)
button2 = Button(17)
#for Debugging

#setup and global variables
#GPIO.setmode(GPIO.BCM)  #set GPIO to BCM numbering
#GPIO.setup(2, GPIO.IN, pull_up_down = GPIO.PUD_UP)
counter = 0             #initalize petrie counter
colonyCount = 0
startInterrupt = False  #initalize startInterrupt
resetInterrupt = False  #initalize resetInterrupt

dataMatrix = ["Petri Num","Colony Count","Pass/Fail"]

threshold = 5
passFail = ""

def startInterruptReceived(petriNumber):
    imageCapture.imageCapture(petriNumber)
    colonyCount = colonyCounter.analyzeImage(petriNumber)
    #print(colonyCount)
    if(colonyCount < threshold):
        passFail = "Pass"
    else:
        passFail = "Fail"
    dataMatrix[petriNumber] = [str(petriNumber), str(colonyCount), passFail]
    outputData.toCSV(dataMatrix)
    return

#main{
#loop forever
while (counter < 10):
    #Debugging
    if(button1.is_pressed):
        startInterrupt = True
        time.sleep(.300)
    if(button2.is_pressed):
        resetInterrupt = True
        time.sleep(.300)
    #Debugging

    if(resetInterrupt == False):
        if(startInterrupt == True):      
            startInterruptReceived(counter)
            #print("startInterrupt Received")
            counter += 1
            startInterrupt = False
    else:
        counter = 0 #reset counter
        #print("resetInterrupt Received")
        startInterrupt = False
        resetInterrupt = False
        continue

outputData.outputData(outputData)
    