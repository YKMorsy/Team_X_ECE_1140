from PyQt5.QtWidgets import QApplication, QFrame, QGridLayout, QAbstractItemView
from PyQt5.QtWidgets import QLabel, QPushButton, QRadioButton, QSlider, QSizePolicy, QTableWidget, QTableView, QAbstractItemView, QHeaderView
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItem
from fbs_runtime.application_context.PyQt5 import ApplicationContext

from TrainModel.Test import TestUI, ExpandedTableUI
from TrainModel.Passenger import PassengerUI
from TrainModel.FontStyles import *
from TrainModel.common import *
    
class MurphyUI(QFrame):
    def __init__(self):
        #Initialize parent class
        super().__init__()

        #Set up some basic window settings
        self.setGeometry(100,100, 500, 700)
        self.setWindowTitle("Train Model")
        self.setAttribute(Qt.WidgetAttribute.WA_AlwaysShowToolTips, True)
        
        #Set up list of expanded table windows
        self.expanded_tables = []

        #Declare labels & buttons
        self.testing_button = QPushButton("Test This Module...")
        self.train_info_select_label = QLabel("Train Information & Selection")
        self.train_info_select_table = QTableView()
        self.train_proxy_model = train_proxy_model
        self.train_info_model = train_info_model
        self.expand_table_button = QPushButton("Expand Table...")
        self.failure_generation_label = QLabel("Failure Generation")
        self.engine_failure_button = QPushButton("Generate Engine Failure for Selected Train")
        self.signal_pickup_failure_button = QPushButton("Generate Signal Pickup Failure for Selected Train")
        self.brake_failure_button = QPushButton("Generate Brake Failure for Selected Train")
        self.failure_removal_label = QLabel("Failure Removal")
        self.train_failure_removal_button = QPushButton("Remove all Failures for Selected Train")
        self.all_failure_removal_button = QPushButton("Remove all Train Failures")
        self.brake_failure_button = QPushButton("Generate Brake Failure for Selected Train")
        self.passenger_UI_button = QPushButton("Open Passenger UI for Selected Train")
            
        #Set up button functions
        self.expand_table_button.clicked.connect(self.launch_expanded_table)
        self.testing_button.clicked.connect(self.test_launch)
        self.engine_failure_button.clicked.connect(self.generate_engine_failure)
        self.signal_pickup_failure_button.clicked.connect(self.generate_signal_failure)
        self.brake_failure_button.clicked.connect(self.generate_brake_failure)
        self.train_failure_removal_button.clicked.connect(self.remove_train_failures)
        self.all_failure_removal_button.clicked.connect(self.remove_all_failures)
        self.passenger_UI_button.clicked.connect(self.open_passenger_window)

        #Set up the table settings
        self.train_proxy_model.setSourceModel(self.train_info_model)
        self.train_info_select_table.setModel(self.train_proxy_model)
        self.train_info_model.setHorizontalHeaderLabels(['Train ID', 'Velocity\n(MPH)', 'Distance\n(Feet)', 'Acceleration\n(Feet/s^2)', 'Commanded Engine Power\n(Watts)', 'Total Mass\n(Tons)', 'Braking', 
                                                                'Track Grade\n(°)', 'Passenger Count', 'Fault(s)', 'Interior Temperature\n(Fahrenheit)',
                                                                'Interior Lights\n(On/Off)', 'Exterior Lights\n(On/Off)', 'Left Doors\n(Open/Closed)', 
                                                                'Right Doors\n(Open/Closed)','Commanded Authority\n(True/False)', 'Commanded Setpoint Speed\n(MPH)',
                                                                'Total Length\n(Feet)', 'Width\n(Feet)', 'Height\n(Feet)',
                                                                'PA\n(On/Off)', 'Stop Announcement\n(On/Off)', 'Stop Text', 'Ad Displayed\n(Displayed/Off)'])

        self.train_info_select_table.verticalHeader().hide()
        self.train_info_select_table.setSortingEnabled(True)
        self.train_info_select_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.train_info_select_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.train_info_select_table.horizontalHeader().setHighlightSections(False)
        self.train_info_select_table.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.train_info_select_table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        
        #Rearrange table s.t. faults are the first column
        self.train_info_select_table.horizontalHeader().moveSection(9,1)
	
	    #Hide Distance Column
        self.train_info_select_table.setColumnHidden(2, True)

        #Set label fonts & buttons
        self.testing_button.setFont(small_font)
        self.train_info_select_label.setFont(section_font)
        self.train_info_select_table.setFont(normal_font)
        self.train_info_select_table.horizontalHeader().setFont(normal_font)
        self.train_info_select_table.verticalHeader().setFont(normal_font)
        self.expand_table_button.setFont(small_font)
        self.failure_generation_label.setFont(section_font)
        self.engine_failure_button.setFont(normal_font)
        self.signal_pickup_failure_button.setFont(normal_font)
        self.brake_failure_button.setFont(normal_font)
        self.failure_removal_label.setFont(section_font)
        self.train_failure_removal_button.setFont(normal_font)
        self.all_failure_removal_button.setFont(normal_font)
        self.passenger_UI_button.setFont(small_font)

        #Color labels & buttons
        self.testing_button.setStyleSheet(gold_button_stylesheet)
        self.train_info_select_label.setStyleSheet(section_label_stylesheet)
        self.train_info_select_table.setStyleSheet(table_stylesheet)
        self.train_info_select_table.setAlternatingRowColors(True)
        self.expand_table_button.setStyleSheet(yellow_button_stylesheet)
        self.failure_generation_label.setStyleSheet(section_label_stylesheet)
        self.engine_failure_button.setStyleSheet(red_button_stylesheet)
        self.signal_pickup_failure_button.setStyleSheet(red_button_stylesheet)
        self.brake_failure_button.setStyleSheet(red_button_stylesheet)
        self.failure_removal_label.setStyleSheet(section_label_stylesheet)
        self.train_failure_removal_button.setStyleSheet(green_button_stylesheet)
        self.all_failure_removal_button.setStyleSheet(green_button_stylesheet)
        self.passenger_UI_button.setStyleSheet(blue_button_stylesheet)

        #Make the buttons as small as possible
        self.testing_button.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        self.engine_failure_button.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        self.signal_pickup_failure_button.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        self.brake_failure_button.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        self.passenger_UI_button.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)

        #Declare the grid and add the necessary widgets to it
        murphy_grid = QGridLayout()
        murphy_grid.addWidget(self.testing_button, 0, 0, 1, 4, alignment=Qt.AlignCenter)
        murphy_grid.addWidget(self.train_info_select_label, 1, 0, 1, 4, alignment=Qt.AlignCenter)
        murphy_grid.addWidget(self.train_info_select_table, 2, 0, 1, 3)
        murphy_grid.addWidget(self.expand_table_button, 2, 3, alignment=Qt.AlignBottom | Qt.AlignLeft)
        murphy_grid.addWidget(self.passenger_UI_button, 3, 0, 1, 4, alignment=Qt.AlignCenter)
        murphy_grid.addWidget(self.failure_generation_label, 4, 0, 1, 4, alignment=Qt.AlignCenter)
        murphy_grid.addWidget(self.engine_failure_button, 5, 0, 1, 4, alignment=Qt.AlignCenter)
        murphy_grid.addWidget(self.signal_pickup_failure_button, 6, 0, 1, 4, alignment=Qt.AlignCenter)
        murphy_grid.addWidget(self.brake_failure_button, 7, 0, 1, 4, alignment=Qt.AlignCenter)
        murphy_grid.addWidget(self.failure_removal_label, 8, 0, 1, 4, alignment=Qt.AlignCenter)
        murphy_grid.addWidget(self.train_failure_removal_button, 9, 0, 1, 4, alignment=Qt.AlignCenter)
        murphy_grid.addWidget(self.all_failure_removal_button, 10, 0, 1, 4, alignment=Qt.AlignCenter)

        #Set up the window color pallete
        self.setObjectName("MurphyWindow")
        self.setStyleSheet('''#MurphyWindow {background-color: rgb(102,102,102); border: 3px solid black;}''')

        #Connect the grid, and show the window
        self.setLayout(murphy_grid)

	#This function launches an expanded table
    def launch_expanded_table(self):
        temp = ExpandedTableUI(self.train_proxy_model)
        temp.show()
        for i, c in enumerate(self.expanded_tables):
            if not c.isVisible():
                self.expanded_tables[i] = temp
                return
        self.expanded_tables.append(temp) 

    def open_passenger_window(self):
        try:
            #First, get the selected ID
            ID = int(self.train_proxy_model.data(self.train_proxy_model.index(self.train_info_select_table.selectedIndexes()[0].row(), 0)))

            #Open the window
            temp = PassengerUI(self, ID)
            temp.show()
            for i, c in enumerate(self.expanded_tables):
                if not c.isVisible():
                    self.expanded_tables[i] = temp
                    return
            self.expanded_tables.append(temp) 

        #If there is an index error, then there is no selection, and we should throw up an error
        except IndexError:
            my_message(msg = "You have not selected a train!\nPlease select a train and try again.", title = "No Train Selected", error = True, parent = self).exec()


    def generate_brake_failure(self):
        try:
            #First, get the selected ID
            ID = int(self.train_proxy_model.data(self.train_proxy_model.index(self.train_info_select_table.selectedIndexes()[0].row(), 0)))

            #Throw up a warning window to make sure it wasn't a misclick
            if not my_warning(msg = "Are you sure you want to generate a brake\nfailure for Train " + str(ID) + "?", title = "Failure Generation Confirmation", parent = self).exec(): return
            
            #Next, update the actual train
            handler.train_list[ID].generate_brake_failure()

            #Finally, update the table
            for i in range(self.train_info_model.rowCount()):
                if int(self.train_info_model.item(i, 0).text()) == ID:
                    
                    #Figure out what the new fault string should be
                    fault = "None"
                    T = handler.train_list[ID]
                    if T.brake_failure and not T.engine_failure and not T.signal_failure: fault = "Brake Failure"
                    elif T.brake_failure and T.engine_failure and not T.signal_failure: fault = "Brake Failure, Engine Failure"
                    elif T.brake_failure and not T.engine_failure and T.signal_failure: fault = "Brake Failure, Signal Pickup Failure"
                    elif T.brake_failure and T.engine_failure and T.signal_failure: fault = "Brake Failure, Engine Failure, Signal Pickup Failure"


                    self.train_info_model.setItem(i, 9, QStandardItem(fault)) 

            #Show a confirmation message to the user
            my_message(msg = "Brake failure successfully generated for Train " + str(ID) + "!", title = "Brake Failure Generated", error = False, parent = self).exec()

        #If there is an index error, then there is no selection, and we should throw up an error
        except IndexError:
            my_message(msg = "You have not selected a train!\nPlease select a train and try again.", title = "No Train Selected", error = True, parent = self).exec()
           

    def generate_engine_failure(self):
        try:
            #First, get the selected ID
            ID = int(self.train_proxy_model.data(self.train_proxy_model.index(self.train_info_select_table.selectedIndexes()[0].row(), 0)))

            #Throw up a warning window to make sure it wasn't a misclick
            if not my_warning(msg = "Are you sure you want to generate an engine\nfailure for Train " + str(ID) + "?", title = "Failure Generation Confirmation", parent = self).exec(): return
            
            #Next, update the actual train
            handler.train_list[ID].generate_engine_failure()

            #Finally, update the table
            for i in range(self.train_info_model.rowCount()):
                if int(self.train_info_model.item(i, 0).text()) == ID:

                    #Figure out what the new fault string should be
                    fault = "None"
                    T = handler.train_list[ID]
                    if not T.brake_failure and T.engine_failure and not T.signal_failure: fault = "Engine Failure"
                    if T.brake_failure and T.engine_failure and not T.signal_failure: fault = "Brake Failure, Engine Failure"
                    elif not T.brake_failure and T.engine_failure and T.signal_failure: fault = "Engine Failure, Signal Pickup Failure"
                    elif T.brake_failure and T.engine_failure and T.signal_failure: fault = "Brake Failure, Engine Failure, Signal Pickup Failure"

                    self.train_info_model.setItem(i, 9, QStandardItem(fault))
            
            #Show a confirmation message to the user
            my_message(msg = "Engine failure successfully generated for Train " + str(ID) + "!", title = "Engine Failure Generated", error = False, parent = self).exec()

        #If there is an index error, then there is no selection, and we should throw up an error
        except IndexError:
            my_message(msg = "You have not selected a train!\nPlease select a train and try again.", title = "No Train Selected", error = True, parent = self).exec()

    def generate_signal_failure(self):
        try:
            #First, get the selected ID
            ID = int(self.train_proxy_model.data(self.train_proxy_model.index(self.train_info_select_table.selectedIndexes()[0].row(), 0)))
            
            #Throw up a warning window to make sure it wasn't a misclick
            if not my_warning(msg = "Are you sure you want to generate a signal\npickup failure for Train " + str(ID) + "?", title = "Failure Generation Confirmation", parent = self).exec(): return
            
            #Next, update the actual train
            handler.train_list[ID].generate_signal_pickup_failure()

            #Finally, update the table
            for i in range(self.train_info_model.rowCount()):
                if int(self.train_info_model.item(i, 0).text()) == ID:
                    
                    #Figure out what the new fault string should be
                    fault = "None"
                    T = handler.train_list[ID]
                    if not T.brake_failure and not T.engine_failure and T.signal_failure: fault = "Signal Pickup Failure"
                    elif T.brake_failure and not T.engine_failure and T.signal_failure: fault = "Brake Failure, Signal Pickup Failure"
                    elif T.brake_failure and T.engine_failure and T.signal_failure: fault = "Brake Failure, Engine Failure, Signal Pickup Failure"
                    elif not T.brake_failure and T.engine_failure and T.signal_failure: fault = "Engine Failure, Signal Pickup Failure"

                    self.train_info_model.setItem(i, 9, QStandardItem(fault))

            #Show a confirmation message to the user
            my_message(msg = "Signal pickup failure successfully generated for Train " + str(ID) + "!", title = "Signal Pickup Failure Generated", error = False, parent = self).exec()

        #If there is an index error, then there is no selection, and we should throw up an error
        except IndexError:
            my_message(msg = "You have not selected a train!\nPlease select a train and try again.", title = "No Train Selected", error = True, parent = self).exec()

    def remove_train_failures(self):
        try:
            #First, get the selected ID
            ID = int(self.train_proxy_model.data(self.train_proxy_model.index(self.train_info_select_table.selectedIndexes()[0].row(), 0)))
            
            #Throw up a warning window to make sure it wasn't a misclick
            if not my_warning(msg = "Are you sure you want to remove all failures for Train " + str(ID) + "?", title = "Failure Removal Confirmation", parent = self).exec(): return
            
            #Next, update the actual train
            handler.train_list[ID].clear_all_failures()

            #Finally, update the table
            for i in range(self.train_info_model.rowCount()):
                if int(self.train_info_model.item(i, 0).text()) == ID:
                    self.train_info_model.setItem(i, 8, QStandardItem("None"))

            #Show a confirmation message to the user
            my_message(msg = "All failures have been successfully removed for Train " + str(ID) + "!", title = "Failures Removed", error = False, parent = self).exec()

        #If there is an index error, then there is no selection, and we should throw up an error
        except IndexError:
            my_message(msg = "You have not selected a train!\nPlease select a train and try again.", title = "No Train Selected", error = True, parent = self).exec()        

    def remove_all_failures(self):
        #Throw an error and return if there are no trains in existance
        if (len(handler.train_list)==0):
             my_message(msg = "There are no trains to clear failures from!", title = "No Trains", error = True, parent = self).exec()
             return
            
        #Throw up a warning window to make sure it wasn't a misclick
        if not my_warning(msg = "Are you sure you want to remove all failures for all trains?" , title = "All Failure Removal Confirmation", parent = self).exec(): return
        
        #Next, update the actual trains
        handler.clear_all_failures()

        #Finally, update the table
        for i in range(self.train_info_model.rowCount()):
            self.train_info_model.setItem(i, 8, QStandardItem("None"))

        #Show a confirmation message to the user
        my_message(msg = "All failures have been successfully removed for all trains!", title = "All Failures Removed", error = False, parent = self).exec()

    #This function launches the test UI
    def test_launch(self):
        if(my_warning("Are you sure that you want to launch the testing windows? \n         (All other activity will be stopped while testing)", title = "Test Launch Confirmation", parent = self).exec()):
            self.my_Test_UI = TestUI()
            self.my_Test_UI.show()

    def update(self):
		#Update the trains and get the data back
        data = handler.get_UI_train_matrix()
		
		#Update the table
        for i in range(train_info_model.rowCount()):
            row_tool_tip = list_to_tooltip(data[i])
            for j in range(train_info_model.columnCount()):
                q = QStandardItem(data[i][j])
                #q.setToolTip(row_tool_tip)
                train_info_model.setItem(i, j, q)

#dlg = my_message("You have not selected a train!\nPlease select a train and try again.", title = "No Train Selected", parent = murphy_window)
#dlg.exec()

#dlg = my_warning("Are you sure you want to generate a brake failure for Train 8?", title = "Failure Generation Confirmation", parent = murphy_window)
#print(dlg.exec())

#appctxt = ApplicationContext()
#app = QApplication([])
#murphy_window = MurphyUI()

#Show the murphy window
#murphy_window.show()

#Start the event loop
#appctxt.app.exec()
