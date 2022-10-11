import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from qtwidgets import Toggle

from multiprocessing import Lock
from ui.support.readAndWriteFiles import  writeTrainModelInputFile
from ui.support.readAndWriteFiles import readTrainModelOutputFile

class MainWindow(QWidget):
        
        def __init__(self, train, lockOutputFile, lockInputFile):
            super().__init__()

            self.train = train
            self.lockOutputFile = lockOutputFile
            self.lockInputFile = lockInputFile
            self.trainNumber = train.trainNumber
            self.trainLine = train.trainLine
            self.modelOutput = train.trainModelOutput
            self.modelInput = train.trainModelInput
            self.powerSpeedSelect = False

            self.inputFileName = "./ui/testUIFiles/utilities/modelInputDB_" + str(self.trainNumber) + ".txt"
            self.outputFileName = "./ui/testUIFiles/utilities/modelOutputDB_" + str(self.trainNumber) + ".txt"

            self.setWindowTitle("Test UI Window " + str(self.trainNumber))
            self.createOutputWidgets()
            self.updateOutputWidgets()
            self.createInputWidgets()
            self.updateInputWidgetsOut()
            self.__layoutInit()

            self.__createHeader()
            self.__powerSpeedEnter()
            self.__outputList()

            self.__toggleSection()
            self.__stationSelect()
        
            self.__assembleLayouts()

            self.setLayout(self.outerLayout)
        
        def __layoutInit(self):
            self.outerLayout = QHBoxLayout()

            self.leftLayout = QVBoxLayout()
            self.rightLayout = QVBoxLayout()

            self.topLeftLayout = QHBoxLayout()
            self.topRightLayout = QHBoxLayout()

            self.currentSetPointLayout = QHBoxLayout()
            self.authorityToggleLayout = QHBoxLayout()

            self.powerSpeedEnterLayout = QHBoxLayout()
            self.powerSpeedEnterLabelLayout = QVBoxLayout()
            self.powerSpeedEnterTextLayout = QVBoxLayout()

            self.outputFieldLayout = QHBoxLayout()
            self.outputFieldLeftLayout = QVBoxLayout()
            self.outputFieldRightLayout = QVBoxLayout()

            self.toggleLayout = QHBoxLayout()
            self.toggleLeftLayout = QHBoxLayout()
            self.toggleLeftLabelLayout = QVBoxLayout()
            self.toggleLeftButtonLayout = QVBoxLayout()

        def __assembleLayouts(self):
            self.powerSpeedEnterLayout.addLayout(self.powerSpeedEnterLabelLayout, 8)
            self.powerSpeedEnterLayout.addLayout(self.powerSpeedEnterTextLayout, 2)
            self.toggleLeftLayout.addLayout(self.toggleLeftLabelLayout, 9)
            self.toggleLeftLayout.addLayout(self.toggleLeftButtonLayout, 1)
            self.toggleLayout.addLayout(self.toggleLeftLayout)

            self.leftLayout.addLayout(self.topLeftLayout, 1)
            self.leftLayout.addWidget(self.currentSetPoint, 1)
            self.leftLayout.addLayout(self.currentSetPointLayout,1)
            self.authorityToggleLayout.addWidget(self.authority, 8)
            self.authorityToggleLayout.addWidget(self.authorityToggle)
            self.leftLayout.addLayout(self.authorityToggleLayout, 1)
            self.leftLayout.addWidget(self.commandSetPoint, 1)
            self.leftLayout.addLayout(self.powerSpeedEnterLayout, 1)
            self.leftLayout.addLayout(self.toggleLayout, 3)
            self.leftLayout.addWidget(self.stationSelect)

            self.outputFieldLayout.addLayout(self.outputFieldLeftLayout)
            self.outputFieldLayout.addLayout(self.outputFieldRightLayout)

            self.rightLayout.addLayout(self.topRightLayout, 1)
            self.rightLayout.addLayout(self.outputFieldLayout, 5)

            self.outerLayout.addLayout(self.leftLayout, 4)
            self.outerLayout.addLayout(self.rightLayout, 6)

        def __createHeader(self):
            inputFieldName = QLabel("Input Field")
            inputFieldName.setAlignment(Qt.AlignCenter)
            self.topLeftLayout.addWidget(inputFieldName)
            outputFieldName = QLabel("Output Field")
            outputFieldName.setAlignment(Qt.AlignCenter)
            self.topRightLayout.addWidget(outputFieldName)
        
        def __powerSpeedEnter(self):
            self.currentSetPointLayout.addWidget(QLabel("Enter Current Set Point: "), 8)
            self.setPointEnterBox = QLineEdit(str(self.modelInput.currentSetPoint))
            self.setPointEnterBox.textChanged[str].connect(self.setPointTextUpdate)
            self.currentSetPointLayout.addWidget(self.setPointEnterBox)

            speedEnterLabel = QLabel("Enter Desired Speed: ")
            self.powerSpeedEnterLabelLayout.addWidget(speedEnterLabel)

            self.speedEnterBox = QLineEdit(str(self.modelInput.commandSetPoint))
            self.speedEnterBox.textChanged[str].connect(self.speedTextUpdate)
            self.powerSpeedEnterTextLayout.addWidget(self.speedEnterBox)
        
        def __outputList(self):
            self.outputFieldLeftLayout.addWidget(self.serviceBrake)
            self.outputFieldLeftLayout.addWidget(self.emergencyBrake)
            self.outputFieldLeftLayout.addWidget(self.leftSideDoors)
            self.outputFieldLeftLayout.addWidget(self.rightSideDoors)

            self.outputFieldRightLayout.addWidget(self.enginePower)
            self.outputFieldRightLayout.addWidget(self.insideLights)
            self.outputFieldRightLayout.addWidget(self.outsideLights)
            self.outputFieldRightLayout.addWidget(self.activateAnnouncement)
        
        def __toggleSection(self):
            brakesLabel = QLabel("Brake Failure")
            engineLabel = QLabel("Engine Failure")
            signalPickupFailureLabel = QLabel("Signal Pick Up Failure")
            self.toggleLeftLabelLayout.addWidget(brakesLabel)
            self.toggleLeftLabelLayout.addWidget(engineLabel)
            self.toggleLeftLabelLayout.addWidget(signalPickupFailureLabel)

            self.brakeToggle = Toggle(checked_color="#00FF00")
            self.brakeToggle.toggled.connect(self.__brakeFailureToggle)
            self.engineToggle = Toggle(checked_color="#00FF00")
            self.engineToggle.toggled.connect(self.__engineFailureToggle)
            self.signalToggle = Toggle(checked_color="#00FF00")
            self.signalToggle.toggled.connect(self.__signalFailureToggle)
            self.toggleLeftButtonLayout.addWidget(self.brakeToggle)
            self.toggleLeftButtonLayout.addWidget(self.engineToggle)
            self.toggleLeftButtonLayout.addWidget(self.signalToggle)
        
        def __stationSelect(self):
            if self.trainLine == 0:
                self.stationSelect.addItems(["YARD", "SHADYSIDE", "HERRON AVE", "SWISSVALE", "PENN STATION", "STEEL PLAZA", "FIRST AVE", "STATION SQUARE", "SOUTH HILLS JUNCTION"])
            else:
                self.stationSelect.addItems(["YARD", "GLENBURY", "DORMONT", "MT LEBANON", "POPLAR", "CASTLE SHANNON", "OVERBROOK", "INGLEWOOD", "CENTRAL", "WHITED", "SOUTH BANK", "STATION", "EDGEBROOK", "PIONEER"])
            self.stationSelect.currentTextChanged.connect(self.__updateStationData)
        
        def update(self):
            readTrainModelOutputFile(self.outputFileName, self.lockOutputFile, self.modelOutput)
            self.updateOutputWidgets()
            writeTrainModelInputFile(self.inputFileName, self.lockInputFile, self.modelInput)
            self.updateInputWidgetsOut()
        
        def createOutputWidgets(self):
            self.serviceBrake = QLabel()
            self.enginePower = QLabel()
            self.emergencyBrake = QLabel()
            self.leftSideDoors = QLabel()
            self.rightSideDoors = QLabel()
            self.announceStop = QLabel()
            self.insideLights = QLabel()
            self.outsideLights = QLabel()
            self.activateAnnouncement = QLabel()

        def updateOutputWidgets(self):
            self.serviceBrake.setText("Service Brake: " + str(self.modelOutput.serviceBrake))
            self.enginePower.setText("Engine Power: " + str(int(self.modelOutput.enginePower)) + " W")
            self.emergencyBrake.setText("Emergency Brake: " + str(self.modelOutput.emergencyBrake))
            self.leftSideDoors.setText("Left Side Doors: " + str(self.modelOutput.leftSideDoors))
            self.rightSideDoors.setText("Right Side Doors: " + str(self.modelOutput.rightSideDoors))
            self.announceStop.setText("Announce Stop: " + str(self.modelOutput.announceStop))
            self.insideLights.setText("Inside Lights: " + str(self.modelOutput.insideLights))
            self.outsideLights.setText("Outside Lights: " + str(self.modelOutput.outsideLights))
            self.activateAnnouncement.setText("Activate Announcement: " + str(self.modelOutput.activateAnnouncement))
        
        def createInputWidgets(self):
            self.commandSetPoint = QLabel()
            self.authority = QLabel()
            self.currentSetPoint = QLabel()
            self.brakeFailure = QLabel()
            self.signalPickupFailure = QLabel()
            self.engineFailure = QLabel()
            self.authorityToggle = Toggle(checked_color="#00FF00")
            self.authorityToggle.toggled.connect(self.__authorityToggle)
            self.stationLabel = QLabel()
            self.stationSelect = QComboBox()
        
        def updateInputWidgetsOut(self):
            self.commandSetPoint.setText("Command Set Point: " + str(int(self.modelInput.commandSetPoint)) + " m/s")
            self.authority.setText("Authority: " + str(self.modelInput.authority))
            self.currentSetPoint.setText("Current Set Point: " + str(int(self.modelInput.currentSetPoint)) + " m/s")
            self.brakeFailure.setText("Brake Failure: " + str(self.modelInput.brakeFailure))
            self.signalPickupFailure.setText("Signal Pickup Failure: " + str(self.modelInput.signalPickupFailure))
            self.engineFailure.setText("Engine Failure: " + str(self.modelInput.engineFailure))
            self.stationLabel.setText("Last Passed Station: " + str(self.modelInput.stationName))
        
        def speedTextUpdate(self, text):
            try:
                self.modelInput.commandSetPoint = float(text)
            except ValueError:
                self.modelInput.commandSetPoint = self.modelInput.commandSetPoint
        
        def setPointTextUpdate(self, text):
            try:
                self.modelInput.currentSetPoint = float(text)
            except ValueError:
                self.modelInput.currentSetPoint = self.modelInput.currentSetPoint
    
        def __authorityToggle(self):
            self.modelInput.authority = self.authorityToggle.isChecked()
        
        def __brakeFailureToggle(self):
            self.modelInput.brakeFailure = self.brakeToggle.isChecked()
        
        def __engineFailureToggle(self):
            self.modelInput.engineFailure = self.engineToggle.isChecked()
        
        def __signalFailureToggle(self):
            self.modelInput.signalPickupFailure = self.signalToggle.isChecked()
        
        def __updateStationData(self, s):
            self.modelInput.stationName = s

def testUI(train, lockOutputFile, lockInputFile):
    app = QApplication([])
    window = MainWindow(train, lockOutputFile, lockInputFile)
    fps = 15
    timer = QTimer()
    timer.timeout.connect(window.update)
    timer.setInterval(int(1000 / fps))
    timer.start()
    window.show()
    app.exec()
