from track_controller.sign_in_window import sign_in_window 
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt, QTimer
import sys

def SetTrackControlData():
    trcControl = window.get_all_track_controllers()
    #occupancy
    Red_master_occ = trcControl[0].get_occupancy() | trcControl[1].get_occupancy() | trcControl[2].get_occupancy()
    Green_master_occ = trcControl[3].get_occupancy() | trcControl[4].get_occupancy() | trcControl[5].get_occupancy()
    
    #switch
    Red_master_switch = trcControl[0].get_switch_positions() | trcControl[1].get_switch_positions() | trcControl[2].get_switch_positions()
    Green_master_switch = trcControl[3].get_switch_positions() | trcControl[4].get_switch_positions() | trcControl[5].get_switch_positions()
    
    #railway 
    Red_master_switch = trcControl[0].get_railway_crossings() | trcControl[1].get_railway_crossings() | trcControl[2].get_railway_crossings()
    Green_master_switch = trcControl[3].get_railway_crossings() | trcControl[4].get_railway_crossings() | trcControl[5].get_railway_crossings()
    
    #status
    Red_master_switch = trcControl[0].get_statuses() | trcControl[1].get_statuses() | trcControl[2].get_statuses()
    Green_master_switch = trcControl[3].get_statuses() | trcControl[4].get_statuses() | trcControl[5].get_statuses()

    print("hello")


app = QtWidgets.QApplication(sys.argv)
window = sign_in_window()
window.show()

timer = QTimer()
timer.timeout.connect(window.timer_track_control)
timer.setInterval(3000)  # 1000ms = 1s
#timer.start()

app.exec_()