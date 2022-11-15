def connect_train_model_train_controller(train_controller, train_model):
    command_set_point = train_model.commanded_speed
    authority = train_model.commanded_authority[0:4] == 'True'
    current_set_point = train_model.velocity
    brake_failure = train_model.brake_failure
    engine_failure = train_model.engine_failure
    signal_failure = train_model.signal_failure
    station_name = "YARD"

    train_controller.set_train_model_input(command_set_point, authority, current_set_point, brake_failure, signal_failure, engine_failure, station_name)
    train_controller.update()
    service_brake, engine_power, emergency_brake, left_side_doors, right_side_doors, announce_stop, inside_lights, outside_lights, activate_announcement = train_controller.get_train_model_output()
    train_model.service_brake = service_brake
    train_model.engine_power = engine_power
    train_model.emergency_brake = emergency_brake
    train_model.left_doors_opened = left_side_doors
    train_model.right_doors_opened = right_side_doors
    #PA link
    train_model.interior_lights = inside_lights
    train_model.exterior_lights = outside_lights
    #PA Link