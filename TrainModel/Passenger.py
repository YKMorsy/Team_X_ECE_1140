from PyQt6.QtWidgets import QApplication, QWidget, QFrame, QDialog, QGridLayout, QAbstractItemView
from PyQt6.QtWidgets import QLabel, QPushButton, QRadioButton, QSlider, QSizePolicy, QTableWidget, QTableView, QAbstractItemView, QHeaderView
from PyQt6.QtCore import Qt, QRect, QTimer, QSortFilterProxyModel
from PyQt6.QtGui import QFont, QStandardItemModel, QStandardItem
from FontStyles import *
from common import *
    
class PassengerUI(QFrame):
    def __init__(self, my_murphy_UI, ID):
        #Initialize parent class
        super().__init__()

        self.setGeometry(100, 100, 400, 400)

        #Set up calling window
        self.my_murphy_UI = my_murphy_UI

        #Set ID
        self.ID = ID

        #Set up window settings
        self.setWindowTitle("Train " + str(ID) + " Passenger UI")
        self.setObjectName("PassengerUI")
        self.setStyleSheet('''#PassengerUI{background-color: rgb(102,102,102); border: 3px solid black;}''')		
                
        #Create a new grid
        self.grid_layout = QGridLayout()

        #Create widgets
        self.emergency_button = QPushButton("Emergency Brake (Hold to Activate)")


        #Set widget fonts and stylesheets
        self.emergency_button.setFont(normal_font)
        self.emergency_button.setStyleSheet(dark_red_button_stylesheet)

        self.emergency_button.pressed.connect(self.emergency_brake_pressed)
        self.emergency_button.released.connect(self.emergency_brake_released)

        self.emergency_button.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        #Add widgets to grid
        self.grid_layout.addWidget(self.emergency_button, 0, 0)

        #Connect grid to window
        self.setLayout(self.grid_layout)

    def emergency_brake_pressed(self):
        #If the brake is pressed, then the button should say "Activated", the train brake should be turn on, and the table should be updated
        self.emergency_button.setText("Activated")

        #Set the associated train's emergency brake, and update the table's value
        handler.train_list[self.ID].emergency_brake = True
        
        for i in range(self.my_murphy_UI.train_info_model.rowCount()):
            if int(self.my_murphy_UI.train_info_model.item(i, 0).text()) == self.ID:
                self.my_murphy_UI.train_info_model.setItem(i, 5, QStandardItem("Emergency"))

    def emergency_brake_released(self):
        #If the brake is released, then the button should say "Emergency Brake (Hold to Activate)", the train brake should be turn off, and the table should be updated
        self.emergency_button.setText("Emergency Brake (Hold to Activate)")

        #Reset the associated train's emergency brake, and update the table's value		
        handler.train_list[self.ID].emergency_brake = False
        
        #If the service brake is on, we should update the table with "Service". Otherwise, we should update it with "No"
        brake = "No"
        if handler.train_list[self.ID].service_brake: brake = "Service"
        
        for i in range(self.my_murphy_UI.train_info_model.rowCount()):
            if int(self.my_murphy_UI.train_info_model.item(i, 0).text()) == self.ID:
                self.my_murphy_UI.train_info_model.setItem(i, 5, QStandardItem(brake))