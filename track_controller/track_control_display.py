import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import Qt
from track_control_controller import track_control_controller
import copy


qt_creator_file = "track_controller.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType("track_controller/"+qt_creator_file)

TestingPLCWind = "testing_PLC.ui"
Ui_TestingWindow, QtBaseClass = uic.loadUiType("track_controller/"+TestingPLCWind)

sign_in_wind = "sign_in.ui"
Ui_sign_in_window, QtBaseClass = uic.loadUiType("track_controller/"+sign_in_wind)

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

    def open_main_window(self):
        if self.UserName_TextBox.toPlainText() =="" and self.Password_TextBox.toPlainText() == "":
            content = self.Track_comboBox.currentText()

            self.main_wind = MainWindow(self.all_tracks.get_track_control_instance(content))
            self.main_wind.show()

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

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, trc):
        self.testWind = test_window(trc)
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.track_data = trc
        self.setupUi(self)

        self.CurrentlyRunningLabel.setText("Currently Running: "+ self.track_data.get_PLC())
        text=open(self.track_data.get_PLC()).read()
        self.PLCTextBrowser.setPlainText(text)

        self.TestPLCButton.clicked.connect(self.OpenTest)
        self.UploadPLCButton.clicked.connect(self.openFileNameDialog)
        self.maint_make_change.clicked.connect(self.make_changes)
        self.maintenance_check_box.stateChanged.connect(self.update_tables)

        self.maint_SwitchPosTable.itemChanged.connect(self.item_changed)
        self.maint_LightColorTable.itemChanged.connect(self.light_item_changed)
        self.maint_RailwayCrossingTable.itemChanged.connect(self.item_changed)
        self.maint_StatusTable.itemChanged.connect(self.item_changed)

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

    def OpenTest(self):
        if self.testWind.isVisible():
            self.testWind.hide()
        else:
            self.testWind.show()

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            self.track_data.set_PLC(fileName)
            self.CurrentlyRunningLabel.setText("Currently Running: "+ fileName)
            text=open(fileName).read()
            self.PLCTextBrowser.setPlainText(text)
            #TODO: Save File Path As Variable
            #TODO: Send File To Be Parsed as PLC

    def update_tables(self):
        self.update_table(self.track_data.get_switch_positions(), self.SwitchPosTable, False)
        self.update_table(self.track_data.get_switch_positions(), self.maint_SwitchPosTable, self.maintenance_check_box.isChecked())
        self.update_table(self.track_data.get_railway_crossings(), self.RailwayCrossingTable, False)
        self.update_light_table(self.track_data.get_light_colors(), self.LightColorTable, False)
        self.update_light_table(self.track_data.get_light_colors(), self.maint_LightColorTable, self.maintenance_check_box.isChecked())
        self.update_table(self.track_data.get_railway_crossings(), self.maint_RailwayCrossingTable, self.maintenance_check_box.isChecked())
        self.update_table(self.track_data.get_statuses(), self.maint_StatusTable, self.maintenance_check_box.isChecked())
        self.unsaved_changes_label.setText("")

    def update_table(self, data, table, changable):
        numrows = len(data)
        table.setRowCount(numrows)
        for row in range(numrows):
            for column in range(2):
                item = QTableWidgetItem(str(data[row][column]))
                if not(changable) or column==0 :
                    item.setFlags(QtCore.Qt.ItemIsEditable)
                table.setItem(row, column, item)

    def update_light_table(self, data, table, changable):
        numrows = len(data)
        table.setRowCount(numrows)
        for row in range(numrows):
            for column in range(2):
                if(column == 1):
                    if(data[row][column] and data[row][column+1]):
                        item = QTableWidgetItem("Green")
                    elif(data[row][column] or data[row][column+1]):
                        item = QTableWidgetItem("Yellow")
                    else:
                        item = QTableWidgetItem("Red")
                else:
                    item = QTableWidgetItem(str(data[row][column]))
                if not(changable) or column==0 :
                    item.setFlags(QtCore.Qt.ItemIsEditable)
                table.setItem(row, column, item)

    def make_changes(self):
        self.get_table_change(self.track_data.get_switch_positions(), self.maint_SwitchPosTable)
        self.get_light_table_change(self.track_data.get_light_colors(), self.maint_LightColorTable)
        self.get_table_change(self.track_data.get_railway_crossings(), self.maint_RailwayCrossingTable)
        self.get_table_change(self.track_data.get_statuses(), self.maint_StatusTable)
        self.unsaved_changes_label.setText("")
        self.update_tables()

    def get_table_change (self, table_data, table):
        rowC = table.rowCount()
        for row in range(rowC):
            for dat_row in range(rowC):
                (block, state) = table_data[dat_row]
                if str(block) == table.item(row, 0).data(0):
                    table_data[dat_row] = (block, table.item(row, 1).data(0))

    def get_light_table_change (self, table_data, table):
        rowC = table.rowCount()
        for row in range(rowC):
            for dat_row in range(rowC):
                (block, state1, state2) = table_data[dat_row]
                if str(block) == table.item(row, 0).data(0):
                    if(table.item(row, 1).data(0) =="Green"):
                        table_data[dat_row] = (block, True, True)
                    elif(table.item(row, 1).data(0) =="Yellow"):
                        table_data[dat_row] = (block, False, True)
                    elif(table.item(row, 1).data(0) =="Red"):
                        table_data[dat_row] = (block, False, False)
                    
class test_window (QtWidgets.QMainWindow, Ui_TestingWindow):
    def __init__(self, trc):
        self.track_control_data = copy.copy(trc)
        QtWidgets.QMainWindow.__init__(self)
        Ui_TestingWindow.__init__(self)
        self.setupUi(self)
        self.UploadNewPLCButton.clicked.connect(self.openFileNameDialog)
        self.run_PLC_button.clicked.connect(self.run_plc)

        self.CurrentPLCLabel.setText("Currently Running: "+ self.track_control_data.get_PLC())

        self.SwitchPosInput_Table.itemChanged.connect(self.item_changed)
        self.Authority_Table.itemChanged.connect(self.item_changed)
        self.Occupancy_Table.itemChanged.connect(self.item_changed)

        cspeed = self.track_control_data.get_commanded_speed()
        #self.commanded_speed_label.setText("Commanded Speed: "+ str(cspeed))

        self.update_tables()

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            self.track_data.set_PLC(filename)
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
        self.update_table(self.track_control_data.get_occupancy(), self.Occupancy_Table, True)
        self.update_table(self.track_control_data.get_switch_positions(), self.SwitchPosOutput_Table, False)
        self.update_light_table(self.track_control_data.get_light_colors(), self.LightColor_Table, False)
        self.update_table(self.track_control_data.get_railway_crossings(), self.RailwayCrossing_Table, False)
        self.update_table(self.track_control_data.get_commanded_speed(), self.Commanded_Speed_Table, False)
        
    def update_table(self, data, table, changable):
        numrows = len(data)
        table.setRowCount(numrows)
        for row in range(numrows):
            for column in range(2):
                item = QTableWidgetItem(str(data[row][column]))
                if not(changable) or column==0 :
                    item.setFlags(QtCore.Qt.ItemIsEditable)
                table.setItem(row, column, item)

    def update_light_table(self, data, table, changable):
        numrows = len(data)
        table.setRowCount(numrows)
        for row in range(numrows):
            for column in range(2):
                if(column == 1):
                    if(data[row][column] and data[row][column+1]):
                        item = QTableWidgetItem("Green")
                    elif(data[row][column] or data[row][column+1]):
                        item = QTableWidgetItem("Yellow")
                    else:
                        item = QTableWidgetItem("Red")
                else:
                    item = QTableWidgetItem(str(data[row][column]))
                if not(changable) or column==0 :
                    item.setFlags(QtCore.Qt.ItemIsEditable)
                table.setItem(row, column, item)

    def run_plc (self):
        self.make_changes()
        self.track_control_data.ParsePLC()
        self.update_tables()

    def make_changes(self):
        self.get_table_change(self.track_control_data.get_switch_positions(), self.SwitchPosInput_Table)
        self.get_table_change(self.track_control_data.get_suggested_speed(), self.Suggested_Speed_Table)
        self.get_table_change(self.track_control_data.get_authority(), self.Authority_Table)
        self.get_table_change(self.track_control_data.get_occupancy(), self.Occupancy_Table)
        self.update_tables()

    def get_table_change (self, table_data, table):
        rowC = table.rowCount()
        for row in range(rowC):
            for dat_row in range(rowC):
                (block, state) = table_data[dat_row]
                if str(block) == table.item(row, 0).data(0):
                    table_data[dat_row] = (block, table.item(row, 1).data(0))


app = QtWidgets.QApplication(sys.argv)
window = sign_in_window()
window.show()
app.exec_()