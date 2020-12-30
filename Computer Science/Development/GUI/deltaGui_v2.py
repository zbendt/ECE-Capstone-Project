from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import deltaImageProcessor
import robo_controls
import time
import sys
import os



CLIENT_NAME = ""
CUR_SAMPLE = 0
TEST_RES = "RESULT"
COL_COUNT = 0
THRESHOLD = 0
TOTAL_SAMPLES = 0
WAIT = False
END = False

class WorkerSignals(QObject):
    finished = pyqtSignal()
    next_samp = pyqtSignal()
    pause = pyqtSignal()
    
class Worker(QRunnable):
        
    def __init__(self, fn):
        super(Worker, self).__init__()
       
        self.fn = fn
        self.signals = WorkerSignals()
        
    @pyqtSlot()
    def run(self):
        global CUR_SAMPLE
        global TEST_RES
        global COL_COUNT
        global THRESHOLD
        global TOTAL_SAMPLES
                    
        while(CUR_SAMPLE < TOTAL_SAMPLES-1):
            
            while(WAIT == True):
                time.sleep(0.01)
            if(END == True):
                print("Resetting System")
                robo_controls.drop()
                robo_controls.move_to_start()
                break
            else:
                robo_controls.move_to_start()
                robo_controls.pickup()
                robo_controls.move_to_camera()
                robo_controls.drop()
                print("Processing Sample " + str(CUR_SAMPLE))
                COL_COUNT = deltaImageProcessor.AnalyzeSample(CUR_SAMPLE) #run analysis
                
                robo_controls.pickup()
                
                if(COL_COUNT < THRESHOLD):                                #assign test result        
                    TEST_RES = "PASS"
                    robo_controls.move_to_passed()
                else:
                    TEST_RES = "FAIL"
                    robo_controls.move_to_failed()

                robo_controls.drop()  
                self.signals.next_samp.emit()
            
        self.signals.finished.emit()  # Done
        
    def __del__(self):
        self.signals.pause.emit()
        
    
class Ui_MicrobialAnalysis(object):

    def setupUi(self, MicrobialAnalysis):
        MicrobialAnalysis.setObjectName("MicrobialAnalysis")
        MicrobialAnalysis.resize(742, 617)
        MicrobialAnalysis.setAutoFillBackground(True)

        self.centralwidget = QWidget(MicrobialAnalysis)
        self.centralwidget.setObjectName("centralwidget")
        self.controls = QGroupBox(self.centralwidget)
        self.controls.setGeometry(QRect(10, 8, 241, 514))

        font = QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)

        self.controls.setFont(font)
        self.controls.setObjectName("controls")

        self.buttonsWidget = QWidget(self.controls)
        self.buttonsWidget.setGeometry(QRect(10, 180, 221, 321))
        self.buttonsWidget.setObjectName("buttonsWidget")

        self.resetButton = QPushButton(self.buttonsWidget)
        self.resetButton.setGeometry(QRect(0, 220, 221, 81))
        self.resetButton.setFont(font)
        self.resetButton.setObjectName("resetButton")

        self.stopButton = QPushButton(self.buttonsWidget)
        self.stopButton.setGeometry(QRect(0, 120, 221, 75))
        self.stopButton.setFont(font)
        self.stopButton.setObjectName("stopButton")

        self.startButton = QPushButton(self.buttonsWidget)
        self.startButton.setGeometry(QRect(0, 20, 221, 75))
        self.startButton.setFont(font)
        self.startButton.setObjectName("startButton")

        self.numberOfSamples = QSpinBox(self.controls)
        self.numberOfSamples.setGeometry(QRect(140, 50, 81, 31))
        self.numberOfSamples.setMaximum(999)
        self.numberOfSamples.setObjectName("numberOfSamples")

        self.spinBoxLabel = QLabel(self.controls)
        self.spinBoxLabel.setGeometry(QRect(10, 30, 121, 64))
        self.spinBoxLabel.setWordWrap(True)
        self.spinBoxLabel.setObjectName("spinBoxLabel")

        self.threshold = QSpinBox(self.controls)
        self.threshold.setGeometry(QRect(140, 110, 81, 31))
        self.threshold.setMaximum(999)
        self.threshold.setObjectName("threshold")

        self.thresholdLabel = QLabel(self.controls)
        self.thresholdLabel.setGeometry(QRect(10, 100, 121, 61))
        self.thresholdLabel.setWordWrap(True)
        self.thresholdLabel.setObjectName("thresholdLabel")

        self.resultsGroupBox = QGroupBox(self.centralwidget)
        self.resultsGroupBox.setGeometry(QRect(260, 8, 471, 234))
        self.resultsGroupBox.setFont(font)
        self.resultsGroupBox.setObjectName("resultsGroupBox")

        self.sampleNumber = QLabel(self.resultsGroupBox)
        self.sampleNumber.setGeometry(QRect(210, 80, 231, 41))
        self.sampleNumber.setFont(font)
        self.sampleNumber.setAutoFillBackground(False)
        self.sampleNumber.setAlignment(Qt.AlignCenter)
        self.sampleNumber.setObjectName("sampleNumber")

        self.clientName = QLabel(self.resultsGroupBox)
        self.clientName.setGeometry(QRect(210, 30, 231, 41))  
        self.clientName.setFont(font)
        self.clientName.setAutoFillBackground(False)
        self.clientName.setScaledContents(False)
        self.clientName.setAlignment(Qt.AlignCenter)
        self.clientName.setObjectName("clientName")

        self.passFail = QLabel(self.resultsGroupBox)
        self.passFail.setGeometry(QRect(210, 130, 231, 41))
        self.passFail.setFont(font)
        self.passFail.setAutoFillBackground(False)
        self.passFail.setAlignment(Qt.AlignCenter)
        self.passFail.setObjectName("passFail")

        self.colonyCount = QLabel(self.resultsGroupBox)
        self.colonyCount.setGeometry(QRect(210, 180, 231, 41))
        self.colonyCount.setFont(font)
        self.colonyCount.setAutoFillBackground(False)
        self.colonyCount.setAlignment(Qt.AlignCenter)
        self.colonyCount.setObjectName("colonyCount")

        self.clientLabel = QLabel(self.resultsGroupBox)
        self.clientLabel.setGeometry(QRect(30, 30, 171, 41))
        self.clientLabel.setObjectName("clientLabel")

        self.sampleNumLabel = QLabel(self.resultsGroupBox)
        self.sampleNumLabel.setGeometry(QRect(30, 80, 171, 41))
        self.sampleNumLabel.setObjectName("sampleNumLabel")

        self.passFailLabel = QLabel(self.resultsGroupBox)
        self.passFailLabel.setGeometry(QRect(30, 130, 171, 41))
        self.passFailLabel.setObjectName("passFailLabel")

        self.colonycountLabel = QLabel(self.resultsGroupBox)
        self.colonycountLabel.setGeometry(QRect(30, 180, 171, 41))
        self.colonycountLabel.setObjectName("colonycountLabel")

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QRect(20, 530, 711, 41))
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 25)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setRange(0, TOTAL_SAMPLES)

        self.Image = QGroupBox(self.centralwidget)
        self.Image.setGeometry(QRect(260, 250, 471, 272))
        self.Image.setFont(font)
        self.Image.setTitle("")
        self.Image.setObjectName("Image")

        self.sampleImage = QLabel(self.Image)
        self.sampleImage.setGeometry(QRect(10, 10, 451, 251))
        self.sampleImage.setText("")
        directory = "/home/pi/Documents/deltaImageProcessor/"
        imageName = "sample.jpg"
        self.sampleImage.setPixmap(QPixmap(os.path.join(directory, imageName)))
        self.sampleImage.setScaledContents(True)
        self.sampleImage.setMinimumSize(10, 10)
        self.sampleImage.setObjectName("sampleImage")

        MicrobialAnalysis.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MicrobialAnalysis)
        self.menubar.setGeometry(QRect(0, 0, 742, 25))
        self.menubar.setObjectName("menubar")
        MicrobialAnalysis.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MicrobialAnalysis)
        self.statusbar.setObjectName("statusbar")
        MicrobialAnalysis.setStatusBar(self.statusbar)
        self.retranslateUi(MicrobialAnalysis)
        QMetaObject.connectSlotsByName(MicrobialAnalysis)
        

        self.startButton.clicked.connect(self.start_clicked)
        self.stopButton.clicked.connect(self.stop_clicked) 
        self.resetButton.clicked.connect(self.reset_clicked)
        
        self.threadpool = QThreadPool()
        

    def retranslateUi(self, MicrobialAnalysis):
        _translate = QCoreApplication.translate
        MicrobialAnalysis.setWindowTitle(_translate("MicrobialAnalysis", "Microbial Analysis Tool"))
        self.controls.setTitle(_translate("MicrobialAnalysis", "Controls"))
        self.resetButton.setText(_translate("MicrobialAnalysis", "Reset"))
        self.stopButton.setText(_translate("MicrobialAnalysis", "Stop"))
        self.startButton.setText(_translate("MicrobialAnalysis", "Start"))
        self.spinBoxLabel.setText(_translate("MicrobialAnalysis", "Number of samples"))
        self.thresholdLabel.setText(_translate("MicrobialAnalysis", "Test Threshold"))
        self.resultsGroupBox.setTitle(_translate("MicrobialAnalysis", "Results"))
        self.sampleNumber.setText(_translate("MicrobialAnalysis", "0"))
        self.clientName.setText(_translate("MicrobialAnalysis", "Brewmeister"))
        self.passFail.setText(_translate("MicrobialAnalysis", "PASS"))
        self.colonyCount.setText(_translate("MicrobialAnalysis", "0"))
        self.clientLabel.setText(_translate("MicrobialAnalysis", "Client Name"))
        self.sampleNumLabel.setText(_translate("MicrobialAnalysis", "Sample Number"))
        self.passFailLabel.setText(_translate("MicrobialAnalysis", "Pass/Fail"))
        self.colonycountLabel.setText(_translate("MicrobialAnalysis", "Colony Count"))
    
    def stop_clicked(self):
        global WAIT
        print ("Pausing system. Finishing current sample...")
        WAIT = True
        END = False
        

    def reset_clicked(self):
        global END
        END = True
        WAIT = False
        
    def execute_this_fn(self):
        print("Running Samples")
        
    def next_sample(self):
        global CUR_SAMPLE
        global COL_COUNT
        global TEST_RES
        self.sampleNumber.setText(str(CUR_SAMPLE))
        self.colonyCount.setText(str(COL_COUNT))
        self.passFail.setText(str(TEST_RES))
        directory = "/home/pi/Documents/deltaImageProcessor/images_with_keys/"
        imageName = str(CUR_SAMPLE) + ".jpg"
        self.sampleImage.setPixmap(QPixmap(os.path.join(directory, imageName)))
        CUR_SAMPLE += 1
        
    def thread_complete(self):
        print("Analysis Complete!")
 
    def start_clicked(self):
        global THRESHOLD
        global TOTAL_SAMPLES
        global WAIT
        if(WAIT == True):
            WAIT = False
        else:
            TOTAL_SAMPLES = self.numberOfSamples.value()
            THRESHOLD = self.threshold.value()
            worker = Worker(self.execute_this_fn)
            worker.signals.next_samp.connect(self.next_sample)
            worker.signals.finished.connect(self.thread_complete)
            self.threadpool.start(worker) 
        
if __name__ == "__main__":
    #import_excel_info()
    app = QApplication(sys.argv)
    MicrobialAnalysis = QMainWindow()
    ui = Ui_MicrobialAnalysis()
    ui.setupUi(MicrobialAnalysis)
    MicrobialAnalysis.show()
    sys.exit(app.exec_())