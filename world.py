import pygame, block, utility

class World:
	def __init__(self, ground_level, gravity):
		self.ground_level = ground_level
		self.gravity = gravity
		self.map = [[None for x in range(utility.screen_width / utility.block_size)] for y in range(utility.screen_height / utility.block_size)] 
		self.ground_y = ground_level / utility.block_size

	def get_gravity(self):
		return self.gravity

	def get_ground_level(self):
		return self.ground_level

	def draw(self):
		new_surface = pygame.Surface((utility.screen_width, utility.screen_height), pygame.SRCALPHA, 32)
		rect = pygame.Rect(0, self.ground_level, utility.screen_width , utility.screen_height - self.ground_level)
		color = (50,200,100)

		pygame.draw.rect(new_surface, color, rect, 0)
		return new_surface;

	def construct_ground(self):
		for x in range(len(self.map[ground_y])):
			self.map[ground_y][x] = block.Block(x,ground_y,0,0, True, False, False, False)
		
		 
