from TrainController.trainController import TrainController
from TrainModel.TrainModel import TrainModel
from TrainModel.common import *
from connect_train_model_train_controller import connect_train_model_train_controller

if __name__ == '__main__':
    try:
        train_controller = TrainController(1,1)
        train_model_handler = TrainModelHandler(train_info_model)
        train_model_handler.create_train(ID = 1, mass = 40.9, crew_count=2, passenger_capacity=222, speed_limit=43.50, acceleration_limit=3.00,
        service_deceleration=3.94, emergency_deceleration=8.96, max_engine_power=480000, length=106, height=11.2, width = 8.69)

    except Exception as e:
        print("Ran into error: " + str(e))