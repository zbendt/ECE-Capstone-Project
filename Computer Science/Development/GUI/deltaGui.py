from PyQt5 import QtCore, QtGui, QtWidgets
import deltaImageProcessor
import time

CLIENT_NAME = ""
CUR_SAMPLE = 0
TEST_RES = "RESULT"
COL_COUNT = 0
THRESHOLD = 0
TOTAL_SAMP = 0

class imageProcessingThread(QtCore.QThread):
    def __init__(self):
        QtCore.QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
         
        THRESHOLD = self.threshold.value()                            #threshold for pass/fail test
        TOTAL_SAMPLES = self.numberOfSamples.value()                  #total number of samples to be tested
        CUR_SAMPLE = 1                                                #current sample number                                                #colony count for current sample
        
        while(CUR_SAMPLE <= TOTAL_SAMPLES):
            print("Current Sample: " + str(CUR_SAMPLE))
            cur_samp_text = str(CUR_SAMPLE)
            self.sampleNumber.setText(cur_samp_text)                  #update current sample on GUI
            self.sampleNumber.update() 
            COL_COUNT = deltaImageProcessor.AnalyzeSample(CUR_SAMPLE) #run analysis
            print("Current Count: " + str(COL_COUNT))
            col_text = str(COL_COUNT)
            self.colonyCount.setText(col_text)                        #update colony count of curent sample
            self.colonyCount.update() 
            time.sleep(.5)                                            #let gui update
            
            if(COL_COUNT < THRESHOLD):                                #assign test result        
                TEST_RES = "PASS"
            else:
                TEST_RES = "FAIL"
                
            CUR_SAMPLE += 1                                           #incerment cur_sample
            self.passFail.setText(TEST_RES)                           #update TEST_RES text
            self.passFail.update()                                    #update GUI

class Ui_MicrobialAnalysis(object):
    def setupUi(self, MicrobialAnalysis):

        MicrobialAnalysis.setObjectName("MicrobialAnalysis")
        MicrobialAnalysis.resize(742, 617)
        MicrobialAnalysis.setAutoFillBackground(True)

        self.centralwidget = QtWidgets.QWidget(MicrobialAnalysis)
        self.centralwidget.setObjectName("centralwidget")
        self.controls = QtWidgets.QGroupBox(self.centralwidget)
        self.controls.setGeometry(QtCore.QRect(10, 8, 241, 514))

        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)

        self.controls.setFont(font)
        self.controls.setObjectName("controls")

        self.buttonsWidget = QtWidgets.QWidget(self.controls)
        self.buttonsWidget.setGeometry(QtCore.QRect(10, 180, 221, 321))
        self.buttonsWidget.setObjectName("buttonsWidget")

        self.resetButton = QtWidgets.QPushButton(self.buttonsWidget)
        self.resetButton.setGeometry(QtCore.QRect(0, 220, 221, 81))
        self.resetButton.setFont(font)
        self.resetButton.setObjectName("resetButton")

        self.stopButton = QtWidgets.QPushButton(self.buttonsWidget)
        self.stopButton.setGeometry(QtCore.QRect(0, 120, 221, 75))
        self.stopButton.setFont(font)
        self.stopButton.setObjectName("stopButton")

        self.startButton = QtWidgets.QPushButton(self.buttonsWidget)
        self.startButton.setGeometry(QtCore.QRect(0, 20, 221, 75))
        self.startButton.setFont(font)
        self.startButton.setObjectName("startButton")

        self.numberOfSamples = QtWidgets.QSpinBox(self.controls)
        self.numberOfSamples.setGeometry(QtCore.QRect(140, 50, 81, 31))
        self.numberOfSamples.setMaximum(999)
        self.numberOfSamples.setObjectName("numberOfSamples")

        self.spinBoxLabel = QtWidgets.QLabel(self.controls)
        self.spinBoxLabel.setGeometry(QtCore.QRect(10, 30, 121, 64))
        self.spinBoxLabel.setWordWrap(True)
        self.spinBoxLabel.setObjectName("spinBoxLabel")

        self.threshold = QtWidgets.QSpinBox(self.controls)
        self.threshold.setGeometry(QtCore.QRect(140, 110, 81, 31))
        self.threshold.setMaximum(999)
        self.threshold.setObjectName("threshold")

        self.thresholdLabel = QtWidgets.QLabel(self.controls)
        self.thresholdLabel.setGeometry(QtCore.QRect(10, 100, 121, 61))
        self.thresholdLabel.setWordWrap(True)
        self.thresholdLabel.setObjectName("thresholdLabel")

        self.resultsGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.resultsGroupBox.setGeometry(QtCore.QRect(260, 8, 471, 234))
        self.resultsGroupBox.setFont(font)
        self.resultsGroupBox.setObjectName("resultsGroupBox")

        self.sampleNumber = QtWidgets.QLabel(self.resultsGroupBox)
        self.sampleNumber.setGeometry(QtCore.QRect(210, 80, 231, 41))
        self.sampleNumber.setFont(font)
        self.sampleNumber.setAutoFillBackground(False)
        self.sampleNumber.setAlignment(QtCore.Qt.AlignCenter)
        self.sampleNumber.setObjectName("sampleNumber")

        self.clientName = QtWidgets.QLabel(self.resultsGroupBox)
        self.clientName.setGeometry(QtCore.QRect(210, 30, 231, 41))  
        self.clientName.setFont(font)
        self.clientName.setAutoFillBackground(False)
        self.clientName.setScaledContents(False)
        self.clientName.setAlignment(QtCore.Qt.AlignCenter)
        self.clientName.setObjectName("clientName")

        self.passFail = QtWidgets.QLabel(self.resultsGroupBox)
        self.passFail.setGeometry(QtCore.QRect(210, 130, 231, 41))
        self.passFail.setFont(font)
        self.passFail.setAutoFillBackground(False)
        self.passFail.setAlignment(QtCore.Qt.AlignCenter)
        self.passFail.setObjectName("passFail")

        self.colonyCount = QtWidgets.QLabel(self.resultsGroupBox)
        self.colonyCount.setGeometry(QtCore.QRect(210, 180, 231, 41))
        self.colonyCount.setFont(font)
        self.colonyCount.setAutoFillBackground(False)
        self.colonyCount.setAlignment(QtCore.Qt.AlignCenter)
        self.colonyCount.setObjectName("colonyCount")

        self.clientLabel = QtWidgets.QLabel(self.resultsGroupBox)
        self.clientLabel.setGeometry(QtCore.QRect(30, 30, 171, 41))
        self.clientLabel.setObjectName("clientLabel")

        self.sampleNumLabel = QtWidgets.QLabel(self.resultsGroupBox)
        self.sampleNumLabel.setGeometry(QtCore.QRect(30, 80, 171, 41))
        self.sampleNumLabel.setObjectName("sampleNumLabel")

        self.passFailLabel = QtWidgets.QLabel(self.resultsGroupBox)
        self.passFailLabel.setGeometry(QtCore.QRect(30, 130, 171, 41))
        self.passFailLabel.setObjectName("passFailLabel")

        self.colonycountLabel = QtWidgets.QLabel(self.resultsGroupBox)
        self.colonycountLabel.setGeometry(QtCore.QRect(30, 180, 171, 41))
        self.colonycountLabel.setObjectName("colonycountLabel")

        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(20, 530, 711, 41))
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 25)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setRange(0, 10000)
        self.createProgressBar

        self.Image = QtWidgets.QGroupBox(self.centralwidget)
        self.Image.setGeometry(QtCore.QRect(260, 250, 471, 272))
        self.Image.setFont(font)
        self.Image.setTitle("")
        self.Image.setObjectName("Image")

        self.sampleImage = QtWidgets.QLabel(self.Image)
        self.sampleImage.setGeometry(QtCore.QRect(10, 10, 451, 251))
        self.sampleImage.setText("")
        self.sampleImage.setPixmap(QtGui.QPixmap("sample.jpg"))
        self.sampleImage.setScaledContents(True)
        self.sampleImage.setMinimumSize(10, 10)
        self.sampleImage.setObjectName("sampleImage")

        MicrobialAnalysis.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MicrobialAnalysis)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 742, 25))
        self.menubar.setObjectName("menubar")
        MicrobialAnalysis.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MicrobialAnalysis)
        self.statusbar.setObjectName("statusbar")
        MicrobialAnalysis.setStatusBar(self.statusbar)
        self.retranslateUi(MicrobialAnalysis)
        QtCore.QMetaObject.connectSlotsByName(MicrobialAnalysis)

        self.startButton.clicked.connect(self.start_clicked)
        self.stopButton.clicked.connect(self.stop_clicked) 
        self.resetButton.clicked.connect(self.reset_clicked)
      
        self.thread1 = imageProcessingThread()
        self.thread1.start()
            
            
    def stop_clicked(self):
        print ("Stop command sent") 

    def reset_clicked(self):
        print ("Reset command sent")

    def advanceProgressBar(self):
        curVal = self.progressBar.value()
        maxVal = self.progressBar.maximum()
        self.progressBar.setValue(curVal + (maxVal - curVal) / 100)

    def createProgressBar(self):
        self.progressBar.setRange(0, 10000)
        self.progressBar.setValue(0)

        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.advanceProgressBar)
        timer.start(1000)   

    def retranslateUi(self, MicrobialAnalysis):
        _translate = QtCore.QCoreApplication.translate
        MicrobialAnalysis.setWindowTitle(_translate("MicrobialAnalysis", "Microbial Analysis Tool"))
        self.controls.setTitle(_translate("MicrobialAnalysis", "Controls"))
        self.resetButton.setText(_translate("MicrobialAnalysis", "Reset"))
        self.stopButton.setText(_translate("MicrobialAnalysis", "Stop"))
        self.startButton.setText(_translate("MicrobialAnalysis", "Start"))
        self.spinBoxLabel.setText(_translate("MicrobialAnalysis", "Number of samples"))
        self.thresholdLabel.setText(_translate("MicrobialAnalysis", "Test Threshold"))
        self.resultsGroupBox.setTitle(_translate("MicrobialAnalysis", "Results"))
        self.sampleNumber.setText(_translate("MicrobialAnalysis", "00000"))
        self.clientName.setText(_translate("MicrobialAnalysis", "Brewmeister"))
        self.passFail.setText(_translate("MicrobialAnalysis", "PASS"))
        self.colonyCount.setText(_translate("MicrobialAnalysis", "000"))
        self.clientLabel.setText(_translate("MicrobialAnalysis", "Client Name"))
        self.sampleNumLabel.setText(_translate("MicrobialAnalysis", "Sample Number"))
        self.passFailLabel.setText(_translate("MicrobialAnalysis", "Pass/Fail"))
        self.colonycountLabel.setText(_translate("MicrobialAnalysis", "Colony Count"))


    def start_clicked(self):
       self.thread1.start()

if __name__ == "__main__":
    import sys
    #import_excel_info()
    app = QtWidgets.QApplication(sys.argv)
    MicrobialAnalysis = QtWidgets.QMainWindow()
    ui = Ui_MicrobialAnalysis()
    ui.setupUi(MicrobialAnalysis)
    MicrobialAnalysis.show()
    sys.exit(app.exec_())