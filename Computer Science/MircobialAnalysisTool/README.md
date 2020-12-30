
GUI.py - User interface source code
The bulk of the design and layout portion of this module was auto generated using QtDesigner then modified to fit our purposes.
The GUI has two threads running simultaneously. One updates the image that is displayed as well as the sample data. The other handles the automation controls and image analysis.

deltaImageProcessor.py - Handles image capture, and data output to .csv file.

colonyCounter.py - Computer Vision analysis
This module takes in a file from the "/images" folder located in the current working directory, performs computer vision analysis and applies keypoints over any detected colonies.

robo_controls.py – Sends automation control messages.
This module sends automation control messages via serial interface to the ATmega328 where they are decoded and used to set the motor anagles.

### User Interface

The GUI was developed using [PyQt5](https://pypi.org/project/PyQt5/). First, [QtDesigner](https://pythonbasics.org/qt-designer-python/) was used to build the basic layout, such as button and label placement placement.

<p align="middle">
   <img src = https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Computer%20Science/Images/Qt_Designer.png/ height="260" width="480">
</p>

Most of the placement of buttons and labels are self explainitory. In order to display the image it has has to displayed in a QLabel feature.

<p align="middle">
   <img src = https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Computer%20Science/Images/pixmap.png/>
</p>

Once the basic layout was set, QtDesigner exported a .ui file. This is then converted into editable code using a program called [pyuic5](https://pypi.org/project/pyuic5-tool/)

This gave a baseline for the GUI and we were then able to implement the fucntions that we need the GUI to perform. We were able to implement PyQt [QThreadPools](https://doc.qt.io/qt-5/qthreadpool.html) the let the GUI update with current image and other relevenat sample data. All threading was based on [this tutorial](https://www.learnpyqt.com/courses/concurrent-execution/multithreading-pyqt-applications-qthreadpool/)

### Computer Vision 

The basics of the computer vision was based on [this tutorial](https://www.learnopencv.com/blob-detection-using-opencv-python-c/). Though we were not able to fully implement the computer vision system due to the COVID19 global health crisis, the provided is a starting point to begin fine tuning the computer vision system.

The computer vision system follows these basic steps:
1. Capture image.
2. Convert image to grayscale.
3. Run analysis based on certain parameters (a full explaination of the parameters can be found in the linked tutorial).

<p align="middle">
   <img src = https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Computer%20Science/Images/BlobTest.jpg>
</p>

4. Keep count of microbial colony growthsd
5. Place keypoints on image over detected microbal colony growths.
6. Output the image with keypoints to the designated directory so it can be dislpayed on the GUI.
7. Output relevenat sample data to a .csv file.
