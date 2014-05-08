class cell():

	def __init__(self, xPos, yPos, state):
		self.x = xPos
		self.y = yPos
		self.current = state
		self.future = state

	def die(self):
		self.future = False

	def respawn(self):
		self.future = True

	def switch(self):
		self.current = self.future