from trainController import TrainController

if __name__ == "__main__":
    normalTrain = TrainController(1, 1)
    redLineTrain = TrainController(2, 0)
    # redLineTrain = TrainController(2, 0)
    # greenLineTrain = TrainController(3, 1)

    normalTrain.startDriverUI()
    normalTrain.startTestUI()
    redLineTrain.startDriverUI()
    redLineTrain.startTestUI()

    while(1):
        normalTrain.update()
        redLineTrain.update()
