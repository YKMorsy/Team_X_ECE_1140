import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import Qt
from track_controller.track_control_controller import track_control_controller
import copy
from track_controller.test_window import test_window

qt_creator_file = "track_controller.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType("track_controller/"+qt_creator_file)

class track_control_display (QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, trc):
        self.testWind = test_window(trc)
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.track_data = trc
        self.setupUi(self)

        self.CurrentlyRunningLabel.setText("Currently Running: "+ self.track_data.get_PLC())
        text=open(self.track_data.get_PLC()).read()
        self.PLCTextBrowser.setPlainText(text)

        self.TestPLCButton.clicked.connect(self.open_test)
        self.UploadPLCButton.clicked.connect(self.openFileNameDialog)
        self.maint_make_change.clicked.connect(self.make_changes)
        self.maintenance_check_box.setChecked(self.track_data.get_maintenance_mode())
        self.maintenance_check_box.stateChanged.connect(self.maintence_box_checked)

        self.maint_SwitchPosTable.itemChanged.connect(self.item_changed)
        self.maint_Auth.itemChanged.connect(self.item_changed)
        self.maint_Occ_table.itemChanged.connect(self.item_changed)
        self.maint_LightColorTable.itemChanged.connect(self.light_item_changed)
        self.maint_RailwayCrossingTable.itemChanged.connect(self.item_changed)
        self.maint_StatusTable.itemChanged.connect(self.item_changed)
        self.maint_StatusTable_2.itemChanged.connect(self.item_changed)

        self.update_tables()

    def maintence_box_checked(self):
        self.track_data.set_maintenance_mode(self.maintenance_check_box.isChecked())
        self.update_tables()

    def item_changed(self, item):
        if item.column() ==1:
            if item.data(0) == "F" or item.data(0) == "f" or item.data(0) == "0":
                item.setText( "False" )
            elif item.data(0) == "T" or item.data(0) == "t" or item.data(0) == "1":
                item.setText( "True" )
            self.unsaved_changes_label.setText("Warning: your have unsaved changes")

    def light_item_changed(self, item):
        if item.column() ==1:
            if item.data(0) == "R" or item.data(0) == "r" or item.data(0) == "red":
                item.setText( "Red" )
            elif item.data(0) == "Y" or item.data(0) == "y" or item.data(0) == "yellow":
                item.setText( "Yellow" )
            elif item.data(0) == "G" or item.data(0) == "g" or item.data(0) == "green":
                item.setText( "Green" )
            self.unsaved_changes_label.setText("Warning: your have unsaved changes")

    def open_test(self):
        if self.testWind.isVisible():
            self.testWind.hide()
        else:
            self.testWind.show()

    def openFileNameDialog(self):
        if(not(self.track_data.get_maintenance_mode())):
            self.ErrorBoxLabel.setText("Cannot upload new file while not in maintence mode")
            return

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            issue = self.track_data.set_PLC(fileName)
            if(isinstance(issue, str)):
                self.ErrorBoxLabel.setText("Cannot run selected file: " + issue)
            else:
                self.ErrorBoxLabel.setText("")
                self.CurrentlyRunningLabel.setText("Currently Running: "+ fileName)
                text=open(fileName).read()
                self.PLCTextBrowser.setPlainText(text)

    def update_tables(self):
        self.update_table(self.track_data.get_switch_positions(), self.SwitchPosTable, False)
        self.update_table(self.track_data.get_switch_positions(), self.maint_SwitchPosTable, self.maintenance_check_box.isChecked())
        self.update_table(self.track_data.get_authority(), self.maint_Auth, False)
        self.update_table(self.track_data.get_commanded_speed(), self.maint_CS, False)
        self.update_table(self.track_data.get_occupancy(), self.maint_Occ_table, False)
        self.update_table(self.track_data.get_railway_crossings(), self.RailwayCrossingTable, False)
        self.update_light_table(self.track_data.get_light_colors(), self.LightColorTable, False)
        self.update_light_table(self.track_data.get_light_colors(), self.maint_LightColorTable, self.maintenance_check_box.isChecked())
        self.update_table(self.track_data.get_railway_crossings(), self.maint_RailwayCrossingTable, self.maintenance_check_box.isChecked())
        self.update_table(self.track_data.get_statuses(), self.maint_StatusTable, self.maintenance_check_box.isChecked())
        self.update_table(self.track_data.get_statuses(), self.maint_StatusTable_2, False)
        self.unsaved_changes_label.setText("")

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
                    item = QTableWidgetItem(str(val))

                if column ==0:
                    item = QTableWidgetItem(str(key))
                if not(changable) or column==0 :
                    item.setFlags(QtCore.Qt.ItemIsEditable)
                table.setItem(row, column, item)
            row=row+1

    def make_changes(self):
        self.get_table_change(self.track_data.get_switch_positions(), self.maint_SwitchPosTable)
        self.get_table_change(self.track_data.get_authority(), self.maint_auth)
        self.get_table_change(self.track_data.get_commanded_speed(), self.maint_CS)
        self.get_table_change(self.track_data.get_occupancy(), self.maint_Occ_table)        
        self.get_light_table_change(self.track_data.get_light_colors(), self.maint_LightColorTable)
        self.get_table_change(self.track_data.get_railway_crossings(), self.maint_RailwayCrossingTable)
        self.get_table_change(self.track_data.get_statuses(), self.maint_StatusTable)
        self.get_table_change(self.track_data.get_statuses(), self.maint_StatusTable_2)
        self.unsaved_changes_label.setText("")
        self.update_tables()

    def get_table_change (self, table_data, table):
        rowC = table.rowCount()
        for row in range(rowC):
            table_data[int(row)] = table.item(row, 1).data(0)

    def get_light_table_change (self, table_data, table):
        rowC = table.rowCount()
        for row in range(rowC):
            if str(block) == table.item(row, 0).data(0):
                if(table.item(row, 1).data(0) =="Green"):
                    table_data[int(row)] = [True, True]
                elif(table.item(row, 1).data(0) =="Yellow"):
                    table_data[int(row)] = [False, True]
                elif(table.item(row, 1).data(0) =="Red"):
                    table_data[int(row)] = [False, False]
                    
    def run_PLC(self):
        #self.track_data.ParsePLC()
        self.update_tables()
        #print("RUN PLC")