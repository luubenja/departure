import pygame, sys, block, world, key_states, utility

def main():
	pygame.init()

	running = True;
	screen = pygame.display.set_mode((utility.screen_width,utility.screen_height))
	world_map = world.World(screen.get_height() - 100,2)
	person = block.Block(0,0)

	input_states = {pygame.K_w:key_states.Key_states()}

	
	
	
	while running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
			screen.fill((255,255,255))

			pressed = pygame.key.get_pressed()

			input_states[pygame.K_w].update(pressed[pygame.K_w])


			screen.blit(world_map.draw(),(0,0))
			screen.blit(person.draw(),(0,0))
			person.apply_gravity(world_map.ground_level, world_map.gravity)


			pygame.display.flip()


if __name__ == "__main__":
	main()
	