import time

from TrainController.trainController import TrainController

from CTC_App.Iteration3.Line import Line
from CTC_App.Iteration3.Dispatcher import Dispatcher
from CTC_App.Iteration3.CTC import CTCApp

from TrainModel.TrainModelHandler import TrainModelHandler
from TrainModel.Murphy import MurphyUI
from TrainModel.common import *

from track_controller.sign_in_window import sign_in_window

from TrackModel.track_model import track_model

from connect_ctc_track_controller import connect_ctc_track_controller
from Connect_Track_Controller_Model import Connect_Track_Control_And_Model
from connect_train_model_train_controller import connect_train_model_train_controller

from PyQt6.QtWidgets import QApplication as q6App
from PyQt5.QtWidgets import QApplication as q5App
from PyQt5.QtCore import QTimer

def update_everything(dispatcher, green_line, track_controller_list, track_model_var, train_model, train_controller):

    connect_ctc_track_controller(dispatcher, green_line, green_line, track_controller_list)

    Connect_Track_Control_And_Model(track_controller_list, track_model_var)

    #Ryan and peter connect here

    for i in range(len(train_controller)):
        connect_train_model_train_controller(train_controller[i], train_model[i])
    
    #Update all modules


if __name__ == '__main__':
    #Initialize  all objects
    fiveO = q5App([])
    sixers = q6App([])
    
    #Build track
    track_model_var = track_model()
    track_model_var.show()

    #Create CTC
    green_line = Line("./CTC_App/Iteration3/Track_Layout_Green.xlsx")
    dispatcher = Dispatcher()
    ctc_office = CTCApp(green_line, dispatcher)
    ctc_office.show()
    #Place waysides
    wayside_sign_in = sign_in_window()
    wayside_sign_in.show()

    #Train Model Handler
    murphy = MurphyUI()
    murphy.show()

    train_controller = []

    fps = 10
    timer = QTimer()
    timer.timeout.connect(update_everything(dispatcher, green_line, wayside_sign_in.get_all_track_controllers(), track_model_var, handler.train_list, train_controller))
    handler.update(1)
    timer.setInterval(int(1000 / fps))
    timer.start()

    fiveO.exec_()
