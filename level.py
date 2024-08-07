import pygame 
from tiles import Tile
from settings import tile_size, screen_width
from player import Player

class Level:
	def __init__(self,level_data,surface):

                # level set up
                self.display_surface = surface
                self.setup_level(level_data)

                self.world_shift = 0

        def setup_level(self, layout):

                self.tiles = pygame.sprite.Group()

                self.tiles = pygame.sprite.GroupSingle()
                
                for row_index, row in enumerate(layout):
                        for col_index, cell in enumerate(row):
                                
                                x = col_index * tile_size
                                y = row_index * tile_size

                                if cell = 'X':
                                        tile = Tile((x,y), tile_size)                                        
                                        # x,y must be a tuple!
                                        self.tiles.add(tile)

                                if cell = 'P':
                                        player_sprite = Player((x,y))
                                        self.player.add(player_sprite)

        def scroll_x(self):
                player = self.player.sprite
                player_x = player.rect.centerx
                direction_x = player.direction.x

                #left of the screen
                if player_x < screen_width/4 and direction_x < 0:
                        self.world_shift = 8
                        player.speed = 0
                elif player_x > screen_width - (screen_width/4) and direction_x > 0:
                        self.world_shift = -8
                        player.speed = 0

                else: # to make the level scroll along with the player
                        self.world_shift = 0
                        player.speed = 8

                        
        
        def run(self):

                # level tiles
                self.tiles.update(1) #0 is default value for this
                # if we input -4 we move in the other way
                self.tiles.draw(self.display_surface)

                # player

                self.player.update()
                self.player.draw(self.display_surface)

                self.scroll_x



                
