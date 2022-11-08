import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from qtwidgets import Toggle

from multiprocessing import Lock
from ui.support.readAndWriteFiles import  write_train_model_input_file
from ui.support.readAndWriteFiles import read_train_model_output_file

class MainWindow(QWidget):
        
        def __init__(self, train, lock_output_file, lock_input_file):
            super().__init__()

            self.train = train
            self.__lock_output_file = lock_output_file
            self.__lock_input_file = lock_input_file
            self.__train_number = train.get_train_number()
            self.__train_line = train.get_train_line()
            self.__model_output = train.get_model_output()
            self.__model_input = train.get_model_input()

            self.__input_file_name = "./ui/testUIFiles/utilities/modelInputDB_" + str(self.__train_number) + ".txt"
            self.__output_file_name = "./ui/testUIFiles/utilities/modelOutputDB_" + str(self.__train_number) + ".txt"

            self.setWindowTitle("Test UI Window " + str(self.__train_number))
            self.__create_output_widgets()
            self.__update_output_widgets()
            self.__create_input_widgets()
            self.__update_input_widgets_out()
            self.__layout_init()

            self.__create_header()
            self.__power_speed_enter()
            self.__output_list()

            self.__toggle_section()
            self.__station_select_create()
        
            self.__assemble_layouts()

            self.setLayout(self.__outer_layout)
        
        def __layout_init(self):
            self.__outer_layout = QHBoxLayout()

            self.__left_layout = QVBoxLayout()
            self.__right_layout = QVBoxLayout()

            self.__top_left_layout = QHBoxLayout()
            self.__top_right_layout = QHBoxLayout()

            self.__current_set_point_layout = QHBoxLayout()
            self.__authority_toggle_layout = QHBoxLayout()

            self.__power_speed_enter_layout = QHBoxLayout()
            self.__power_speed_enter_label_layout = QVBoxLayout()
            self.__power_speed_enter_text_layout = QVBoxLayout()

            self.__output_field_layout = QHBoxLayout()
            self.__output_field_left_layout = QVBoxLayout()
            self.__output_field_right_layout = QVBoxLayout()

            self.__toggle_layout = QHBoxLayout()
            self.__toggle_left_layout = QHBoxLayout()
            self.__toggle_left_label_layout = QVBoxLayout()
            self.__toggle_left_button_layout = QVBoxLayout()

        def __assemble_layouts(self):
            self.__power_speed_enter_layout.addLayout(self.__power_speed_enter_label_layout, 8)
            self.__power_speed_enter_layout.addLayout(self.__power_speed_enter_text_layout, 2)
            self.__toggle_left_layout.addLayout(self.__toggle_left_label_layout, 9)
            self.__toggle_left_layout.addLayout(self.__toggle_left_button_layout, 1)
            self.__toggle_layout.addLayout(self.__toggle_left_layout)

            self.__left_layout.addLayout(self.__top_left_layout, 1)
            self.__left_layout.addWidget(self.__current_set_point, 1)
            self.__left_layout.addLayout(self.__current_set_point_layout,1)
            self.__authority_toggle_layout.addWidget(self.__authority, 8)
            self.__authority_toggle_layout.addWidget(self.__authority_toggle)
            self.__left_layout.addLayout(self.__authority_toggle_layout, 1)
            self.__left_layout.addWidget(self.__command_set_point, 1)
            self.__left_layout.addLayout(self.__power_speed_enter_layout, 1)
            self.__left_layout.addLayout(self.__toggle_layout, 3)
            self.__left_layout.addWidget(self.__station_select)

            self.__output_field_layout.addLayout(self.__output_field_left_layout)
            self.__output_field_layout.addLayout(self.__output_field_right_layout)

            self.__right_layout.addLayout(self.__top_right_layout, 1)
            self.__right_layout.addLayout(self.__output_field_layout, 5)

            self.__outer_layout.addLayout(self.__left_layout, 4)
            self.__outer_layout.addLayout(self.__right_layout, 6)

        def __create_header(self):
            __input_field_name = QLabel("Input Field")
            __input_field_name.setAlignment(Qt.AlignCenter)
            self.__top_left_layout.addWidget(__input_field_name)
            __output_field_name = QLabel("Output Field")
            __output_field_name.setAlignment(Qt.AlignCenter)
            self.__top_right_layout.addWidget(__output_field_name)
        
        def __power_speed_enter(self):
            self.__current_set_point_layout.addWidget(QLabel("Enter Current Set Point: "), 8)
            self.__set_point_enter_box = QLineEdit(str(self.__model_input.current_set_point))
            self.__set_point_enter_box.textChanged[str].connect(self.__set_point_text_update)
            self.__current_set_point_layout.addWidget(self.__set_point_enter_box)

            speed_enter_label = QLabel("Enter Desired Speed: ")
            self.__power_speed_enter_label_layout.addWidget(speed_enter_label)

            self.__speed_enter_box = QLineEdit(str(self.__model_input.command_set_point))
            self.__speed_enter_box.textChanged[str].connect(self.__speed_text_update)
            self.__power_speed_enter_text_layout.addWidget(self.__speed_enter_box)
        
        def __output_list(self):
            self.__output_field_left_layout.addWidget(self.__service_brake)
            self.__output_field_left_layout.addWidget(self.__emergency_brake)
            self.__output_field_left_layout.addWidget(self.__left_side_doors)
            self.__output_field_left_layout.addWidget(self.__right_side_doors)

            self.__output_field_right_layout.addWidget(self.__engine_power)
            self.__output_field_right_layout.addWidget(self.__inside_lights)
            self.__output_field_right_layout.addWidget(self.__outside_lights)
            self.__output_field_right_layout.addWidget(self.__activate_announcment)
        
        def __toggle_section(self):
            brakes_label = QLabel("Brake Failure")
            engine_label = QLabel("Engine Failure")
            signal_pickup_failure_label = QLabel("Signal Pick Up Failure")
            self.__toggle_left_label_layout.addWidget(brakes_label)
            self.__toggle_left_label_layout.addWidget(engine_label)
            self.__toggle_left_label_layout.addWidget(signal_pickup_failure_label)

            self.__brake_toggle = Toggle(checked_color="#00FF00")
            self.__brake_toggle.toggled.connect(self.__brake_failure_toggle)
            self.__engine_toggle = Toggle(checked_color="#00FF00")
            self.__engine_toggle.toggled.connect(self.__engine_failure_toggle)
            self.__signal_toggle = Toggle(checked_color="#00FF00")
            self.__signal_toggle.toggled.connect(self.__signal_failure_toggle)
            self.__toggle_left_button_layout.addWidget(self.__brake_toggle)
            self.__toggle_left_button_layout.addWidget(self.__engine_toggle)
            self.__toggle_left_button_layout.addWidget(self.__signal_toggle)
        
        def __station_select_create(self):
            if self.__train_line == 0:
                self.__station_select.addItems(["YARD", "SHADYSIDE", "HERRON AVE", "SWISSVALE", "PENN STATION", "STEEL PLAZA", "FIRST AVE", "STATION SQUARE", "SOUTH HILLS JUNCTION"])
            else:
                self.__station_select.addItems(["YARD", "GLENBURY", "DORMONT", "MT LEBANON", "POPLAR", "CASTLE SHANNON", "OVERBROOK", "INGLEWOOD", "CENTRAL", "WHITED", "SOUTH BANK", "STATION", "EDGEBROOK", "PIONEER"])
            self.__station_select.currentTextChanged.connect(self.__update_station_data)
        
        def update(self):
            read_train_model_output_file(self.__output_file_name, self.__lock_output_file, self.__model_output)
            self.__update_output_widgets()
            write_train_model_input_file(self.__input_file_name, self.__lock_input_file, self.__model_input)
            self.__update_input_widgets_out()
        
        def __create_output_widgets(self):
            self.__service_brake = QLabel()
            self.__engine_power = QLabel()
            self.__emergency_brake = QLabel()
            self.__left_side_doors = QLabel()
            self.__right_side_doors = QLabel()
            self.__announce_stop = QLabel()
            self.__inside_lights = QLabel()
            self.__outside_lights = QLabel()
            self.__activate_announcment = QLabel()

        def __update_output_widgets(self):
            self.__service_brake.setText("Service Brake: " + str(self.__model_output.service_brake))
            self.__engine_power.setText("Engine Power: " + str(int(self.__model_output.engine_power)) + " W")
            self.__emergency_brake.setText("Emergency Brake: " + str(self.__model_output.emergency_brake))
            self.__left_side_doors.setText("Left Side Doors: " + str(self.__model_output.left_side_doors))
            self.__right_side_doors.setText("Right Side Doors: " + str(self.__model_output.right_side_doors))
            self.__announce_stop.setText("Announce Stop: " + str(self.__model_output.announce_stop))
            self.__inside_lights.setText("Inside Lights: " + str(self.__model_output.inside_lights))
            self.__outside_lights.setText("Outside Lights: " + str(self.__model_output.outside_lights))
            self.__activate_announcment.setText("Activate Announcement: " + str(self.__model_output.activate_announcement))
        
        def __create_input_widgets(self):
            self.__command_set_point = QLabel()
            self.__authority = QLabel()
            self.__current_set_point = QLabel()
            self.__brake_failure = QLabel()
            self.__signal_pickup_failure = QLabel()
            self.__engine_failure = QLabel()
            self.__authority_toggle = Toggle(checked_color="#00FF00")
            self.__authority_toggle.toggled.connect(self.__authority_toggle_action)
            self.__station_label = QLabel()
            self.__station_select = QComboBox()
        
        def __update_input_widgets_out(self):
            self.__command_set_point.setText("Command Set Point: " + str(int(self.__model_input.command_set_point)) + " m/s")
            self.__authority.setText("Authority: " + str(self.__model_input.authority))
            self.__current_set_point.setText("Current Set Point: " + str(int(self.__model_input.current_set_point)) + " m/s")
            self.__brake_failure.setText("Brake Failure: " + str(self.__model_input.brake_failure))
            self.__signal_pickup_failure.setText("Signal Pickup Failure: " + str(self.__model_input.signal_pickup_failure))
            self.__engine_failure.setText("Engine Failure: " + str(self.__model_input.engine_failure))
            self.__station_label.setText("Last Passed Station: " + str(self.__model_input.station_name))
        
        def __speed_text_update(self, text):
            try:
                self.__model_input.command_set_point = float(text)
            except ValueError:
                self.__model_input.command_set_point = self.__model_input.command_set_point
        
        def __set_point_text_update(self, text):
            try:
                self.__model_input.current_set_point = float(text)
            except ValueError:
                self.__model_input.current_set_point = self.__model_input.current_set_point
    
        def __authority_toggle_action(self):
            self.__model_input.authority = self.__authority_toggle.isChecked()
        
        def __brake_failure_toggle(self):
            self.__model_input.brake_failure = self.__brake_toggle.isChecked()
        
        def __engine_failure_toggle(self):
            self.__model_input.engine_failure = self.__engine_toggle.isChecked()
        
        def __signal_failure_toggle(self):
            self.__model_input.signal_pickup_failure = self.__signal_toggle.isChecked()
        
        def __update_station_data(self, s):
            self.__model_input.station_name = s

def test_ui(train, lock_output_file, lock_input_file):
    app = QApplication([])
    window = MainWindow(train, lock_output_file, lock_input_file)
    fps = 15
    timer = QTimer()
    timer.timeout.connect(window.update)
    timer.setInterval(int(1000 / fps))
    timer.start()
    window.show()
    app.exec()
