import pygame

class Key_states:
	def __init__(self):
		self.states = ["PRESSED", "RELEASED", "UP", "DOWN"]
		self.current_state = "RELEASED"
		self.handlers = {"PRESSED": self.pressed_handler, "RELEASED": self.released_handler, "UP": self.up_handler, "DOWN": self.down_handler}

	def pressed_handler(self, key_down):
		if key_down:
			self.current_state = self.states[3]
		else:
			self.current_state = self.states[1]

	def released_handler(self, key_down):
		if key_down:
			self.current_state = self.states[0]
		else:
			self.current_state = self.states[2]

	def up_handler(self, key_down):
		if key_down:
			self.current_state = self.states[0]

	def down_handler(self, key_down):
		if not key_down:
			self.current_state = self.states[1]

	def get_current_state(self):
		return self.current_state

	def update(self, key_down):
		#print "BEFORE: " +  self.current_state
		#print "KEYDOWN " + str(key_down)
		self.handlers[self.current_state](key_down)
		#print "AFTER: " + self.current_state + "\n"


'''k = key_states();
k.update(0)
k.update(1)
k.update(1)
k.update(0)
k.update(1)
k.update(0)
k.update(0)'''



	

