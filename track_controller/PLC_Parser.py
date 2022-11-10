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
			return "PLC_file is null";
		try: 
			plcFile = open(self.PLC_file, 'r')
		except:
			return "Issue Opening the PLC File"

		Lines = plcFile.readlines()
		plcFile.close()
		changes = []
		logic_queue = queue.LifoQueue()
		condition = None
		expression = queue.LifoQueue()
		set_var =[]
		# Strips the newline character
		for line in Lines:
			args = line.split(' ')
			for arg in args:
				arg = arg.strip('\n')
				if (arg == "IF"):
					condition =  None
					expression = queue.LifoQueue()
					logic_queue.put("if")
				elif (arg == "ELSE"):
					condition =  not(condition)
					logic_queue.put("else")
				elif (arg == "("):
					expression.put("(")
				elif (arg == ")"):
					expression.put(")")
					
				elif (arg == "{"):
					if(logic_queue.get() == "if"):
						condition = self.determine_condition(expression)
					logic_queue.put("{")
				elif (arg == "}"):
					logic_queue.get()
				elif (arg == "="):
					logic_queue.put("=")
					print(" ")
				elif (arg == "&"):
					print(" ")
					expression.put("&")
				elif (arg == "|"):
					print(" ")
					expression.put("|")
				elif (arg == "!"):
					print(" ")
					expression.put("!")
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
								return "You can't make desicions off of the Railway Crossings"
						elif (var[0] == "S"):
							if ( state == "{" or state == " "):
								set_var.append("S")
								set_var.append(var[1])
							else:
								val = self.get_table_value(switchPos, var[1])
								expression.put(val == "True" or val == True)
						elif (var[0] == "O"):
							state = self.get_state(logic_queue)
							if ( state == "{" or state == " "):
								return "You can't set Occupancy"
							else:
								val = self.get_table_value(Occupancy, var[1])
								expression.put(val == "True" or val == True)
						elif (var[0] == "L"):
							if ( state == "{" or state == " "):
								set_var.append("L")
								set_var.append(var[1])
							else:
								return "You can't make desicions off of the Lights"
						elif (var[0] == "F"):
							if ( state == "{" or state == " "):
								return "You can't set the failures"
							else:
								val = self.get_table_value(status, var[1])
								expression.put(val == "True" or val == True)
						elif (var[0] == "A"):
							state = self.get_state(logic_queue)
							if ( state == "{" or state == " "):
								return "You can't set the Authority"
							else:
								val = self.get_table_value(Authority, var[1])
								expression.put(val == "True" or val == True)
						elif (var[0] == "C"):
							if ( state == "{" or state == " "):
								set_var.append("C")
								set_var.append(var[1])
							else:
								return "You can't make desicions off of the Commanded Speed"
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
							return "Found Unknown character '"+ str(arg) +"' in line '"+str(line)+" '"
					except  Exception as e:
						print(e)
						return str(e)
		return changes

	def determine_condition(self, expression):
		condition = None
		newQueue = queue.LifoQueue()
		while expression.qsize()>0:
			state = expression.get()
			if ( state == ")" ):
				while expression.qsize()>0:
					expp = expression.get()
					if(expp=='('):
						break
					if(expp==')'):
						expression.put(expp)
						expp = self.determine_condition(expression)
					newQueue.put(expp)
				expression.put(self.determine_condition(newQueue))
			elif ( state == "(" ):
				continue
			elif ( state == "|" ):
				operate = expression.get()
				if(operate == ')'):
					expression.put(operate)
					operate = self.determine_condition(expression)
				elif(operate == '!'):
					operate = not(expression.get())
				condition = condition or operate
			elif ( state == "&" ):
				operate = expression.get()
				if(operate == ')'):
					expression.put(operate)
					operate = self.determine_condition(expression)
				elif(operate == '!'):
					operate = not(expression.get())
				condition = condition and operate
			elif ( state == "!" ):
				expression.put(not(expression.get()))
				condition = self.determine_condition(expression)
			elif (isinstance(state, bool)):
				condition = state
			else:
				print("Issue in conditional")
				
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