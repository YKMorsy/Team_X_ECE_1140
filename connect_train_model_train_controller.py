import random

def connect_train_model_train_controller(train_controller, train_model):
    command_set_point = float(train_model.commanded_speed) * 0.277778
    authority = train_model.commanded_authority[0:4] == 'True'
    current_set_point = train_model.velocity
    brake_failure = train_model.brake_failure
    engine_failure = train_model.engine_failure
    signal_failure = train_model.signal_failure
    
    if len(train_model.beacon_data) > 0:
        for station_data in train_model.beacon_data.values():
            station_name = station_data[0][0]
    else:
        station_name = "N/A"

    train_controller.set_train_model_input(command_set_point, authority, current_set_point, brake_failure, signal_failure, engine_failure, station_name)
    train_controller.update()
    service_brake, engine_power, emergency_brake, left_side_doors, right_side_doors, announce_stop, inside_lights, outside_lights, activate_announcement, current_stop, play_ad = train_controller.get_train_model_output()

    if ((left_side_doors and not train_model.left_doors_opened) or (right_side_doors and not train_model.right_doors_opened)):
        train_model.passenger_count -= random.randint(0,train_model.passenger_count)
        passengers_to_add = train_model.track_model.get_passengers(train_model.passenger_capacity - train_model.passenger_count)
        train_model.passenger_count += passengers_to_add

    train_model.service_brake = service_brake
    train_model.engine_power = engine_power
    train_model.emergency_brake = emergency_brake
    train_model.left_doors_opened = left_side_doors
    train_model.right_doors_opened = right_side_doors
    #PA link
    train_model.interior_lights = inside_lights
    train_model.exterior_lights = outside_lights
    train_model.activate_anouncement = activate_announcement
    train_model.announce_stop = announce_stop
    train_model.play_ad = play_ad
    train_model.current_stop = current_stop
    #PA Link