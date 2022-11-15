from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets
from PyQt5 import QtCore as qtc

import pandas as pd
import numpy as np

class DispatchTrainWindow(QWidget):

    submitClicked = qtc.pyqtSignal(pd.DataFrame)

    def __init__(self, parent):
        self.parent = parent
        super().__init__()

        self.setWindowTitle("Dispatch Train(s)")

        self.train_line_station_df = pd.DataFrame()

        # Define layout
        layout1 = QVBoxLayout()

        # Button for inputting schedule from file
        self.load_schedule_button = QPushButton("Upload Train Schedule")
        self.load_schedule_button.setCheckable(True)
        self.load_schedule_button.clicked.connect(self.load_schedule_handler)

        # Combo box with list of available lines from parent class
        self.select_line_combo_box = QComboBox()
        self.select_line_combo_box.addItems(self.parent.unique_lines)
        self.select_line_combo_box.currentTextChanged.connect(self.line_combo_box_txt_changed)

        # Combo box with list of available stations from parent class
        # Updates when select_line_combo_box is updated
        self.select_station_combo_box = QListWidget()
        self.select_station_combo_box.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.select_station_combo_box.itemSelectionChanged.connect(self.select_station_handler)

        # Button to submit selected stations and line
        self.confirm_button = QPushButton("Submit")
        self.confirm_button.setCheckable(True)
        self.confirm_button.clicked.connect(self.submit_handler)
        
        layout1.addWidget(self.load_schedule_button)
        layout1.addWidget(self.select_line_combo_box)
        layout1.addWidget(self.select_station_combo_box)
        layout1.addWidget(self.confirm_button)

        self.setLayout(layout1)

    def submit_handler(self):
        self.submitClicked.emit(self.train_line_station_df)
        self.close()

    def select_station_handler(self):
        items = self.select_station_combo_box.selectedItems()
        self.selected_stations = []
        self.selected_line = []
        for i in range(len(items)):
            self.selected_line.append(self.selected_line_cur)
            self.selected_stations.append(str(self.select_station_combo_box.selectedItems()[i].text()))

        train_line_station = {"Line": self.selected_line, "Infrastructure": self.selected_stations}
        self.train_line_station_df = pd.DataFrame(train_line_station)
        # print(self.train_line_station_df)

    def line_combo_box_txt_changed(self, s):
        # Clear stations text box
        self.select_station_combo_box.clear()

        # Filter stations based on line
        self.line_stations = self.parent.block_station
        self.line_stations = self.line_stations.loc[self.line_stations["Line"] == s]

        # Add stations to combo box
        self.select_station_combo_box.addItems(self.line_stations["Infrastructure"])

        self.selected_line_cur = s

    def load_schedule_handler(self):
        # Load file as dataframe 
        file_path = self.open_file()
        df_track_layout = pd.read_excel(file_path)

        self.train_line_station_df = df_track_layout.loc[:,["Line", "Infrastructure"]]

        # print(self.train_line_station_df)

    def open_file(self):
        filename = QFileDialog.getOpenFileName()
        path = filename[0]
        return path

class TestUI(QWidget):

    def __init__(self, parent):
        self.parent = parent
        super().__init__()

        self.setWindowTitle("Test UI")

        # Define main layout
        self.layout0 = QVBoxLayout()
        self.title_resolve_fault = QVBoxLayout()
        self.title_Authority = QVBoxLayout()
        self.layout_resolve_fault = QHBoxLayout()
        self.layout_Authority_block = QVBoxLayout()

        ########### Create layout with 2 drop downs for block chooser and crossing status ###########
        # Section label
        TitleWidget = QLabel("Crossing Status")
        font = TitleWidget.font()
        font.setPointSize(10)
        TitleWidget.setFont(font)
        self.layout0.addWidget(TitleWidget)
        
        #Layout
        self.layout_crossing_status = QHBoxLayout()

        # Block chooser
        self.block_crossing_combo_box = QComboBox()
        # Add items to combo box
        for i in range(0, len(self.parent.block_crossing)):
            # print(str(self.parent.all_blocks[i]))
            self.block_crossing_combo_box.addItems([str(self.parent.block_crossing[i])])

        # Status chooser
        self.status_crossing_combo_box = QComboBox()
        self.status_crossing_combo_box.addItems(["Open", "Close"])

        # Add Button
        self.add_crossing_button = QPushButton("Add")
        self.add_crossing_button.setCheckable(True)
        self.add_crossing_button.clicked.connect(self.add_crossing_handler)

        self.layout_crossing_status.addWidget(self.block_crossing_combo_box)
        self.layout_crossing_status.addWidget(self.status_crossing_combo_box)
        self.layout_crossing_status.addWidget(self.add_crossing_button)

        self.layout0.addLayout(self.layout_crossing_status)

        ########### Create layout with 2 drop downs for switch position ###########
        # Section label
        TitleWidget = QLabel("Switch Position")
        font = TitleWidget.font()
        font.setPointSize(10)
        TitleWidget.setFont(font)
        self.layout0.addWidget(TitleWidget)
        
        #Layout
        self.layout_switch_position = QHBoxLayout()

        # Block chooser
        self.swith_from_combo_box = QComboBox()
        self.swith_from_combo_box.addItems(["5"])

        # Status chooser
        self.swith_to_combo_box = QComboBox()
        self.swith_to_combo_box.addItems(["6", "11"])

        # Add Button
        self.switch_position_button = QPushButton("Add")
        self.switch_position_button.setCheckable(True)
        self.switch_position_button.clicked.connect(self.switch_position_handler)

        self.layout_switch_position.addWidget(self.swith_from_combo_box)
        self.layout_switch_position.addWidget(self.swith_to_combo_box)
        self.layout_switch_position.addWidget(self.switch_position_button)

        self.layout0.addLayout(self.layout_switch_position)

        ########### Create layout with threshold input ###########
        # Section label
        TitleWidget = QLabel("Threshold")
        font = TitleWidget.font()
        font.setPointSize(10)
        TitleWidget.setFont(font)
        self.layout0.addWidget(TitleWidget)
        
        #Layout
        self.layout_switch_position = QHBoxLayout()

        # Threshold input
        self.threhsold_input_line = QLineEdit()
        self.threhsold_input_line.setPlaceholderText("Threshold")

        # Add Button
        self.threshold_add_button = QPushButton("Add")
        self.threshold_add_button.setCheckable(True)
        self.threshold_add_button.clicked.connect(self.threhsold_add_handler)

        self.layout_switch_position.addWidget(self.threhsold_input_line)
        self.layout_switch_position.addWidget(self.threshold_add_button)

        self.layout0.addLayout(self.layout_switch_position)

        ########### Create layout with 1 drop downs for adding fault ###########
        # Section label
        TitleWidget = QLabel("Add Fault")
        font = TitleWidget.font()
        font.setPointSize(10)
        TitleWidget.setFont(font)
        self.layout0.addWidget(TitleWidget)
        
        #Layout
        self.layout_add_fault = QHBoxLayout()

        # Block chooser
        self.block_fault_combo_box = QComboBox()
        # Add items to combo box
        for i in range(0, len(self.parent.all_blocks)):
            # print(str(self.parent.all_blocks[i]))
            self.block_fault_combo_box.addItems([str(self.parent.all_blocks[i])])

        # Add Button
        self.add_fault_button = QPushButton("Add")
        self.add_fault_button.setCheckable(True)
        self.add_fault_button.clicked.connect(self.add_fault_handler)

        self.layout_add_fault.addWidget(self.block_fault_combo_box)
        self.layout_add_fault.addWidget(self.add_fault_button)

        self.layout0.addLayout(self.layout_add_fault)

        ####### Title for resolve fault layout #######
        # Section label
        TitleWidget = QLabel("Resolve Fault")
        font = TitleWidget.font()
        font.setPointSize(10)
        TitleWidget.setFont(font)
        self.title_resolve_fault.addWidget(TitleWidget)

        self.my_timer = qtc.QTimer()
        self.my_timer.timeout.connect(self.create_maintenance_widgest)

        ####### Title for Authority #######
        # Section label
        TitleWidget = QLabel("Authority")
        font = TitleWidget.font()
        font.setPointSize(10)
        TitleWidget.setFont(font)
        self.title_Authority.addWidget(TitleWidget)

        self.my_timer.timeout.connect(self.create_authority_widget)

        self.my_timer.start(3000) #interval

        self.layout0.addLayout(self.title_resolve_fault)
        self.title_resolve_fault.addLayout(self.layout_resolve_fault)
        self.layout0.addLayout(self.title_Authority)
        self.title_Authority.addLayout(self.layout_Authority_block)

        self.setLayout(self.layout0)

    def create_authority_widget(self):

        # Clear all widgets in layout
        for i in reversed(range(self.layout_Authority_block.count())): 
            self.layout_Authority_block.itemAt(i).widget().setParent(None)

        block_authority_df = pd.read_excel("Track_Layout_Authority.xlsx")

        for i in range(0, len(block_authority_df)):
            if (block_authority_df.loc[i,"Authority"] == 1):
                suggested_speed = 50
            else:
                suggested_speed = 0
            authority_widget = QLabel("Block: " + str(block_authority_df.loc[i,"Block"]) + " Authority: " + str(block_authority_df.loc[i,"Authority"]) + " Speed (Km/H): " + str(suggested_speed))
            self.layout_Authority_block.addWidget(authority_widget)

    def resolve_fault_handler(self):
        block_fault_df = pd.read_excel("Block_Faults.xlsx")
        current_block = int(str(self.block_resolve_combo_box.currentText()))
        try:
            i = block_fault_df[block_fault_df['Block'] == current_block].index[0]
            block_fault_df = block_fault_df.drop(i)
            block_fault_df.reset_index(drop=True, inplace=True)
            with pd.ExcelWriter("Block_Faults.xlsx") as writer:  
                block_fault_df.to_excel(writer, index=False)
        except:
            print()

    def create_maintenance_widgest(self):
        ########### Create layout with 1 drop downs for removing fault in maintenance ###########
        
        # Clear all widgets in layout
        for i in reversed(range(self.layout_resolve_fault.count())): 
            self.layout_resolve_fault.itemAt(i).widget().setParent(None)

        # Block chooser
        self.block_resolve_combo_box = QComboBox()
        # Add items to combo box
        # print(self.parent.maintenance_blocks)
        for i in range(0, len(self.parent.maintenance_blocks)):
            # print(str(self.parent.maintenance_blocks[i]))
            self.block_resolve_combo_box.addItems([str(self.parent.maintenance_blocks[i])])

        # Add Button
        self.resolve_fault_button = QPushButton("Add")
        self.resolve_fault_button.setCheckable(True)
        self.resolve_fault_button.clicked.connect(self.resolve_fault_handler)

        self.layout_resolve_fault.addWidget(self.block_resolve_combo_box)
        self.layout_resolve_fault.addWidget(self.resolve_fault_button)

        

    def add_fault_handler(self):
        block_fault_df = pd.read_excel("Block_Faults.xlsx")
        end_idx = len(block_fault_df)
        block_fault_df.loc[end_idx, "Block"]= int(str(self.block_fault_combo_box.currentText()))
        block_fault_df.loc[end_idx, "Status"] = "Fault"
        block_fault_df = block_fault_df.drop_duplicates(subset=['Block'])
        # print(block_cross_df)
        with pd.ExcelWriter("Block_Faults.xlsx") as writer:  
            block_fault_df.to_excel(writer, index=False)

    def threhsold_add_handler(self):
        threshold_df = pd.read_excel("Ticket_Sales.xlsx")
        threshold_df.loc[0, "Line"]= "Blue"
        threshold_df.loc[0, "Sales"] = int(str(self.threhsold_input_line.text()))
        # print(switch_status_df)
        with pd.ExcelWriter("Ticket_Sales.xlsx") as writer:  
            threshold_df.to_excel(writer, index=False)

    def switch_position_handler(self):
        switch_status_df = pd.read_excel("Switch_Position.xlsx")
        switch_status_df.loc[0, "From"]= int(str(self.swith_from_combo_box.currentText()))
        switch_status_df.loc[0, "To"] = int(str(self.swith_to_combo_box.currentText()))
        # print(switch_status_df)
        with pd.ExcelWriter("Switch_Position.xlsx") as writer:  
            switch_status_df.to_excel(writer, index=False)

    def add_crossing_handler(self):
        block_cross_df = pd.read_excel("Crossing_Status.xlsx")
        end_idx = len(block_cross_df)
        block_cross_df.loc[end_idx, "Block"]= int(str(self.block_crossing_combo_box.currentText()))
        block_cross_df.loc[end_idx, "Status"] = str(self.status_crossing_combo_box.currentText())
        # print(block_cross_df)
        # with pd.ExcelWriter("Switch_Position.xlsx") as writer:  
        #     switch_position_df.to_excel(writer, index=False)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("CTC Main")
        widget = QWidget()

        # Variable initialization
        self.block_switch = pd.DataFrame()
        self.manual_mode_flag = True
        self.train_location = 0
        self.train_destination = 10

        # Continuously update authority based on where train is (estimated based on speed limits)

        # Define layout
        self.layout0 = QHBoxLayout()
        
        self.layout1 = QVBoxLayout() # In Layout 0

        self.layout2 = QHBoxLayout() # In Layout 1
        self.layout3 = QVBoxLayout() # In Layout 2
        self.layout4 = QVBoxLayout() # In Layout 2

        self.layout5 = QHBoxLayout() # In Layout 8

        self.layout6 = QVBoxLayout() # In Layout 1

        self.layout7 = QVBoxLayout() # In Layout 1

        self.layout8 = QVBoxLayout() # In Layout 1

        self.layout9 = QVBoxLayout() # In Layout 1

        self.layout10 = QVBoxLayout() # In Layout 0

        self.layout11 = QVBoxLayout() # In Layout 10
        self.layout12 = QVBoxLayout() # In Layout 11
        self.layout_add_fault = QHBoxLayout()
        # self.layout13 = QVBoxLayout() # In Layout 11
        # self.layout14 = QVBoxLayout() # In Layout 11

        # Button to open test ui
        # self.test_ui_window = None  # No external window yet.
        self.test_ui_button = QPushButton("Open Test UI")
        self.test_ui_button.setCheckable(True)
        self.test_ui_button.clicked.connect(self.test_ui_handler)

        # Button for inputting track
        self.load_track_button = QPushButton("Load Track Layout")
        self.load_track_button.setCheckable(True)
        self.load_track_button.clicked.connect(self.load_track_handler)

        # Button to open dispatch train window
        # self.dispatch_train_window = None  # No external window yet.
        self.dispatch_train_button = QPushButton("Dispatch Train(s)")
        self.dispatch_train_button.setCheckable(True)
        self.dispatch_train_button.clicked.connect(self.dispatch_train_handler)

        self.layout1.addWidget(self.test_ui_button)
        self.layout1.addWidget(self.load_track_button)
        self.layout1.addWidget(self.dispatch_train_button)

        # Manual mode Check Box

        TitleWidget = QLabel("Manual Switch State")
        font = TitleWidget.font()
        font.setPointSize(10)
        TitleWidget.setFont(font)
        self.layout8.addWidget(TitleWidget)

        self.manual_mode_check_box = QCheckBox()
        # self.manual_mode_check_box.setCheckState(Qt.Checked)
        self.manual_mode_check_box.stateChanged.connect(self.manual_mode_check_box_handler)

        self.manual_mode_label = QLabel("Manual Mode (Check for Manual)")

        self.layout5.addWidget(self.manual_mode_check_box)
        self.layout5.addWidget(self.manual_mode_label)

        # Section label
        TitleWidget = QLabel("Maintenance")
        font = TitleWidget.font()
        font.setPointSize(10)
        TitleWidget.setFont(font)
        self.layout12.addWidget(TitleWidget)


        self.my_timer = qtc.QTimer()
        self.my_timer.timeout.connect(self.get_display_throughput)
        self.my_timer.timeout.connect(self.populate_automatic_switch_pos_table)
        self.my_timer.timeout.connect(self.populate_manual_switch_pos_table)
        self.my_timer.timeout.connect(self.populate_crossing_table)
        self.my_timer.timeout.connect(self.populate_block_faults_table)
        self.my_timer.timeout.connect(self.fault_maintence_widgets)
        self.my_timer.timeout.connect(self.update_train_location)
        self.my_timer.start(3000) #interval


        # Nest layouts
        self.layout1.addLayout(self.layout9)
        self.layout1.addLayout(self.layout7)
        self.layout1.addLayout(self.layout6)
        self.layout8.addLayout(self.layout5)
        self.layout1.addLayout(self.layout8)
        self.layout2.addLayout(self.layout3)
        self.layout2.addLayout(self.layout4)
        self.layout1.addLayout(self.layout2)
        self.layout1.addLayout(self.layout2)
        self.layout0.addLayout(self.layout1)
        self.layout0.addLayout(self.layout10)
        self.layout10.addLayout(self.layout11)
        self.layout10.addLayout(self.layout12)
        self.layout12.addLayout(self.layout_add_fault)
        
        # self.layout10.addLayout(self.layout13)
        
        
        widget.setLayout(self.layout0)
        self.setCentralWidget(widget)

    def update_train_location(self):
        block_fault_df = pd.read_excel("Track_Layout_Authority.xlsx")
        if self.train_location >= 1:
            cur_block = self.train_location
                
            block_fault_df.loc[cur_block-1, "Authority"] = 0
            to_block = block_fault_df.loc[cur_block-1, "Link"]

            with pd.ExcelWriter("Track_Layout_Authority.xlsx") as writer:  
                block_fault_df.to_excel(writer, index=False)

            # print(block_fault_df)

            if (type(to_block) == int) and (block_fault_df.loc[to_block-1, "Authority"] == 1):
                self.train_location = to_block
                block_fault_df.loc[cur_block-1, "Authority"] = 1

            if (type(to_block) == str):
                block_fault_df.loc[cur_block-1, "Authority"] = 1


            

    def add_maintenance_handler(self):
        block_fault_df = pd.read_excel("Block_Faults.xlsx")
        selected_block = int(str(self.block_maintenance_combo_box.currentText()))
        i = block_fault_df[block_fault_df['Block'] == selected_block].index[0]
        block_fault_df.at[i,'Status'] = "Maintenance"
        with pd.ExcelWriter("Block_Faults.xlsx") as writer:  
            block_fault_df.to_excel(writer, index=False)

    def fault_maintence_widgets(self):
        ########### Create layout with 1 drop downs for adding fault ###########
        #Layout
        for i in reversed(range(self.layout_add_fault.count())): 
            self.layout_add_fault.itemAt(i).widget().setParent(None)

        block_failure_df = pd.read_excel("Block_Faults.xlsx")

        self.maintenance_blocks = block_failure_df[block_failure_df["Status"].str.contains("maintenance", case = False)]
        self.maintenance_blocks = self.maintenance_blocks.loc[:,"Block"]
        self.maintenance_blocks.reset_index(drop=True, inplace=True)
        # print(self.maintenance_blocks[0])
        # self.maintenance_blocks = block_failure_df[i,:]
        
        # Block chooser
        self.block_maintenance_combo_box = QComboBox()
        # Add items to combo box
        for i in range(0, len(block_failure_df)):
            # print(str(self.parent.all_blocks[i]))
            self.block_maintenance_combo_box.addItems([str(block_failure_df.loc[i, "Block"])])

        # Add Button
        self.add_maintenance_button = QPushButton("Add")
        self.add_maintenance_button.setCheckable(True)
        self.add_maintenance_button.clicked.connect(self.add_maintenance_handler)

        self.layout_add_fault.addWidget(self.block_maintenance_combo_box)
        self.layout_add_fault.addWidget(self.add_maintenance_button)

    def test_ui_handler(self, checked):
        self.test_ui_window = TestUI(parent=self)
        self.test_ui_window.show()

    # def maintenance_button_handler(self, block):
    #     print(block)
    #     block_failure_df = pd.read_excel("Block_Faults.xlsx")


    def populate_block_faults_table(self):

        # Clear all widgets in layout
        for i in reversed(range(self.layout11.count())): 
            self.layout11.itemAt(i).widget().setParent(None)
        # for i in reversed(range(self.layout13.count())): 
        #     self.layout13.itemAt(i).widget().setParent(None)

        # Title for block fault status section
        TitleWidget = QLabel("Block Fault Status")
        font = TitleWidget.font()
        font.setPointSize(10)
        TitleWidget.setFont(font)
        TitleWidget.setAlignment(Qt.AlignTop)
        self.layout11.addWidget(TitleWidget)

        self.block_fault_label_arr = []
        self.send_maintenance_button_arr = []
        block_failure_df = pd.read_excel("Block_Faults.xlsx")
        Track_Layout_df = pd.read_excel("Track_Layout_Authority.xlsx")
        all_blocks = Track_Layout_df.loc[:,"Block"]

        # print(block_failure_df.loc[:, "Block"])
        widgetIdx = 0
        for i in range(0, len(all_blocks)):
            if (all_blocks[i] in block_failure_df.loc[:, "Block"].values):
                # print(all_blocks[i])
                label_widget = QLabel("Fault on block " + str(all_blocks[i]))
                self.block_fault_label_arr.append(label_widget)
                self.layout11.addWidget(self.block_fault_label_arr[widgetIdx])
                widgetIdx = widgetIdx + 1

                Track_Layout_df.loc[Track_Layout_df["Block"] == all_blocks[i],"Authority"] = 0
            else:
                Track_Layout_df.loc[Track_Layout_df["Block"] == all_blocks[i],"Authority"] = 1
                
        
        # for i in range(0, len(block_failure_df)):
        #     label_widget = QLabel("Fault on block " + str(block_failure_df.loc[i, "Block"]))
        #     self.block_fault_label_arr.append(label_widget)
        #     self.layout11.addWidget(self.block_fault_label_arr[i])

        #     Track_Layout_df.loc[Track_Layout_df["Block"] == block_failure_df.loc[i, "Block"],"Authority"] = 0

        # print(Track_Layout_df)
        with pd.ExcelWriter("Track_Layout_Authority.xlsx") as writer:  
            Track_Layout_df.to_excel(writer, index=False)
            


    def get_display_throughput(self):

        # Clear all widgets in layout
        for i in reversed(range(self.layout9.count())): 
            self.layout9.itemAt(i).widget().setParent(None)

        ticket_sales_df = pd.read_excel("Ticket_Sales.xlsx")
        label_widget = QLabel("Throughput: " + str(ticket_sales_df.loc[0, "Sales"]) + " Tickets/Line/Hour")
        font = label_widget.font()
        font.setPointSize(8)
        label_widget.setFont(font)
        self.layout9.addWidget(label_widget)

    def populate_crossing_table(self):

        # Clear all widgets in layout
        for i in reversed(range(self.layout7.count())): 
            self.layout7.itemAt(i).widget().setParent(None)

        TitleWidget = QLabel("Crossing Status")
        font = TitleWidget.font()
        font.setPointSize(10)
        TitleWidget.setFont(font)
        self.layout7.addWidget(TitleWidget)


        crossing_status_df = pd.read_excel("Crossing_Status.xlsx")
        self.crossing_block_status_widget_arr = []
        for i in range(0, len(crossing_status_df)):
            label_widget = QLabel("Crossing Block: " + str(crossing_status_df.loc[i, "Block"]) + "      Crossing Status: " + str(crossing_status_df.loc[i, "Status"]))
            self.crossing_block_status_widget_arr.append(label_widget)
            self.layout7.addWidget(self.crossing_block_status_widget_arr[i])

    def switch_state_changed_handler(self, s, i):
        # Change switch state excel file if manua_mode_flag is true (manual box is checked)
        if (self.manual_mode_flag == True):
            switch_position_df = pd.read_excel("Switch_Position.xlsx")
            switch_position_df.at[i,'To'] = int(s)
            # print(switch_position_df)
            with pd.ExcelWriter("Switch_Position.xlsx") as writer:  
                switch_position_df.to_excel(writer, index=False)

            self.populate_automatic_switch_pos_table()


    def populate_manual_switch_pos_table(self):
        self.from_block_label_arr = []
        self.to_block_drop_down = []
        switch_position_df = pd.read_excel("Switch_Position.xlsx")
        
        # Clear all widgets in layout
        for i in reversed(range(self.layout3.count())): 
            self.layout3.itemAt(i).widget().setParent(None)
        for i in reversed(range(self.layout4.count())): 
            self.layout4.itemAt(i).widget().setParent(None)
        
        # Label and drop down to show switch position
        for i in range(0, len(switch_position_df)):
            label_widget = QLabel("From Block " + str(switch_position_df.loc[i, "From"]) + " To Block")
            self.from_block_label_arr.append(label_widget)

            combo_box_widget = QComboBox()
            self.to_block_drop_down.append(combo_box_widget)
            self.to_block_drop_down[i].addItems(["6", "11"]) # HARD CODED
            self.to_block_drop_down[i].currentTextChanged.connect(lambda s: self.switch_state_changed_handler(s, i))

            self.layout3.addWidget(self.from_block_label_arr[i])
            self.layout4.addWidget(self.to_block_drop_down[i])


    def populate_automatic_switch_pos_table(self):
        
        self.from_to_block_label_arr_manual = []
        # Open switch status file
        switch_position_df = pd.read_excel("Switch_Position.xlsx")

        # Clear all widgets in layout
        for i in reversed(range(self.layout6.count())): 
            self.layout6.itemAt(i).widget().setParent(None)

        TitleWidget = QLabel("Current Switch State")
        font = TitleWidget.font()
        font.setPointSize(10)
        TitleWidget.setFont(font)
        self.layout6.addWidget(TitleWidget)

        # Create QLabel widget
        for i in range(0, len(switch_position_df)):
            label_widget = QLabel("From Block " + str(switch_position_df.loc[i, "From"]) + " To Block " + str(switch_position_df.loc[i, "To"]))
            self.from_to_block_label_arr_manual.append(label_widget)
            self.layout6.addWidget(self.from_to_block_label_arr_manual[i])

        # Change Track_layout_link table
        Track_Layout_df = pd.read_excel("Track_Layout_Authority.xlsx")
        # i = Track_Layout_df[Track_Layout_df["Block"] == switch_position_df.loc[0, "From"]].index[0]
        Track_Layout_df.loc[Track_Layout_df["Block"] == switch_position_df.loc[0, "From"],"Link"] = switch_position_df.loc[0, "To"]
        with pd.ExcelWriter("Track_Layout_Authority.xlsx") as writer:  
            Track_Layout_df.to_excel(writer, index=False)

    def manual_mode_check_box_handler(self, s):
        if (s == Qt.Checked):
            self.manual_mode_flag = True
        else:
            self.manual_mode_flag = False

        # print(self.manual_mode_flag)

    def train_schedule_submitted_handler(self, train_schedule):
        block_fault_df = pd.read_excel("Track_Layout_Authority.xlsx")
        block_fault_df.loc[0, "Authority"] = 0
        self.train_location = 1
        with pd.ExcelWriter("Track_Layout_Authority.xlsx") as writer:  
            block_fault_df.to_excel(writer, index=False)
        
        # Adjust authority based on new train schedule
        # print(train_schedule)

    def dispatch_train_handler(self, checked):
        # if self.dispatch_train_window is None:
        self.dispatch_train_window = DispatchTrainWindow(parent=self)
        self.dispatch_train_window.submitClicked.connect(self.train_schedule_submitted_handler)
        self.dispatch_train_window.show()
        # else:
        #     self.dispatch_train_window.close()  # Close window.
        #     self.dispatch_train_window = None  # Discard reference.

    def load_track_handler(self):
        # Load file as dataframe
        file_path = self.open_file()
        df_track_layout = pd.read_excel(file_path)

        # Get all blocks
        self.all_blocks = df_track_layout.loc[:,"Block Number"]

        # Get lines from schedule
        self.unique_lines = df_track_layout.loc[:,"Line"]
        self.unique_lines = pd.unique(self.unique_lines)
        self.unique_lines = np.concatenate([[""], self.unique_lines]) # insert empty element for use in QComboBox

        # Filter on blocks with infrastructure
        self.block_infrastructure = df_track_layout.loc[:,["Line", "Block Number", "Infrastructure"]]
        self.block_infrastructure = self.block_infrastructure.dropna(subset=["Infrastructure"])

        # Filter on blocks with station
        self.block_station = self.block_infrastructure[self.block_infrastructure["Infrastructure"].str.contains("station", case = False)]

        # Filter on blocks with switches 
        self.block_switch = self.block_infrastructure[self.block_infrastructure["Infrastructure"].str.contains("switch", case = False)]
        self.block_switch = self.block_switch[self.block_switch["Infrastructure"].str.contains("or", case = False)]

        # Filter on blocks with railway crossing
        self.block_crossing = self.block_infrastructure[self.block_infrastructure["Infrastructure"].str.contains("crossing", case = False)]

        self.data_loaded_flag = True

        # print(self.block_switch.iloc[0]["Block Number"])

    def open_file(self):
        filename = QFileDialog.getOpenFileName()
        path = filename[0]
        return path

# Create QApplication instance 
app = QApplication([])

# Create Qt main window
window = MainWindow()

# fps = 15
# timer = QTimer()
# timer.timeout.connect(window.update)
# timer.setInterval(1)
# timer.start()

# Show window
window.show()



# Start event loop
app.exec()