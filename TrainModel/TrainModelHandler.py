from TrainModel import TrainModel

class TrainModelHandler:
	def __init__(self):
		self.train_list = {}
		
	def update(self, time_step = 0):
		#This function will build a list of all the train rows, and return it back to the thread that called it
		list_of_lists = []
		
		#Build the list of lists
		for T in self.train_list.values():
			T.update(time_step)
			list_of_lists.append(self.UI_train_row(T))
		
		#Return it back
		return list_of_lists

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

		#Return back the fully assembled list
		return [str(T.ID), "{:.2f}".format(round(T.velocity/0.44704, 2)), "{:.2f}".format(round(T.distance/0.3048, 2)), str(round(T.engine_power)), brake,
				str(round(T.current_grade)), str(T.passenger_count), str(fault), str(T.interior_temperature), interior_lights,
				exterior_lights, left_doors, right_doors, T.commanded_authority, str(T.commanded_speed)]
	
	def create_train(self, ID, mass, crew_count, passenger_capacity, speed_limit, acceleration_limit, 
					 service_deceleration, emergency_deceleration, max_engine_power, length, height, width):
						 
		#Create an instance of TrainModel and add it to the dictionary
		self.train_list[ID] =  TrainModel(self, ID, mass, crew_count, passenger_capacity, speed_limit, acceleration_limit, 
                                          service_deceleration, emergency_deceleration, max_engine_power, length, height, width)
		
		#Return the row for the UI table
		return self.UI_train_row(self.train_list[ID])
		
	def modify_train(self, old_ID, new_ID, mass, crew_count, passenger_capacity, speed_limit, acceleration_limit, 
    service_deceleration, emergency_deceleration, max_engine_power, length, height, width):
		self.train_list[old_ID].modify_train(new_ID, mass, crew_count, passenger_capacity, speed_limit, acceleration_limit, 
											 service_deceleration, emergency_deceleration, max_engine_power, length, height, width)
		self.train_list[new_ID] = self.train_list.pop(old_ID)
				
	def delete_train(self, ID):
		self.train_list.pop(ID)
				
	def delete_all_trains(self):
		self.train_list = {}
		
	def clear_all_failures(self):
		for T in self.train_list.values():
			T.clear_all_failures()
