from trainController import TrainController
import time
from multiprocessing import Process

def normalVibe(newTrain):
    while(1):
        newTrain.update()

def rideTheRedLine(newTrain):
    while(1):
        newTrain.beaconCall("SHADYSIDE")
        newTrain.update()
        time.sleep(3)
        newTrain.beaconCall("HERRON AVE")
        newTrain.update()
        time.sleep(3)
        newTrain.beaconCall("SWISSVALE")
        newTrain.update()
        time.sleep(3)
        newTrain.beaconCall("PENN STATION")
        newTrain.update()
        time.sleep(3)
        newTrain.beaconCall("STEEL PLAZA")
        newTrain.update()
        time.sleep(3)
        newTrain.beaconCall("FIRST AVE")
        newTrain.update()
        time.sleep(3)
        newTrain.beaconCall("STATION SQUARE")
        newTrain.update()
        time.sleep(3)
        newTrain.beaconCall("SOUTH HILLS JUNCTION")
        newTrain.update()
        time.sleep(3)

def greenLineSpeedSucks(newTrain):
    while(1):
        newTrain.beaconCall("STATION")
        for i in range(0, 1000000):
            newTrain.update()

if __name__ == "__main__":
    normalTrain = TrainController(1, 1)
    # redLineTrain = TrainController(2, 0)
    # greenLineTrain = TrainController(3, 1)

    normalTrain.startDriverUI()
    normalTrain.startTestUI()

    while(1):
        normalTrain.update()

    # redLineTrain.startDriverUI()
    # redLineTrain.startTestUI()

    # greenLineTrain.startDriverUI()
    # greenLineTrain.startTestUI()

    # normalProcess = Process(target=normalVibe, args=(normalTrain,))
    # redLineProcess = Process(target=rideTheRedLine, args=(redLineTrain,))
    # greenLineTrain = Process(target=greenLineSpeedSucks, args=(greenLineTrain,))

    # normalProcess.start()
    # redLineProcess.start()
    # greenLineTrain.start()