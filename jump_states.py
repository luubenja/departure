import key_states

class Jump_states:
	def __init__(self):
		self.states = ["GROUNDED", "JUMPING", "FALLING", "GLIDING"]
		self.current_state = None
		self.handlers = {}

	def set_current_state(self, index):
		if (index < 0 or index >= len(self.states)):
			current_state = self.states[index]
		else:
			print "ERROR: index out of range"	

	def get_current_state(self):
		return current_state


	def grounded_handler(self, jump_key):
		if jump_key.get_current_state == "PRESSED":
			self.current_state = self.states[1]

	def jumping_handler(self, jump_key, vy):
		if vy > 0:
			self.current_state = self.states[2]
		else if jump_key.get_current_state == "PRESSED":
			self.current_state = self.states[3]


	def falling_handler(self, jump_key):
		if 


	def gliding_handler(self, jump_key):













