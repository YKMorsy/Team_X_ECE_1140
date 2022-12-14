import sys
import os
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from qtwidgets import Toggle
from QLed import QLed

from multiprocessing import Lock
from TrainController.ui.support.readAndWriteFiles import  write_driver_input_file
from TrainController.ui.support.readAndWriteFiles import read_driver_output_file
from TrainController.ui.support.readAndWriteFiles import read_engineer_input_file
from TrainController.ui.support.readAndWriteFiles import write_engineer_input_file

class EngineerWindow(QWidget):
    def __init__(self, lock_engineer_file, train_number):
        super().__init__()
        self.setWindowTitle("Engineer Input Box")

        self.__lock_engineer_file = lock_engineer_file

        self.__output_file_name = "./TrainController/ui/driverUIFiles/utilities/engineerInputDB_" + str(train_number) + ".txt"
        self.__kp, self.__ki = read_engineer_input_file(self.__output_file_name, self.__lock_engineer_file)

        layout = QHBoxLayout()
        layout.addWidget(QLabel("Kp Value: "))
        kp_enter_box = QLineEdit(str(self.__kp))
        kp_enter_box.textChanged[str].connect(self.__update_kp_value)
        layout.addWidget(kp_enter_box)
        layout.addWidget(QLabel("Ki Value: "))
        ki_enter_box = QLineEdit(str(self.__ki))
        ki_enter_box.textChanged[str].connect(self.__update_ki_value)
        layout.addWidget(ki_enter_box)

        self.setLayout(layout)
    
    def __update_kp_value(self, text):
        try:
            self.__kp = float(text)
        except ValueError:
            self.__kp = self.__kp
        
        write_engineer_input_file(self.__output_file_name, self.__lock_engineer_file, self.__kp, self.__ki)
    
    def __update_ki_value(self, text):
        try:
            self.__ki = float(text)
        except ValueError:
            self.__ki = self.__ki
        write_engineer_input_file(self.__output_file_name, self.__lock_engineer_file, self.__kp, self.__ki)


class LoginForm(QWidget):
    def __init__(self, lock_engineer_file, train_number):
        super().__init__()
        self.setWindowTitle('Login Form')
        self.resize(500, 120)
        self.__lock_engineer_file = lock_engineer_file
        self.__train_number = train_number

        layout = QGridLayout()

        label_name = QLabel('<font size="4"> Username </font>')
        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setPlaceholderText('Please enter your username')
        layout.addWidget(label_name, 0, 0)
        layout.addWidget(self.lineEdit_username, 0, 1)

        label_password = QLabel('<font size="4"> Password </font>')
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText('Please enter your password')
        layout.addWidget(label_password, 1, 0)
        layout.addWidget(self.lineEdit_password, 1, 1)

        button_login = QPushButton('Login')
        button_login.clicked.connect(self.check_password)
        layout.addWidget(button_login, 2, 0, 1, 2)
        layout.setRowMinimumHeight(2, 75)

        self.setLayout(layout)


    def check_password(self):
        if self.lineEdit_username.text() == "admin" and self.lineEdit_password.text() ==  "password":
            self.close()
            self.__edit_kp_and_ki = EngineerWindow(self.__lock_engineer_file, self.__train_number)
            self.__edit_kp_and_ki.show()

class MainWindow(QWidget):
    def __init__(self, train, lock_output_file, lock_input_file, lock_engineer_file):
        super().__init__()

        self.__train = train
        self.__lock_output_file = lock_output_file
        self.__lock_input_file = lock_input_file
        self.__lock_engineer_file = lock_engineer_file
        self.__train_number = train.get_train_number()
        self.__driver_output = train.get_driver_output()
        self.__driver_input = train.get_driver_input()
        self.__train_line = train.get_train_line()

        self.__input_file_name = "./TrainController/ui/driverUIFiles/utilities/driverInputDB_" + str(self.__train_number) + ".txt"
        self.__output_file_name = "./TrainController/ui/driverUIFiles/utilities/driverOutputDB_" + str(self.__train_number) + ".txt"

        self.setWindowTitle("Train Controller: " + str(self.__train_number))

        self.__layout_init()

        self.__create_header()
        self.__create_driver_ouput_widgets()
        self.__create_speed_info_layout()
        self.__create_speed_button_layout()
        self.__create_service_brake_button()
        self.__create_system_monitor()
        self.__create_fault_indicator()
        self.__create_middle_top_right()
        self.__create_temperature_control()
        self.__create_toggle_labels()
        self.__create_toggle_buttons()
        self.__create_emergency_brake_button()

        self.__assemble_layouts()
        self.setLayout(self.__main_layout)


    def __layout_init(self):
        self.__main_layout = QVBoxLayout()

        self.__header_layout = QHBoxLayout()
        self.__body_layout = QHBoxLayout()

        self.__left_layout = QVBoxLayout()
        self.__middle_layout = QVBoxLayout()
        self.__right_layout = QVBoxLayout()

        self.__speed_info_layout = QVBoxLayout()
        self.__speed_change_layout = QHBoxLayout()
        self.__speed_buttons_layout = QVBoxLayout()

        self.__middle_top_layout = QHBoxLayout()
        self.__fault_layout = QHBoxLayout()
        self.__fault_label_layout = QVBoxLayout()
        self.__fault_indicator_layout = QVBoxLayout()
        self.__middle_top_right_layout = QVBoxLayout()
        self.__manual_mode_toggle_layout = QHBoxLayout()

        self.__non_vital_controls_layout = QVBoxLayout()
        self.__temperature_control_layout = QHBoxLayout()
        self.__toggles_layout = QHBoxLayout()
        self.__toggle_labels_layout = QVBoxLayout()
        self.__toggles_buttons_layout = QVBoxLayout()
    
    def __assemble_layouts(self):
        self.__left_layout.addLayout(self.__speed_info_layout)
        self.__left_layout.addLayout(self.__speed_change_layout)
        self.__left_layout.addWidget(self.__power)
        self.__left_layout.addWidget(self.__service_brake_button)

        self.__fault_layout.addLayout(self.__fault_label_layout, 8)
        self.__fault_layout.addLayout(self.__fault_indicator_layout, 2)
        self.__middle_top_layout.addLayout(self.__fault_layout)
        self.__middle_top_layout.addLayout(self.__middle_top_right_layout)
        self.__middle_layout.addLayout(self.__middle_top_layout)

        self.__non_vital_controls_layout.addWidget(self.__interior_temperature_output)
        self.__non_vital_controls_layout.addLayout(self.__temperature_control_layout)
        self.__toggles_layout.addLayout(self.__toggle_labels_layout)
        self.__toggles_layout.addLayout(self.__toggles_buttons_layout)
        self.__non_vital_controls_layout.addLayout(self.__toggles_layout)
        self.__non_vital_controls_layout.addWidget(self.__activate_announcment_button)
        self.__right_layout.addLayout(self.__non_vital_controls_layout)
        self.__right_layout.addWidget(self.__emergency_brake_button)

        self.__body_layout.addLayout(self.__left_layout)
        self.__body_layout.addLayout(self.__middle_layout)
        self.__body_layout.addLayout(self.__right_layout)

        self.__main_layout.addLayout(self.__header_layout, 1)
        self.__main_layout.addLayout(self.__body_layout, 9)

    def __create_header(self):
        self.__engineer_login = QPushButton("Engineer Login")
        self.__engineer_login.clicked.connect(self.__login_window)
        
        self.__date_and_time = QLabel("Pittsburgh\nPennsylvania")
        self.__date_and_time.setAlignment(Qt.AlignCenter)

        self.__train_information = QLabel("Flexity Tram 2 Train " + str(self.__train_number))
        self.__train_information.setAlignment(Qt.AlignRight)

        self.__header_layout.addWidget(self.__engineer_login)
        self.__header_layout.addWidget(self.__date_and_time)
        self.__header_layout.addWidget(self.__train_information)
    
    def __create_speed_info_layout(self):
        self.__speed_info_layout.addWidget(self.__current_set_point_output)
        self.__speed_info_layout.addWidget(self.__speed_limit_output)
        self.__speed_info_layout.addWidget(self.__command_set_point_output)
    
    def __create_speed_button_layout(self):
        self.__speed_bar = QProgressBar()
        self.__speed_increment = QPushButton("Up")
        self.__speed_increment.pressed.connect(self.__increase_speed_button)
        self.__speed_decrement = QPushButton("Down")
        self.__speed_decrement.pressed.connect(self.__decrease_speed_button)

        self.__speed_buttons_layout.addWidget(self.__speed_increment)
        self.__speed_buttons_layout.addWidget(self.__speed_decrement)

        self.__speed_change_layout.addWidget(self.__speed_bar)
        self.__speed_change_layout.addLayout(self.__speed_buttons_layout)
    
    def __create_service_brake_button(self):
        self.__service_brake_button = QPushButton("Service Brake")
        self.__service_brake_button.pressed.connect(self.__service_brake_button_action_on)
        self.__service_brake_button.released.connect(self.__service_brake_button_action_off)
    
    def __create_system_monitor(self):
        self.__brake_failure_label = QLabel("Brakes")
        self.__engine_failure_label = QLabel("Engine")
        self.__signal_failure_label = QLabel("Signal Pickup Failure")

        self.__fault_label_layout.addWidget(self.__brake_failure_label)
        self.__fault_label_layout.addWidget(self.__engine_failure_label)
        self.__fault_label_layout.addWidget(self.__signal_failure_label)

    def __create_fault_indicator(self):
        self.__brake_failure_indicator = QLed(offColour= QLed.Green, onColour = QLed.Red, shape=QLed.Circle)
        self.__brake_failure_indicator.value = self.__driver_output.brake_failure
        self.__engine_fault_indicator = QLed(offColour= QLed.Green,onColour = QLed.Red, shape=QLed.Circle)
        self.__engine_fault_indicator.value = self.__driver_output.engine_failure
        self.__signal_failure_indicator = QLed(offColour= QLed.Green,onColour = QLed.Red, shape=QLed.Circle)
        self.__signal_failure_indicator.value = self.__driver_output.signal_pickup_failure

        self.__fault_indicator_layout.addWidget(self.__brake_failure_indicator)
        self.__fault_indicator_layout.addWidget(self.__engine_fault_indicator)
        self.__fault_indicator_layout.addWidget(self.__signal_failure_indicator)
    
    def __create_middle_top_right(self):
        self.__manual_mode_toggle = Toggle(checked_color="#00FF00")
        self.__manual_mode_toggle.toggled.connect(self.__manual_mode_toggle_check)
        self.__train_line_label = QLabel()
        if self.__train_line == 1:
            self.__train_line_label.setText("Green Line")
        else:
            self.__train_line_label.setText("Red Line")

        self.__manual_mode_toggle_layout.addWidget(QLabel("Manual Mode"), 8)
        self.__manual_mode_toggle_layout.addWidget(self.__manual_mode_toggle)
        self.__middle_top_right_layout.addWidget(self.__authority_output)
        self.__middle_top_right_layout.addLayout(self.__manual_mode_toggle_layout)
        self.__middle_top_right_layout.addWidget(self.__train_line_label)
        self.__middle_top_right_layout.addWidget(self.__next_stop)

    def __create_temperature_control(self):
        self.__increment_temperature = QPushButton("Up")
        self.__increment_temperature.pressed.connect(self.__increment_temperature_button)
        self.__decrement_temperature = QPushButton("Down")
        self.__decrement_temperature.pressed.connect(self.__decrement_temperature_button)
        self.__temperature_control_layout.addWidget(self.__increment_temperature)
        self.__temperature_control_layout.addWidget(self.__decrement_temperature)
    
    def __create_toggle_labels(self):
        self.__toggle_labels_layout.addWidget(QLabel("Left Side Doors"))
        self.__toggle_labels_layout.addWidget(QLabel("Right Side Doors"))
        self.__toggle_labels_layout.addWidget(QLabel("Interior Lights"))
        self.__toggle_labels_layout.addWidget(QLabel("Exterior Lights"))
    
    def __create_toggle_buttons(self):
        self.__toggle_left_side_doors_button = Toggle(checked_color="#00FF00")
        self.__toggle_left_side_doors_button.toggled.connect(self.__left_side_doors_toggle)
        self.__toggle_right_side_doors_button = Toggle(checked_color="#00FF00")
        self.__toggle_right_side_doors_button.toggled.connect(self.__right_side_doors_toggle)
        self.__toggle_inside_lights_button = Toggle(checked_color="#00FF00")
        self.__toggle_inside_lights_button.toggled.connect(self.__inside_lights_toggle)
        self.__toggle_outside_lights_button = Toggle(checked_color="#00FF00")
        self.__toggle_outside_lights_button.toggled.connect(self.__outside_lights_toggle)

        self.__activate_announcment_button = QPushButton("Activate Announcement")
        self.__activate_announcment_button.pressed.connect(self.__activate_announcement_press)
        self.__activate_announcment_button.released.connect(self.__activate_announcement_release)

        self.__toggles_buttons_layout.addWidget(self.__toggle_left_side_doors_button)
        self.__toggles_buttons_layout.addWidget(self.__toggle_right_side_doors_button)
        self.__toggles_buttons_layout.addWidget(self.__toggle_inside_lights_button)
        self.__toggles_buttons_layout.addWidget(self.__toggle_outside_lights_button)
    
    def __create_emergency_brake_button(self):
        self.__emergency_brake_button = QPushButton("Emergency Brake")
        self.__emergency_brake_button.pressed.connect(self.__emergency_brake_button_action_on)
        self.__emergency_brake_button.released.connect(self.__emergency_brake_button_action_off)
    
    def __create_driver_ouput_widgets(self):
        self.__current_set_point_output = QLabel()
        self.__speed_limit_output = QLabel()
        self.__interior_temperature_output = QLabel()
        self.__command_set_point_output = QLabel()
        self.__authority_output = QLabel()
        self.__authority_output.setAlignment(Qt.AlignCenter)
        self.__next_stop = QLabel()
        self.__power = QLabel()
    
    def __update_output_widgets(self):
        self.__current_set_point_output.setText("Current Speed: " + str(int(self.__driver_output.current_set_point * 2.237)) + " mph")
        self.__speed_limit_output.setText("Speed Limit: " + str(int(self.__driver_output.speed_limit * 2.23694)) + " mph")
        self.__interior_temperature_output.setText("A/C Temperature: " + str(self.__driver_output.interior_temperature) + "F")
        self.__command_set_point_output.setText("Target Speed: " + str(int(self.__driver_output.command_set_point * 2.237)) + " mph")
        if self.__driver_output.authority:
            self.__authority_output.setText("Go")
        else:
            self.__authority_output.setText("Stop")

        self.__brake_failure_indicator.value = self.__driver_output.brake_failure
        self.__engine_fault_indicator.value = self.__driver_output.engine_failure
        self.__signal_failure_indicator.value = self.__driver_output.signal_pickup_failure
        if self.__driver_output.speed_limit == 0:
            self.__speed_bar.setValue(0)
        else:
            self.__speed_bar.setValue(int(self.__driver_output.current_set_point / self.__driver_output.speed_limit * 100))
        self.__next_stop.setText("Next Stop: " + self.__driver_output.next_stop)
        self.__power.setText("Power: " + str(int(self.__driver_output.power)))
    
    def update(self):
        read_driver_output_file(self.__output_file_name, self.__lock_output_file, self.__driver_output)
        self.__update_output_widgets()
        if not self.__driver_input.manual_mode:
            self.__driver_input.command_set_point = self.__driver_output.speed_limit
        write_driver_input_file(self.__input_file_name, self.__lock_input_file, self.__driver_input)
    
    
    def __service_brake_button_action_on(self):
        self.__driver_input.service_brake = True
    
    def __service_brake_button_action_off(self):
        self.__driver_input.service_brake = False
    
    def __emergency_brake_button_action_on(self):
        self.__driver_input.emergency_brake = True

    def __emergency_brake_button_action_off(self):
        self.__driver_input.emergency_brake = False

    def __manual_mode_toggle_check(self):
        self.__driver_input.manual_mode = self.__manual_mode_toggle.isChecked()
    
    def __left_side_doors_toggle(self):
        self.__driver_input.left_side_doors = self.__toggle_left_side_doors_button.isChecked()
        if self.__driver_output.current_set_point > 0:
            self.__driver_input.left_side_doors = False
            self.__toggle_left_side_doors_button.setChecked(False)
    
    def __right_side_doors_toggle(self):
        self.__driver_input.right_side_doors = self.__toggle_right_side_doors_button.isChecked()
        if self.__driver_output.current_set_point > 0:
            self.__driver_input.right_side_doors = False
            self.__toggle_right_side_doors_button.setChecked(False)
    
    def __inside_lights_toggle(self):
        self.__driver_input.inside_lights = self.__toggle_inside_lights_button.isChecked()
    
    def __outside_lights_toggle(self):
        self.__driver_input.outside_lights = self.__toggle_outside_lights_button.isChecked()
    
    def __increase_speed_button(self):
        if self.__driver_input.manual_mode:
            if self.__driver_input.command_set_point < self.__driver_output.speed_limit:
                self.__driver_input.command_set_point += 0.44704
    
    def __decrease_speed_button(self):
        if self.__driver_input.manual_mode:
            if self.__driver_input.command_set_point > 0:
                self.__driver_input.command_set_point -= 0.44704
    
    def __activate_announcement_press(self):
        self.__driver_input.activate_announcement = True
    
    def __activate_announcement_release(self):
        self.__driver_input.activate_announcement = False
    
    def __increment_temperature_button(self):
        if self.__driver_output.interior_temperature < 78:
            self.__driver_input.interior_temperature_control += 1
    
    def __decrement_temperature_button(self):
        if self.__driver_output.interior_temperature > 65:
            self.__driver_input.interior_temperature_control -= 1
    
    def __login_window(self):
        if not self.__driver_output.train_movement:
            self.__new_login = LoginForm(self.__lock_engineer_file, self.__train_number)
            self.__new_login.show()
        
    

def driver_ui(train, lock_output_file, lock_input_file, lock_engineer_input):
    app = QApplication([])
    window = MainWindow(train, lock_output_file, lock_input_file, lock_engineer_input)
    fps = 15
    timer = QTimer()
    timer.timeout.connect(window.update)
    timer.setInterval(int(1000 / fps))
    timer.start()
    window.show()
    sys.exit(app.exec_())
    