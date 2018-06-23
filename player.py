import pygame, jump_states, utility

class Player:
	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.vx = 0
		self.vy = 0
		self.on_ground = False
		self.jump_state = jump_states.Jump_states()
		self.size = (1,2) #1 block wide 2 blocks tall

	def draw(self):
		new_surface = pygame.Surface((utilty.screen_width, utility.screen_height), pygame.SRCALPHA, 32)
		rect = pygame.Rect(self.x,self.y, utility.block_size*self.size[0], utility.block_size*self.size[1])
		color = (0,0,0)
		if self.on_ground:
			color = (255,0,0)

		pygame.draw.rect(new_surface, color, rect, 0)
		return new_surface;


	def check_collisions(self, platform_grid):

		x_edge = None
		y_edge = None

		if (self.vx != 0):
			if self.vx < 0:
				x_edge = self.x
			if self.vx > 0:
				x_edge = self.x + utility.block_size * self.size[0]
			
		if (self.vy != 0):
			if self.vy < 0:
				y_edge = self.y
			if self.vy > 0:
				y_edge = self.y + utility.block_size * self.size[1]

		


















		