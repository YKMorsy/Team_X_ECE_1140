from TrainController.trainController import TrainController
from TrainModel.TrainModel import TrainModel
from TrainModel.common import *
from connect_train_model_train_controller import connect_train_model_train_controller

if __name__ == '__main__':
    train_controller = TrainController(1,1)
    train_driver_input = train_controller.get_driver_input()
    train_model_handler = TrainModelHandler(train_info_model)
    train_model_handler.create_train(ID = 1, mass = 40.9, crew_count=2, passenger_capacity=222, speed_limit=43.50, acceleration_limit=3.00,
    service_deceleration=3.94, emergency_deceleration=8.96, max_engine_power=480000, length=106, height=11.2, width = 8.69, car_count=1)

    #Service Brakes
    train_driver_input.service_brake = True
    train_controller.set_train_driver_input(train_driver_input)
    connect_train_model_train_controller(train_controller, train_model_handler.train_list[1])
    train_model_handler.update(1)
    assert train_model_handler.train_list[1].service_brake
    train_driver_input.service_brake = False

    #Emergency Brakes
    train_driver_input.emergency_brake = True
    train_controller.set_train_driver_input(train_driver_input)
    connect_train_model_train_controller(train_controller, train_model_handler.train_list[1])
    train_model_handler.update(1)
    assert train_model_handler.train_list[1].emergency_brake
    train_driver_input.emergency_brake = False

    #Interior Lights
    train_driver_input.inside_lights = True
    train_controller.set_train_driver_input(train_driver_input)
    connect_train_model_train_controller(train_controller, train_model_handler.train_list[1])
    train_model_handler.update(1)
    assert train_model_handler.train_list[1].interior_lights
    train_driver_input.inside_lights = False

    #Exterior Lights
    train_driver_input.outside_lights = True
    train_controller.set_train_driver_input(train_driver_input)
    connect_train_model_train_controller(train_controller, train_model_handler.train_list[1])
    train_model_handler.update(1)
    assert train_model_handler.train_list[1].exterior_lights
    train_driver_input.outside_lights = False

    #Power
    train_model_handler.train_list[1].commanded_speed = 10
    train_model_handler.train_list[1].commanded_authority = "True"
    connect_train_model_train_controller(train_controller, train_model_handler.train_list[1])
    train_model_handler.update(1)
    assert train_model_handler.train_list[1].engine_power > 0
    old_power = train_model_handler.train_list[1].engine_power
    connect_train_model_train_controller(train_controller, train_model_handler.train_list[1])
    train_model_handler.update(1)
    assert train_model_handler.train_list[1].engine_power > old_power

