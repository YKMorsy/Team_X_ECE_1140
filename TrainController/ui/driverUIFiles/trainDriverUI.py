import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from qtwidgets import Toggle
from QLed import QLed

from multiprocessing import Lock
from ui.support.readAndWriteFiles import  writeDriverInputFile
from ui.support.readAndWriteFiles import readDriverOutputFile
from ui.support.readAndWriteFiles import readEngineerInputFile
from ui.support.readAndWriteFiles import writeEngineerInputFile

class EngineerWindow(QWidget):
    def __init__(self, lockEngineerFile, trainNumber):
        super().__init__()
        self.setWindowTitle("Engineer Input Box")

        self.lockEngineerFile = lockEngineerFile

        self.outputFileName = "./ui/driverUIFiles/utilities/engineerInputDB_" + str(trainNumber) + ".txt"
        self.kp, self.ki = readEngineerInputFile(self.outputFileName, self.lockEngineerFile)

        layout = QHBoxLayout()
        layout.addWidget(QLabel("Kp Value: "))
        kpEnterBox = QLineEdit(str(self.kp))
        kpEnterBox.textChanged[str].connect(self.__updateKpValue)
        layout.addWidget(kpEnterBox)
        layout.addWidget(QLabel("Ki Value: "))
        kiEnterBox = QLineEdit(str(self.ki))
        kiEnterBox.textChanged[str].connect(self.__updateKivalue)
        layout.addWidget(kiEnterBox)

        self.setLayout(layout)
    
    def __updateKpValue(self, text):
        try:
            self.kp = float(text)
        except ValueError:
            self.kp = self.kp
        
        writeEngineerInputFile(self.outputFileName, self.lockEngineerFile, self.kp, self.ki)
    
    def __updateKivalue(self, text):
        try:
            self.ki = float(text)
        except ValueError:
            self.ki = self.ki
        writeEngineerInputFile(self.outputFileName, self.lockEngineerFile, self.kp, self.ki)


class LoginForm(QWidget):
    def __init__(self, lockEngineerFile, trainNumber):
        super().__init__()
        self.setWindowTitle('Login Form')
        self.resize(500, 120)
        self.lockEngineerFile = lockEngineerFile
        self.trainNumber = trainNumber

        layout = QGridLayout()

        label_name = QLabel('<font size="4"> Username </font>')
        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setPlaceholderText('Please enter your username')
        layout.addWidget(label_name, 0, 0)
        layout.addWidget(self.lineEdit_username, 0, 1)

        label_password = QLabel('<font size="4"> Password </font>')
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText('Please enter your password')
        layout.addWidget(label_password, 1, 0)
        layout.addWidget(self.lineEdit_password, 1, 1)

        button_login = QPushButton('Login')
        button_login.clicked.connect(self.check_password)
        layout.addWidget(button_login, 2, 0, 1, 2)
        layout.setRowMinimumHeight(2, 75)

        self.setLayout(layout)

    def check_password(self):
        if self.lineEdit_username.text() == "admin" and self.lineEdit_password.text() ==  "password":
            self.close()
            self.editKpAndKi = EngineerWindow(self.lockEngineerFile, self.trainNumber)
            self.editKpAndKi.show()

class MainWindow(QWidget):
    def __init__(self, train, lockOutputFile, lockInputFile, lockEngineerFile):
        super().__init__()

        self.train = train
        self.lockOutputFile = lockOutputFile
        self.lockInputFile = lockInputFile
        self.lockEngineerFile = lockEngineerFile
        self.trainNumber = train.trainNumber
        self.driverOutput = train.trainDriverOutput
        self.driverInput = train.trainDriverInput
        self.trainLine = train.trainLine

        self.inputFileName = "./ui/driverUIFiles/utilities/driverInputDB_" + str(self.trainNumber) + ".txt"
        self.outputFileName = "./ui/driverUIFiles/utilities/driverOutputDB_" + str(self.trainNumber) + ".txt"

        self.setWindowTitle("Train Controller: " + str(self.trainNumber))

        self.__layoutInit()

        self.__createHeader()
        self.__createDriverOuputWidgets()
        self.__createSpeedInfoLayout()
        self.__createSpeedButtonLayout()
        self.__createServiceBrakeButton()
        self.__createSystemMonitor()
        self.__createFaultIndicator()
        self.__createMiddleTopRight()
        self.__createMap()
        self.__createTemperatureControl()
        self.__createToggleLabels()
        self.__createToggleButtons()
        self.__createEmergencyBrakeButton()

        self.__assembleLayouts()
        self.setLayout(self.mainLayout)
    
    def __layoutInit(self):
        self.mainLayout = QVBoxLayout()

        self.headerLayout = QHBoxLayout()
        self.bodyLayout = QHBoxLayout()

        self.leftLayout = QVBoxLayout()
        self.middleLayout = QVBoxLayout()
        self.rightLayout = QVBoxLayout()

        self.speedInfoLayout = QVBoxLayout()
        self.speedChangeLayout = QHBoxLayout()
        self.speedButtonsLayout = QVBoxLayout()

        self.middleTopLayout = QHBoxLayout()
        self.faultLayout = QHBoxLayout()
        self.faultLabelLayout = QVBoxLayout()
        self.faultIndicatorLayout = QVBoxLayout()
        self.middleTopRightLayout = QVBoxLayout()
        self.manualModeToggleLayout = QHBoxLayout()

        self.nonVitalControlsLayout = QVBoxLayout()
        self.temperatureControlLayout = QHBoxLayout()
        self.togglesLayout = QHBoxLayout()
        self.toggleLabelsLayout = QVBoxLayout()
        self.togglesButtonsLayout = QVBoxLayout()
    
    def __assembleLayouts(self):
        self.leftLayout.addLayout(self.speedInfoLayout)
        self.leftLayout.addLayout(self.speedChangeLayout)
        self.leftLayout.addWidget(self.serviceBrakeButton)

        self.faultLayout.addLayout(self.faultLabelLayout, 8)
        self.faultLayout.addLayout(self.faultIndicatorLayout, 2)
        self.middleTopLayout.addLayout(self.faultLayout)
        self.middleTopLayout.addLayout(self.middleTopRightLayout)
        self.middleLayout.addLayout(self.middleTopLayout)
        self.middleLayout.addWidget(self.map)

        self.nonVitalControlsLayout.addWidget(self.interiorTemperatureOutput)
        self.nonVitalControlsLayout.addLayout(self.temperatureControlLayout)
        self.togglesLayout.addLayout(self.toggleLabelsLayout)
        self.togglesLayout.addLayout(self.togglesButtonsLayout)
        self.nonVitalControlsLayout.addLayout(self.togglesLayout)
        self.nonVitalControlsLayout.addWidget(self.activateAnnouncmentButton)
        self.rightLayout.addLayout(self.nonVitalControlsLayout)
        self.rightLayout.addWidget(self.emergencyBrakeButton)

        self.bodyLayout.addLayout(self.leftLayout)
        self.bodyLayout.addLayout(self.middleLayout)
        self.bodyLayout.addLayout(self.rightLayout)

        self.mainLayout.addLayout(self.headerLayout, 1)
        self.mainLayout.addLayout(self.bodyLayout, 9)

    def __createHeader(self):
        self.engineerLogin = QPushButton("Engineer Login")
        self.engineerLogin.clicked.connect(self.__loginWindow)
        
        self.dateAndTime = QLabel("10/8/2022\n5:00 PM")
        self.dateAndTime.setAlignment(Qt.AlignCenter)

        self.trainInformation = QLabel("Flexity Tram 2 Train " + str(self.trainNumber))
        self.trainInformation.setAlignment(Qt.AlignRight)

        self.headerLayout.addWidget(self.engineerLogin)
        self.headerLayout.addWidget(self.dateAndTime)
        self.headerLayout.addWidget(self.trainInformation)
    
    def __createSpeedInfoLayout(self):
        self.speedInfoLayout.addWidget(self.currentSetPointOutput)
        self.speedInfoLayout.addWidget(self.speedLimitOutput)
        self.speedInfoLayout.addWidget(self.commandSetPointOutput)
    
    def __createSpeedButtonLayout(self):
        self.speedBar = QProgressBar()
        self.speedIncrement = QPushButton("Up")
        self.speedIncrement.pressed.connect(self.__increaseSpeedButton)
        self.speedDecrement = QPushButton("Down")
        self.speedDecrement.pressed.connect(self.__decreaseSpeedButton)

        self.speedButtonsLayout.addWidget(self.speedIncrement)
        self.speedButtonsLayout.addWidget(self.speedDecrement)

        self.speedChangeLayout.addWidget(self.speedBar)
        self.speedChangeLayout.addLayout(self.speedButtonsLayout)
    
    def __createServiceBrakeButton(self):
        self.serviceBrakeButton = QPushButton("Service Brake")
        self.serviceBrakeButton.pressed.connect(self.__serviceBrakeButtonActionOn)
        self.serviceBrakeButton.released.connect(self.__serviceBrakeButtonActionOff)
    
    def __createSystemMonitor(self):
        self.brakeFailureLabel = QLabel("Brakes")
        self.engineFailureLabel = QLabel("Engine")
        self.wheelFailureLabel = QLabel("Wheels")
        self.signalFailureLabel = QLabel("Signal Pickup Failure")

        self.faultLabelLayout.addWidget(self.brakeFailureLabel)
        self.faultLabelLayout.addWidget(self.engineFailureLabel)
        self.faultLabelLayout.addWidget(self.wheelFailureLabel)
        self.faultLabelLayout.addWidget(self.signalFailureLabel)

    def __createFaultIndicator(self):
        self.brakeFailureIndicator = QLed(offColour= QLed.Green, onColour = QLed.Red, shape=QLed.Circle)
        self.brakeFailureIndicator.value = self.driverOutput.brakeFailure
        self.engineFailureIndicator = QLed(offColour= QLed.Green,onColour = QLed.Red, shape=QLed.Circle)
        self.engineFailureIndicator.value = self.driverOutput.engineFailure
        self.wheelFailureIndicator = QLed(offColour= QLed.Green,onColour = QLed.Red, shape=QLed.Circle)
        self.wheelFailureIndicator.value = self.driverOutput.wheelFailure
        self.signalFailureIndicator = QLed(offColour= QLed.Green,onColour = QLed.Red, shape=QLed.Circle)
        self.signalFailureIndicator.value = self.driverOutput.signalPickUpFailure

        self.faultIndicatorLayout.addWidget(self.brakeFailureIndicator)
        self.faultIndicatorLayout.addWidget(self.engineFailureIndicator)
        self.faultIndicatorLayout.addWidget(self.wheelFailureIndicator)
        self.faultIndicatorLayout.addWidget(self.signalFailureIndicator)
    
    def __createMiddleTopRight(self):
        self.manualModeToggle = Toggle(checked_color="#00FF00")
        self.manualModeToggle.toggled.connect(self.__manualModeToggle)
        self.trainLineLabel = QLabel()
        if self.trainLine == 1:
            self.trainLineLabel.setText("Green Line")
        else:
            self.trainLineLabel.setText("Red Line")

        self.manualModeToggleLayout.addWidget(QLabel("Manual Mode"), 8)
        self.manualModeToggleLayout.addWidget(self.manualModeToggle)
        self.middleTopRightLayout.addWidget(self.authorityOutput)
        self.middleTopRightLayout.addLayout(self.manualModeToggleLayout)
        self.middleTopRightLayout.addWidget(self.trainLineLabel)
        self.middleTopRightLayout.addWidget(self.nextStop)

    
    def __createMap(self):
        self.map = QLabel("Map")

    def __createTemperatureControl(self):
        self.incrementTemperature = QPushButton("Up")
        self.incrementTemperature.pressed.connect(self.__incrementTemperature)
        self.decrementTemperature = QPushButton("Down")
        self.decrementTemperature.pressed.connect(self.__decrementTemperature)
        self.temperatureControlLayout.addWidget(self.incrementTemperature)
        self.temperatureControlLayout.addWidget(self.decrementTemperature)
    
    def __createToggleLabels(self):
        self.toggleLabelsLayout.addWidget(QLabel("Left Side Doors"))
        self.toggleLabelsLayout.addWidget(QLabel("Right Side Doors"))
        self.toggleLabelsLayout.addWidget(QLabel("Interior Lights"))
        self.toggleLabelsLayout.addWidget(QLabel("Exterior Lights"))
    
    def __createToggleButtons(self):
        self.toggleLeftSideDoorsButton = Toggle(checked_color="#00FF00")
        self.toggleLeftSideDoorsButton.toggled.connect(self.__leftSideDoorsToggle)
        self.toggleRightSideDoorsButton = Toggle(checked_color="#00FF00")
        self.toggleRightSideDoorsButton.toggled.connect(self.__rightSideDoorsToggle)
        self.toggleInsideLightsButton = Toggle(checked_color="#00FF00")
        self.toggleInsideLightsButton.toggled.connect(self.__insideLightsToggle)
        self.toggleOutsideLightsButton = Toggle(checked_color="#00FF00")
        self.toggleOutsideLightsButton.toggled.connect(self.__outsideLightsToggle)

        self.activateAnnouncmentButton = QPushButton("Activate Announcement")
        self.activateAnnouncmentButton.pressed.connect(self.__activateAnnouncmentPress)
        self.activateAnnouncmentButton.released.connect(self.__activateAnnouncementRelease)

        self.togglesButtonsLayout.addWidget(self.toggleLeftSideDoorsButton)
        self.togglesButtonsLayout.addWidget(self.toggleRightSideDoorsButton)
        self.togglesButtonsLayout.addWidget(self.toggleInsideLightsButton)
        self.togglesButtonsLayout.addWidget(self.toggleOutsideLightsButton)
    
    def __createEmergencyBrakeButton(self):
        self.emergencyBrakeButton = QPushButton("Emergency Brake")
        self.emergencyBrakeButton.pressed.connect(self.__emergencyBrakeButtonActionOn)
        self.emergencyBrakeButton.released.connect(self.__emergencyBrakeButtonActionOff)
    
    def __createDriverOuputWidgets(self):
        self.currentSetPointOutput = QLabel()
        self.speedLimitOutput = QLabel()
        self.interiorTemperatureOutput = QLabel()
        self.commandSetPointOutput = QLabel()
        self.authorityOutput = QLabel()
        self.authorityOutput.setAlignment(Qt.AlignCenter)
        self.nextStop = QLabel()
    
    def __updateOutputWidgets(self):
        self.currentSetPointOutput.setText("Current Speed: " + str(int(self.driverOutput.currentSetPoint * 2.237)) + " mph")
        self.speedLimitOutput.setText("Speed Limit: " + str(int(self.driverOutput.speedLimit * 0.621371)) + " mph")
        self.interiorTemperatureOutput.setText("A/C Temperature: " + str(self.driverOutput.interiorTemperature) + "F")
        self.commandSetPointOutput.setText("Target Speed: " + str(int(self.driverOutput.commandSetPoint * 2.237)) + " mph")
        if self.driverOutput.authority:
            self.authorityOutput.setText("Go")
        else:
            self.authorityOutput.setText("Stop")

        self.brakeFailureIndicator.value = self.driverOutput.brakeFailure
        self.engineFailureIndicator.value = self.driverOutput.engineFailure
        self.wheelFailureIndicator.value = self.driverOutput.wheelFailure
        self.signalFailureIndicator.value = self.driverOutput.signalPickUpFailure
        if self.driverOutput.speedLimit == 0:
            self.speedBar.setValue(0)
        else:
            self.speedBar.setValue(int(self.driverOutput.currentSetPoint / self.driverOutput.speedLimit * 100))
        self.nextStop.setText("Next Stop: " + self.driverOutput.nextStop)
    
    def update(self):
        readDriverOutputFile(self.outputFileName, self.lockOutputFile, self.driverOutput)
        self.__updateOutputWidgets()
        if not self.driverInput.manualMode:
            self.driverInput.commandSetPoint = self.driverOutput.commandSetPoint
        writeDriverInputFile(self.inputFileName, self.lockInputFile, self.driverInput)
    
    
    def __serviceBrakeButtonActionOn(self):
        self.driverInput.serviceBrake = True
    
    def __serviceBrakeButtonActionOff(self):
        self.driverInput.serviceBrake = False
    
    def __emergencyBrakeButtonActionOn(self):
        self.driverInput.emergencyBrake = True

    def __emergencyBrakeButtonActionOff(self):
        self.driverInput.emergencyBrake = False

    def __manualModeToggle(self):
        self.driverInput.manualMode = self.manualModeToggle.isChecked()
    
    def __leftSideDoorsToggle(self):
        self.driverInput.leftSideDoors = self.toggleLeftSideDoorsButton.isChecked()
    
    def __rightSideDoorsToggle(self):
        self.driverInput.rightSideDoors = self.toggleRightSideDoorsButton.isChecked()
    
    def __insideLightsToggle(self):
        self.driverInput.insideLights = self.toggleInsideLightsButton.isChecked()
    
    def __outsideLightsToggle(self):
        self.driverInput.outsideLights = self.toggleOutsideLightsButton.isChecked()
    
    def __increaseSpeedButton(self):
        if self.driverInput.manualMode:
            self.driverInput.commandSetPoint += 0.44704
    
    def __decreaseSpeedButton(self):
        if self.driverInput.manualMode:
            self.driverInput.commandSetPoint -= 0.44704
    
    def __activateAnnouncmentPress(self):
        self.driverInput.activateAnnouncement = True
    
    def __activateAnnouncementRelease(self):
        self.driverInput.activateAnnouncement = False
    
    def __incrementTemperature(self):
        if self.driverOutput.interiorTemperature < 78:
            self.driverInput.interiorTemperatureControl += 1
    
    def __decrementTemperature(self):
        if self.driverOutput.interiorTemperature > 65:
            self.driverInput.interiorTemperatureControl -= 1
    
    def __loginWindow(self):
        self.newLogin = LoginForm(self.lockEngineerFile, self.trainNumber)
        self.newLogin.show()
        
    

def driverUI(train, lockOutputFile, lockInputFile, lockEngineerInput):
    app = QApplication([])
    window = MainWindow(train, lockOutputFile, lockInputFile, lockEngineerInput)
    fps = 15
    timer = QTimer()
    timer.timeout.connect(window.update)
    timer.setInterval(int(1000 / fps))
    timer.start()
    window.show()
    app.exec()
    