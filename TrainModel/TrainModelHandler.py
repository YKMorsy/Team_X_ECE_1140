from TrainModel import TrainModel

from PyQt6.QtGui import QStandardItem

class TrainModelHandler:
	def __init__(self, train_info_model, track_model):
		self.train_list = {}
		self.train_info_model = train_info_model
		self.track_model = track_model
		
	def UI_update(self, list_of_lists):
		for i in range(self.train_info_model.rowCount()):
			#row_tool_tip = list_to_tooltip(list_of_lists[i])
			for j in range(self.train_info_model.columnCount()):
				q = QStandardItem(list_of_lists[i][j])
				#q.setToolTip(row_tool_tip)
				self.train_info_model.setItem(i, j, q)

	def update(self, time_step = 0):
		#This function will build a list of all the train rows, and return it back to the thread that called it
		list_of_lists = []
		
		#Build the list of lists
		for T in self.train_list.values():
			T.update(time_step)
			list_of_lists.append(self.UI_train_row(T))
		
		#Check that no trains have crashed into each other
		blocks_occupied = {}
		for T in self.train_list.values():
			for B in T.block_list:
				if B in blocks_occupied.keys():
					#The dictionary consists of blocks for the keys and IDs for the values, so if the block is already in the dicionary, a crash is assumed
					print("TRAIN " + str(blocks_occupied[B]) + " AND TRAIN " + str(T.ID) + " HAVE BOTH ENTERED BLOCK " + str(B) + ".\nA CRASH HAS BEEN ASSUMED.")
				else:
					blocks_occupied[B] = T.ID

		#Update the UI

		self.UI_update(list_of_lists)

	def set_authority(self, Authority):
		for T in self.train_list.values:
			if T.most_recent_block in Authority.keys:
				if Authority[T.most_recent_block]: T.commanded_authority = "True"
				else: T.commanded_authority = "False"


	def set_speed(self, Speed):
		for T in self.train_list.values:
			if T.most_recent_block in Speed.keys:
				T.commanded_speed = Speed[T.most_recent_block]


	def reset_time(self, time_step = 0):
		#This function will build a list of all the train rows, and return it back
		list_of_lists = []
		
		#Build the list of lists while reseting the trains
		for T in self.train_list.values():
			T.reset_time()
			list_of_lists.append(self.UI_train_row(T))
		
		#Return it back
		return list_of_lists
		
	def UI_train_matrix(self):
		list_of_lists = []
		
		#Build the list of lists
		for T in self.train_list.values():
			list_of_lists.append(self.UI_train_row(T))
		
		#Return it back
		return list_of_lists
		
	#This function "translates" the current state of the passed in train model T into a string list
	def UI_train_row(self, T):
		#Build the brake, fault, lights, and doors strings
		brake = "No"
		if T.service_brake: brake = "Service"
		if T.emergency_brake: brake = "Emergency"

		fault = "None"
		if T.brake_failure and not T.engine_failure and not T.signal_failure: fault = "Brake Failure"
		elif T.brake_failure and T.engine_failure and not T.signal_failure: fault = "Brake Failure, Engine Failure"
		elif T.brake_failure and not T.engine_failure and T.signal_failure: fault = "Brake Failure, Signal Pickup Failure"
		elif T.brake_failure and T.engine_failure and T.signal_failure: fault = "Brake Failure, Engine Failure, Signal Pickup Failure"
		elif not T.brake_failure and T.engine_failure and not T.signal_failure: fault = "Engine Failure"
		elif not T.brake_failure and T.engine_failure and T.signal_failure: fault = "Engine Failure, Signal Pickup Failure"
		elif not T.brake_failure and not T.engine_failure and T.signal_failure: fault = "Signal Pickup Failure"
		
		interior_lights = "Off"
		if T.interior_lights: interior_lights = "On"

		exterior_lights = "Off"
		if T.exterior_lights: exterior_lights = "On"

		left_doors = "Closed"
		if T.left_doors_opened: left_doors = "Opened"

		right_doors = "Closed"
		if T.right_doors_opened: right_doors = "Opened"

		total_mass = (T.mass + (T.passenger_count + T.crew_count)*75.0)/907.185

		#Return back the fully assembled list
		return [str(T.ID), "{:.2f}".format(round(T.velocity/0.44704, 2)), "{:.2f}".format(round(T.current_distance_in_block/0.3048, 2)), str(round(T.engine_power)), "{:.2f}".format(round(total_mass, 2)), brake,
				str(round(T.current_grade)), str(T.passenger_count), str(fault), str(T.interior_temperature), interior_lights,
				exterior_lights, left_doors, right_doors, T.commanded_authority, str(T.commanded_speed)]
	
	def create_train(self, ID, mass = 40.9, crew_count = 2, passenger_capacity = 222, speed_limit = 43.50, acceleration_limit = 3.00, 
    service_deceleration = 3.94, emergency_deceleration = 8.96, max_engine_power = 480000, length = 106, height = 11.2, width = 8.69, 
    car_count = 1, direction = True, line_name = "Red"):
						 
		#Create an instance of TrainModel and add it to the dictionary
		self.train_list[ID] =  TrainModel(self, ID, mass, crew_count, passenger_capacity, speed_limit, acceleration_limit, 
                                          service_deceleration, emergency_deceleration, max_engine_power, length, height, 
										  width, car_count, direction, line_name, self.track_model)

		#Put the train in the UI table
		self.train_info_model.insertRow(self.train_info_model.rowCount())

		#row_tool_tip = list_to_tooltip(row)
		
		for i, r in enumerate(self.UI_train_row(self.train_list[ID])):
			q = QStandardItem(r)
			#q.setToolTip(row_tool_tip)
			self.train_info_model.setItem(self.train_info_model.rowCount() - 1, i, q)
		
	def modify_train(self, old_ID, new_ID, mass, crew_count, passenger_capacity, speed_limit, acceleration_limit, 
    service_deceleration, emergency_deceleration, max_engine_power, length, height, width, car_count):
		self.train_list[old_ID].modify_train(new_ID, mass, crew_count, passenger_capacity, speed_limit, acceleration_limit, 
											 service_deceleration, emergency_deceleration, max_engine_power, length, height, width, car_count)
		self.train_list[new_ID] = self.train_list.pop(old_ID)
				
	def delete_train(self, ID):
		self.train_list.pop(ID)
				
	def delete_all_trains(self):
		self.train_list = {}
		
	def clear_all_failures(self):
		for T in self.train_list.values():
			T.clear_all_failures()
