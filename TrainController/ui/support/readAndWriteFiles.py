def readDriverInputFile(inputFileName, lockDriverInput, trainDriverInput):
    lockDriverInput.acquire()
    inputFile = open(inputFileName, "r")

    trainDriverInput.commandSetPoint = float(inputFile.readline())
    trainDriverInput.serviceBrake = inputFile.readline()[0:4] == 'True'
    trainDriverInput.emergencyBrake = inputFile.readline()[0:4] == 'True'
    trainDriverInput.manualMode = inputFile.readline()[0:4] == 'True'
    trainDriverInput.interiorTemperatureControl = int(inputFile.readline())
    trainDriverInput.insideLights = inputFile.readline()[0:4] == 'True'
    trainDriverInput.outsideLights = inputFile.readline()[0:4] == 'True'
    trainDriverInput.rightSideDoors = inputFile.readline()[0:4] == 'True'
    trainDriverInput.leftSideDoors = inputFile.readline()[0:4] == 'True'
    trainDriverInput.activateAnnouncement = inputFile.readline()[0:4] == 'True'

    inputFile.close()
    lockDriverInput.release()

def readDriverOutputFile(outputFileName, lockOutputFile, driverOutput):
    lockOutputFile.acquire()

    outputFile = open(outputFileName, "r")
    driverOutput.currentSetPoint = float(outputFile.readline())
    driverOutput.speedLimit = float(outputFile.readline())
    driverOutput.interiorTemperature = int(outputFile.readline())
    driverOutput.commandSetPoint = float(outputFile.readline())
    driverOutput.brakeFailure = outputFile.readline()[0:4] == 'True'
    driverOutput.engineFailure = outputFile.readline()[0:4] == 'True'
    driverOutput.wheelFailure = outputFile.readline()[0:4] == 'True'
    driverOutput.signalPickUpFailure = outputFile.readline()[0:4] == 'True'
    driverOutput.authority = outputFile.readline()[0:4] == 'True'
    driverOutput.nextStop = outputFile.readline().strip()

    outputFile.close()
    lockOutputFile.release()

def writeDriverInputFile(inputFileName, lockInputFile, driverInput):
    lockInputFile.acquire()
    inputFile = open(inputFileName, "w")

    inputFile.write(str(driverInput.commandSetPoint) + "\n")
    inputFile.write(str(driverInput.serviceBrake) + "\n")
    inputFile.write(str(driverInput.emergencyBrake) + "\n")
    inputFile.write(str(driverInput.manualMode) + "\n")
    inputFile.write(str(driverInput.interiorTemperatureControl) + "\n") 
    inputFile.write(str(driverInput.insideLights) + "\n")
    inputFile.write(str(driverInput.outsideLights) + "\n")
    inputFile.write(str(driverInput.rightSideDoors) + "\n")
    inputFile.write(str(driverInput.leftSideDoors) + "\n")
    inputFile.write(str(driverInput.activateAnnouncement) + "\n")
    inputFile.close()
    lockInputFile.release()

def writeDriverOutputFile(outputFileName, lockDriverOutput, trainDriverOutput):
    lockDriverOutput.acquire()
    outputFile = open(outputFileName, "w")

    outputFile.write(str(trainDriverOutput.currentSetPoint) + "\n")
    outputFile.write(str(trainDriverOutput.speedLimit) + "\n")
    outputFile.write(str(trainDriverOutput.interiorTemperature) + "\n")
    outputFile.write(str(trainDriverOutput.commandSetPoint) + "\n")
    outputFile.write(str(trainDriverOutput.brakeFailure) + "\n")
    outputFile.write(str(trainDriverOutput.engineFailure) + "\n")
    outputFile.write(str(trainDriverOutput.wheelFailure) + "\n")
    outputFile.write(str(trainDriverOutput.signalPickUpFailure) + "\n")
    outputFile.write(str(trainDriverOutput.authority) + "\n")
    outputFile.write(str(trainDriverOutput.nextStop) + "\n")

    outputFile.close()
    lockDriverOutput.release()

def readTrainModelInputFile(inputFileName, lockModelInput, trainModelInput):
    lockModelInput.acquire()
    inputFile = open(inputFileName, "r")

    trainModelInput.commandSetPoint = float(inputFile.readline())
    trainModelInput.authority = inputFile.readline()[0:4] == 'True'
    trainModelInput.currentSetPoint = float(inputFile.readline())
    trainModelInput.brakeFailure = inputFile.readline()[0:4] == 'True'
    trainModelInput.signalPickupFailure = inputFile.readline()[0:4] == 'True'
    trainModelInput.engineFailure = inputFile.readline()[0:4] == 'True'
    trainModelInput.stationName = inputFile.readline().strip()

    inputFile.close()
    lockModelInput.release()

def readTrainModelOutputFile(outputFileName, lockModelOutput, trainModelOutput):
    lockModelOutput.acquire()
    outputFile = open(outputFileName, "r")

    trainModelOutput.serviceBrake = outputFile.readline()[0:4] == 'True'
    trainModelOutput.enginePower = float(outputFile.readline())
    trainModelOutput.emergencyBrake = outputFile.readline()[0:4] == 'True'
    trainModelOutput.leftSideDoors = outputFile.readline()[0:4] == 'True'
    trainModelOutput.rightSideDoors = outputFile.readline()[0:4] == 'True'
    trainModelOutput.announceStop = outputFile.readline()[0:4] == 'True'
    trainModelOutput.insideLights = outputFile.readline()[0:4] == 'True'
    trainModelOutput.outsideLights = outputFile.readline()[0:4] == 'True'
    trainModelOutput.activateAnnouncement = outputFile.readline()[0:4] == 'True'

    outputFile.close()
    lockModelOutput.release()

def writeTrainModelInputFile(inputFileName, lockModelInput, trainModelInput):
    lockModelInput.acquire()
    inputFile = open(inputFileName, "w")

    inputFile.write(str(trainModelInput.commandSetPoint) + "\n")
    inputFile.write(str(trainModelInput.authority) + "\n")
    inputFile.write(str(trainModelInput.currentSetPoint) + "\n")
    inputFile.write(str(trainModelInput.brakeFailure) + "\n")
    inputFile.write(str(trainModelInput.signalPickupFailure) + "\n")
    inputFile.write(str(trainModelInput.engineFailure) + "\n")
    inputFile.write(str(trainModelInput.stationName) + "\n")

    inputFile.close()
    lockModelInput.release()

def writeTrainModelOutputFile(outputFileName, lockModelOutput, trainModelOutput):
    lockModelOutput.acquire()
    outputFile = open(outputFileName, "w")

    outputFile.write(str(trainModelOutput.serviceBrake) + "\n")
    outputFile.write(str(trainModelOutput.enginePower) + "\n")
    outputFile.write(str(trainModelOutput.emergencyBrake) + "\n")
    outputFile.write(str(trainModelOutput.leftSideDoors) + "\n")
    outputFile.write(str(trainModelOutput.rightSideDoors) + "\n")
    outputFile.write(str(trainModelOutput.announceStop) + "\n")
    outputFile.write(str(trainModelOutput.insideLights) + "\n")
    outputFile.write(str(trainModelOutput.outsideLights) + "\n")
    outputFile.write(str(trainModelOutput.activateAnnouncement) + "\n")

    outputFile.close()
    lockModelOutput.release()

def readEngineerInputFile(outputFileName, lockEngineerInput):
    lockEngineerInput.acquire()
    outputFile = open(outputFileName, "r")

    kp = float(outputFile.readline())
    ki = float(outputFile.readline())

    outputFile.close()
    lockEngineerInput.release()
    return kp, ki

def writeEngineerInputFile(outputFileName, lockEngineerInput, kp, ki):
    lockEngineerInput.acquire()
    outputFile = open(outputFileName, "w")

    outputFile.write(str(kp) + "\n")
    outputFile.write(str(ki) + "\n")

    outputFile.close()
    lockEngineerInput.release()