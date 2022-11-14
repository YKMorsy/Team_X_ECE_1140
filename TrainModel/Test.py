from PyQt6.QtWidgets import QApplication, QWidget, QFrame, QDialog, QGridLayout
from PyQt6.QtWidgets import QLabel, QPushButton, QRadioButton, QSlider, QLineEdit, QSizePolicy, QTableView, QAbstractItemView, QHeaderView, QToolTip
from PyQt6.QtCore import Qt, QRect, QTimer, QSortFilterProxyModel, QThread
from PyQt6.QtGui import QFont, QStandardItemModel, QStandardItem
from TrainModel.FontStyles import *
from TrainModel.common import *
from TrainModel.TrainModelHandler import TrainModelHandler

class TestUICreatorModifier(QFrame):
	def __init__(self, my_test_UI, modification = False, ID = None):
		#Initialize parent class
		super().__init__()
		
		#Set the modification status
		self.modification = modification
		
		#If there is an ID, set it
		self.ID = ID
		
		#Set up calling window
		self.my_test_UI = my_test_UI
				
		#Create a new grid
		self.grid_layout = QGridLayout()
				
		#Set up window settings
		if modification: self.setWindowTitle("Train Modification")
		else: self.setWindowTitle("Train Creation")
		self.setObjectName("TestUICreator")
		self.setStyleSheet('''#TestUICreator{background-color: rgb(102,102,102); border: 3px solid black;}''')
		
		#Create widgets
		self.train_settings_label = QLabel("Train Settings")
		self.train_ID_label = QLabel("Train ID:")
		self.train_ID_entry = QLineEdit()
		self.train_mass_label = QLabel("Mass (US Tons):")
		self.train_mass_entry = QLineEdit()
		self.train_crew_label = QLabel("Crew Count:")
		self.train_crew_entry = QLineEdit()
		self.train_passenger_label = QLabel("Passenger Capacity:")
		self.train_passenger_entry = QLineEdit()
		self.train_speed_label = QLabel("Speed Limit (MPH):")
		self.train_speed_entry = QLineEdit()
		self.train_acceleration_label = QLabel("Acceleration Limit (ft/s^2):")
		self.train_acceleration_entry = QLineEdit()
		self.train_service_label = QLabel("Service Brake Deceleration (ft/s^2):")
		self.train_service_entry = QLineEdit()
		self.train_emergency_label = QLabel("Emergency Brake Deceleration (ft/s^2):")
		self.train_emergency_entry = QLineEdit()
		self.train_power_label = QLabel("Maximum Engine Power (Watts):")
		self.train_power_entry = QLineEdit()
		self.train_length_label = QLabel("Length (Feet):")
		self.train_length_entry = QLineEdit()
		self.train_height_label = QLabel("Height (Feet):")
		self.train_height_entry = QLineEdit()
		self.train_width_label = QLabel("Width (Feet):")
		self.train_width_entry = QLineEdit()
		if modification: self.modify_train_button = QPushButton("Save Modifications")
		else: self.create_train_button = QPushButton("Create New Train")
		
		#Set fonts and stylesheets
		self.train_settings_label.setFont(section_font)
		self.train_ID_label.setFont(normal_font)
		self.train_ID_entry.setFont(normal_font)
		self.train_mass_label.setFont(normal_font)
		self.train_mass_entry.setFont(normal_font)
		self.train_crew_label.setFont(normal_font)
		self.train_crew_entry.setFont(normal_font)
		self.train_passenger_label.setFont(normal_font)
		self.train_passenger_entry.setFont(normal_font)
		self.train_speed_label.setFont(normal_font)
		self.train_speed_entry.setFont(normal_font)
		self.train_acceleration_label.setFont(normal_font)
		self.train_acceleration_entry.setFont(normal_font)
		self.train_service_label.setFont(normal_font)
		self.train_service_entry.setFont(normal_font)
		self.train_emergency_label.setFont(normal_font)
		self.train_emergency_entry.setFont(normal_font)
		self.train_power_label.setFont(normal_font)
		self.train_power_entry.setFont(normal_font)
		self.train_length_label.setFont(normal_font)
		self.train_length_entry.setFont(normal_font)
		self.train_height_label.setFont(normal_font)
		self.train_height_entry.setFont(normal_font)
		self.train_width_label.setFont(normal_font)
		self.train_width_entry.setFont(normal_font)
		if modification: self.modify_train_button.setFont(normal_font)
		else: self.create_train_button.setFont(normal_font)

		self.train_settings_label.setStyleSheet(section_label_stylesheet)
		self.train_ID_label.setStyleSheet(normal_label_stylesheet)
		self.train_ID_entry.setStyleSheet(entry_stylesheet)
		self.train_mass_label.setStyleSheet(normal_label_stylesheet)
		self.train_mass_entry.setStyleSheet(entry_stylesheet)
		self.train_crew_label.setStyleSheet(normal_label_stylesheet)
		self.train_crew_entry.setStyleSheet(entry_stylesheet)
		self.train_passenger_label.setStyleSheet(normal_label_stylesheet)
		self.train_passenger_entry.setStyleSheet(entry_stylesheet)
		self.train_speed_label.setStyleSheet(normal_label_stylesheet)
		self.train_speed_entry.setStyleSheet(entry_stylesheet)
		self.train_acceleration_label.setStyleSheet(normal_label_stylesheet)
		self.train_acceleration_entry.setStyleSheet(entry_stylesheet)
		self.train_service_label.setStyleSheet(normal_label_stylesheet)
		self.train_service_entry.setStyleSheet(entry_stylesheet)
		self.train_emergency_label.setStyleSheet(normal_label_stylesheet)
		self.train_emergency_entry.setStyleSheet(entry_stylesheet)
		self.train_power_label.setStyleSheet(normal_label_stylesheet)
		self.train_power_entry.setStyleSheet(entry_stylesheet)
		self.train_length_label.setStyleSheet(normal_label_stylesheet)
		self.train_length_entry.setStyleSheet(entry_stylesheet)
		self.train_height_label.setStyleSheet(normal_label_stylesheet)
		self.train_height_entry.setStyleSheet(entry_stylesheet)
		self.train_width_label.setStyleSheet(normal_label_stylesheet)
		self.train_width_entry.setStyleSheet(entry_stylesheet)
		if modification: self.modify_train_button.setStyleSheet(gold_button_stylesheet)
		else: self.create_train_button.setStyleSheet(green_button_stylesheet)
		
		#Connect creation/modification button functionality
		if modification: self.modify_train_button.clicked.connect(self.modify_train)
		else: self.create_train_button.clicked.connect(self.create_train)
		
		#We need to populate the entries if we are doing modification
		if modification:
			#Get train model object from ID
			train_model = handler.train_list[ID]
			
			#Populate entries from model
			self.train_ID_entry.setText(str(ID))
			self.train_mass_entry.setText("{:.2f}".format(round(train_model.mass/907.185, 2)))
			self.train_crew_entry.setText(str(train_model.crew_count))
			self.train_passenger_entry.setText(str(train_model.passenger_capacity))
			self.train_speed_entry.setText("{:.2f}".format(round(train_model.speed_limit/0.44704, 2)))
			self.train_acceleration_entry.setText("{:.2f}".format(round(train_model.acceleration_limit/0.3048, 2)))
			self.train_service_entry.setText("{:.2f}".format(round(train_model.service_deceleration/0.3048, 2)))
			self.train_emergency_entry.setText("{:.2f}".format(round(train_model.emergency_deceleration/0.3048, 2)))
			self.train_power_entry.setText("{:.2f}".format(round(train_model.max_engine_power, 2)))
			self.train_length_entry.setText("{:.2f}".format(round(train_model.length/0.3048, 2)))
			self.train_height_entry.setText("{:.2f}".format(round(train_model.height/0.3048, 2)))
			self.train_width_entry.setText("{:.2f}".format(round(train_model.width/0.3048, 2)))
		
		#Add widgets to grid
		self.grid_layout.addWidget(self.train_settings_label, 0, 0, 1, 2, alignment=Qt.AlignmentFlag.AlignCenter)
		self.grid_layout.addWidget(self.train_ID_label, 1, 0, alignment=Qt.AlignmentFlag.AlignRight)
		self.grid_layout.addWidget(self.train_ID_entry, 1, 1)
		self.grid_layout.addWidget(self.train_mass_label, 2, 0, alignment=Qt.AlignmentFlag.AlignRight)
		self.grid_layout.addWidget(self.train_mass_entry, 2, 1)
		self.grid_layout.addWidget(self.train_crew_label, 3, 0, alignment=Qt.AlignmentFlag.AlignRight)
		self.grid_layout.addWidget(self.train_crew_entry, 3, 1)
		self.grid_layout.addWidget(self.train_passenger_label, 4, 0, alignment=Qt.AlignmentFlag.AlignRight)
		self.grid_layout.addWidget(self.train_passenger_entry, 4, 1)
		self.grid_layout.addWidget(self.train_speed_label, 5, 0, alignment=Qt.AlignmentFlag.AlignRight)
		self.grid_layout.addWidget(self.train_speed_entry, 5, 1)
		self.grid_layout.addWidget(self.train_acceleration_label, 6, 0, alignment=Qt.AlignmentFlag.AlignRight)
		self.grid_layout.addWidget(self.train_acceleration_entry, 6, 1)
		self.grid_layout.addWidget(self.train_service_label, 7, 0, alignment=Qt.AlignmentFlag.AlignRight)
		self.grid_layout.addWidget(self.train_service_entry, 7, 1)
		self.grid_layout.addWidget(self.train_emergency_label, 8, 0, alignment=Qt.AlignmentFlag.AlignRight)
		self.grid_layout.addWidget(self.train_emergency_entry, 8, 1)
		self.grid_layout.addWidget(self.train_power_label, 9, 0, alignment=Qt.AlignmentFlag.AlignRight)
		self.grid_layout.addWidget(self.train_power_entry, 9, 1)
		self.grid_layout.addWidget(self.train_length_label, 10, 0, alignment=Qt.AlignmentFlag.AlignRight)
		self.grid_layout.addWidget(self.train_length_entry, 10, 1)
		self.grid_layout.addWidget(self.train_height_label, 11, 0, alignment=Qt.AlignmentFlag.AlignRight)
		self.grid_layout.addWidget(self.train_height_entry, 11, 1)
		self.grid_layout.addWidget(self.train_width_label, 12, 0, alignment=Qt.AlignmentFlag.AlignRight)
		self.grid_layout.addWidget(self.train_width_entry, 12, 1)
		if modification: self.grid_layout.addWidget(self.modify_train_button, 13, 0, 1, 2)
		else: self.grid_layout.addWidget(self.create_train_button, 13, 0, 1, 2)
		
		#Set spacing of the grid
		self.grid_layout.setVerticalSpacing(5)
        
		#Connect grid to window
		self.setLayout(self.grid_layout)
	
	def error_checking(self):
		messageThrown = False
		msg = ""
		title = ""
		
		try:
			ID = int(self.train_ID_entry.text())
			if ((ID in handler.train_list) and not self.modification) or ID<0 or ("." in self.train_ID_entry.text()):
				self.train_ID_entry.setStyleSheet(red_entry_stylesheet)
				if not messageThrown:
					msg = "ERROR: Please enter a Train ID that is a unique positive integer."
					title = "Invalid ID"
					messageThrown = True
			else: self.train_ID_entry.setStyleSheet(entry_stylesheet)
		except ValueError:
			self.train_ID_entry.setStyleSheet(red_entry_stylesheet)
			if not messageThrown:
				msg = "ERROR: Please enter a Train ID that is a unique positive integer."
				title = "Invalid ID"
				messageThrown = True

		try:
			mass = float(self.train_mass_entry.text())
			if mass<=0:
				self.train_mass_entry.setStyleSheet(red_entry_stylesheet)
				if not messageThrown:
					msg = "ERROR: Please enter a mass that is a positive decimal."
					title = "Invalid Mass"
					messageThrown = True
			else: self.train_mass_entry.setStyleSheet(entry_stylesheet)
		except ValueError:
			self.train_mass_entry.setStyleSheet(red_entry_stylesheet)
			if not messageThrown:
				msg = "ERROR: Please enter a mass that is a positive decimal."
				title = "Invalid Mass"
				messageThrown = True
		try:
			crew = int(self.train_crew_entry.text())
			if crew<0 or ("." in self.train_crew_entry.text()):
				self.train_crew_entry.setStyleSheet(red_entry_stylesheet)
				if not messageThrown:
					msg = "ERROR: Please enter a crew number that is a non-negative integer."
					title = "Invalid Crew Number"
					messageThrown = True
			else: self.train_crew_entry.setStyleSheet(entry_stylesheet)
		except ValueError:
			self.train_crew_entry.setStyleSheet(red_entry_stylesheet)
			if not messageThrown:
				msg = "ERROR: Please enter a crew number that is a non-negative integer."
				title = "Invalid Crew Number"
				messageThrown = True

		try:
			passenger = int(self.train_passenger_entry.text())
			if passenger<0 or ("." in self.train_passenger_entry.text()):
				self.train_passenger_entry.setStyleSheet(red_entry_stylesheet)
				if not messageThrown:
					msg = "ERROR: Please enter a passenger capacity that is a non-negative integer."
					title = "Invalid Passenger Capacity"
					messageThrown = True
			else: self.train_passenger_entry.setStyleSheet(entry_stylesheet)
		except ValueError:
			self.train_passenger_entry.setStyleSheet(red_entry_stylesheet)
			if not messageThrown:
				msg = "ERROR: Please enter a passenger capacity that is a non-negative integer."
				title = "Invalid Passenger Capacity"
				messageThrown = True

		try:
			speed_limit = float(self.train_speed_entry.text())
			if speed_limit<=0:
				self.train_speed_entry.setStyleSheet(red_entry_stylesheet)
				if not messageThrown:
					msg = "ERROR: Please enter a speed limit that is a positive decimal."
					title = "Invalid Speed Limit"
					messageThrown = True
			else: self.train_speed_entry.setStyleSheet(entry_stylesheet)
		except ValueError:
			self.train_speed_entry.setStyleSheet(red_entry_stylesheet)
			if not messageThrown:
				msg = "ERROR: Please enter a speed limit that is a positive decimal."
				title = "Invalid Speed Limit"
				messageThrown = True
				
		try:
			accel_limit = float(self.train_acceleration_entry.text())
			if accel_limit<=0:
				self.train_acceleration_entry.setStyleSheet(red_entry_stylesheet)
				if not messageThrown:
					msg = "ERROR: Please enter an acceleration limit that is a positive decimal."
					title = "Invalid Acceleration Limit"
					messageThrown = True
			else: self.train_acceleration_entry.setStyleSheet(entry_stylesheet)
		except ValueError:
			self.train_acceleration_entry.setStyleSheet(red_entry_stylesheet)
			if not messageThrown:
				msg = "ERROR: Please enter an acceleration limit that is a positive decimal."
				title = "Invalid Acceleration Limit"
				messageThrown = True

		try:
			service = float(self.train_service_entry.text())
			if service<=0:
				self.train_service_entry.setStyleSheet(red_entry_stylesheet)
				if not messageThrown:
					msg = "ERROR: Please enter a service brake deceleration that is a positive decimal."
					title = "Invalid Service Brake Deceleration"
					messageThrown = True
			else: self.train_service_entry.setStyleSheet(entry_stylesheet)
		except ValueError:
			self.train_service_entry.setStyleSheet(red_entry_stylesheet)
			if not messageThrown:
				msg = "ERROR: Please enter a service brake deceleration that is a positive decimal."
				title = "Invalid Service Brake Deceleration"
				messageThrown = True

		try:
			emergency = float(self.train_emergency_entry.text())
			if emergency<=0:
				self.train_emergency_entry.setStyleSheet(red_entry_stylesheet)
				if not messageThrown:
					msg = "ERROR: Please enter an emergency brake deceleration that is a positive decimal."
					title = "Invalid Emergency Brake Deceleration"
					messageThrown = True
			else: self.train_emergency_entry.setStyleSheet(entry_stylesheet)
		except ValueError:
			self.train_emergency_entry.setStyleSheet(red_entry_stylesheet)
			if not messageThrown:
				msg = "ERROR: Please enter an emergency brake deceleration that is a positive decimal."
				title = "Invalid Emergency Brake Deceleration"
				messageThrown = True

		try:
			max_power = float(self.train_power_entry.text())
			if max_power<=0:
				self.train_power_entry.setStyleSheet(red_entry_stylesheet)
				if not messageThrown:
					msg = "ERROR: Please enter a maximum engine power that is a positive decimal."
					title = "Invalid Maximum Engine Power"
					messageThrown = True
			else: self.train_power_entry.setStyleSheet(entry_stylesheet)
		except ValueError:
			self.train_power_entry.setStyleSheet(red_entry_stylesheet)
			if not messageThrown:
				msg = "ERROR: Please enter an emergency brake deceleration that is a positive decimal."
				title = "Invalid Emergency Brake Deceleration"
				messageThrown = True

		try:
			train_length = float(self.train_length_entry.text())
			if train_length<=0:
				self.train_length_entry.setStyleSheet(red_entry_stylesheet)
				if not messageThrown:
					msg = "ERROR: Please enter a train length that is a positive decimal."
					title = "Invalid Train Length"
					messageThrown = True
			else: self.train_length_entry.setStyleSheet(entry_stylesheet)
		except ValueError:
			self.train_length_entry.setStyleSheet(red_entry_stylesheet)
			if not messageThrown:
				msg = "ERROR: Please enter a train length that is a positive decimal."
				title = "Invalid Train Length"
				messageThrown = True

		try:
			train_height = float(self.train_height_entry.text())
			if train_height<=0:
				self.train_height_entry.setStyleSheet(red_entry_stylesheet)
				if not messageThrown:
					msg = "ERROR: Please enter a train height that is a positive decimal."
					title = "Invalid Train Height"
					messageThrown = True
			else: self.train_height_entry.setStyleSheet(entry_stylesheet)
		except ValueError:
			self.train_height_entry.setStyleSheet(red_entry_stylesheet)
			if not messageThrown:
				msg = "ERROR: Please enter a train height that is a positive decimal."
				title = "Invalid Train Height"
				messageThrown = True

		try:
			train_width = float(self.train_width_entry.text())
			if train_width<=0:
				self.train_width_entry.setStyleSheet(red_entry_stylesheet)
				if not messageThrown:
					msg = "ERROR: Please enter a train width that is a positive decimal."
					title = "Invalid Train Width"
					messageThrown = True
			else: self.train_width_entry.setStyleSheet(entry_stylesheet)
		except ValueError:
			self.train_width_entry.setStyleSheet(red_entry_stylesheet)
			if not messageThrown:
				msg = "ERROR: Please enter a train width that is a positive decimal."
				title = "Invalid Train Width"
				messageThrown = True

		if messageThrown:
			my_message(msg, title, error = True, parent = self).exec()
			return False
		
		return True

	
	def create_train(self):
		if not self.error_checking(): return
		
		row = handler.create_train(int(self.train_ID_entry.text()), float(self.train_mass_entry.text()), int(self.train_crew_entry.text()),
			int(self.train_passenger_entry.text()), float(self.train_speed_entry.text()), float(self.train_acceleration_entry.text()),
			float(self.train_service_entry.text()), float(self.train_emergency_entry.text()), float(self.train_power_entry.text()),
			float(self.train_length_entry.text()), float(self.train_height_entry.text()), float(self.train_width_entry.text()))

		self.my_test_UI.train_info_model.insertRow(self.my_test_UI.train_info_model.rowCount())

		row_tool_tip = list_to_tooltip(row)
		
		for i, r in enumerate(row):
			q = QStandardItem(r)
			#q.setToolTip(row_tool_tip)
			self.my_test_UI.train_info_model.setItem(self.my_test_UI.train_info_model.rowCount() - 1, i, q)
				
		self.close()

		my_message("Train " + str(int(self.train_ID_entry.text())) + " was successfully created!", "Creation Complete", error = False, parent = self).exec()
	
	def modify_train(self):
		if not self.error_checking(): return
		
		handler.modify_train(self.ID, int(self.train_ID_entry.text()), float(self.train_mass_entry.text()), int(self.train_crew_entry.text()),
			int(self.train_passenger_entry.text()), float(self.train_speed_entry.text()), float(self.train_acceleration_entry.text()),
			float(self.train_service_entry.text()), float(self.train_emergency_entry.text()), float(self.train_power_entry.text()),
			float(self.train_length_entry.text()), float(self.train_height_entry.text()), float(self.train_width_entry.text()))
			
		self.my_test_UI.train_proxy_model.setData(self.my_test_UI.train_proxy_model.index(self.my_test_UI.train_info_select_table.selectedIndexes()[0].row(), 0), self.train_ID_entry.text())
		
		#Next, we need to find the row in the info table that has the new train ID, and modify the hovertips for that row.
		# for i in range(train_info_model.rowCount()):
			# if train_info_model.item(i, 0).text()==self.train_ID_entry.text():
				# new_tooltip = list_to_tooltip(handler.UI_train_row(handler.train_list[i]))
				# for j in range(train_info_model.columnCount()):
					# train_info_model.item(i, j).setToolTip(new_tooltip)
				# break;
			
		
		self.close()

		my_message("Train " + str(int(self.train_ID_entry.text())) + " was successfully modified!", "Modification Complete", error = False, parent = self).exec()

class TestUIPassengerDialog(QDialog):
	def __init__(self, parent = None):
		#Initialize parent class
		super().__init__(parent)
		
		#Set up windows settings
		self.setWindowTitle("Add/Remove Passengers")
		self.setObjectName("TestUIPassengerDialog")
		self.setStyleSheet('''#TestUIPassengerDialog{background-color: rgb(102,102,102); border: 3px solid black;}''')		

		#Create layout
		self.layout = QGridLayout()

		#Create label, entry, and button
		self.prompt_label = QLabel("Please enter how much the\npassenger count should change by:\n(Negative numbers are allowed)")
		self.passenger_entry = QLineEdit()		 
		self.submit_button = QPushButton("Submit")
			
		#Set fonts and stylesheets
		self.prompt_label.setFont(normal_font)
		self.passenger_entry.setFont(normal_font)
		self.submit_button.setFont(normal_font)

		self.prompt_label.setStyleSheet(normal_label_stylesheet)
		self.passenger_entry.setStyleSheet(entry_stylesheet)
		self.submit_button.setStyleSheet(green_button_stylesheet)

		#Connect button functionality
		self.submit_button.clicked.connect(self.accept)

		#Add widgets to layout
		self.layout.addWidget(self.prompt_label, 0, 0, alignment=Qt.AlignmentFlag.AlignCenter)
		self.layout.addWidget(self.passenger_entry, 1, 0)
		self.layout.addWidget(self.submit_button, 2, 0)

		#Set spacing of the grid
		self.layout.setVerticalSpacing(5)

		#Add the layout to the window
		self.setLayout(self.layout)

		#Fix the size of the window
		self.setFixedSize(self.sizeHint());
		
	def getChange(self):
		try:
			#Just return what's in the entry
			return int(self.passenger_entry.text())
		except ValueError:
			my_message("ERROR: The passenger count change you entered was not a number. Please try again.", error = True).exec()
			return 0
			


class TestUIController(QFrame):
	def __init__(self, my_test_UI, ID):
		#Initialize parent class
		super().__init__()

		self.setGeometry(100,100, 530, 400)

		#Set up calling window
		self.my_test_UI = my_test_UI
		
		#Set ID
		self.ID = ID

		#Set up window settings
		self.setWindowTitle("Train " + str(ID) + " Control Panel")
		self.setObjectName("TestUIController")
		self.setStyleSheet('''#TestUIController{background-color: rgb(102,102,102); border: 3px solid black;}''')		
				
		#Create a new grid
		self.grid_layout = QGridLayout()
		
		#Create widgets
		self.major_control_label = QLabel("Major Controls")
		self.engine_power_label = QLabel("Commanded Engine Power (Watts):")
		self.engine_power_slider = QSlider(Qt.Orientation.Horizontal)
		self.engine_power_entry = QLineEdit()
		self.service_label = QLabel("Service Brake:")
		self.service_button = QPushButton("Hold to Activate")
		self.emergency_label = QLabel("Emergency Brake:")
		self.emergency_button = QPushButton("Hold to Activate")
		self.track_grade_label = QLabel("Current Grade of Track (°):")
		self.track_grade_slider = QSlider(Qt.Orientation.Horizontal)
		self.track_grade_entry = QLineEdit()
		self.passenger_button = QPushButton("Add or Remove Passengers")
		self.minor_control_label = QLabel("Minor Controls")
		self.temperature_label = QLabel("Interior Temperature (°F): ")
		self.temperature_slider = QSlider(Qt.Orientation.Horizontal)
		self.temperature_entry = QLineEdit()
		self.right_doors_label = QLabel("Right Doors (Click to Toggle): ")
		self.right_doors_button = QPushButton("Closed")
		self.left_doors_label = QLabel("Left Doors (Click to Toggle): ")
		self.left_doors_button = QPushButton("Closed")
		self.interior_lights_label = QLabel("Interior Lights (Click to Toggle): ")
		self.interior_lights_button = QPushButton("Off")
		self.exterior_lights_label = QLabel("Exterior Lights (Click to Toggle): ")
		self.exterior_lights_button = QPushButton("Off")
		self.authority_label = QLabel("Commanded Authority (String of Binaries): ")
		self.authority_entry = QLineEdit()
		self.authority_button = QPushButton("Set")
		self.setpoint_speed_label = QLabel("Commanded Setpoint Speed (Integer MPH): ")
		self.setpoint_speed_entry = QLineEdit()
		self.setpoint_speed_button = QPushButton("Set")
		
		#Set widget fonts and stylesheets
		self.major_control_label.setFont(section_font)
		self.engine_power_label.setFont(normal_font)
		self.engine_power_entry.setFont(normal_font)
		self.service_label.setFont(normal_font)
		self.service_button.setFont(normal_font)
		self.emergency_label.setFont(normal_font)
		self.emergency_button.setFont(normal_font)
		self.track_grade_label.setFont(normal_font)
		self.track_grade_entry.setFont(normal_font)
		self.passenger_button.setFont(normal_font)
		self.minor_control_label.setFont(section_font)
		self.temperature_label.setFont(small_font)
		self.temperature_entry.setFont(small_font)
		self.right_doors_label.setFont(small_font)
		self.right_doors_button.setFont(small_font)
		self.left_doors_label.setFont(small_font)
		self.left_doors_button.setFont(small_font)
		self.interior_lights_label.setFont(small_font)
		self.interior_lights_button.setFont(small_font)
		self.exterior_lights_label.setFont(small_font)
		self.exterior_lights_button.setFont(small_font)
		self.authority_label.setFont(small_font)
		self.authority_entry.setFont(small_font)
		self.authority_button.setFont(small_font)
		self.setpoint_speed_label.setFont(small_font)
		self.setpoint_speed_entry.setFont(small_font)
		self.setpoint_speed_button.setFont(small_font)

		self.major_control_label.setStyleSheet(section_label_stylesheet)
		self.engine_power_label.setStyleSheet(normal_label_stylesheet)
		self.engine_power_entry.setStyleSheet(entry_stylesheet)
		self.service_label.setStyleSheet(normal_label_stylesheet)
		self.service_button.setStyleSheet(light_red_button_stylesheet)
		self.emergency_label.setStyleSheet(normal_label_stylesheet)
		self.emergency_button.setStyleSheet(dark_red_button_stylesheet)
		self.track_grade_label.setStyleSheet(normal_label_stylesheet)
		self.track_grade_entry.setStyleSheet(entry_stylesheet)
		self.passenger_button.setStyleSheet(blue_button_stylesheet)
		self.minor_control_label.setStyleSheet(section_label_stylesheet)
		self.temperature_label.setStyleSheet(normal_label_stylesheet)
		self.temperature_entry.setStyleSheet(entry_stylesheet)
		self.right_doors_label.setStyleSheet(normal_label_stylesheet)
		self.left_doors_label.setStyleSheet(normal_label_stylesheet)
		self.interior_lights_label.setStyleSheet(normal_label_stylesheet)
		self.exterior_lights_label.setStyleSheet(normal_label_stylesheet)
		self.exterior_lights_button.setStyleSheet(black_button_stylesheet)
		self.authority_label.setStyleSheet(normal_label_stylesheet)
		self.authority_entry.setStyleSheet(entry_stylesheet)
		self.authority_button.setStyleSheet(gold_button_stylesheet)
		self.setpoint_speed_label.setStyleSheet(normal_label_stylesheet)
		self.setpoint_speed_entry.setStyleSheet(entry_stylesheet)
		self.setpoint_speed_button.setStyleSheet(gold_button_stylesheet)

		#Make sure the door and light toggles line up with the actual values
		if handler.train_list[ID].right_doors_opened:
			self.right_doors_button.setStyleSheet(red_button_stylesheet)
			self.right_doors_button.setText("Opened")
		else: self.right_doors_button.setStyleSheet(green_button_stylesheet)

		if handler.train_list[ID].left_doors_opened:
			self.left_doors_button.setStyleSheet(red_button_stylesheet)
			self.left_doors_button.setText("Opened")
		else: self.left_doors_button.setStyleSheet(green_button_stylesheet)

		if handler.train_list[ID].interior_lights:
			self.interior_lights_button.setStyleSheet(yellow_button_stylesheet)
			self.interior_lights_button.setText("On")
		else: self.interior_lights_button.setStyleSheet(black_button_stylesheet)

		if handler.train_list[ID].exterior_lights:
			self.exterior_lights_button.setStyleSheet(yellow_button_stylesheet)
			self.exterior_lights_button.setText("On")
		else: self.exterior_lights_button.setStyleSheet(black_button_stylesheet)
		
		#Set slider ranges
		self.engine_power_slider.setMinimum(0)
		self.engine_power_slider.setValue(round(handler.train_list[ID].engine_power))
		self.engine_power_slider.setMaximum(round(handler.train_list[ID].max_engine_power))

		self.track_grade_slider.setMinimum(-90)
		self.track_grade_slider.setValue(round(handler.train_list[ID].current_grade))
		self.track_grade_slider.setMaximum(90)
		
		self.temperature_slider.setMinimum(60)
		self.temperature_slider.setValue(round(handler.train_list[ID].interior_temperature))
		self.temperature_slider.setMaximum(80)
		
		#Make the controls change whenever the sliders are RELEASED, so that we don't get many, many updates when the sliders are moved.
		self.engine_power_slider.setTracking(False)
		self.track_grade_slider.setTracking(False)
		self.temperature_slider.setTracking(False)
		
		self.engine_power_slider.valueChanged.connect(self.engine_power_slider_change)
		self.track_grade_slider.valueChanged.connect(self.track_grade_slider_change)
		self.temperature_slider.valueChanged.connect(self.temperature_slider_change)
		
		#Set default entry values
		self.engine_power_entry.setText(str(round(handler.train_list[ID].engine_power)))
		self.track_grade_entry.setText(str(round(handler.train_list[ID].current_grade)))
		self.temperature_entry.setText(str(round(handler.train_list[ID].interior_temperature)))
		self.authority_entry.setText(handler.train_list[ID].commanded_authority)
		self.setpoint_speed_entry.setText(str(round(handler.train_list[ID].commanded_speed)))

		#Connect entry change events as well
		self.engine_power_entry.textChanged.connect(self.engine_power_entry_change)
		self.track_grade_entry.textChanged.connect(self.track_grade_entry_change)
		self.temperature_entry.textChanged.connect(self.temperature_entry_change)
		self.authority_entry.textChanged.connect(self.authority_entry_change)
		self.setpoint_speed_entry.textChanged.connect(self.speed_entry_change)
				
		#Connect the buttons
		self.service_button.pressed.connect(self.service_brake_pressed)
		self.service_button.released.connect(self.service_brake_released)
		self.emergency_button.pressed.connect(self.emergency_brake_pressed)
		self.emergency_button.released.connect(self.emergency_brake_released)
		self.passenger_button.clicked.connect(self.add_remove_passengers)
		self.right_doors_button.clicked.connect(self.right_doors_clicked)
		self.left_doors_button.clicked.connect(self.left_doors_clicked)
		self.interior_lights_button.clicked.connect(self.interior_lights_clicked)
		self.exterior_lights_button.clicked.connect(self.exterior_lights_clicked)
		self.authority_button.clicked.connect(self.set_authority)
		self.setpoint_speed_button.clicked.connect(self.set_speed)
		
		#Disable "Set" buttons by default
		self.authority_button.setEnabled(False)
		self.setpoint_speed_button.setEnabled(False)

		#Add widgets to grid
		self.grid_layout.addWidget(self.major_control_label, 0, 0, 1, 3, alignment=Qt.AlignmentFlag.AlignCenter)
		self.grid_layout.addWidget(self.engine_power_label, 1, 0, alignment=Qt.AlignmentFlag.AlignRight)
		self.grid_layout.addWidget(self.engine_power_slider, 1, 1)
		self.grid_layout.addWidget(self.engine_power_entry, 1, 2, alignment=Qt.AlignmentFlag.AlignLeft)
		self.grid_layout.addWidget(self.service_label, 2, 0, alignment=Qt.AlignmentFlag.AlignRight)
		self.grid_layout.addWidget(self.service_button, 2, 1)
		self.grid_layout.addWidget(self.emergency_label, 3, 0, alignment=Qt.AlignmentFlag.AlignRight)
		self.grid_layout.addWidget(self.emergency_button, 3, 1)
		self.grid_layout.addWidget(self.track_grade_label, 4, 0, alignment=Qt.AlignmentFlag.AlignRight)
		self.grid_layout.addWidget(self.track_grade_slider, 4, 1)
		self.grid_layout.addWidget(self.track_grade_entry, 4, 2, alignment=Qt.AlignmentFlag.AlignLeft)
		self.grid_layout.addWidget(self.passenger_button, 5, 0, 1, 3)
		self.grid_layout.addWidget(self.minor_control_label, 6, 0, 1, 3, alignment=Qt.AlignmentFlag.AlignCenter)
		self.grid_layout.addWidget(self.temperature_label, 7, 0, alignment=Qt.AlignmentFlag.AlignRight)
		self.grid_layout.addWidget(self.temperature_slider, 7, 1)
		self.grid_layout.addWidget(self.temperature_entry, 7, 2, alignment=Qt.AlignmentFlag.AlignLeft)
		self.grid_layout.addWidget(self.right_doors_label, 8, 0, alignment=Qt.AlignmentFlag.AlignRight)
		self.grid_layout.addWidget(self.right_doors_button, 8, 1)
		self.grid_layout.addWidget(self.left_doors_label, 9, 0, alignment=Qt.AlignmentFlag.AlignRight)
		self.grid_layout.addWidget(self.left_doors_button, 9, 1)
		self.grid_layout.addWidget(self.interior_lights_label, 10, 0, alignment=Qt.AlignmentFlag.AlignRight)
		self.grid_layout.addWidget(self.interior_lights_button, 10, 1)
		self.grid_layout.addWidget(self.exterior_lights_label, 11, 0, alignment=Qt.AlignmentFlag.AlignRight)
		self.grid_layout.addWidget(self.exterior_lights_button, 11, 1)
		self.grid_layout.addWidget(self.authority_label, 12, 0, alignment=Qt.AlignmentFlag.AlignRight)
		self.grid_layout.addWidget(self.authority_entry, 12, 1)
		self.grid_layout.addWidget(self.authority_button, 12, 2)
		self.grid_layout.addWidget(self.setpoint_speed_label, 13, 0, alignment=Qt.AlignmentFlag.AlignRight)
		self.grid_layout.addWidget(self.setpoint_speed_entry, 13, 1)
		self.grid_layout.addWidget(self.setpoint_speed_button, 13, 2)
				
		#Set spacing of the grid
		self.grid_layout.setVerticalSpacing(5)
        
		#Connect grid to window
		self.setLayout(self.grid_layout)
	
	def add_remove_passengers(self):
		#Initialize the dialog and passenger change variable
		passenger_dialog = TestUIPassengerDialog(parent = self)
		passenger_change = 0
		
		#Run the dialog. If it runs successfully, i.e. a value has been submitted, then retrieve it and assign it to passenger_change. Else assign 0 to passenger_change
		if (passenger_dialog.exec()): passenger_change = passenger_dialog.getChange()
		
		#Add/Remove the passengers to the train model
		handler.train_list[self.ID].passenger_count += passenger_change;
		
		#Do the same to the table
		for i in range(self.my_test_UI.train_info_model.rowCount()):
				if int(self.my_test_UI.train_info_model.item(i, 0).text()) == self.ID:
					old_passenger_count = int(self.my_test_UI.train_info_model.item(i, 6).text())
					self.my_test_UI.train_info_model.setItem(i, 6, QStandardItem(str(old_passenger_count + passenger_change)))
		
	
	def right_doors_clicked(self):
		#If the doors are open, then close them
		if self.right_doors_button.text() == "Opened":
			self.right_doors_button.setText("Closed")
			self.right_doors_button.setStyleSheet(green_button_stylesheet)

			#Close the train model's right doors
			handler.train_list[self.ID].right_doors_opened = False
			
			#Update the table with "Closed"
			for i in range(self.my_test_UI.train_info_model.rowCount()):
				if int(self.my_test_UI.train_info_model.item(i, 0).text()) == self.ID:
					self.my_test_UI.train_info_model.setItem(i, 12, QStandardItem("Closed"))
								
		#Else open them
		else:
			self.right_doors_button.setText("Opened")
			self.right_doors_button.setStyleSheet(red_button_stylesheet)

			#Open the train model's left doors
			handler.train_list[self.ID].right_doors_opened = True
			
			#Update the table with "Opened"
			for i in range(self.my_test_UI.train_info_model.rowCount()):
				if int(self.my_test_UI.train_info_model.item(i, 0).text()) == self.ID:
					self.my_test_UI.train_info_model.setItem(i, 12, QStandardItem("Opened"))
					
	def left_doors_clicked(self):
		#If the doors are open, then close them
		if self.left_doors_button.text() == "Opened":
			self.left_doors_button.setText("Closed")
			self.left_doors_button.setStyleSheet(green_button_stylesheet)

			#Close the train model's left doors
			handler.train_list[self.ID].left_doors_opened = False
			
			#Update the table with "Closed"
			for i in range(self.my_test_UI.train_info_model.rowCount()):
				if int(self.my_test_UI.train_info_model.item(i, 0).text()) == self.ID:
					self.my_test_UI.train_info_model.setItem(i, 11, QStandardItem("Closed"))
			
		#Else open them
		else:
			self.left_doors_button.setText("Opened")
			self.left_doors_button.setStyleSheet(red_button_stylesheet)

			#Open the train model's left doors
			handler.train_list[self.ID].left_doors_opened = True
			
			#Update the table with "Opened"
			for i in range(self.my_test_UI.train_info_model.rowCount()):
				if int(self.my_test_UI.train_info_model.item(i, 0).text()) == self.ID:
					self.my_test_UI.train_info_model.setItem(i, 11, QStandardItem("Opened"))
					
	def interior_lights_clicked(self):
		#If the lights are off, then turn them on
		if self.interior_lights_button.text() == "Off":
			self.interior_lights_button.setText("On")
			self.interior_lights_button.setStyleSheet(yellow_button_stylesheet)

			#Turn on the train model's interior lights
			handler.train_list[self.ID].interior_lights = True
			
			#Update the table with "On"
			for i in range(self.my_test_UI.train_info_model.rowCount()):
				if int(self.my_test_UI.train_info_model.item(i, 0).text()) == self.ID:
					self.my_test_UI.train_info_model.setItem(i, 9, QStandardItem("On"))
								
		#Else turn them off
		else:
			self.interior_lights_button.setText("Off")
			self.interior_lights_button.setStyleSheet(black_button_stylesheet)

			#Turn off the train model's interior lights
			handler.train_list[self.ID].interior_lights = False
			
			#Update the table with "Off"
			for i in range(self.my_test_UI.train_info_model.rowCount()):
				if int(self.my_test_UI.train_info_model.item(i, 0).text()) == self.ID:
					self.my_test_UI.train_info_model.setItem(i, 9, QStandardItem("Off"))
					
	def exterior_lights_clicked(self):
		#If the lights are off, then turn them on
		if self.exterior_lights_button.text() == "Off":
			self.exterior_lights_button.setText("On")
			self.exterior_lights_button.setStyleSheet(yellow_button_stylesheet)

			#Turn on the train model's exterior lights
			handler.train_list[self.ID].exterior_lights = True
			
			#Update the table with "On"
			for i in range(self.my_test_UI.train_info_model.rowCount()):
				if int(self.my_test_UI.train_info_model.item(i, 0).text()) == self.ID:
					self.my_test_UI.train_info_model.setItem(i, 10, QStandardItem("On"))
			
		#Else turn them off
		else:
			self.exterior_lights_button.setText("Off")
			self.exterior_lights_button.setStyleSheet(black_button_stylesheet)

			#Turn off the train model's exterior lights
			handler.train_list[self.ID].exterior_lights = False
			
			#Update the table with "Off"
			for i in range(self.my_test_UI.train_info_model.rowCount()):
				if int(self.my_test_UI.train_info_model.item(i, 0).text()) == self.ID:
					self.my_test_UI.train_info_model.setItem(i, 10, QStandardItem("Off"))
			
	def service_brake_pressed(self):
		#If the brake is pressed, then the button should say "Activated"
		self.service_button.setText("Activated")
		
		handler.train_list[self.ID].service_brake = True
		
		#We should set the engine power to 0 when the brake is pressed
		self.engine_power_slider_change(0)
		
		#If the emergency brake is on, we should "update" the table with "Emergency". Otherwise, we should update it with "Service"
		brake = "Service"
		if handler.train_list[self.ID].emergency_brake: brake = "Emergency"
		
		for i in range(self.my_test_UI.train_info_model.rowCount()):
			if int(self.my_test_UI.train_info_model.item(i, 0).text()) == self.ID:
				self.my_test_UI.train_info_model.setItem(i, 4, QStandardItem(brake))


	def service_brake_released(self):
		#If the brake is released, then the button should say "Hold to Activate"
		self.service_button.setText("Hold to Activate")

		#Reset the associated train's service brake, and update the table's value
				
		handler.train_list[self.ID].service_brake = False
		
		#If the emergency brake is on, we should "update" the table with "Emergency". Otherwise, we should update it with "No"
		brake = "No"
		if handler.train_list[self.ID].emergency_brake: brake = "Emergency"
		
		for i in range(self.my_test_UI.train_info_model.rowCount()):
			if int(self.my_test_UI.train_info_model.item(i, 0).text()) == self.ID:
				self.my_test_UI.train_info_model.setItem(i, 4, QStandardItem(brake))
		
	def emergency_brake_pressed(self):
		#If the brake is pressed, then the button should say "Activated", the train brake should be turn on, and the table should be updated
		self.emergency_button.setText("Activated")

		#We should set the engine power to 0 when the brake is pressed
		self.engine_power_slider_change(0)

		#Set the associated train's emergency brake, and update the table's value
		handler.train_list[self.ID].emergency_brake = True
		
		for i in range(self.my_test_UI.train_info_model.rowCount()):
			if int(self.my_test_UI.train_info_model.item(i, 0).text()) == self.ID:
				self.my_test_UI.train_info_model.setItem(i, 4, QStandardItem("Emergency"))

	def emergency_brake_released(self):
		#If the brake is released, then the button should say "Hold to Activate", the train brake should be turn off, and the table should be updated
		self.emergency_button.setText("Hold to Activate")

		#Reset the associated train's emergency brake, and update the table's value		
		handler.train_list[self.ID].emergency_brake = False
		
		#If the service brake is on, we should update the table with "Service". Otherwise, we should update it with "No"
		brake = "No"
		if handler.train_list[self.ID].service_brake: brake = "Service"
		
		for i in range(self.my_test_UI.train_info_model.rowCount()):
			if int(self.my_test_UI.train_info_model.item(i, 0).text()) == self.ID:
				self.my_test_UI.train_info_model.setItem(i, 4, QStandardItem(brake))
	
	def engine_power_change(self, value):		
		#Set the associated train's engine power, and update the table's value
		handler.train_list[self.ID].set_engine_power(value + 0.0)
		
		for i in range(self.my_test_UI.train_info_model.rowCount()):
			if int(self.my_test_UI.train_info_model.item(i, 0).text()) == self.ID:
				self.my_test_UI.train_info_model.setItem(i, 3, QStandardItem(str(value)))

	def track_grade_change(self, value):		
		#Set the associated train's engine power, and update the table's value
		handler.train_list[self.ID].current_grade = value + 0.0
		
		for i in range(self.my_test_UI.train_info_model.rowCount()):
			if int(self.my_test_UI.train_info_model.item(i, 0).text()) == self.ID:
				self.my_test_UI.train_info_model.setItem(i, 5, QStandardItem(str(value)))

	def temperature_change(self, value):		
		#Set the associated train's engine power, and update the table's value
		handler.train_list[self.ID].interior_temperature = value + 0.0
		
		for i in range(self.my_test_UI.train_info_model.rowCount()):
			if int(self.my_test_UI.train_info_model.item(i, 0).text()) == self.ID:
				self.my_test_UI.train_info_model.setItem(i, 8, QStandardItem(str(value)))
	
	def engine_power_slider_change(self, value):
		#Set the engine power entry
		self.engine_power_entry.setText(str(round(value)))
		
		#Call the function that actually changes the train and table values
		self.engine_power_change(round(value))
		
	def track_grade_slider_change(self, value):
		self.track_grade_entry.setText(str(round(value)))
		
		#Call the function that actually changes the train and table values
		self.track_grade_change(round(value))

	def temperature_slider_change(self, value):
		self.temperature_entry.setText(str(round(value)))

		#Call the function that actually changes the train and table values
		self.temperature_change(round(value))

	def engine_power_entry_change(self):
		#Try to update the slider when the entry changes. If the entry isn't in the right format, just return
		try:
			#If the entry is above the max, set the slider and entry to the max, and call the actual setter
			if (int(self.engine_power_entry.text())>round(handler.train_list[self.ID].max_engine_power)):
				self.engine_power_slider.setValue(round(handler.train_list[self.ID].max_engine_power))
				self.engine_power_entry.setText(str(round(handler.train_list[self.ID].max_engine_power)))
				self.engine_power_change(round(handler.train_list[self.ID].max_engine_power))
				return
			
			#Same goes for the minimum
			if (int(self.engine_power_entry.text())<0):
				self.engine_power_slider.setValue(0)
				self.engine_power_entry.setText("0")
				self.engine_power_change(0)
				return
			
			#Otherwise, just set the slider to the entry, and call the actual setter wtith the same value
			self.engine_power_slider.setValue(int(self.engine_power_entry.text()))
			self.engine_power_change(int(self.engine_power_entry.text()))
		except ValueError:
			return

	def track_grade_entry_change(self):
		#Try to update the slider when the entry changes. If the entry isn't in the right format, just return
		try:
			#If the entry is above the max, set the slider and entry to the max, and call the actual setter
			if (int(self.track_grade_entry.text())>90):
				self.track_grade_slider.setValue(90)
				self.track_grade_entry.setText("90")
				self.track_grade_change(90)
				return
			
			#Same goes for the minimum
			if (int(self.track_grade_entry.text())<-90):
				self.track_grade_slider.setValue(-90)
				self.track_grade_entry.setText("-90")
				self.track_grade_change(-90)
				return

			#Otherwise, just set the slider to the entry, and call the actual setter wtith the same value
			self.track_grade_slider.setValue(int(self.track_grade_entry.text()))
			self.track_grade_change(int(self.track_grade_entry.text()))
		except ValueError:
			return

	def temperature_entry_change(self):
		#Try to update the slider when the entry changes. If the entry isn't in the right format, just return
		try:
			#If the temperature is above or below the minimum, just return
			if (int(self.temperature_entry.text())<60 or int(self.temperature_entry.text())>80): return
			
			#If not, then update the slider value, and call the actual setter wtith the same value
			self.temperature_slider.setValue(int(self.temperature_entry.text()))
			self.temperature_change(int(self.temperature_entry.text()))
		except ValueError:
			return

	def set_authority(self):
		#Set the authority and disable the button
		handler.train_list[self.ID].commanded_authority = self.authority_entry.text()
		self.authority_button.setEnabled(False)

		#Reflect these changes in the table
		for i in range(self.my_test_UI.train_info_model.rowCount()):
			if int(self.my_test_UI.train_info_model.item(i, 0).text()) == self.ID:
				self.my_test_UI.train_info_model.setItem(i, 13, QStandardItem(self.authority_entry.text()))

	def authority_entry_change(self):
		#If the authority text is different from the actual authority, enable the button, otherwise, disable it
		self.authority_button.setEnabled(self.authority_entry.text()!=handler.train_list[self.ID].commanded_authority)

		#Check to see if there are any characters in the string that aren't a zero or a one. If so, then disable the button and return
		for c in self.authority_entry.text():
			if (c!='0' and c!='1'):
				self.authority_button.setEnabled(False)
				return

	def set_speed(self):
		#Set the speed and disable the button
		handler.train_list[self.ID].commanded_speed = int(self.setpoint_speed_entry.text())
		self.setpoint_speed_button.setEnabled(False)

		#Reflect these changes in the table
		for i in range(self.my_test_UI.train_info_model.rowCount()):
			if int(self.my_test_UI.train_info_model.item(i, 0).text()) == self.ID:
				self.my_test_UI.train_info_model.setItem(i, 14, QStandardItem(self.setpoint_speed_entry.text()))


	def speed_entry_change(self):
		try:
			#If the speed text is different from the actual speed, enable the button, otherwise, disable it
			self.setpoint_speed_button.setEnabled(int(self.setpoint_speed_entry.text())!=int(handler.train_list[self.ID].commanded_speed))

			#If the integer speed is lower than 0, then disable the button
			if (int(self.setpoint_speed_entry.text()) < 0): self.setpoint_speed_button.setEnabled(False)

			#If there is a period in the entry, then it is a decimal, and the button should be disabled
			if '.' in self.setpoint_speed_entry.text(): self.setpoint_speed_button.setEnabled(False)
		except ValueError:
			#If it can't be converted to an int, just disable the button
			self.setpoint_speed_button.setEnabled(False)



class ExpandedTableUI(QFrame):
	def __init__(self, train_proxy_mod):
		#Initialize parent class
		super().__init__()

		#Set up window settings
		self.setWindowTitle("Expanded Table")
		self.setObjectName("ExpandedTableUI")
		self.setGeometry(100,100, 700, 700)
		self.setStyleSheet('''#ExpandedTableUI{background-color: rgb(102,102,102);}''')

		#Create a new grid
		self.grid_layout = QGridLayout()

		#Initialize and set up table settings
		self.train_info_select_table = QTableView()
		self.train_info_select_table.setModel(train_proxy_mod)
		self.train_info_select_table.verticalHeader().hide()
		self.train_info_select_table.setSortingEnabled(True)
		self.train_info_select_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
		self.train_info_select_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows); 
		self.train_info_select_table.horizontalHeader().setHighlightSections(False);
		self.train_info_select_table.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
		self.train_info_select_table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers);
		self.train_info_select_table.setFont(normal_font);
		self.train_info_select_table.horizontalHeader().setFont(normal_font);
		self.train_info_select_table.verticalHeader().setFont(normal_font);
		self.train_info_select_table.setStyleSheet(table_stylesheet)
		self.train_info_select_table.setAlternatingRowColors(True);

		#Put the table on the grid
		self.grid_layout.addWidget(self.train_info_select_table, 0, 0)
			
		#Make the table completely fill the grid
		self.grid_layout.setSpacing(0);
		self.grid_layout.setContentsMargins(0, 0, 0, 0);
		
		#Connect grid to window
		self.setLayout(self.grid_layout)


#Create the thread that will update the train model
class UpdateThreadClass(QThread):
	def __init__(self, time_step = 0, parent = None):
		super().__init__(parent)
		self.time_step = time_step
		
	def run(self):
		#Update the trains and get the data back
		data = handler.update(self.time_step)
		
		#Update the table
		for i in range(train_info_model.rowCount()):
			row_tool_tip = list_to_tooltip(data[i])
			for j in range(train_info_model.columnCount()):
				q = QStandardItem(data[i][j])
				#q.setToolTip(row_tool_tip)
				train_info_model.setItem(i, j, q)

		
class TestUI(QFrame):
	def __init__(self, parent = None):
		#Initialize parent class
		super().__init__(parent)
						
		#Set up window settings
		self.setWindowTitle("Test UI")
		self.setObjectName("TestUI")
		self.setAttribute(Qt.WidgetAttribute.WA_AlwaysShowToolTips, True)
		self.setStyleSheet('''#TestUI{background-color: rgb(102,102,102); border: 3px solid black;}''')
		
		#Create a new grid
		self.grid_layout = QGridLayout()
		
		#Declare widgets
		self.time_section_label = QLabel("Time Control")
		self.time_label = QLabel("Current Time: 0.000 s")
		self.speed_label = QLabel("Current Simulation Speed:")
		self.one_speed_button = QPushButton("1x")
		self.two_speed_button = QPushButton("2x")
		self.three_speed_button = QPushButton("3x")
		self.time_resolution_label = QLabel("Time Resolution (msec):")
		self.time_resolution_entry = QLineEdit()
		self.time_resolution_button = QPushButton("Set")
		self.pause_resume_button = QPushButton("Start")
		self.reset_button = QPushButton("Reset Time")
		self.clear_button = QPushButton("Clear All and Reset Time")
		self.simulate_to_label = QLabel("Simulate To (s):")
		self.simulate_to_entry = QLineEdit()
		self.simulate_to_button = QPushButton("Go")
		self.train_selection_label = QLabel("Train Selection")
		self.train_info_select_table = QTableView()
		self.train_proxy_model = train_proxy_model
		self.train_info_model = train_info_model
		self.expand_table_button = QPushButton("Expand Table...")
		self.train_options_label = QLabel("Train Options")
		self.create_train_button = QPushButton("Create a New Train")
		self.delete_train_button = QPushButton("Delete Selected Train")
		self.modify_train_button = QPushButton("Modify Selected Train Configuration")
		self.delete_all_button = QPushButton("Delete All Trains")
		self.control_panel_button = QPushButton("Open Control Panel for Selected Train")

		#Set up table settings
		self.train_info_select_table.setModel(self.train_proxy_model)
		self.train_info_select_table.verticalHeader().hide()
		self.train_info_select_table.setSortingEnabled(True)
		self.train_info_select_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
		self.train_info_select_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows); 
		self.train_info_select_table.horizontalHeader().setHighlightSections(False);
		self.train_info_select_table.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
		self.train_info_select_table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers);
				
		#Set fonts and stylesheets
		self.time_section_label.setFont(section_font)
		self.train_selection_label.setFont(section_font)
		self.train_options_label.setFont(section_font)
		self.time_label.setFont(time_font)
		self.speed_label.setFont(normal_font)
		self.one_speed_button.setFont(normal_font)
		self.two_speed_button.setFont(normal_font)
		self.three_speed_button.setFont(normal_font)
		self.time_resolution_label.setFont(normal_font)
		self.time_resolution_entry.setFont(normal_font)
		self.time_resolution_button.setFont(normal_font)
		self.pause_resume_button.setFont(normal_font)
		self.reset_button.setFont(normal_font)
		self.clear_button.setFont(normal_font)
		self.simulate_to_label.setFont(normal_font)
		self.simulate_to_entry.setFont(normal_font)
		self.simulate_to_button.setFont(normal_font)
		self.expand_table_button.setFont(small_font)
		self.create_train_button.setFont(normal_font)
		self.delete_train_button.setFont(normal_font)
		self.modify_train_button.setFont(small_font)
		self.delete_all_button.setFont(small_font)
		self.control_panel_button.setFont(normal_font)
		self.train_info_select_table.setFont(normal_font);
		self.train_info_select_table.horizontalHeader().setFont(normal_font);
		self.train_info_select_table.verticalHeader().setFont(normal_font);

		self.time_section_label.setStyleSheet(section_label_stylesheet)
		self.train_selection_label.setStyleSheet(section_label_stylesheet)
		self.train_options_label.setStyleSheet(section_label_stylesheet)
		self.time_label.setStyleSheet(time_label_stylesheet)
		self.speed_label.setStyleSheet(normal_label_stylesheet)
		self.one_speed_button.setStyleSheet(selected_speed_button_stylesheet)
		self.two_speed_button.setStyleSheet(speed_button_stylesheet)
		self.three_speed_button.setStyleSheet(speed_button_stylesheet)
		self.time_resolution_label.setStyleSheet(normal_label_stylesheet)
		self.time_resolution_entry.setStyleSheet(entry_stylesheet)
		self.time_resolution_button.setStyleSheet(gold_button_stylesheet)
		self.pause_resume_button.setStyleSheet(green_button_stylesheet)
		self.reset_button.setStyleSheet(purple_button_stylesheet)
		self.clear_button.setStyleSheet(dark_purple_button_stylesheet)
		self.simulate_to_label.setStyleSheet(normal_label_stylesheet)
		self.simulate_to_entry.setStyleSheet(entry_stylesheet)
		self.simulate_to_button.setStyleSheet(green_button_stylesheet)
		self.train_info_select_table.setStyleSheet(table_stylesheet)
		self.train_info_select_table.setAlternatingRowColors(True);
		self.expand_table_button.setStyleSheet(yellow_button_stylesheet)
		self.create_train_button.setStyleSheet(green_button_stylesheet)
		self.delete_train_button.setStyleSheet(red_button_stylesheet)
		self.modify_train_button.setStyleSheet(gold_button_stylesheet)
		self.delete_all_button.setStyleSheet(dark_red_button_stylesheet)
		self.control_panel_button.setStyleSheet(blue_button_stylesheet)

		#Set default entry values and disable the set and go buttons by default, along with all train options involving selections
		self.time_resolution_entry.setText("1000")
		self.time_resolution = 1.0
		self.time_resolution_button.setEnabled(False)

		self.simulate_to_entry.setText("0")
		self.simulate_to_button.setEnabled(False)
		
		#self.delete_train_button.setEnabled(False)
		#self.modify_train_button.setEnabled(False)
		#self.delete_all_button.setEnabled(False)
		#self.control_panel_button.setEnabled(False)
		
		#Set up speed button toggles
		self.one_speed_button.setCheckable(True)
		self.one_speed_button.setChecked(True)
		self.two_speed_button.setCheckable(True)
		self.three_speed_button.setCheckable(True)
		
		#Connect button and entry functionality
		self.pause_resume_button.clicked.connect(self.pause)
		self.reset_button.clicked.connect(self.reset_time)
		self.clear_button.clicked.connect(self.clear_reset)
		self.one_speed_button.toggled.connect(self.speed_button_one_change)
		self.two_speed_button.toggled.connect(self.speed_button_two_change)
		self.three_speed_button.toggled.connect(self.speed_button_three_change)
		self.time_resolution_entry.textChanged.connect(self.time_res_entry_change)
		self.time_resolution_button.clicked.connect(self.time_res_change)
		self.simulate_to_entry.textChanged.connect(self.simulate_to_entry_change)
		self.simulate_to_button.clicked.connect(self.simulate_to)
		self.expand_table_button.clicked.connect(self.launch_expanded_table)
		self.create_train_button.clicked.connect(self.launch_train_creator)
		self.delete_train_button.clicked.connect(self.delete_selected_train)
		self.modify_train_button.clicked.connect(self.launch_train_modifier)
		self.delete_all_button.clicked.connect(self.delete_all_trains)
		self.control_panel_button.clicked.connect(self.launch_train_controller)
		
		#Add widgets to grid
		self.grid_layout.addWidget(self.time_section_label, 0, 0, 1, 4, alignment=Qt.AlignmentFlag.AlignCenter)
		self.grid_layout.addWidget(self.time_label, 1, 0, 1, 4, alignment=Qt.AlignmentFlag.AlignCenter)
		self.grid_layout.addWidget(self.pause_resume_button, 2, 0)
		self.grid_layout.addWidget(self.reset_button, 2, 1, 1, 2)
		self.grid_layout.addWidget(self.clear_button, 2, 3)
		self.grid_layout.addWidget(self.speed_label, 3, 0, alignment=Qt.AlignmentFlag.AlignRight)
		self.grid_layout.addWidget(self.one_speed_button, 3, 1)
		self.grid_layout.addWidget(self.two_speed_button, 3, 2)
		self.grid_layout.addWidget(self.three_speed_button, 3, 3, alignment=Qt.AlignmentFlag.AlignLeft)
		self.grid_layout.addWidget(self.time_resolution_label, 4, 0, alignment=Qt.AlignmentFlag.AlignRight)
		self.grid_layout.addWidget(self.time_resolution_entry, 4, 1, 1, 2)
		self.grid_layout.addWidget(self.time_resolution_button, 4, 3, alignment=Qt.AlignmentFlag.AlignLeft)
		self.grid_layout.addWidget(self.simulate_to_label, 5, 0, alignment=Qt.AlignmentFlag.AlignRight)
		self.grid_layout.addWidget(self.simulate_to_entry, 5, 1, 1, 2)
		self.grid_layout.addWidget(self.simulate_to_button, 5, 3, alignment=Qt.AlignmentFlag.AlignLeft)
		self.grid_layout.addWidget(self.train_selection_label, 6, 0, 1, 4, alignment=Qt.AlignmentFlag.AlignCenter)
		self.grid_layout.addWidget(self.train_info_select_table, 7, 0, 1, 3)
		self.grid_layout.addWidget(self.expand_table_button, 7, 3, alignment=Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignLeft)
		self.grid_layout.addWidget(self.train_options_label, 8, 0, 1, 4, alignment=Qt.AlignmentFlag.AlignCenter)
		self.grid_layout.addWidget(self.create_train_button, 9, 0, 1, 2)
		self.grid_layout.addWidget(self.delete_train_button, 9, 2, 1, 2)
		self.grid_layout.addWidget(self.modify_train_button, 10, 0, 1, 2)
		self.grid_layout.addWidget(self.delete_all_button, 10, 2, 1, 2)
		self.grid_layout.addWidget(self.control_panel_button, 11, 0, 1, 4)
		
		#Set spacing of the grid
		self.grid_layout.setVerticalSpacing(5)
        
		#Connect grid to window
		self.setLayout(self.grid_layout)
		
		#Set up time interrupts and current time and speed
		self.timer = QTimer()
		self.timer.setTimerType(Qt.TimerType.PreciseTimer)
		self.timer.timeout.connect(self.update_time)
		self.current_time = 0.0
		self.current_speed = 1.0
		
		#Set up list of windows that this window has spawned
		self.creators = []
	
	#This function launches an expanded table
	def launch_expanded_table(self):
		temp = ExpandedTableUI(self.train_proxy_model)
		temp.show()
		for i, c in enumerate(self.creators):
			if not c.isVisible():
				self.creators[i] = temp
				return
		self.creators.append(temp) 
	
	#This function launches a train creator
	def launch_train_creator(self):
		temp = TestUICreatorModifier(self)
		temp.show()
		for i, c in enumerate(self.creators):
			if not c.isVisible():
				self.creators[i] = temp
				return
		self.creators.append(temp)
	
	#This function deletes a train
	def delete_selected_train(self):
		try:
			ID = int(self.train_proxy_model.data(self.train_proxy_model.index(self.train_info_select_table.selectedIndexes()[0].row(), 0)))
			
			if not my_warning(msg = "Are you sure you want to permanently delete Train " + str(ID) + "?", title = "Train Deletion Confirmation", parent = self).exec(): return			

			#This very long statement deletes the train in the train handler
			handler.delete_train(ID)
					
			#This statemenet actually deletes the row in the table corresponding to the train		
			self.train_proxy_model.removeRow(self.train_info_select_table.selectedIndexes()[0].row())
			
			my_message(msg = "Train " + str(ID) + " has been deleted successfully!", title = "Train Successfully Deleted", error = False, parent = self).exec()
		except IndexError:
			my_message(msg = "You have not selected a train!\nPlease select a train and try again.", title = "No Train Selected", error = True, parent = self).exec()			

	#This function deletes all trains
	def delete_all_trains(self):
		if len(handler.train_list) == 0:
			my_message(msg = "There are no trains to delete!", title = "No Trains", error = True, parent = self).exec()
			return

		if not my_warning(msg = "Are you sure you want to permanently delete all trains?", title = "All Train Deletion Confirmation", parent = self).exec(): return			

		#This statemement clears the handler list
		handler.delete_all_trains()
				
		#This statemenet actually deletes all rows in the UI table	
		self.train_info_model.removeRows(0, self.train_info_model.rowCount())

		my_message(msg = "All trains have been deleted successfully!", title = "All Trains Successfully Deleted", error = False, parent = self).exec()

	#This function launches the train modifier, which is the same as the creator, but passes true to the TestUICreatorModifier Modifier variable to indicate its modifing an existing row, along with the train ID.
	def launch_train_modifier(self):
		try:
			#First, check to see if there is a controller with that ID already
			ID = int(self.train_proxy_model.data(self.train_proxy_model.index(self.train_info_select_table.selectedIndexes()[0].row(), 0)))
			for c in self.creators:
				if isinstance(c, TestUIController):
					if c.ID == ID and c.isVisible():
						my_message(msg = "There is a controller open for Train " + str(ID) + ".\nPlease close it to modify its configuration.", title = "Train Controller Open", error = True, parent = self).exec()			
						return

			temp = TestUICreatorModifier(self, modification = True, ID = ID)
			temp.show()			
			for i, c in enumerate(self.creators):
				if not c.isVisible():
					self.creators[i] = temp
					return
			self.creators.append(temp)
		except IndexError:
			my_message(msg = "You have not selected a train!\nPlease select a train and try again.", title = "No Train Selected", error = True, parent = self).exec()			

	#This function launches a train controller
	def launch_train_controller(self):
		try:
			temp = TestUIController(self, ID = int(self.train_proxy_model.data(self.train_proxy_model.index(self.train_info_select_table.selectedIndexes()[0].row(), 0))))
			temp.show()
			for i, c in enumerate(self.creators):
				if not c.isVisible():
					self.creators[i] = temp
					return
			self.creators.append(temp)
		except IndexError:
			my_message(msg = "You have not selected a train!\nPlease select a train and try again.", title = "No Train Selected", error = True, parent = self).exec()			

	#The following three functions ensure that one and only one speed button is toggled at a time
	def speed_button_one_change(self, checked):
		self.one_speed_button.setStyleSheet(selected_speed_button_stylesheet)
		if (round(self.current_speed) != 1):
			self.current_speed = 1.0
			if (self.pause_resume_button.text()=="Pause"): self.timer.start(round(self.time_resolution*1000))
		self.two_speed_button.setStyleSheet(speed_button_stylesheet)
		self.three_speed_button.setStyleSheet(speed_button_stylesheet)
			
	def speed_button_two_change(self, checked):
		self.two_speed_button.setStyleSheet(selected_speed_button_stylesheet)
		if (round(self.current_speed) != 2):
			self.current_speed = 2.0
			if (self.pause_resume_button.text()=="Pause"): self.timer.start(round(self.time_resolution*1000/2.0))
		self.one_speed_button.setStyleSheet(speed_button_stylesheet)
		self.three_speed_button.setStyleSheet(speed_button_stylesheet)

	def speed_button_three_change(self, checked):
		self.three_speed_button.setStyleSheet(selected_speed_button_stylesheet)
		if (round(self.current_speed) != 3):
			self.current_speed = 3.0
			if (self.pause_resume_button.text()=="Pause"): self.timer.start(round(self.time_resolution*1000/3.0))
		self.one_speed_button.setStyleSheet(speed_button_stylesheet)
		self.two_speed_button.setStyleSheet(speed_button_stylesheet)
	
	def simulate_to_entry_change(self):
		#If the entry is above the current time in ms, then the button should be enabled. Otherwise it should be disabled.
		try: 
			if (round(float(self.simulate_to_entry.text())*1000)>round(self.current_time*1000)): self.simulate_to_button.setEnabled(True)
			else: self.simulate_to_button.setEnabled(False)
		except ValueError:
			#If the entry can't be converted to a float, just disable the button
			self.simulate_to_button.setEnabled(False)
		
	
	def time_res_entry_change(self):
		#When the entry for time resolutions changes, if it is different, the time resolution should be enabled. Otherwise, it should be disabled. It should also be disabled when the time is running
		try:
			if (self.pause_resume_button.text()=="Start" or self.pause_resume_button.text()=="Resume"):
				if (int(self.time_resolution_entry.text()) != self.time_resolution*1000 and int(self.time_resolution_entry.text())>0): self.time_resolution_button.setEnabled(True)
				else: self.time_resolution_button.setEnabled(False)
			else:
				self.time_resolution_entry.setEnabled(False)
				self.time_resolution_button.setEnabled(False)
		except ValueError:
			#If the entry can't be converted to a float, just disable the button
			self.time_resolution_button.setEnabled(False)

	def time_res_change(self):
		#Update the time resolution and disable the button
		self.time_resolution = int(self.time_resolution_entry.text())/1000.0
		self.time_resolution_button.setEnabled(False)
	
	def pause(self):
		if (self.pause_resume_button.text()=="Start" or self.pause_resume_button.text()=="Resume"):
			#If the timer has been paused, restart it and change the start/resume button to a pause button
			self.timer.start(round(self.time_resolution*1000/self.current_speed))
			self.pause_resume_button.setText("Pause")
			self.pause_resume_button.setStyleSheet(red_button_stylesheet)
			
			#Also, disable the time resolution options and set the entry box to whatever the actual resolution is
			self.time_resolution_entry.setEnabled(False)
			self.time_resolution_button.setEnabled(False)
			self.time_resolution_entry.setText(str(round(self.time_resolution*1000)))			
			
			#Disable the goto entry as well
			self.simulate_to_entry.setEnabled(False)

			#Set the window title to reflect that the UI is running
			self.setWindowTitle("Test UI (Running...)")

		else:
			#If the timer has been going, stop it and change the puase button to a start/resume button
			self.timer.stop()
			if (self.current_time == 0): self.pause_resume_button.setText("Start")
			else: self.pause_resume_button.setText("Resume")
			self.pause_resume_button.setStyleSheet(green_button_stylesheet)

			#Also, enable the time resolution and goto entry boxes
			self.time_resolution_entry.setEnabled(True)
			self.simulate_to_entry.setEnabled(True)

			#Set the window title to reflect that the UI is paused
			self.setWindowTitle("Test UI (Paused)")
	
	def reset_time(self):
		#When we restart, we should pause the timer and make sure the button is a start button
		self.timer.stop()
		self.pause_resume_button.setText("Start")
		self.pause_resume_button.setStyleSheet(green_button_stylesheet)
		self.setWindowTitle("Test UI (Paused)")

		if not my_warning(msg = "Are you sure you want to reset time?", title = "Reset Time Confirmation", parent = self).exec(): return			
		
		#Also change the current time and label to 0
		self.current_time =  0.0
		self.time_label.setText("Current Time: " + "{:.3f}".format(self.current_time) + " s")

		#Also, enable the time resolution and goto entry boxes
		self.time_resolution_entry.setEnabled(True)
		self.simulate_to_entry.setEnabled(True)
		
		#Call the simulate_to_entry_change function to enable the button if it can be enabled
		self.simulate_to_entry_change()

		#Set the window title back to normal
		self.setWindowTitle("Test UI")
		
		#Finally, reset the trains, and update the table

		#Reset the trains
		data = handler.reset_time()
		
		#Update the table
		for i in range(self.train_info_model.rowCount()):
			for j in range(self.train_info_model.columnCount()):
				self.train_info_model.setItem(i, j, QStandardItem(data[i][j]))		

		my_message(msg = "The time has been reset", title = "Time Reset Successful", parent = self).exec()			
	
	def clear_reset(self):
		self.timer.stop()
		self.pause_resume_button.setText("Start")
		self.pause_resume_button.setStyleSheet(green_button_stylesheet)
		self.setWindowTitle("Test UI (Paused)")

		if not my_warning(msg = "Are you sure you want to reset time and permanently delete all trains?", title = "Clear & Reset Time Confirmation", parent = self).exec(): return			
		
		#We reset the time below
		
		#Change the current time and label to 0
		self.current_time =  0.0
		self.time_label.setText("Current Time: " + "{:.3f}".format(self.current_time) + " s")

		#Also, enable the time resolution and goto entry boxes
		self.time_resolution_entry.setEnabled(True)
		self.simulate_to_entry.setEnabled(True)
		
		#Call the simulate_to_entry_change function to enable the button if it can be enabled
		self.simulate_to_entry_change()

		#Set the window title back to normal
		self.setWindowTitle("Test UI")
		
		#Finally, reset the trains, and update the table

		#Reset the trains
		data = handler.reset_time()
		
		#Update the table
		for i in range(self.train_info_model.rowCount()):
			for j in range(self.train_info_model.columnCount()):
				self.train_info_model.setItem(i, j, QStandardItem(data[i][j]))

		#We delete all trains below
		
		#This statemement clears the handler list
		handler.delete_all_trains()
				
		#This statemenet actually deletes all rows in the UI table	
		self.train_info_model.removeRows(0, self.train_info_model.rowCount())

		my_message(msg = "All trains have been deleted, and the time has been reset", title = "Clear & Reset Successful", parent = self).exec()			
	
	def update_time(self):
		#When we update, the time should tick up by 1, and the label should reflect that
		self.current_time = self.current_time + self.time_resolution
		self.time_label.setText("Current Time: " + "{:.3f}".format(self.current_time) + " s")
		
		#Create and run the thread that updates train and table values
		self.update_thread = UpdateThreadClass(self.time_resolution, self)
		self.update_thread.start()

	def simulate_to(self):
		if not my_warning(msg = "Are you sure you want to simulate to t = " + "{:.3f}".format(float(self.simulate_to_entry.text())) + " s?", title = "Simulate To Confirmation", parent = self).exec(): return			


		#Update the trains and table
		
		#We can update the trains by doing a for loop stepping across the change with our
		#resolution until the remaining change is smaller than the resolution, where we can do it outside the loop
		
		change = round(float(self.simulate_to_entry.text())*1000)/1000.0 - self.current_time
		while (change > self.time_resolution):
			change = change - self.time_resolution
			handler.update(self.time_resolution)

		#Finish off the remainder
		data = handler.update(change)
		
		#Update the table
		for i in range(self.train_info_model.rowCount()):
			for j in range(self.train_info_model.columnCount()):
				self.train_info_model.setItem(i, j, QStandardItem(data[i][j]))		
		
		#Set the current time and disable the go button
		self.current_time = round(float(self.simulate_to_entry.text())*1000)/1000.0
		self.time_label.setText("Current Time: " + "{:.3f}".format(self.current_time) + " s")
		self.simulate_to_button.setEnabled(False)

		#Set the window title to reflect that the UI is paused
		self.setWindowTitle("Test UI (Paused)")
		
		my_message(msg = "The time has been advanced to t = " + "{:.3f}".format(float(self.simulate_to_entry.text())) + " s.", title = "Simulate To Successful", parent = self).exec()			
