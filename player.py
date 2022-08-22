import pygame 

class Player(pygame.sprite.Sprite):
	def __init__(self,pos):
		super().__init__()
		
		self.image = pygame.Surface((32,64))
		self.image.fill('red)
		self.rect = self.image.get_rect(topleft = pos)

                # VECTORS
                # arrows you can draw in a coordinate system
                # eg vec(100,50)

                # this makes the movement smoother by looking at two diff
                # variables at once

                self.direction = pygame.math.Vector2(0,0)
                self.speed = 8 # to increase the speed of the player
	

        def get_input(self):
                
                keys = pygame.key.get_pressed()

                                if keys[pygame.K_RIGHT]:
                                # we want the player to move right
                                        self.direction = 1

                                elif keys[pygame.K_LEFT]:
                                        self.direction = -1

                                else:
                                        self.direction = 0

        def update(self):

                self.get_input()
                self.rect.x += self.direction.x * self.speed 
                                
                                
                                
