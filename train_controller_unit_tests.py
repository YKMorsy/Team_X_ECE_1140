from TrainController.trainController import TrainController

if __name__ == '__main__':
    # Green Line Train
    greenTrain = TrainController(1, 1)
    train_driver_input = greenTrain.get_driver_input()
    train_driver_output = greenTrain.get_driver_output()
    train_model_input = greenTrain.get_model_input()
    train_model_output = greenTrain.get_model_output()

    # Test Service Brake
    train_driver_input.service_brake = True
    greenTrain.update()
    assert(train_model_output.service_brake)
    train_driver_input.service_brake = False

    #Test Emergency Brake
    train_driver_input.emergency_brake = True
    greenTrain.update()
    assert(train_model_output.emergency_brake)
    train_driver_input.emergency_brake = False

    #Test Inside Lights
    train_driver_input.inside_lights = True
    greenTrain.update()
    assert(train_model_output.inside_lights)
    train_driver_input.inside_lights = False

    #Test Outside Lights
    train_driver_input.outside_lights = True
    greenTrain.update()
    assert(train_model_output.outside_lights)
    train_driver_input.outside_lights = False

    #Test Right Doors
    train_driver_input.right_side_doors = True
    greenTrain.update()
    assert(train_model_output.right_side_doors)
    train_driver_input.right_side_doors = False

    #Test Left Side Doors
    train_driver_input.left_side_doors = True
    greenTrain.update()
    assert(train_model_output.left_side_doors)
    train_driver_input.left_side_doors = False

    #Test current set point < command set point
    train_model_input.command_set_point = 10
    train_model_input.authority = True
    greenTrain.update()
    assert(train_model_output.engine_power > 0)
    train_model_input.command_set_point = 0
    train_model_input.authority = False

    #Test current set point > command set point
    train_model_input.command_set_point = 5
    train_model_input.authority = True
    train_model_input.current_set_point = 10
    greenTrain.update()
    assert(train_model_output.service_brake and train_model_output.engine_power == 0)
    train_model_input.command_set_point = 0
    train_model_input.authority = False
    train_model_input.current_set_point = 0

    #Test authority of 0
    train_model_input.command_set_point = 5
    train_model_input.authority = False
    greenTrain.update()
    assert(train_model_output.engine_power == 0 and train_model_output.service_brake)
    train_model_input.command_set_point = 0

    #Test faults
    train_model_input.command_set_point = 10
    train_model_input.current_set_point = 5
    train_model_input.authority = True
    greenTrain.update()

    #Engine Failure
    train_model_input.engine_failure = True
    greenTrain.update()
    assert(train_model_output.emergency_brake and train_model_output.engine_power == 0)
    train_model_input.engine_failure = False
    greenTrain.update()

    #Brake Failure
    train_model_input.brake_failure = True
    greenTrain.update()
    assert(train_model_output.emergency_brake and train_model_output.engine_power == 0)
    train_model_input.brake_failure = False
    greenTrain.update()

    #Signal Failure
    train_model_input.signal_pickup_failure = True
    greenTrain.update()
    assert(train_model_output.emergency_brake and train_model_output.engine_power == 0)
    train_model_input.signal_pickup_failure = False
    greenTrain.update()

    train_model_input.command_set_point = 0
    train_model_input.current_set_point = 0
    train_model_input.authority = False

    #Test edge cases
    train_model_input.command_set_point = -50
    greenTrain.update()
    assert(train_model_input.command_set_point == 0)

    train_model_input.current_set_point = -50
    greenTrain.update()
    assert(train_model_input.current_set_point == 0)