from PyQt6.QtWidgets import QDialog, QGridLayout
from PyQt6.QtWidgets import QLabel, QPushButton
from PyQt6.QtCore import Qt, QSortFilterProxyModel
from PyQt6.QtGui import QFont, QStandardItemModel
from TrainModel.FontStyles import *
from TrainModel.TrainModelHandler import TrainModelHandler

#Declare global models and handler
train_proxy_model = QSortFilterProxyModel()
train_info_model = QStandardItemModel(0, 15)
handler = TrainModelHandler()


#Tooltip Builder
def list_to_tooltip(L):
    return ("Train ID: " + L[0] + "\nVelocity: " + L[1] + " MPH\nDistance: " + L[2] + " Feet\nCommanded Engine Power: "
    + L[3] + " Watts\nBraking: " + L[4] + "\nTrack Grade: " + L[5] + "°\nPassenger Count: " + L[6] + "\nFault(s): " + L[7]
    + "\nInterior Temperature: " + L[8] + "\nInterior Lights: " + L[9] + "\nExterior Lights: " + L[10] + "\nLeft Doors: " + L[11]
    + "\nRight Doors: " + L[12])

#Custom message window
class my_message(QDialog):
    def __init__(self, msg, title = "Message", error = False, parent = None):    
        #Initialize parent class and set title
        super().__init__(parent)
        self.setWindowTitle(title)
         
        #Create layout
        self.layout = QGridLayout()

        #Create labels and buttons
        self.prompt_label = QLabel(msg)
        self.OK_button = QPushButton("     OK     ")
        
        #Set labels and buttons font and color
        self.label_font = QFont("Helvetica", 10)
        self.label_font.setBold(True)
        
        self.prompt_label.setFont(self.label_font)
        self.prompt_label.setStyleSheet("QLabel { color : rgb(221, 221, 221); border: 0px}")

        self.OK_button.setFont(self.label_font)
                
        #Color buttons and window
        
        #If this is an error, we should color the button red. Otherwise, it should be green
        if error: self.OK_button.setStyleSheet(red_button_stylesheet)
        else: self.OK_button.setStyleSheet(green_button_stylesheet)
			
                     
        self.setStyleSheet('''background: rgb(102,102,102); border: 3px solid black;''')

        #Connect ok button
        self.OK_button.clicked.connect(self.accept)
                                                          
        #Add widgets to layout
        self.layout.addWidget(self.prompt_label, 0, 0, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.OK_button, 1, 0, alignment=Qt.AlignmentFlag.AlignCenter)
        
        #Set spacing of the grid
        self.layout.setVerticalSpacing(15)
        
        #Add the layout to the warning window
        self.setLayout(self.layout)
        
        #Fix the size of the window
        self.setFixedSize(self.sizeHint());

#Custom warning window
class my_warning(QDialog):
    def __init__(self, msg, title = "Warning", parent = None):    
        #Initialize parent class and set title
        super().__init__(parent)
        self.setWindowTitle(title)
         
        #Create layout
        self.layout = QGridLayout()

        #Create labels and buttons
        self.prompt_label = QLabel(msg)
        self.yes_button = QPushButton("     Yes     ")
        self.no_button = QPushButton("     No     ")
        
        #Set labels and buttons font and color
        self.label_font = QFont("Helvetica", 10)
        self.label_font.setBold(True)
        
        self.prompt_label.setFont(self.label_font)
        self.prompt_label.setStyleSheet("QLabel { color : rgb(221, 221, 221); border: 0px}")

        self.yes_button.setFont(self.label_font)
        self.no_button.setFont(self.label_font)
        
        #Connect yes and no buttons
        self.yes_button.clicked.connect(self.accept)
        self.no_button.clicked.connect(self.reject)
        
        #Color buttons and window
        self.yes_button.setStyleSheet(green_button_stylesheet)
                     
        self.no_button.setStyleSheet(red_button_stylesheet)

                     
        self.setStyleSheet('''background: rgb(102,102,102); border: 3px solid black;''')
                                                          
        #Add widgets to layout
        self.layout.addWidget(self.prompt_label, 0, 0, 1, 2, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.yes_button, 1, 0, alignment=Qt.AlignmentFlag.AlignRight)
        self.layout.addWidget(self.no_button, 1, 1, alignment=Qt.AlignmentFlag.AlignLeft)
        
        #Set spacing of the grid
        self.layout.setHorizontalSpacing(30)
        self.layout.setVerticalSpacing(15)
        
        #Add the layout to the warning window
        self.setLayout(self.layout)
        
        #Fix the size of the window
        self.setFixedSize(self.sizeHint());
