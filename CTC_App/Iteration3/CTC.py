import sys
import time
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from CTC_App.Iteration3.Line import Line
from CTC_App.Iteration3.Dispatcher import Dispatcher
from datetime import datetime

# greenLine = Line("Iteration3/Track_Layout_Green.xlsx")

# CTCDispatcher = Dispatcher()

class CTCApp(QWidget):
    def __init__(self, greenLine, redLine, CTCDispatcher):
        super().__init__()
        
        self.greenLine = greenLine
        self.redLine = redLine
        self.CTCDispatcher = CTCDispatcher

        self.train_list_length = 0
    
        uic.loadUi('./CTC_App/Iteration3/CTC.ui', self)
        self.tabWidget.setTabText(0,'Schedule/Trains')
        self.tabWidget.setTabText(1,'Track')
        
        # Sizing stuff
        header = self.stationsTable.horizontalHeader() 
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header = self.redEditDispatchTable.horizontalHeader() 
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header = self.greenEditDispatchTable.horizontalHeader() 
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header = self.greenTrainTable.horizontalHeader() 
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header = self.redTrainTable.horizontalHeader() 
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header = self.greenClosedBlocksTable.horizontalHeader() 
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header = self.greenSwitchStateTable.horizontalHeader() 
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header = self.greenCrossingTable.horizontalHeader() 
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header = self.redClosedBlocksTable.horizontalHeader() 
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header = self.redSwitchStateTable.horizontalHeader() 
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header = self.redCrossingTable.horizontalHeader() 
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)

        ############### SCHEDULE/TRAINS WINDOW ###############

        # Functionality for line choose buttons
        self.redLineButton.clicked.connect(self.chooseRedLine)
        self.greenLineButton.clicked.connect(self.chooseGreenLine)
        self.current_line = ""

        # Function to update destination list when add button is pressed
        self.addDestinationButton.clicked.connect(self.addDestinationList)

        # Function to dispatch current station list
        self.dispatchButton.clicked.connect(self.dispatchSchedule)

        # Function to display correct stations to add/remove combo box when train is chosen
        self.greenChooseTrain.currentTextChanged.connect(self.updateAddRemoveCombo)
        self.redChooseTrain.currentTextChanged.connect(self.updateAddRemoveCombo)

        # Function to update edited destination list when add button is pressed
        self.greenAddButton.clicked.connect(self.addEditDestinationList)
        self.redAddButton.clicked.connect(self.addEditDestinationList)
        self.greenRemoveButton.clicked.connect(self.removeEditDestinationList)
        self.redRemoveButton.clicked.connect(self.removeEditDestinationList)
        # self.redUpdateButton.clicked.connect(self.updateEditDispatch)
        # self.greenUpdateButton.clicked.connect(self.updateEditDispatch)

        self.openFile.clicked.connect(self.loadSchedule)

        ############### MAINTENANCE WINDOW ###############
        self.redLineButton_2.clicked.connect(self.chooseRedLineMaint)
        self.greenLineButton_2.clicked.connect(self.chooseGreenLineMaint)
        self.current_line_maint = ""
        self.greenMaintenanceButton.clicked.connect(self.putMaintenance)
        self.redMaintenanceButton.clicked.connect(self.putMaintenance)

        self.greenChooseOriginCombo.currentTextChanged.connect(self.updateTargetComboBox)
        self.redChooseOriginCombo.currentTextChanged.connect(self.updateTargetComboBox)

        self.greenSetState.clicked.connect(self.setState)
        self.redSetState.clicked.connect(self.setState)


        ############### CONSTANT UPDATES ###############
        # Initialize timer
        self.start_time = round(time.time())
        self.hour_time_stamp = round(time.time())
        # self.timer = Qimer()
        # self.timer.timeout.connect(self.updateTimer)
        # self.timer.setInterval(1000)
        # self.timer.start()


        # Constantly update train table

    # Function to call all constatn updates
    def updateTimer(self):
        # Update time in dispatcher
        self.start_time = self.start_time + 1
        self.CTCDispatcher.updateTime(self.start_time)
        time_dt = datetime.fromtimestamp(self.start_time)

        self.timeValue.setText(time_dt.strftime('%Y/%m/%d %I:%M:%S %p'))

        if self.current_line == "Green":
            self.CTCDispatcher.checkDispatch(self.greenLine)
        elif self.current_line == "Red":
            self.CTCDispatcher.checkDispatch(self.redLine)

        output = []

        while (self.train_list_length != len(self.CTCDispatcher.trains)):
            # self.greenLine.block_list[0].block_authority = True
            # self.greenLine.block_list[0].block_suggested_speed = self.greenLine.block_list[0].block_speed_limit

            if self.train_list_length <= len(self.CTCDispatcher.trains): 
                output.append((self.CTCDispatcher.trains[self.train_list_length]))
                self.train_list_length += 1


        # Table updates
        self.updateTrainTable()
        self.updateClosedBlocksTable()
        self.updateSwitchStateTable()
        self.updateCrossStatusTable()
        self.updateThroughPutLabel()
        self.updateTrainStationTable()

        for train in self.CTCDispatcher.all_trains:
            train.update_time(self.start_time)
        # for train in self.CTCDispatcher.trains:
        #     train.update_time(self.start_time)

        return output

    def updateThroughPutLabel(self):
        if self.current_line == "Green":
            self.throughPutValue.setText(str(self.greenLine.throughput))
            # Check if hour has passed and reset throughput
            if(self.start_time - self.hour_time_stamp >= 3600):
                self.greenLine.throughput = 0
                self.hour_time_stamp = self.start_time

        elif self.current_line == "Red":
            self.throughPutValue.setText(str(self.redLine.throughput))
            # Check if hour has passed and reset throughput
            if(self.start_time - self.hour_time_stamp >= 3600):
                self.redLine.throughput = 0
                self.hour_time_stamp = self.start_time

    # Function to update closed blocks table
    def updateClosedBlocksTable(self):
        
        if self.current_line_maint == "Green":
            self.greenClosedBlocksTable.setRowCount(0)
            closed_blocks = self.greenLine.getClosedBlocks()
            for block in closed_blocks:
                rowPosition = self.greenClosedBlocksTable.rowCount()
                self.greenClosedBlocksTable.insertRow(rowPosition)
                self.greenClosedBlocksTable.setItem(rowPosition, 0, QTableWidgetItem(str(block)))

        elif self.current_line_maint == "Red":
            self.redClosedBlocksTable.setRowCount(0)
            closed_blocks = self.redLine.getClosedBlocks()
            for block in closed_blocks:
                rowPosition = self.redClosedBlocksTable.rowCount()
                self.redClosedBlocksTable.insertRow(rowPosition)
                self.redClosedBlocksTable.setItem(rowPosition, 0, QTableWidgetItem(str(block)))

    # Function to update switch state table
    def updateSwitchStateTable(self):
        if self.current_line_maint == "Green":
            self.greenSwitchStateTable.setRowCount(0)
            switch_orig_targ = self.greenLine.getSwitchState()
            for switch in switch_orig_targ:
                rowPosition = self.greenSwitchStateTable.rowCount()
                self.greenSwitchStateTable.insertRow(rowPosition)
                self.greenSwitchStateTable.setItem(rowPosition, 0, QTableWidgetItem(str(switch[0])))
                self.greenSwitchStateTable.setItem(rowPosition, 1, QTableWidgetItem(str(switch[1])))

        elif self.current_line_maint == "Red":
            self.redSwitchStateTable.setRowCount(0)
            switch_orig_targ = self.redLine.getSwitchState()
            for switch in switch_orig_targ:
                rowPosition = self.redSwitchStateTable.rowCount()
                self.redSwitchStateTable.insertRow(rowPosition)
                self.redSwitchStateTable.setItem(rowPosition, 0, QTableWidgetItem(str(switch[0])))
                self.redSwitchStateTable.setItem(rowPosition, 1, QTableWidgetItem(str(switch[1])))

    # Function to update cross status table
    def updateCrossStatusTable(self):
        if self.current_line_maint == "Green":
            self.greenCrossingTable.setRowCount(0)
            cross_status = self.greenLine.getCrossingState()
            for cross in cross_status:
                rowPosition = self.greenCrossingTable.rowCount()
                self.greenCrossingTable.insertRow(rowPosition)
                self.greenCrossingTable.setItem(rowPosition, 0, QTableWidgetItem(str(cross[0])))
                self.greenCrossingTable.setItem(rowPosition, 1, QTableWidgetItem(str(cross[1])))

        elif self.current_line_maint == "Red":
            self.redCrossingTable.setRowCount(0)
            cross_status = self.redLine.getCrossingState()
            for cross in cross_status:
                rowPosition = self.redCrossingTable.rowCount()
                self.redCrossingTable.insertRow(rowPosition)
                self.redCrossingTable.setItem(rowPosition, 0, QTableWidgetItem(str(cross[0])))
                self.redCrossingTable.setItem(rowPosition, 1, QTableWidgetItem(str(cross[1])))

    # Function to update train Table
    def updateTrainTable(self):
        if self.current_line == "Green":
            self.greenTrainTable.setRowCount(0)
            trains = self.CTCDispatcher.all_trains

            for train in trains:
                if train.line.line_color == "Green" and len(train.route) > 2:
                    rowPosition = self.greenTrainTable.rowCount()
                    self.greenTrainTable.insertRow(rowPosition)
                    cur_train_id = train.train_id
                    self.greenTrainTable.setItem(rowPosition, 0, QTableWidgetItem(str(cur_train_id)))
                    if len(train.station_list) > 0:
                        next_station = train.station_list[0]
                        self.greenTrainTable.setItem(rowPosition, 1, QTableWidgetItem(str(train.current_position)))
                        self.greenTrainTable.setItem(rowPosition, 2, QTableWidgetItem(str(next_station)))
                    else:
                        self.greenTrainTable.setItem(rowPosition, 1, QTableWidgetItem(str(train.current_position)))
                        self.greenTrainTable.setItem(rowPosition, 2, QTableWidgetItem("YARD"))

        elif self.current_line == "Red":
            self.redTrainTable.setRowCount(0)
            trains = self.CTCDispatcher.all_trains

            for train in trains:
                if train.line.line_color == "Red" and len(train.route) > 2:
                    rowPosition = self.redTrainTable.rowCount()
                    self.redTrainTable.insertRow(rowPosition)
                    cur_train_id = train.train_id
                    self.redTrainTable.setItem(rowPosition, 0, QTableWidgetItem(str(cur_train_id)))
                    if len(train.station_list) > 0:
                        next_station = train.station_list[0]
                        self.redTrainTable.setItem(rowPosition, 1, QTableWidgetItem(str(train.current_position)))
                        self.redTrainTable.setItem(rowPosition, 2, QTableWidgetItem(str(next_station)))
                    else:
                        self.redTrainTable.setItem(rowPosition, 1, QTableWidgetItem(str(train.current_position)))
                        self.redTrainTable.setItem(rowPosition, 2, QTableWidgetItem("YARD"))

    def updateTrainStationTable(self):
        if self.current_line == "Green":
            # Get train station list
            green_line_trains = []
            ctc_all_trains = self.CTCDispatcher.all_trains
            for train in ctc_all_trains:
                if train.line.line_color == "Green":
                    green_line_trains.append(train)

            if len(green_line_trains) > 0:
                cur_train = self.CTCDispatcher.all_trains[int(self.greenChooseTrain.currentText())-1]
                cur_train_stations = cur_train.station_list

                # update table
                self.greenEditDispatchTable.setRowCount(0)
                for station in cur_train_stations:
                    rowPosition = self.greenEditDispatchTable.rowCount()
                    self.greenEditDispatchTable.insertRow(rowPosition)
                    self.greenEditDispatchTable.setItem(rowPosition, 0, QTableWidgetItem(station))

        elif self.current_line == "Red":
            red_line_trains = []
            ctc_all_trains = self.CTCDispatcher.all_trains
            for train in ctc_all_trains:
                if train.line.line_color == "Red":
                    red_line_trains.append(train)

            if len(red_line_trains) > 0:
                # Get train station list
                cur_train = self.CTCDispatcher.all_trains[int(self.redChooseTrain.currentText())-1]
                cur_train_stations = cur_train.station_list

                # update table
                self.redEditDispatchTable.setRowCount(0)
                for station in cur_train_stations:
                    rowPosition = self.redEditDispatchTable.rowCount()
                    self.redEditDispatchTable.insertRow(rowPosition)
                    self.redEditDispatchTable.setItem(rowPosition, 0, QTableWidgetItem(station))

    # Function to update maintenace display when red line is chosen
    def chooseRedLineMaint(self):
        self.current_line_maint = "Red"
        self.currentLineValue_2.setText(self.current_line_maint)
        self.maintenanceStack.setCurrentIndex(0)

        # Fill combo box
        self.redChooseMaintenanceCombo.clear()
        block_list = self.redLine.getClosedBlocks()
        for block in block_list:
            self.redChooseMaintenanceCombo.addItem(str(block))

        self.redChooseOriginCombo.clear()
        switch_list = self.redLine.getSwitchState()
        for switch in switch_list:
            self.redChooseOriginCombo.addItem(str(switch[0]))

    # Function to update maintenace display when green line is chosen
    def chooseGreenLineMaint(self):
        self.current_line_maint = "Green"
        self.currentLineValue_2.setText(self.current_line_maint)
        self.maintenanceStack.setCurrentIndex(1)

        # Fill combo box
        self.greenChooseMaintenanceCombo.clear()
        block_list = self.greenLine.getClosedBlocks()
        for block in block_list:
            self.greenChooseMaintenanceCombo.addItem(str(block))

        self.greenChooseOriginCombo.clear()
        switch_list = self.greenLine.getSwitchState()
        for switch in switch_list:
            self.greenChooseOriginCombo.addItem(str(switch[0]))
        
    # Function to update display when red line is chosen
    def chooseRedLine(self):
        self.current_line = "Red"
        self.currentLineValue.setText(self.current_line)
        self.editDispatchStacked.setCurrentIndex(0)
        self.trainTableStacked.setCurrentIndex(0)
        self.chooseStationCombo.clear()
        station_list = self.redLine.line_station_list
        for station in station_list:
            self.chooseStationCombo.addItem(station)

    # Function to update display when green line is chosen
    def chooseGreenLine(self):
        self.current_line = "Green"
        self.currentLineValue.setText(self.current_line)
        self.editDispatchStacked.setCurrentIndex(1)
        self.trainTableStacked.setCurrentIndex(1)
        self.chooseStationCombo.clear()
        station_list = self.greenLine.line_station_list
        for station in station_list:
            self.chooseStationCombo.addItem(station)
    
    # Function to add to desination list
    def addDestinationList(self):
        cur_station = self.chooseStationCombo.currentText()
        
        # Get current table items and put in list
        station_rows = self.getDestinationList()
        rowPosition = self.stationsTable.rowCount()
        if (cur_station not in station_rows) and (cur_station != ""):
            self.stationsTable.insertRow(rowPosition)
            self.stationsTable.setItem(rowPosition, 0, QTableWidgetItem(cur_station))

    # Function to add to edit desination list #################### FIX ADD AND REMOVE FUNCTIONS
    def addEditDestinationList(self):
        if self.current_line == "Green":

            # Get current station
            cur_station = self.greenAddStation.currentText()
            # Get station list
            # Add station to correct index
            destination_stations = self.CTCDispatcher.all_trains[int(self.greenChooseTrain.currentText())-1].station_list
            destination_stations.append(cur_station)
            order_list = []
            for station in destination_stations:
                order_list.append(self.greenLine.line_station_list.index(station))
            destination_stations = [x for _, x in sorted(zip(order_list, destination_stations))]
            # Update station
            self.CTCDispatcher.updateStations(int(self.greenChooseTrain.currentText())-1, destination_stations)
            
            self.greenAddStation.removeItem(self.greenAddStation.currentIndex())
            self.greenRemoveStation.addItem(cur_station)

        elif self.current_line == "Red":
            # Get current station
            cur_station = self.redAddStation.currentText()
            # Get station list
            # Add station to correct index
            destination_stations = self.CTCDispatcher.all_trains[int(self.redChooseTrain.currentText())-1].station_list
            destination_stations.append(cur_station)
            order_list = []
            for station in destination_stations:
                order_list.append(self.redLine.line_station_list.index(station))
            destination_stations = [x for _, x in sorted(zip(order_list, destination_stations))]
            # Update station
            self.CTCDispatcher.updateStations(int(self.redChooseTrain.currentText())-1, destination_stations)

            self.redAddStation.removeItem(self.redAddStation.currentIndex())
            self.redRemoveStation.addItem(cur_station)

    # Function to remove from edit desination list
    def removeEditDestinationList(self):
        if self.current_line == "Green":

            # Get current text station
            cur_station = self.greenRemoveStation.currentText()
            # Get train stations
            train_stations = self.CTCDispatcher.all_trains[int(self.greenChooseTrain.currentText())-1].station_list
            # Remove station from list
            train_stations.remove(cur_station)
            # Update station list
            self.CTCDispatcher.updateStations(int(self.greenChooseTrain.currentText())-1, train_stations)

            # Remove removed item from combo box
            self.greenRemoveStation.removeItem(self.greenRemoveStation.currentIndex())
            self.greenAddStation.addItem(cur_station)

        elif self.current_line == "Red":

            # Get current text station
            cur_station = self.redRemoveStation.currentText()
            # Get train stations
            train_stations = self.CTCDispatcher.all_trains[int(self.redChooseTrain.currentText())-1].station_list
            # Remove station from list
            train_stations.remove(cur_station)
            # Update station list
            self.CTCDispatcher.updateStations(int(self.redChooseTrain.currentText())-1, train_stations)

            # Remove removed item from combo box
            self.redRemoveStation.removeItem(self.redRemoveStation.currentIndex())
            self.redAddStation.addItem(cur_station)

    # Function to get from destination list
    def getDestinationList(self):
        rowPosition = self.stationsTable.rowCount()
        station_rows = []
        for row in range(0, rowPosition):
            station_rows.append(self.stationsTable.item(row,0).text())
        return station_rows
    # def getGreenEditDestinationList(self):
    #     rowPosition = self.greenEditDispatchTable.rowCount()
    #     station_rows = []
    #     for row in range(0, rowPosition):
    #         station_rows.append(self.greenEditDispatchTable.item(row,0).text())
    #     return station_rows
    # def getRedEditDestinationList(self):
        rowPosition = self.redEditDispatchTable.rowCount()
        station_rows = []
        for row in range(0, rowPosition):
            station_rows.append(self.redEditDispatchTable.item(row,0).text())
        return station_rows

    def dispatchSchedule(self):
        destination_stations = self.getDestinationList()
        if (len(destination_stations) > 0):
            # clear destination table
            self.stationsTable.setRowCount(0)

            # # Order destinations correctly
            # order_list = []
            # for station in destination_stations:
            #     order_list.append(self.greenLine.line_station_list.index(station))

            # destination_stations = [x for _, x in sorted(zip(order_list, destination_stations))]

            # # Call dispatch function
            # if self.current_line == "Green":
            #     self.CTCDispatcher.scheduleSingle(destination_stations, self.greenLine)

            if self.current_line == "Green":
                # Call dispatch function
                self.CTCDispatcher.scheduleSingle(destination_stations, self.greenLine)
                # Update table with train
                cur_train = self.CTCDispatcher.all_trains[-1]
                rowPosition = self.greenTrainTable.rowCount()
                self.greenTrainTable.insertRow(rowPosition)
                self.greenTrainTable.setItem(rowPosition, 0, QTableWidgetItem(str(cur_train.train_id)))
                self.greenTrainTable.setItem(rowPosition, 1, QTableWidgetItem(str(cur_train.current_position)))
                self.greenTrainTable.setItem(rowPosition, 2, QTableWidgetItem(str(cur_train.station_list[0])))

                self.greenChooseTrain.addItem(str(cur_train.train_id))
            elif self.current_line == "Red":

                self.CTCDispatcher.scheduleSingle(destination_stations, self.redLine)

                cur_train = self.CTCDispatcher.all_trains[-1]
                rowPosition = self.redTrainTable.rowCount()
                self.redTrainTable.insertRow(rowPosition)
                self.redTrainTable.setItem(rowPosition, 0, QTableWidgetItem(str(cur_train.train_id)))
                self.redTrainTable.setItem(rowPosition, 1, QTableWidgetItem(str(cur_train.current_position)))
                self.redTrainTable.setItem(rowPosition, 2, QTableWidgetItem(str(cur_train.station_list[0])))

                self.redChooseTrain.addItem(str(cur_train.train_id))

    def updateAddRemoveCombo(self):
        if self.current_line == "Green":
            cur_train = self.CTCDispatcher.all_trains[int(self.greenChooseTrain.currentText())-1]
            cur_train_stations = cur_train.station_list
            # Put missing stations in add combo box
            self.greenAddStation.clear()

            missing_stations = list(set(self.greenLine.line_station_list) - set(cur_train_stations))
            for station in missing_stations:
                self.greenAddStation.addItem(str(station))

            # Put chosen stations in remove combo box
            self.greenRemoveStation.clear()

            for station in cur_train_stations:
                self.greenRemoveStation.addItem(str(station))

        elif self.current_line == "Red":
            cur_train = self.CTCDispatcher.all_trains[int(self.redChooseTrain.currentText())-1]
            cur_train_stations = cur_train.station_list

            # Put missing stations in add combo box
            self.redAddStation.clear()

            missing_stations = list(set(self.redLine.line_station_list) - set(cur_train_stations))
            for station in missing_stations:
                self.redAddStation.addItem(station)

            # Put chosen stations in remove combo box
            self.redRemoveStation.clear()

            for station in cur_train_stations:
                self.redRemoveStation.addItem(station)

    # # Function to update train's schedule
    # def updateEditDispatch(self):
    #     if self.current_line == "Green":
    #         destination_stations = self.getGreenEditDestinationList()
    #         order_list = []
    #         for station in destination_stations:
    #             order_list.append(self.greenLine.line_station_list.index(station))
    #         destination_stations = [x for _, x in sorted(zip(order_list, destination_stations))]
    #         self.CTCDispatcher.updateStations(int(self.greenChooseTrain.currentText())-1, destination_stations)

    #         # self.greenEditDispatchTable.setRowCount(0)
            
    #     elif self.current_line == "Red":
    #         destination_stations = self.getRedEditDestinationList()
    #         order_list = []
    #         for station in destination_stations:
    #             order_list.append(self.redLine.line_station_list.index(station))
    #         destination_stations = [x for _, x in sorted(zip(order_list, destination_stations))]
    #         self.CTCDispatcher.updateStations(int(self.redChooseTrain.currentText())-1, destination_stations)

    # Function to update closed blocks when put in maintenance using button
    def putMaintenance(self):
        if self.manualModeCheck.isChecked() == True:
            if self.current_line_maint == "Green":
                selected_block = self.greenChooseMaintenanceCombo.currentText()
                self.greenLine.maintenance_blocks.append(selected_block)
                self.greenChooseMaintenanceCombo.removeItem(self.greenChooseMaintenanceCombo.currentIndex())
                # Set block status to True in line object and update choose block list
                # greenLine.setBlockStatus(int(selected_block), True)
                # self.greenChooseMaintenanceCombo.removeItem(self.greenChooseMaintenanceCombo.currentIndex())

            elif self.current_line_maint == "Red":
                selected_block = self.redChooseMaintenanceCombo.currentText()
                self.redLine.maintenance_blocks.append(selected_block)
                self.redChooseMaintenanceCombo.removeItem(self.greenChooseMaintenanceCombo.currentIndex())
                # Set block status to True in line object and update choose block list
                # greenLine.setBlockStatus(int(selected_block), True)
                # self.redChooseMaintenanceCombo.removeItem(self.redChooseMaintenanceCombo.currentIndex())


    def updateTargetComboBox(self):
        if self.current_line_maint == "Green":
            cur_origin = self.greenChooseOriginCombo.currentText()
            if (cur_origin != ""):
                cur_block = self.greenLine.block_list[int(cur_origin)]
                switch_1 = cur_block.block_switch_1
                switch_2 = cur_block.block_switch_2

                self.greenChooseTargetCombo.clear()
                self.greenChooseTargetCombo.addItem(str(switch_1))
                self.greenChooseTargetCombo.addItem(str(switch_2))

        elif self.current_line_maint == "Red":
            cur_origin = self.redChooseOriginCombo.currentText()
            if (cur_origin != ""):
                cur_block = self.redLine.block_list[int(cur_origin)]
                switch_1 = cur_block.block_switch_1
                switch_2 = cur_block.block_switch_2

                self.redChooseTargetCombo.clear()
                self.redChooseTargetCombo.addItem(str(switch_1))
                self.redChooseTargetCombo.addItem(str(switch_2))

    def setState(self):
        if self.manualModeCheck.isChecked() == True:
            if self.current_line_maint == "Green":
                selected_origin = self.greenChooseOriginCombo.currentText()
                selected_target = self.greenChooseTargetCombo.currentText()

                cur_block = self.greenLine.block_list[int(selected_origin)]
                switch_1 = cur_block.block_switch_1
                switch_2 = cur_block.block_switch_2

                if(int(selected_target) == switch_1):
                    if (int(selected_target) > switch_2):
                        self.greenLine.block_list[int(selected_origin)].setSwitchPos(True)
                        # self.greenLine.setSwitchPosition(int(selected_origin), True)
                    else:
                        self.greenLine.block_list[int(selected_origin)].setSwitchPos(False)
                        # self.greenLine.setSwitchPosition(int(selected_origin), False)
                else:
                    if (int(selected_target) > switch_1):
                        self.greenLine.block_list[int(selected_origin)].setSwitchPos(True)
                    #    self. greenLine.setSwitchPosition(int(selected_origin), True)
                    else:
                        self.greenLine.block_list[int(selected_origin)].setSwitchPos(False)
                        # self.greenLine.setSwitchPosition(int(selected_origin), False)

            elif self.current_line_maint == "Red":
                selected_origin = self.redChooseOriginCombo.currentText()
                selected_target = self.redChooseTargetCombo.currentText()

                cur_block = self.redLine.block_list[int(selected_origin)]
                switch_1 = cur_block.block_switch_1
                switch_2 = cur_block.block_switch_2

                if(int(selected_target) == switch_1):
                    if (int(selected_target) > switch_2):
                        self.redLine.block_list[int(selected_origin)].setSwitchPos(True)
                        # self.greenLine.setSwitchPosition(int(selected_origin), True)
                    else:
                        self.redLine.block_list[int(selected_origin)].setSwitchPos(False)
                        # self.greenLine.setSwitchPosition(int(selected_origin), False)
                else:
                    if (int(selected_target) > switch_1):
                        self.redLine.block_list[int(selected_origin)].setSwitchPos(True)
                    #    self. greenLine.setSwitchPosition(int(selected_origin), True)
                    else:
                        self.redLine.block_list[int(selected_origin)].setSwitchPos(False)
                        # self.greenLine.setSwitchPosition(int(selected_origin), False)

    def open_file(self):
        filename = QFileDialog.getOpenFileName()
        path = filename[0]
        return path

    def loadSchedule(self):
        # get file path and call dispatcher
        file_path = self.open_file()
        if self.current_line == "Green":
            self.CTCDispatcher.scheduleMultiple(file_path, self.greenLine)
            cur_train = self.CTCDispatcher.all_trains[-1]
            self.greenChooseTrain.addItem(str(cur_train.train_id))
        if self.current_line == "Red":
            self.CTCDispatcher.scheduleMultiple(file_path, self.redLine)
            cur_train = self.CTCDispatcher.all_trains[-1]
            self.redChooseTrain.addItem(str(cur_train.train_id))
        # elif self.current_line == "Red":
        #     rowPosition = self.redTrainTable.rowCount()
        #     self.redTrainTable.insertRow(rowPosition)
        #     self.redTrainTable.setItem(rowPosition, 0, QTableWidgetItem(str(cur_train.train_id)))
        #     self.redTrainTable.setItem(rowPosition, 1, QTableWidgetItem(str(cur_train.current_position)))
        #     self.redTrainTable.setItem(rowPosition, 2, QTableWidgetItem(str(cur_train.station_list[0])))

        #     self.redChooseTrain.addItem(str(cur_train.train_id))
        
