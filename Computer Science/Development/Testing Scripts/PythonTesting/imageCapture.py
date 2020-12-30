import picamera
camera = picamera.PiCamera() # initalize variable

"""
The imageCapture function takes a picture,
names it using the imageNumber variable
and saves it to a specified directory.
"""
def imageCapture(imageNumber):
    # sets the camera resolution
    camera.resolution = (1280,720)
    
    # sets the directory where the image is stored
    fileName = \
        "/home/pi/Documents/deltaImageProcessor/images/"\
        + str(imageNumber) + ".jpg"                       
    
    # takes an image and stores in specified directory fileName
    camera.capture(fileName)                              
    return