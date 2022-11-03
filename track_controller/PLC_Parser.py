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

	def parse_PLC (self, switchPos, Occupancy, Authority, sugSpeed, status, speedLim):
		logic_queue = queue.LifoQueue()
		if(self.PLC_file == ""):
			return False;
		try: 
			plcFile = open(self.PLC_file, 'r')
		except:
			return False

		Lines = plcFile.readlines()
		plcFile.close()
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
					condition =  None
					#logic_queue.put("if")
				elif (arg == "ELSE"):
					condition =  not(condition)
				elif (arg == "("):
					logic_queue.put("(")
					condition =  None
				elif (arg == ")"):
					logic_queue.get()
				elif (arg == "{"):
					logic_queue.put("{")
				elif (arg == "}"):
					logic_queue.get()
					#logic_queue.get()
				elif (arg == "="):
					logic_queue.put("=")
				elif (arg == "&"):
					logic_queue.put("&")
				elif (arg == "|"):
					logic_queue.put("|")
				elif (arg == "!"):
					logic_queue.put("!")
				else:
					if(condition == False and (self.get_state(logic_queue) == "{" or self.get_state(logic_queue) == "=")):
						continue
					var = arg.split('-')
					value = None
					try:
						state = self.get_state(logic_queue) 
						if (var[0] == "R"):
							if ( state == "{" or state == " "):
								set_var.append("R")
								set_var.append(var[1])
							else:
								print("no")
						elif (var[0] == "S"):
							if ( state == "{" or state == " "):
								set_var.append("S")
								set_var.append(var[1])
							else:
								val = self.get_table_value(switchPos, var[1])
								condition = self.set_condition(val, var[1], condition, logic_queue)
						elif (var[0] == "O"):
							state = self.get_state(logic_queue)
							if ( state == "{" or state == " "):
								set_var.append("O")
								set_var.append(var[1])
							else:
								val = self.get_table_value(Occupancy, var[1])
								condition = self.set_condition(val, var[1], condition, logic_queue)
						elif (var[0] == "L"):
							if ( state == "{" or state == " "):
								set_var.append("L")
								set_var.append(var[1])
							else:
								print("no")
						elif (var[0] == "F"):
							if ( state == "{" or state == " "):
								print("no")
							else:
								val = self.get_table_value(status, var[1])
								condition = self.set_condition(val, var[1], condition, logic_queue)
						elif (var[0] == "A"):
							state = self.get_state(logic_queue)
							if ( state == "{" or state == " "):
								print("no")
							else:
								val = self.get_table_value(Authority, var[1])
								condition = self.set_condition(val, var[1], condition, logic_queue)
						elif (var[0] == "C"):
							if ( state == "{" or state == " "):
								set_var.append("C")
								set_var.append(var[1])
							else:
								print("no")
						elif(state == "="):
							if(var[0] == '0'):
								theBool = "False"
							elif(var[0] == '1'):
								theBool = "True"

							if(set_var[0] == "C"):
								if var[0] == "D":
									sug = self.get_table_value(sugSpeed, var[1])
									lim = self.get_table_value(speedLim, var[1])
									if (int(sug)>int(lim)): 
										setVa = lim
									else:
										setVa = sug
									tup = (set_var[0], set_var[1], setVa)
								else:
									tup= (set_var[0], set_var[1], int(var[0]))
							else:
								tup= (set_var[0], set_var[1], theBool)

							set_var.clear()
							changes.append(tup)
							logic_queue.get()
						else:
							return False
					except  Exception as e:
						print(e)
						return False
		return changes

	def set_condition(self, val, block, condition, logic_queue):
		state = self.get_state(logic_queue)
		if ( state == "(" ):
			condition = val == "True" or val == True
		elif ( state == "|" ):
			condition = condition or (val == "True" or val == True)
			logic_queue.get()
		elif ( state == "&" ):
			condition = condition and (val == "True" or val == True)
			logic_queue.get()
		elif ( state == "!" ):
			if (val == "True"):
				val ="False"
			else:
				val = "True"
			logic_queue.get()
			condition = self.set_condition(val, block, condition, logic_queue)
		return condition

	def get_state(self, qu):
		if qu.empty() :
			return " "
		state = qu.get()
		qu.put(state)
		return state

	def change_PLC_file(self, new_file):
		self.PLC_file = new_file

	def get_PLC_file(self):
		return self.PLC_file