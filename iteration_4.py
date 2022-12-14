import time

from TrainController.trainController import TrainController

from CTC_App.Iteration3.Line import Line
from CTC_App.Iteration3.Dispatcher import Dispatcher
from CTC_App.Iteration3.CTC import CTCApp

from TrainModel.Murphy import MurphyUI
from TrainModel.common import *

from track_controller.sign_in_window import sign_in_window

from TrackModel.track_model import track_model

from connect_ctc_track_controller import connect_ctc_track_controller
from Connect_Track_Controller_Model import Connect_Track_Control_And_Model
from connect_train_model_train_controller import connect_train_model_train_controller
from connect_ctc_track_model import connect_ctc_track_model

from PyQt6.QtWidgets import QApplication as q6App
from PyQt5.QtWidgets import QApplication as q5App
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Iteration_4(QWidget):
    def __init__(self, fps):
        super().__init__()
        self.__fps = fps 
        self.__time_step = 1
        self.__count = 0
        self.__multiplier = 1
        self.__pause = False
        
        #Create track model
        self.__track_model_var = track_model()
        handler.track_model = self.__track_model_var
        

        #Create CTC
        self.__green_line = Line("./CTC_App/Iteration3/Track_Layout_Green.xlsx")
        self.__red_line = Line("./CTC_App/Iteration3/Track_Layout_Red.xlsx")
        self.__dispatcher = Dispatcher()
        self.__dispatcher.updateTime(time.time())
        self.__ctc_office = CTCApp(self.__green_line, self.__red_line, self.__dispatcher)

        #Place waysides
        self.__wayside_sign_in = sign_in_window()


        #Train Model Handler
        self.__murphy = MurphyUI()

        self.__train_controller_buttons = {}
        self.__train_x_axis = 0
        self.__train_y_axis = 0

        self.__train_id_list = []
        self.__train_controller = {}
        self.__new_train = []

        self.__layout_init()
        
        self.__create_simulation_settings()

        self.__tabs_init()

        self.__assemble_layouts()

        self.setLayout(self.__main_layout)
    
    def __layout_init(self):
        self.__main_layout = QHBoxLayout()
        
        self.__simulation_layout = QVBoxLayout()
        self.__train_controller_layout = QGridLayout()
    
    def __assemble_layouts(self):
        self.__simulation_layout.setAlignment(Qt.AlignVCenter)
        self.__simulation_layout.setAlignment(Qt.AlignCenter)
        self.__main_layout.addLayout(self.__simulation_layout, 1)
        self.__main_layout.addWidget(self.__tabs, 9)
    
    def __create_simulation_settings(self):
        self.__simulation_label = QLabel()
        self.__simulation_label.setText("Current Simulation Speed: " + str(self.__multiplier))
        self.__simulation_slider = QSlider()
        self.__simulation_slider.setGeometry(QRect(190, 100, 160, 16))
        self.__simulation_slider.setOrientation(Qt.Horizontal)
        self.__simulation_slider.valueChanged.connect(self.__change_speed)
        self.__simulation_pause_label = QLabel("Pause Simulation")
        self.__simulation_pause = QRadioButton()
        self.__simulation_pause.toggled.connect(self.__pause_simulation)

        self.__simulation_layout.addWidget(self.__simulation_label)
        self.__simulation_layout.addWidget(self.__simulation_slider)
        self.__simulation_layout.addWidget(self.__simulation_pause_label)
        self.__simulation_layout.addWidget(self.__simulation_pause)
    
    def __change_speed(self, value):
        self.__multiplier = int(value / 10) + 1 
    
    def __tabs_init(self):
        self.__tabs = QTabWidget()
        self.__tabs.addTab(self.__ctc_office, "CTC Office")
        self.__tabs.addTab(self.__wayside_sign_in, "Track Controller")
        self.__tabs.addTab(self.__track_model_var.get_widget(), "Track Model")
        self.__tabs.addTab(self.__murphy, "Train Model")
        self.__train_controller_tab = QWidget()
        self.__train_controller_tab.setLayout(self.__train_controller_layout)
        self.__tabs.addTab(self.__train_controller_tab, "Train Controller")
    
    def __add_train_button(self, train_id):
        newButton = QPushButton("Train " + str(train_id))
        newButton.pressed.connect(lambda: self.__train_controller_show(train_id))
        self.__train_controller_layout.addWidget(newButton, self.__train_x_axis, self.__train_y_axis)
        self.__train_controller_buttons[train_id] = newButton
        self.__train_y_axis += 1
        if self.__train_y_axis >= 10:
            self.__train_y_axis = 0
            self.__train_x_axis += 1
    
    def __train_controller_show(self, value):
        self.__train_controller[value].start_driver_ui()
    
    def __pause_simulation(self):
        self.__pause = self.__simulation_pause.isChecked()
    
    def __delete_train_controller(self, index):
        self.__train_controller_buttons[index].deleteLater()
        del self.__train_controller_buttons[index]
        del self.__train_controller[index]
    
    def update_with_fps(self):
        self.__simulation_label.setText("Current Simulation Speed: " + str(self.__multiplier))
        if not self.__pause:
            self.__count += 1
        if self.__count > (self.__fps / self.__multiplier):
            self.__count = 0
            self.__update_everything()
            
    def __update_everything(self):

        connect_ctc_track_model(self.__green_line, self.__red_line, self.__track_model_var)

        connect_ctc_track_controller(self.__dispatcher, self.__green_line, self.__red_line, self.__wayside_sign_in.get_all_track_controllers(), self.__ctc_office.manualModeCheck.isChecked())
        self.__wayside_sign_in.timer_track_control()
        Connect_Track_Control_And_Model(self.__wayside_sign_in.get_all_track_controllers(), self.__track_model_var)

        #Ryan and peter connect here

        for i in range(len(handler.train_list)):
            if len(self.__train_controller) and len(handler.train_list) > 0:
                connect_train_model_train_controller(self.__train_controller[self.__train_id_list[i]], handler.train_list[self.__train_id_list[i]])
        
        #Update all modules
        #Yassers update
        new_trains = self.__ctc_office.updateTimer()
        for train in new_trains:
            self.__new_train.append(train)
        #Sierra call your update here
        

        #Peter call your update here
        self.__track_model_var.ui.set_block_status_table()
        #Ryans update
        to_delete = handler.update(self.__time_step, self.__track_model_var)

        for i in to_delete:
            print("Deleting Train")
            self.__train_id_list.remove(i)
            self.__delete_train_controller(i)

        #New train creation, Ryan can you add in the coded needed to create your train
        for train in self.__new_train:
            train_id = train.train_id
            train_line = train.line.line_color
            self.__train_id_list.append(train_id)
            if train_line == 'Red':
                self.__train_controller[train_id] = TrainController(train_id, 0)
                handler.create_train(ID=train_id, line_name='Red')
            else:
                self.__train_controller[train_id] = TrainController(train_id, 1)
                handler.create_train(ID=train_id, line_name='Green')
            self.__add_train_button(train_id)

            self.__new_train.remove(train)

        self.__ctc_office.greenLine.setThroughput(self.__track_model_var.stations.get_throughput())
        self.__ctc_office.redLine.setThroughput(self.__track_model_var.stations.get_throughput())
        #Train deletion, wont do this for iteration 3 cause too hard

if __name__ == '__main__':
    #Initialize  all objects
    fiveO = q5App([])
    sixers = q6App([])

    fps = 100
    god_help_us = Iteration_4(fps)
    god_help_us.show()

    timer = QTimer()
    timer.timeout.connect(god_help_us.update_with_fps)
    handler.update(1)
    timer.setInterval(int(1000/fps))
    timer.start()

    fiveO.exec_()
