class cell():

	def __init__(self, xPos, yPos, state):
		self.x = xPos
		self.y = yPos
		self.alive = state

	def die(self):
		self.alive = False

	def respawn(self):
		self.alive = True