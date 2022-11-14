import sys
import time
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6 import uic
from Line import Line
from Dispatcher import Dispatcher

greenLine = Line("Iteration3/Track_Layout_Green.xlsx")

CTCDispatcher = Dispatcher()

class CTCApp(QWidget):
    def __init__(self):
        super().__init__()

        uic.loadUi('Iteration3/CTC.ui', self)
        self.tabWidget.setTabText(0,'Schedule/Trains')
        self.tabWidget.setTabText(1,'Maintenace')

        self.cur_time = 0

        # Functionality for line choose buttons
        self.redLineButton.clicked.connect(self.chooseRedLine)
        self.greenLineButton.clicked.connect(self.chooseGreenLine)
        self.current_line = ""

        # Function to update destination list when add button is pressed
        self.addDestinationButton.clicked.connect(self.addDestinationList)

        # Function to dispatch current station list
        self.dispatchButton.clicked.connect(self.dispatchSchedule)
        

    # Function to update display when red line is chosen
    def chooseRedLine(self):
        pass

    # Function to update display when green line is chosen
    def chooseGreenLine(self):
        self.current_line = "Green"
        station_list = greenLine.line_station_list
        self.chooseStationCombo.clear()
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

    # Function to get from destination list
    def getDestinationList(self):
        rowPosition = self.stationsTable.rowCount()
        station_rows = []
        for row in range(0, rowPosition):
            station_rows.append(self.stationsTable.item(row,0).text())
        return station_rows

    def dispatchSchedule(self):
        destination_stations = self.getDestinationList()

        if (len(destination_stations) > 0):
            # clear destination table
            self.stationsTable.setRowCount(0)

            # Order destinations correctly
            order_list = []
            for station in destination_stations:
                order_list.append(greenLine.line_station_list.index(station))
            destination_stations = [x for _, x in sorted(zip(order_list, destination_stations))]

            # Call dispatch function
            if self.current_line == "Green":
                CTCDispatcher.scheduleSingle(destination_stations, greenLine, self.cur_time)

            # Update table with train
            cur_train = CTCDispatcher.trains[-1]
            rowPosition = self.trainTable.rowCount()
            self.trainTable.insertRow(rowPosition)
            self.trainTable.setItem(rowPosition, 0, QTableWidgetItem(str(cur_train.train_id)))
            self.trainTable.setItem(rowPosition, 1, QTableWidgetItem(str(cur_train.current_position)))
            self.trainTable.setItem(rowPosition, 2, QTableWidgetItem(str(cur_train.station_list[0])))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CTCApp()
    window.show()
    try:
        sys.exit(app.exec())
    except SystemExit:
        print('Closing Window')