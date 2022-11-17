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

from PyQt6.QtWidgets import QApplication as q6App
from PyQt5.QtWidgets import QApplication as q5App
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QTimer

class Iteration3(QWidget):
    def __init__(self):
        super().__init__()
        self.time_step = 1
        #Create track model
        self.track_model_var = track_model()
        self.track_model_var.show()
        handler.track_model = self.track_model_var

        #Create CTC
        self.green_line = Line("./CTC_App/Iteration3/Track_Layout_Green.xlsx")
        self.dispatcher = Dispatcher()
        self.ctc_office = CTCApp(self.green_line, self.dispatcher)
        self.ctc_office.show()
        #Place waysides
        self.wayside_sign_in = sign_in_window()
        self.wayside_sign_in.show()

        #Train Model Handler
        self.murphy = MurphyUI()
        self.murphy.show()

        self.train_id_list = []
        self.train_controller = {}

    def update_everything(self):

        connect_ctc_track_controller(self.dispatcher, self.green_line, self.green_line, self.wayside_sign_in.get_all_track_controllers())

        Connect_Track_Control_And_Model(self.wayside_sign_in.get_all_track_controllers(), self.track_model_var)

        #Ryan and peter connect here

        for i in range(len(self.train_controller)):
            connect_train_model_train_controller(self.train_controller[self.train_id_list[i]], handler.train_list[self.train_id_list[i]])
        
        #Update all modules
        #Yassers update
        new_trains = self.ctc_office.updateTimer()
        #Sierra call your update here

        #Peter call your update here

        #Ryans update
        handler.update(self.time_step)

        #New train creation, Ryan can you add in the coded needed to create your train
        for train in new_trains:
            train_id = train.train_id
            train_line = train.line.line_color
            self.train_id_list.append(train_id)
            if train_line == 'Red':
                self.train_controller[train_id] = TrainController(train_id, 0)
                handler.create_train(ID=train_id, line_name='Red')
            else:
                self.train_controller[train_id] = TrainController(train_id, 1)
                handler.create_train(ID=train_id, line_name='Green')
            self.train_controller[train_id].start_driver_ui()
        
        #Train deletion, wont do this for iteration 3 cause too hard



if __name__ == '__main__':
    #Initialize  all objects
    fiveO = q5App([])
    sixers = q6App([])

    god_help_us = Iteration3()

    fps = 10
    timer = QTimer()
    timer.timeout.connect(god_help_us.update_everything)
    handler.update(1)
    timer.setInterval(int(1000 / fps))
    timer.start()

    fiveO.exec_()
