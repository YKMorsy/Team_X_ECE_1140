import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import Qt
from track_controller.track_control_controller import track_control_controller
import copy
from track_controller.track_control_display import track_control_display

sign_in_wind = "sign_in.ui"
Ui_sign_in_window, QtBaseClass = uic.loadUiType("track_controller/UIs/"+sign_in_wind)

class sign_in_window (QtWidgets.QMainWindow, Ui_sign_in_window):
    def __init__(self):
        #self.main_wind = MainWindow()
        QtWidgets.QMainWindow.__init__(self)
        Ui_sign_in_window.__init__(self)
        self.setupUi(self)
        self.SignInButton.clicked.connect(self.open_main_window)
        self.Password_TextBox.installEventFilter(self)
        self.UserName_TextBox.installEventFilter(self)

        self.all_tracks = track_control_controller()
        track_ids = self.all_tracks.get_names_of_controllers()
        string_track_ids = [str(x) for x in track_ids]
        self.Track_comboBox.addItems(string_track_ids)
        #self.Password_TextBox.setEchoMode(QLineEdit.Password)
        self.main_wind = track_control_display(self.all_tracks.get_track_control_instance(self.Track_comboBox.currentText()))

    def timer_track_control(self):
        self.all_tracks.run_all_track_controllers_plc()
        self.main_wind.run_PLC()


    def open_main_window(self):
        if self.UserName_TextBox.toPlainText() =="" and self.Password_TextBox.toPlainText() == "":
            self.error_label.setText(" ")
            content = self.Track_comboBox.currentText()

            self.main_wind = track_control_display(self.all_tracks.get_track_control_instance(content))
            self.main_wind.show()
        else:
            self.error_label.setText("Error: username or password is incorrect")
            self.error_label.setStyleSheet("color: red;")

    def eventFilter(self, obj, event):
        if obj is self.Password_TextBox and event.type() == QtCore.QEvent.KeyPress:
            if event.key() in (QtCore.Qt.Key_Return, QtCore.Qt.Key_Enter):
                self.open_main_window()
                return True
        elif obj is self.UserName_TextBox and event.type() == QtCore.QEvent.KeyPress:
            if event.key() in (QtCore.Qt.Key_Return, QtCore.Qt.Key_Enter):
                self.open_main_window()
                return True
        return False

    def get_all_track_controllers(self):
        return self.all_tracks.track_controller_list
