def read_driver_input_file(input_file_name, lock_driver_input, train_driver_input):
    lock_driver_input.acquire()
    input_file = open(input_file_name, "r")

    train_driver_input.command_set_point = float(input_file.readline())
    train_driver_input.service_brake = input_file.readline()[0:4] == 'True'
    train_driver_input.emergency_brake = input_file.readline()[0:4] == 'True'
    train_driver_input.manual_mode = input_file.readline()[0:4] == 'True'
    train_driver_input.interior_temperature_control = int(input_file.readline())
    train_driver_input.inside_lights = input_file.readline()[0:4] == 'True'
    train_driver_input.outside_lights = input_file.readline()[0:4] == 'True'
    train_driver_input.right_side_doors = input_file.readline()[0:4] == 'True'
    train_driver_input.left_side_doors = input_file.readline()[0:4] == 'True'
    train_driver_input.activate_announcement = input_file.readline()[0:4] == 'True'

    input_file.close()
    lock_driver_input.release()

def read_driver_output_file(output_file_name, lock_output_file, driver_output):
    lock_output_file.acquire()

    output_file = open(output_file_name, "r")
    driver_output.current_set_point = float(output_file.readline())
    driver_output.speed_limit = float(output_file.readline())
    driver_output.interior_temperature = int(output_file.readline())
    driver_output.command_set_point = float(output_file.readline())
    driver_output.brake_failure = output_file.readline()[0:4] == 'True'
    driver_output.engine_failure = output_file.readline()[0:4] == 'True'
    driver_output.wheel_failure = output_file.readline()[0:4] == 'True'
    driver_output.signal_pickup_failure = output_file.readline()[0:4] == 'True'
    driver_output.authority = output_file.readline()[0:4] == 'True'
    driver_output.next_stop = output_file.readline().strip()
    driver_output.train_movement = output_file.readline()[0:4] == 'True'
    driver_output.power = float(output_file.readline())

    output_file.close()
    lock_output_file.release()

def write_driver_input_file(input_file_name, lockinput_file, driverInput):
    lockinput_file.acquire()
    input_file = open(input_file_name, "w")

    input_file.write(str(driverInput.command_set_point) + "\n")
    input_file.write(str(driverInput.service_brake) + "\n")
    input_file.write(str(driverInput.emergency_brake) + "\n")
    input_file.write(str(driverInput.manual_mode) + "\n")
    input_file.write(str(driverInput.interior_temperature_control) + "\n") 
    input_file.write(str(driverInput.inside_lights) + "\n")
    input_file.write(str(driverInput.outside_lights) + "\n")
    input_file.write(str(driverInput.right_side_doors) + "\n")
    input_file.write(str(driverInput.left_side_doors) + "\n")
    input_file.write(str(driverInput.activate_announcement) + "\n")
    input_file.close()
    lockinput_file.release()

def write_driver_output_file(output_file_name, lockdriver_output, traindriver_output):
    lockdriver_output.acquire()
    output_file = open(output_file_name, "w")

    output_file.write(str(traindriver_output.current_set_point) + "\n")
    output_file.write(str(traindriver_output.speed_limit) + "\n")
    output_file.write(str(traindriver_output.interior_temperature) + "\n")
    output_file.write(str(traindriver_output.command_set_point) + "\n")
    output_file.write(str(traindriver_output.brake_failure) + "\n")
    output_file.write(str(traindriver_output.engine_failure) + "\n")
    output_file.write(str(traindriver_output.wheel_failure) + "\n")
    output_file.write(str(traindriver_output.signal_pickup_failure) + "\n")
    output_file.write(str(traindriver_output.authority) + "\n")
    output_file.write(str(traindriver_output.next_stop) + "\n")
    output_file.write(str(traindriver_output.train_movement) + "\n")
    output_file.write(str(traindriver_output.power) + "\n")

    output_file.close()
    lockdriver_output.release()

def read_train_model_input_file(input_file_name, lock_model_input, train_model_input):
    lock_model_input.acquire()
    input_file = open(input_file_name, "r")

    train_model_input.command_set_point = float(input_file.readline())
    train_model_input.authority = input_file.readline()[0:4] == 'True'
    train_model_input.current_set_point = float(input_file.readline())
    train_model_input.brake_failure = input_file.readline()[0:4] == 'True'
    train_model_input.signal_pickup_failure = input_file.readline()[0:4] == 'True'
    train_model_input.engine_failure = input_file.readline()[0:4] == 'True'
    train_model_input.station_name = input_file.readline().strip()

    input_file.close()
    lock_model_input.release()

def read_train_model_output_file(output_file_name, lock_model_output, train_model_output):
    lock_model_output.acquire()
    output_file = open(output_file_name, "r")

    train_model_output.service_brake = output_file.readline()[0:4] == 'True'
    train_model_output.engine_power = float(output_file.readline())
    train_model_output.emergency_brake = output_file.readline()[0:4] == 'True'
    train_model_output.left_side_doors = output_file.readline()[0:4] == 'True'
    train_model_output.right_side_doors = output_file.readline()[0:4] == 'True'
    train_model_output.announce_stop = output_file.readline()[0:4] == 'True'
    train_model_output.inside_lights = output_file.readline()[0:4] == 'True'
    train_model_output.outside_lights = output_file.readline()[0:4] == 'True'
    train_model_output.activate_announcement = output_file.readline()[0:4] == 'True'
    train_model_output.current_stop = output_file.read_line().strip()
    train_model_output.play_ad = output_file.readline()[0:4] == 'True'

    output_file.close()
    lock_model_output.release()

def write_train_model_input_file(input_file_name, lock_model_input, train_model_input):
    lock_model_input.acquire()
    input_file = open(input_file_name, "w")

    input_file.write(str(train_model_input.command_set_point) + "\n")
    input_file.write(str(train_model_input.authority) + "\n")
    input_file.write(str(train_model_input.current_set_point) + "\n")
    input_file.write(str(train_model_input.brake_failure) + "\n")
    input_file.write(str(train_model_input.signal_pickup_failure) + "\n")
    input_file.write(str(train_model_input.engine_failure) + "\n")
    input_file.write(str(train_model_input.station_name) + "\n")

    input_file.close()
    lock_model_input.release()

def write_train_model_output_file(output_file_name, lock_model_output, train_model_output):
    lock_model_output.acquire()
    output_file = open(output_file_name, "w")

    output_file.write(str(train_model_output.service_brake) + "\n")
    output_file.write(str(train_model_output.engine_power) + "\n")
    output_file.write(str(train_model_output.emergency_brake) + "\n")
    output_file.write(str(train_model_output.left_side_doors) + "\n")
    output_file.write(str(train_model_output.right_side_doors) + "\n")
    output_file.write(str(train_model_output.announce_stop) + "\n")
    output_file.write(str(train_model_output.inside_lights) + "\n")
    output_file.write(str(train_model_output.outside_lights) + "\n")
    output_file.write(str(train_model_output.activate_announcement) + "\n")
    output_file.write(str(train_model_output.current_stop) + "\n")
    output_file.write(str(train_model_output.play_ad) + "\n")

    output_file.close()
    lock_model_output.release()

def read_engineer_input_file(output_file_name, lock_engineer_input):
    lock_engineer_input.acquire()
    output_file = open(output_file_name, "r")

    kp = float(output_file.readline())
    ki = float(output_file.readline())

    output_file.close()
    lock_engineer_input.release()
    return kp, ki

def write_engineer_input_file(output_file_name, lock_engineer_input, kp, ki):
    lock_engineer_input.acquire()
    output_file = open(output_file_name, "w")

    output_file.write(str(kp) + "\n")
    output_file.write(str(ki) + "\n")

    output_file.close()
    lock_engineer_input.release()