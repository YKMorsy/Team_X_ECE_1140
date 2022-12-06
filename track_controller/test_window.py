import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import Qt
from track_controller.track_control_controller import track_control_controller
import copy
from track_controller.track_controller import WaysideController

TestingPLCWind = "testing_PLC.ui"
Ui_TestingWindow, QtBaseClass = uic.loadUiType("track_controller/"+TestingPLCWind)

class test_window (QtWidgets.QMainWindow, Ui_TestingWindow):
    def __init__(self, trc):
        self.track_control_data = copy.copy(trc)
        QtWidgets.QMainWindow.__init__(self)
        Ui_TestingWindow.__init__(self)
        self.setupUi(self)
        self.UploadNewPLCButton.clicked.connect(self.open_file_name_dialog)
        self.run_PLC_button.clicked.connect(self.run_plc)

        self.CurrentPLCLabel.setText("Currently Running: "+ self.track_control_data.get_PLC())

        self.SwitchPosInput_Table.itemChanged.connect(self.item_changed)
        self.Authority_Table.itemChanged.connect(self.item_changed)
        self.Occupancy_Table.itemChanged.connect(self.item_changed)
        self.Status_Table.itemChanged.connect(self.item_changed)

        cspeed = self.track_control_data.get_commanded_speed()
        #self.commanded_speed_label.setText("Commanded Speed: "+ str(cspeed))

        self.update_tables()

    def open_file_name_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            issue = self.track_control_data.set_PLC(fileName)
            if(isinstance(issue, str)):
                self.ErrorBoxLabel.setText("Cannot run selected file: " + issue)
            else:
                self.ErrorBoxLabel.setText(" ")
                self.track_control_data.set_PLC(fileName)
                self.CurrentPLCLabel.setText("Currently Running: "+ fileName)
    
    def item_changed(self, item):
        if item.column() ==1:
            if item.data(0) == "F" or item.data(0) == "f" or item.data(0) == "0":
                item.setText( "False" )
            elif item.data(0) == "T" or item.data(0) == "t" or item.data(0) == "1":
                item.setText( "True" )

    def update_tables(self):
        self.update_table(self.track_control_data.get_switch_positions(), self.SwitchPosInput_Table, True)
        self.update_table(self.track_control_data.get_authority(), self.Authority_Table, True)
        self.update_table(self.track_control_data.get_suggested_speed(), self.Suggested_Speed_Table, True)
        self.update_table(self.track_control_data.get_speed_limit(), self.speed_limit_table, True)
        self.update_table(self.track_control_data.get_occupancy(), self.Occupancy_Table, True)
        self.update_table(self.track_control_data.get_statuses(), self.Status_Table, True)

        self.update_table(self.track_control_data.get_switch_positions(), self.SwitchPosOutput_Table, False)
        self.update_light_table(self.track_control_data.get_light_colors(), self.LightColor_Table, False)
        self.update_table(self.track_control_data.get_railway_crossings(), self.RailwayCrossing_Table, False)
        self.update_table(self.track_control_data.get_commanded_speed(), self.Commanded_Speed_Table, False)
        
    def update_table(self, data, table, changable):
        numrows = len(data)
        table.setRowCount(numrows)
        row=0
        for key, val in data.items():
            for column in range(2):
                item = QTableWidgetItem(str(val))
                if column ==0:
                    item = QTableWidgetItem(str(key))
                if not(changable) or column==0 :
                    item.setFlags(QtCore.Qt.ItemIsEditable)
                table.setItem(row, column, item)
            row=row+1

    def update_light_table(self, data, table, changable):
        numrows = len(data)
        table.setRowCount(numrows)
        row=0
        for key, val in data.items():
            for column in range(2):
                if(column == 1):
                    if(val[0] and val[1]):
                        item = QTableWidgetItem("Green")
                    elif(val[0] or val[1]):
                        item = QTableWidgetItem("Yellow")
                    else:
                        item = QTableWidgetItem("Red")
                else:
                    item = QTableWidgetItem(str(key))
                if not(changable) or column==0 :
                    item.setFlags(QtCore.Qt.ItemIsEditable)
                table.setItem(row, column, item)
            row=row+1

    def run_plc (self):
        self.make_changes()
        self.track_control_data.parse_plc()
        self.update_tables()

    def make_changes(self):
        self.get_table_change(self.track_control_data.get_switch_positions(), self.SwitchPosInput_Table)
        self.get_table_change(self.track_control_data.get_suggested_speed(), self.Suggested_Speed_Table)
        self.get_table_change(self.track_control_data.get_speed_limit(), self.speed_limit_table)
        self.get_table_change(self.track_control_data.get_authority(), self.Authority_Table)
        self.get_table_change(self.track_control_data.get_occupancy(), self.Occupancy_Table)
        self.get_table_change(self.track_control_data.get_statuses(), self.Status_Table)
        self.update_tables()

    def get_table_change (self, table_data, table):
        rowC = table.rowCount()
        for row in range(rowC):
            table_data.update({int(table.item(row, 0).data(0)): table.item(row, 1).data(0) })

