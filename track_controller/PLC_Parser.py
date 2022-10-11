import queue
from threading import Condition

class PLC_Parser ():
	def __init__(self):
		self.PLC_file = ""

	def get_table_value(self, table_data, block_value):
		rowC = len(table_data)
		for row in range(rowC):
			(block, state) = table_data[row]
			if str(block) == block_value:
				return state
		return False

	def parse_PLC (self, switchPos, Occupancy):
		logic_queue = queue.LifoQueue()
		if(self.PLC_file == ""):
			return False;
		try: 
			plcFile = open(self.PLC_file, 'r')
		except:
			return False

		Lines = plcFile.readlines()
		changes = []
		logic_queue = queue.LifoQueue()
		condition = None
		set_var =[]
		# Strips the newline character
		for line in Lines:
			args = line.split(' ')
			for arg in args:
				arg = arg.strip('\n')
				if (arg == "IF"):
					logic_queue.put("if")
				elif (arg == "("):
					logic_queue.put("(")
					condition =  None
				elif (arg == ")"):
					logic_queue.get()
				elif (arg == "{"):
					logic_queue.put("{")
				elif (arg == "}"):
					logic_queue.get()
					condition =  None
				elif (arg == "="):
					logic_queue.put("=")
				elif (arg == "&"):
					logic_queue.put("&")
				elif (arg == "|"):
					logic_queue.put("|")
				else:
					if(condition == False and self.get_state(logic_queue) == "{"):
						continue
					var = arg.split('-')
					value = None
					try:
						state = self.get_state(logic_queue) 
						if (var[0] == "R"):
							if ( state == "{" ):
								set_var.append("R")
								set_var.append(var[1])
						elif (var[0] == "S"):
							if ( state == "{" ):
								set_var.append("S")
								set_var.append(var[1])
							else:
								condition = self.set_condition(switchPos, var[1], condition, state)
						elif (var[0] == "O"):
							state = self.get_state(logic_queue)
							if ( state == "{" ):
								set_var.append("O")
								set_var.append(var[1])
							else:
								condition = self.set_condition(Occupancy, var[1], condition, state)
						elif (var[0] == "L"):
							if ( state == "{" ):
								set_var.append("L")
								set_var.append(var[1])
						elif (var[0] == "A"):
							print("Authority")
						elif(state == "="):
							if(var[0] == '0'):
								theBool = "False"
							else:
								theBool = "True"
							tup= (set_var[0], set_var[1], theBool)
							set_var.clear()
							changes.append(tup)
					except  Exception as e:
						print(e)
		return changes

	def set_condition(self, data, block, condition, state):
		if ( state == "(" ):
			val = self.get_table_value(data, block)
			condition = val == "True"
		elif ( state == "|" ):
			val = self.get_table_value(data, block)
			condition = condition or (val == "True")
		elif ( state == "&" ):
			val = self.get_table_value(data, block)
			condition = condition and (val == "True")
		return condition

	def get_state(self, qu):
		state = qu.get()
		qu.put(state)
		return state

	def change_PLC_file(self, new_file):
		self.PLC_file = new_file

	def get_PLC_file(self):
		return self.PLC_file