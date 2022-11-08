from trainController import TrainController
import time
if __name__ == "__main__":
    normalTrain = TrainController(1, 1)
    # redLineTrain = TrainController(2, 0)

    normalTrain.start_driver_ui()
    normalTrain.start_test_ui()
    # redLineTrain.startDriverUI()
    # redLineTrain.startTestUI()

    while(1):
        normalTrain.update()
        # redLineTrain.update()
