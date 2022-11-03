from track_controller.sign_in_window import sign_in_window 
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt, QTimer
import sys

def tesTransfer_Data():
    print("1 sec")
    window.get_all_track_controllers()

app = QtWidgets.QApplication(sys.argv)
window = sign_in_window()
window.show()

timer = QTimer()
timer.timeout.connect(window.Timer_TrackControl)
timer.setInterval(1000)  # 1000ms = 1s
timer.start()

app.exec_()