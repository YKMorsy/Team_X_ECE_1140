from math import sin, pi

class TrainModel:
    def __init__(self, handler, ID, mass = 40.9, crew_count = 2, passenger_capacity = 74, speed_limit = 43.50, acceleration_limit = 1.64, 
    service_deceleration = 3.94, emergency_deceleration = 8.96, max_engine_power = 480, length = 106, height = 11.2, width = 8.69):
		
        #Copy all the inputs to the class, with all the necessary conversions
        self.handler = handler
        self.ID = ID
        self.mass = mass * 907.185
        self.crew_count = crew_count
        self.passenger_capacity = passenger_capacity
        self.speed_limit = speed_limit * 0.44704
        self.acceleration_limit = acceleration_limit * 0.3048
        self.service_deceleration = service_deceleration * 0.3048
        self.emergency_deceleration = emergency_deceleration * 0.3048
        self.max_engine_power = max_engine_power
        self.length = length * 0.3048
        self.height = height * 0.3048
        self.width = width * 0.3048


        self.velocity = 0.0
        self.distance = 0.0
        self.engine_power = 0.0
        self.service_brake = False
        self.emergency_brake = False
        self.current_grade = 0.0
        self.passenger_count = 0
        self.brake_failure = False
        self.engine_failure = False
        self.signal_failure = False
        self.interior_temperature = 70
        self.interior_lights = False
        self.exterior_lights = False
        self.left_doors_opened = False
        self.right_doors_opened = False
        self.commanded_authority = ""
        self.commanded_speed = 0
        
    def modify_train(self, ID, mass, crew_count, passenger_capacity, speed_limit, acceleration_limit, 
    service_deceleration, emergency_deceleration, max_engine_power, length, height, width):
		
        #Copy all the inputs to the class, with all the necessary conversions
        self.ID = ID
        self.mass = mass * 907.185
        self.crew_count = crew_count
        self.passenger_capacity = passenger_capacity
        self.speed_limit = speed_limit * 0.44704
        self.acceleration_limit = acceleration_limit * 0.3048
        self.service_deceleration = service_deceleration * 0.3048
        self.emergency_deceleration = emergency_deceleration * 0.3048
        self.max_engine_power = max_engine_power
        self.length = length * 0.3048
        self.height = height * 0.3048
        self.width = width * 0.3048
        
    def reset_time(self):
        self.velocity = 0.0
        self.distance = 0.0
        self.passenger_count = 0
        self.brake_failure = False
        self.engine_failure = False
        self.signal_failure = False

    
    def clear_all_failures(self):
        self.brake_failure = False        
        self.engine_failure = False
        self.signal_failure = False
    
    def generate_brake_failure(self):
        self.brake_failure = True

    def generate_engine_failure(self):
        self.engine_failure = True
        
        #The engine power needs to be set to 0 as well as part of the failure
        self.engine_power = 0.0

    def generate_signal_pickup_failure(self):
        self.signal_failure = True
        
    def set_engine_power(self, value):
        #If there is an engine failure, the power can't be set, and we should return
        if(self.engine_failure): return

        self.engine_power = value

    def update(self, time_step):
        #First, calculate total mass from # of passengers and crew
        total_mass = self.mass + (self.passenger_count + self.crew_count)*75.0

        #Next, calculate the change in velocity
        
        #Set the default change to 0
        velocity_change = 0.0
        
        #If the velocity is 0 and the engine power or track grade are non-zero, the change is limited by the max acceleration
        if int(round(self.velocity,2) * 100) == 0:
            if int(round(self.engine_power,2) * 100) != 0 or int(round(self.current_grade,2) * 100) != 0: velocity_change = self.acceleration_limit * time_step
                
        #Otherwise, it should be based off of the engine power, unless it is higher than the max acceleration
        else:
            velocity_change = (self.engine_power/(total_mass*self.velocity) - 9.8*sin(2*pi*self.current_grade/360)) * time_step
            if velocity_change > self.acceleration_limit * time_step: velocity_change = self.acceleration_limit * time_step
        
        #Make sure there isn't a brake failure before doing brake calculations
        if not self.brake_failure:
            #If the brakes are pressed, then we assume that the engine power is zero. Also, if both are pressed, then the emergency brake takes precedence

            if self.service_brake: velocity_change = (-self.service_deceleration - 9.8*sin(2*pi*self.current_grade/360)) * time_step
            if self.emergency_brake: velocity_change = (-self.emergency_deceleration - 9.8*sin(2*pi*self.current_grade/360)) * time_step

        #Set the new velocity in a temp variable
        new_velocity = self.velocity + velocity_change
        
        #The velocity should never be negative. The only circumstance where the 
        #velocity variable could become negative is when the brake deceleration would cause it to 
        #"overshoot" 0, in which case, we should set it back to 0
        if new_velocity<0.0: new_velocity = 0.0 
        
        #If the new velocity is above the speed limit, set it to the speed limit
        if new_velocity>self.speed_limit: new_velocity = self.speed_limit
        
        #Calculate the new position by taking the average of the old and new velocities
        self.distance = self.distance + (self.velocity + new_velocity)/2 * time_step
        
        #Actually set the new velocity
        self.velocity = new_velocity
