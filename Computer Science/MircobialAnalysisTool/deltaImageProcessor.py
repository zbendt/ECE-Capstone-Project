import colonyCounter
import time
import csv
#import picamera
import os

#camera = picamera.PiCamera()           #initalize camera

SAMPLE_CNT = 0                          #initalize number of samples
CUR_SAMPLE = 0                          #sample number of current sample
COL_COUNT = 0                           #number of colonies found
DATA_ARRAY = [" " for i in range(5)]    #array that holds data for output to .csv
COL_MAX = 5                             #test threshold
CLI_INFO = "Client1"                    #initalize client info
TEST_RES = ""                           #initalize PASS/FAIL test result 

def imageCapture(imageNumber):
    """captures an image using the RaspberryPi camera
        and saves it in a folder called 'images' in the current working
        directory. It names the file the number of the current sample"""

#set the camera resolution
    #camera.resolution = (1920,1080)    #set the camera resolution
    
    cwd = os.getcwd()                   #gets the directory where the image is stored
    fileName = cwd + str(imageNumber) + ".jpg"                       
    
    #camera.capture(fileName)           #takes an image and stores in specified directory fileName

def toCSV(data):
    """creates a .csv in a folder named 'Database' in the current working directory
        where the collected information about the sample is stored"""

    cwd = os.getcwd()
    with open(cwd + '/Database/output.csv', 'w') as file:
        data_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        data_writer.writerow('/n')
        data_writer.writerow(data)
        
        
def AnalyzeSample(petriNumber):
    """Takes in the current sample number and runs image analysis.
        returns the number of microbial samples found"""

    col_count = 0
    imageCapture(petriNumber)
    #perform image analysis.
    col_count = colonyCounter.analyzeImage(petriNumber)
    return col_count
#    if(COL_COUNT < COL_MAX):      #checks number of samples against threshold
#        TEST_RES = "Pass"         #and applies a PASS/FAIL result.
#    else:
#        TEST_RES = "Fail"
        
    #organize data for output
#    DATA_ARRAY = [str(petriNumber), str(COL_COUNT), TEST_RES, CLI_INFO]

#    toCSV(DATA_ARRAY)             #write to .csv file
    

#def startCommand(sampleCount, sampleNum):
#    SAMPLE_CNT = sampleCount
#    CUR_SAMPLE = 0
#    start_time = time.time()    
#if __name__ == '__main__':  
#    for SAMPLE_CNT in range(SAMPLE_CNT, 0, -1):
#        AnalyzeSample(CUR_SAMPLE)
#        CUR_SAMPLE += 1           #increment current sample number
#    print("--- %s seconds ---" % (time.time() - start_time))
