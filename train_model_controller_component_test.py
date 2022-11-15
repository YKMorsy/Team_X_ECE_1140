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
    connect_train_model_train_controller(train_controller, train_model_handler.train_list[1])
    train_model_handler.update(1)
    assert train_model_handler.train_list[1].service_brake
    train_driver_input.service_brake = False

    #Emergency Brakes
    train_driver_input.emergency_brake = True
    connect_train_model_train_controller(train_controller, train_model_handler.train_list[1])
    train_model_handler.update(1)
    assert train_model_handler.train_list[1].emergency_brake
    train_driver_input.emergency_brake = False

    #Interior Lights
    train_driver_input.inside_lights = True
    connect_train_model_train_controller(train_controller, train_model_handler.train_list[1])
    train_model_handler.update(1)
    assert train_model_handler.train_list[1].interior_lights
    train_driver_input.inside_lights = False

    #Exterior Lights
    train_driver_input.outside_lights = True
    connect_train_model_train_controller(train_controller, train_model_handler.train_list[1])
    train_model_handler.update(1)
    assert train_model_handler.train_list[1].exterior_lights
    train_driver_input.outside_lights = False

    #Right side doors
    train_driver_input.right_side_doors = True
    connect_train_model_train_controller(train_controller, train_model_handler.train_list[1])
    train_model_handler.update(1)
    assert train_model_handler.train_list[1].right_doors_opened
    train_driver_input.right_side_doors = True

    #Left side doors
    train_driver_input.left_side_doors = True
    connect_train_model_train_controller(train_controller, train_model_handler.train_list[1])
    train_model_handler.update(1)
    assert train_model_handler.train_list[1].left_doors_opened
    train_driver_input.left_side_doors = True

    #Power
    train_model_handler.train_list[1].commanded_speed = 10
    train_model_handler.train_list[1].commanded_authority = "True"
    connect_train_model_train_controller(train_controller, train_model_handler.train_list[1])
    train_model_handler.update(1)
    assert train_model_handler.train_list[1].engine_power > 0
    for i in range(100):
        connect_train_model_train_controller(train_controller, train_model_handler.train_list[1])
        train_model_handler.update(1)
        assert train_model_handler.train_list[1].velocity <= train_model_handler.train_list[1].commanded_speed
    
    #Service brake with speed
    train_driver_input.service_brake = True
    old_velocity = train_model_handler.train_list[1].velocity
    connect_train_model_train_controller(train_controller, train_model_handler.train_list[1])
    train_model_handler.update(1)
    assert train_model_handler.train_list[1].velocity < old_velocity
    while(train_model_handler.train_list[1].velocity > 0):
        connect_train_model_train_controller(train_controller, train_model_handler.train_list[1])
        train_model_handler.update(1)
    assert train_model_handler.train_list[1].velocity == 0
    train_driver_input.service_brake = False

    #Emergency brake with speed  
    connect_train_model_train_controller(train_controller, train_model_handler.train_list[1])
    train_model_handler.update(1)
    for i in range(15):
        connect_train_model_train_controller(train_controller, train_model_handler.train_list[1])
        train_model_handler.update(1)
    
    train_driver_input.emergency_brake = True
    old_velocity = train_model_handler.train_list[1].velocity
    connect_train_model_train_controller(train_controller, train_model_handler.train_list[1])
    train_model_handler.update(1)
    assert train_model_handler.train_list[1].velocity < old_velocity
    while(train_model_handler.train_list[1].velocity > 0):
        connect_train_model_train_controller(train_controller, train_model_handler.train_list[1])
        train_model_handler.update(1)
    assert train_model_handler.train_list[1].velocity == 0
    train_driver_input.emergency_brake = False

    #Brake Failure
    train_model_handler.train_list[1].brake_failure = True
    old_velocity = train_model_handler.train_list[1].velocity
    connect_train_model_train_controller(train_controller, train_model_handler.train_list[1])
    train_model_handler.update(1)
    assert train_model_handler.train_list[1].emergency_brake
    train_model_handler.train_list[1].brake_failure = False
    connect_train_model_train_controller(train_controller, train_model_handler.train_list[1])
    train_model_handler.update(1)
    assert not train_model_handler.train_list[1].emergency_brake

    #Engine Failure
    train_model_handler.train_list[1].engine_failure = True
    old_velocity = train_model_handler.train_list[1].velocity
    connect_train_model_train_controller(train_controller, train_model_handler.train_list[1])
    train_model_handler.update(1)
    assert train_model_handler.train_list[1].emergency_brake
    train_model_handler.train_list[1].engine_failure = False
    connect_train_model_train_controller(train_controller, train_model_handler.train_list[1])
    train_model_handler.update(1)
    assert not train_model_handler.train_list[1].emergency_brake

    #Signal Failure
    train_model_handler.train_list[1].signal_failure = True
    old_velocity = train_model_handler.train_list[1].velocity
    connect_train_model_train_controller(train_controller, train_model_handler.train_list[1])
    train_model_handler.update(1)
    assert train_model_handler.train_list[1].emergency_brake
    train_model_handler.train_list[1].signal_failure = False
    connect_train_model_train_controller(train_controller, train_model_handler.train_list[1])
    train_model_handler.update(1)
    assert not train_model_handler.train_list[1].emergency_brake

    #Authority to zero
    train_model_handler.train_list[1].commanded_speed = 10
    train_model_handler.train_list[1].commanded_authority = "True"
    for i in range(15):
        connect_train_model_train_controller(train_controller, train_model_handler.train_list[1])
        train_model_handler.update(1)
    
    train_model_handler.train_list[1].commanded_authority = "False"
    connect_train_model_train_controller(train_controller, train_model_handler.train_list[1])
    train_model_handler.update(1)
    assert train_model_handler.train_list[1].service_brake