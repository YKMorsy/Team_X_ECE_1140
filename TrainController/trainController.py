from dataclasses import dataclass
import os
from input import *
from input.trainDriverInput import TrainDriverInput
from input.trainModelInput import TrainModelInput
from input.passengerInput import PassengerInput
from input.engineerInput import EngineerInput
from output.trainDriverOutput import TrainDriverOutput
from output.trainModelOutput import TrainModelOutput
from resources.findSpeedLimit import *
from ui.testUIFiles.testUI import testUI
from ui.driverUIFiles.trainDriverUI import driverUI
from multiprocessing import Process
from multiprocessing import Lock
from ui.support.readAndWriteFiles import readDriverInputFile, writeDriverInputFile, writeDriverOutputFile, writeTrainModelInputFile, writeTrainModelOutputFile, readTrainModelInputFile
from ui.support.readAndWriteFiles import readEngineerInputFile
from ui.support.readAndWriteFiles import writeEngineerInputFile

class TrainController:
    def __init__(self, trainNumber, trainLine):
        self.lockDriverInput = Lock()
        self.lockDriverOutput = Lock()
        self.lockModelInput= Lock()
        self.lockModelOutput = Lock()
        self.lockEngineerInput = Lock()

        self.trainNumber = trainNumber
        self.trainLine = trainLine
        self.testUIStart = False
        self.driverUIStart = False
        self.maxPower = 120000

        self.commandSetPoint = 0.0
        self.power = 0.0
        self.serviceBrakes = False
        self.emergencyBrakes = False
        self.leftSideDoors = False
        self.rightSideDoors = False
        self.announceStop = False
        self.insideLights = False
        self.outsideLights = False
        self.activateAnnouncment = False

        self.authority = False
        self.speedLimit = 0.0
        self.uValue = 0.0
        self.eValue = 0.0
        self.timeStep = 1.0

        self.lastStation = "YARD"
        self.nextStation = ""
        self.direction = 0
        self.distance = 0.0

        self.trainDriverInput = TrainDriverInput()
        self.trainModelInput = TrainModelInput()
        self.passengerInput = PassengerInput()
        self.engineerInput = EngineerInput()
        self.trainDriverOutput = TrainDriverOutput()
        self.trainModelOutput = TrainModelOutput()

        self.inputModelTestUIFileName = "./ui/testUIFiles/utilities/modelInputDB_" + str(self.trainNumber) + ".txt"
        self.outputModelTestUIFileName = "./ui/testUIFiles/utilities/modelOutputDB_" + str(self.trainNumber) + ".txt"
        self.inputDriverDriverUIFileName = "./ui/driverUIFiles/utilities/driverInputDB_" + str(self.trainNumber) + ".txt"
        self.outputDriverDriverUIFileName = "./ui/driverUIFiles/utilities/driverOutputDB_" + str(self.trainNumber) + ".txt"
        self.inputEngineerUIFileName = "./ui/driverUIFiles/utilities/engineerInputDB_" + str(trainNumber) + ".txt"

        writeDriverInputFile(self.inputDriverDriverUIFileName, self.lockDriverInput, self.trainDriverInput)
        writeDriverOutputFile(self.outputDriverDriverUIFileName, self.lockDriverOutput, self.trainDriverOutput)
        writeTrainModelInputFile(self.inputModelTestUIFileName, self.lockModelInput, self.trainModelInput)
        writeTrainModelOutputFile(self.outputModelTestUIFileName, self.lockModelOutput, self.trainModelOutput)
        writeEngineerInputFile(self.inputEngineerUIFileName, self.lockEngineerInput, self.engineerInput.Kp, self.engineerInput.Ki)

    def startTestUI(self):
        self.testUIStart = True
        testUIProcess = Process(target=testUI, args=(self, self.lockModelOutput, self.lockModelInput))
        testUIProcess.start()
    
    def startDriverUI(self):
        self.driverUIStart = True
        driverUIProcess = Process(target=driverUI, args=(self, self.lockDriverOutput, self.lockDriverInput, self.lockEngineerInput))
        driverUIProcess.start()
    
    def __driverOutputMapper(self):
        self.trainDriverOutput.currentSetPoint = self.trainModelInput.currentSetPoint
        self.trainDriverOutput.speedLimit = self.speedLimit
        self.trainDriverOutput.interiorTemperature = self.trainDriverInput.interiorTemperatureControl
        if(self.trainDriverInput.manualMode):
            self.trainDriverOutput.commandSetPoint = self.trainDriverInput.commandSetPoint
        else:
            self.trainDriverOutput.commandSetPoint = self.trainModelInput.commandSetPoint    
        self.trainDriverOutput.brakeFailure = self.trainModelInput.brakeFailure
        self.trainDriverOutput.engineFailure = self.trainModelInput.engineFailure
        self.trainDriverOutput.wheelFailure = False
        self.trainDriverOutput.signalPickUpFailure = self.trainModelInput.signalPickupFailure
        self.trainDriverOutput.authority = self.trainModelInput.authority and self.authority
        self.trainDriverOutput.nextStop = self.nextStation

    def __modelOutputMapper(self):
        self.trainModelOutput.serviceBrake = self.trainDriverInput.serviceBrake or self.serviceBrakes
        self.trainModelOutput.emergencyBrake = self.trainDriverInput.emergencyBrake or self.emergencyBrakes
        self.trainModelOutput.enginePower = self.power
        self.trainModelOutput.leftSideDoors = self.trainDriverInput.leftSideDoors or self.leftSideDoors                                
        self.trainModelOutput.rightSideDoors = self.trainDriverInput.rightSideDoors or self.rightSideDoors
        self.trainModelOutput.announceStop = self.announceStop
        self.trainModelOutput.insideLights = self.insideLights or self.trainDriverInput.insideLights
        self.trainModelOutput.outsideLights = self.outsideLights or self.trainDriverInput.outsideLights
        self.trainModelOutput.activateAnnouncement = self.trainDriverInput.activateAnnouncement or self.activateAnnouncment

    def __updateInternalValues(self):
        self.distance += self.trainModelInput.currentSetPoint * self.timeStep
        if self.lastStation != self.trainModelInput.stationName:
            self.beaconCall(self.trainModelInput.stationName)
        self.__getSpeedLimit()

        if self.trainDriverInput.manualMode:
            self.commandSetPoint = self.trainDriverInput.commandSetPoint
        else:
            self.commandSetPoint = self.trainModelInput.commandSetPoint    
        if self.commandSetPoint > self.speedLimit:
            self.commandSetPoint = self.speedLimit
        
        if self.authority and not self.serviceBrakes and not self.emergencyBrakes:
            self.__calculatePower()

        if self.power > self.maxPower:
            self.power = self.maxPower
        
        if self.trainModelInput.currentSetPoint > self.speedLimit * 0.277778:
            self.power = 0.0
            self.serviceBrakes = True
        else:
            self.serviceBrakes = self.trainDriverInput.serviceBrake
        
        self.authority = self.trainModelInput.authority and not(self.trainModelInput.brakeFailure or self.trainModelInput.signalPickupFailure or self.trainModelInput.engineFailure)
        
        if not self.authority:
            self.power = 0.0
            self.emergencyBrakes = True
        else:
            self.emergencyBrakes = self.trainDriverInput.emergencyBrake or self.passengerInput.emergencyBrake

        if self.serviceBrakes or self.emergencyBrakes:
            self.power = 0.0
            
    def __calculatePower(self):
        if self.power < self.maxPower:
            self.uValue = self.uValue + (self.timeStep / 2 * (self.commandSetPoint - self.trainModelInput.currentSetPoint + self.eValue))
            if(self.uValue  < 0):
                self.uValue = 0
        self.power = self.engineerInput.Kp * (self.commandSetPoint - self.trainModelInput.currentSetPoint) + self.engineerInput.Ki * self.uValue
        if self.power < 0:
            self.power = 0

    def __getSpeedLimit(self):
        if self.trainLine == 0:
            self.speedLimit, self.direction, self.nextStation, self.outsideLights, self.insideLights = getSpeedLimitRed(self.lastStation, self.direction, self.distance)
        else:
            self.speedLimit, self.direction, self.nextStation, self.outsideLights, self.insideLights = getSpeedLimitGreen(self.lastStation, self.direction, self.distance)

    def beaconCall(self, station):
        self.lastStation = station
        self.distance = 0
    
    def update(self):
        self.eValue = self.commandSetPoint - self.trainModelInput.currentSetPoint

        if(self.testUIStart):
            writeTrainModelOutputFile(self.outputModelTestUIFileName, self.lockModelOutput, self.trainModelOutput)
            readTrainModelInputFile(self.inputModelTestUIFileName, self.lockModelInput, self.trainModelInput)
        if(self.driverUIStart):
            writeDriverOutputFile(self.outputDriverDriverUIFileName, self.lockDriverOutput, self.trainDriverOutput)
            readDriverInputFile(self.inputDriverDriverUIFileName, self.lockDriverInput, self.trainDriverInput)
            self.engineerInput.Kp, self.engineerInput.Ki = readEngineerInputFile(self.inputEngineerUIFileName, self.lockEngineerInput)
        
        self.__updateInternalValues()
        self.__driverOutputMapper()
        self.__modelOutputMapper()