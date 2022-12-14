from dataclasses import dataclass
from TrainController.input.trainDriverInput import TrainDriverInput
from TrainController.input.trainModelInput import TrainModelInput
from TrainController.input.passengerInput import PassengerInput
from TrainController.input.engineerInput import EngineerInput
from TrainController.output.trainDriverOutput import TrainDriverOutput
from TrainController.output.trainModelOutput import TrainModelOutput
from TrainController.ui.testUIFiles.testUI import test_ui
from TrainController.ui.driverUIFiles.trainDriverUI import driver_ui
from multiprocessing import Process
from multiprocessing import Lock
from TrainController.ui.support.readAndWriteFiles import *
from TrainController.resources.findSpeedLimit import *
import psutil
import os, signal

class TrainController:
    def __init__(self, train_number, train_line):
        self.__lock_driver_input = Lock()
        self.__lock_driver_output = Lock()
        self.__lock_model_input = Lock()
        self.__lock_model_output = Lock()
        self.__lock_engineer_input = Lock()
        self.__driver_ui_pid = -1
        self.__test_ui_pid = -1

        self.__train_number = train_number
        self.__train_line = train_line
        self.__test_ui_start = False
        self.__driver_ui_start = False
        self.__max_power = 480000

        self.__command_set_point = 0.0
        self.__power = 0.0
        self.__service_brakes = False
        self.__emergency_brakes = False
        self.__left_side_doors = False
        self.__right_side_doors = False
        self.__announce_stop = False
        self.__inside_lights = False
        self.__outside_lights = False
        self.__activate_announcment = False
        self.__old_current_set_point = 0.0

        self.__authority = False
        self.__speed_limit = 0.0
        self.__u_value = 0.0
        self.__e_value = 0.0
        self.__time_step = 1

        self.__last_station = "YARD"
        self.__next_station = ""
        self.__direction = 0
        self.__distance = 0.0
        self.__begin_slow_down = False
        self.__distance_to_station = 1
        self.__door_side_left = False
        self.__door_side_right = False
        self.__stopping_at_station = False
        self.__waiting_time = 30
        self.__past_time = 0
        self.__begin_wait = False
        self.__acceleration = 0.0
        self.__completed_stop = False

        self.__train_driver_input = TrainDriverInput()
        self.__train_model_input = TrainModelInput()
        self.__passenger_input = PassengerInput()
        self.__engineer_input = EngineerInput()
        self.__train_driver_output = TrainDriverOutput()
        self.__train_model_output = TrainModelOutput()

        self.__input_model_test_ui_file_name = "./TrainController/ui/testUIFiles/utilities/modelInputDB_" + str(self.__train_number) + ".txt"
        self.__output_model_test_ui_file_name = "./TrainController/ui/testUIFiles/utilities/modelOutputDB_" + str(self.__train_number) + ".txt"
        self.__input_driver_driver_ui_file_name = "./TrainController/ui/driverUIFiles/utilities/driverInputDB_" + str(self.__train_number) + ".txt"
        self.__output_driver_driver_ui_file_name = "./TrainController/ui/driverUIFiles/utilities/driverOutputDB_" + str(self.__train_number) + ".txt"
        self.__input_engineer_ui_file_name = "./TrainController/ui/driverUIFiles/utilities/engineerInputDB_" + str(self.__train_number) + ".txt"

    def start_test_ui(self):
        if not self.__test_ui_start:
            write_train_model_input_file(self.__input_model_test_ui_file_name, self.__lock_model_input, self.__train_model_input)
            write_train_model_output_file(self.__output_model_test_ui_file_name, self.__lock_model_output, self.__train_model_output)
            self.__test_ui_start = True
            test_ui_process = Process(target=test_ui, args=(self, self.__lock_model_output, self.__lock_model_input))
            test_ui_process.start()
            self.__test_ui_pid = test_ui_process.pid
    
    def start_driver_ui(self):
        if not self.__driver_ui_start:
            write_driver_input_file(self.__input_driver_driver_ui_file_name, self.__lock_driver_input, self.__train_driver_input)
            write_driver_output_file(self.__output_driver_driver_ui_file_name, self.__lock_driver_output, self.__train_driver_output)
            write_engineer_input_file(self.__input_engineer_ui_file_name, self.__lock_engineer_input, self.__engineer_input.kp, self.__engineer_input.ki)
            self.__driver_ui_start = True
            driver_ui_process = Process(target=driver_ui, args=(self, self.__lock_driver_output, self.__lock_driver_input, self.__lock_engineer_input))
            driver_ui_process.start()
            self.__driver_ui_pid = driver_ui_process.pid
    
    def set_train_driver_input(self, train_driver_input):
        self.__train_driver_input = train_driver_input
    def get_train_number(self):
        return self.__train_number
    
    def get_train_line(self):
        return self.__train_line
    
    def get_driver_input(self):
        return self.__train_driver_input
    
    def get_driver_output(self):
        return self.__train_driver_output
    
    def get_model_input(self):
        return self.__train_model_input
    
    def get_model_output(self):
        return self.__train_model_output
    
    def __driver_output_mapper(self):
        self.__train_driver_output.current_set_point = self.__train_model_input.current_set_point
        self.__train_driver_output.speed_limit = self.__speed_limit
        self.__train_driver_output.interior_temperature = self.__train_driver_input.interior_temperature_control
        if(self.__train_driver_input.manual_mode):
            self.__train_driver_output.command_set_point = self.__train_driver_input.command_set_point
        else:
            self.__train_driver_output.command_set_point = self.__command_set_point
        self.__train_driver_output.brake_failure = self.__train_model_input.brake_failure
        self.__train_driver_output.engine_failure = self.__train_model_input.engine_failure
        self.__train_driver_output.wheel_failure = False
        self.__train_driver_output.signal_pickup_failure = self.__train_model_input.signal_pickup_failure
        self.__train_driver_output.authority = self.__train_model_input.authority and self.__authority
        self.__train_driver_output.next_stop = self.__next_station
        self.__train_driver_output.power = self.__power

    def __model_output_mapper(self):
        self.__train_model_output.service_brake = self.__train_driver_input.service_brake or self.__service_brakes
        self.__train_model_output.emergency_brake = self.__train_driver_input.emergency_brake or self.__emergency_brakes
        self.__train_model_output.engine_power = self.__power
        if self.__train_model_input.current_set_point == 0:
            self.__train_model_output.left_side_doors = self.__train_driver_input.left_side_doors or self.__left_side_doors                                
            self.__train_model_output.right_side_doors = self.__train_driver_input.right_side_doors or self.__right_side_doors
        else:
            self.__train_model_output.left_side_doors = False                           
            self.__train_model_output.right_side_doors = False
        self.__train_model_output.announce_stop = self.__announce_stop
        self.__train_model_output.inside_lights = self.__inside_lights or self.__train_driver_input.inside_lights
        self.__train_model_output.outside_lights = self.__outside_lights or self.__train_driver_input.outside_lights
        self.__train_model_output.activate_announcement = self.__train_driver_input.activate_announcement or self.__activate_announcment

    def __update_internal_values(self):
        self.__distance += .5 * (self.__train_model_input.current_set_point + self.__old_current_set_point) * self.__time_step

        if self.__last_station != self.__train_model_input.station_name and self.__train_model_input.station_name != "N/A":
            self.beaconCall(self.__train_model_input.station_name)
            self.__completed_stop = False
            # if self.__train_model_input.command_set_point < 2 and self.__train_model_input.command_set_point > 0:
            #     self.__stopping_at_station = True
            #     self.__begin_slow_down = False
            # else:
            #     self.__stopping_at_station = False
        if self.__train_model_input.command_set_point < 2 and self.__train_model_input.command_set_point > 0 and not self.__completed_stop:
            self.__stopping_at_station = True
            self.__begin_slow_down = False
            self.__completed_stop = True

        self.__get_speed_limit()

        self.__authority = self.__train_model_input.authority and not(self.__train_model_input.brake_failure or self.__train_model_input.signal_pickup_failure or self.__train_model_input.engine_failure)
        
        if not self.__authority and not(self.__train_model_input.brake_failure or self.__train_model_input.signal_pickup_failure or self.__train_model_input.engine_failure):
            self.power = 0.0
            self.__service_brakes = True
        elif not self.__authority:
            self.power = 0.0
            self.__emergency_brakes = True
        else:
            self.__emergency_brakes = self.__train_driver_input.emergency_brake or self.__passenger_input.emergency_brake
            self.__service_brakes = self.__train_driver_input.service_brake

        if not self.__stopping_at_station:
            if self.__train_driver_input.manual_mode and self.__train_model_input.authority:
                self.__command_set_point = self.__train_driver_input.command_set_point
            elif self.__train_model_input.authority:
                self.__command_set_point = self.__train_model_input.command_set_point
            else:
                self.__command_set_point = 0
            
            if self.__command_set_point > self.__speed_limit:
                self.__command_set_point = self.__speed_limit
        else:
            self.__approaching_station()
            if self.__command_set_point == 0 and self.__train_model_input.current_set_point == 0:
                self.__begin_wait = True
                self.__left_side_doors = self.__door_side_left
                self.__right_side_doors = self.__door_side_right
        
        if self.__begin_wait:
            self.__past_time += self.__time_step
        
        if self.__past_time >= self.__waiting_time:
            self.__right_side_doors = False
            self.__left_side_doors = False
            self.__past_time = 0
            self.__stopping_at_station = False
            self.__begin_wait = False
        
        if not self.__service_brakes and not self.__emergency_brakes:
            self.__calculate_power()
            
        if (self.__train_model_input.current_set_point + self.__acceleration * self.__time_step) > self.__speed_limit or (self.__train_model_input.current_set_point + self.__acceleration * self.__time_step) > self.__command_set_point:
            self.__power = 0.0
            self.__u_value /= 1.5
            self.__service_brakes = True
        elif self.__authority:
            self.__service_brakes = self.__train_driver_input.service_brake

        if self.__service_brakes or self.__emergency_brakes:
            self.__power = 0.0

        if self.__command_set_point == 0:
            self.__power = 0.0
            
    def __calculate_power(self):
        if self.__power < self.__max_power:
            self.__u_value = self.__u_value + ((self.__time_step / 2) * (self.__command_set_point - self.__train_model_input.current_set_point + self.__e_value))
        self.__power = self.__engineer_input.kp * (self.__command_set_point - self.__train_model_input.current_set_point) + self.__engineer_input.ki * self.__u_value
        if self.__power < 0:
            self.__power = 0
        if self.__power > self.__max_power:
            self.__power = self.__max_power

    def __get_speed_limit(self):
        self.__speed_limit = self.__train_model_input.command_set_point
        if self.__train_line == 1:
            self.__direction, self.__next_station, self.__outside_lights, self.__inside_lights, self.__distance_to_station, self.__door_side_left, self.__door_side_right = get_speed_limit_green(self.__last_station, self.__direction, self.__distance)
        else:
            self.__direction, self.__next_station, self.__outside_lights, self.__inside_lights, self.__distance_to_station, self.__door_side_left, self.__door_side_right = get_speed_limit_red(self.__last_station, self.__direction, self.__distance)

    def beaconCall(self, station):
        self.__last_station = station
        self.__distance = 0
    
    def update(self):
        self.__e_value = self.__command_set_point - self.__train_model_input.current_set_point

        if(self.__test_ui_start):
            if psutil.pid_exists(self.__test_ui_pid):
                self.__old_current_set_point = self.__train_driver_output.current_set_point
                write_train_model_output_file(self.__output_model_test_ui_file_name, self.__lock_model_output, self.__train_model_output)
                read_train_model_input_file(self.__input_model_test_ui_file_name, self.__lock_model_input, self.__train_model_input)
            else:
                os.remove(self.__output_model_test_ui_file_name)
                os.remove(self.__input_model_test_ui_file_name)
                self.__test_ui_start = False
        if(self.__driver_ui_start):
            if psutil.pid_exists(self.__driver_ui_pid):
                write_driver_output_file(self.__output_driver_driver_ui_file_name, self.__lock_driver_output, self.__train_driver_output)
                read_driver_input_file(self.__input_driver_driver_ui_file_name, self.__lock_driver_input, self.__train_driver_input)
                self.__engineer_input.kp, self.__engineer_input.ki = read_engineer_input_file(self.__input_engineer_ui_file_name, self.__lock_engineer_input)
            else:
                os.remove(self.__output_driver_driver_ui_file_name)
                os.remove(self.__input_driver_driver_ui_file_name)
                os.remove(self.__input_engineer_ui_file_name)
                self.__driver_ui_start = False
        if self.__command_set_point > 0:
            self.__train_driver_output.train_movement = True
        
        if self.__train_model_input.command_set_point < 0:
            self.__train_model_input.command_set_point = 0
        if self.__train_model_input.current_set_point < 0:
            self.__train_model_input.current_set_point = 0

        self.__update_internal_values()
        self.__driver_output_mapper()
        self.__model_output_mapper()
    
    def get_train_model_output(self):
        return self.__train_model_output.service_brake, self.__train_model_output.engine_power, self.__train_model_output.emergency_brake, self.__train_model_output.left_side_doors, self.__train_model_output.right_side_doors, self.__train_model_output.announce_stop, self.__train_model_output.inside_lights, self.__train_model_output.outside_lights, self.__train_model_output.activate_announcement
    
    def set_train_model_input(self, command_set_point, authority, current_set_point, brake_failure, signal_pickup_failure, engine_failure, station_name):
        self.__old_current_set_point = self.__train_driver_output.current_set_point
        self.__train_model_input.command_set_point = command_set_point
        self.__train_model_input.authority = authority
        self.__acceleration = (current_set_point - self.__train_model_input.current_set_point) / self.__time_step
        self.__train_model_input.current_set_point = current_set_point
        self.__train_model_input.brake_failure = brake_failure
        self.__train_model_input.signal_pickup_failure = signal_pickup_failure
        self.__train_model_input.engine_failure = engine_failure
        self.__train_model_input.station_name = station_name
    
    def __approaching_station(self):
        if not self.__begin_slow_down:
            self.__begin_slow_down = True
            deceleration = 2 ** 2 / (2 * (self.__distance_to_station + 16.1)) * self.__time_step
            self.__command_set_point_list = []
            current_speed = 2
            while(current_speed > 0):
                self.__command_set_point_list.append(current_speed)
                current_speed -= deceleration
            self.__command_set_point_list.append(0)
        if len(self.__command_set_point_list) == 0:
            self.__command_set_point = 0.0
        else:
            self.__command_set_point = self.__command_set_point_list[0]
            self.__command_set_point_list.remove(self.__command_set_point_list[0])
