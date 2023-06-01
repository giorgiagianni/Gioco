import pygame

class Enemy(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('img/blob.png')
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.move_direction = 1
		self.move_counter = 0

	def update(self):
		self.rect.x += self.move_direction
		self.move_counter += 1
		if abs(self.move_counter) > 50:
			self.move_direction *= -1
			self.move_counter *= -1
   
class Lava(pygame.sprite.Sprite):
	def __init__(self, x, y, tile_size = 40):
		pygame.sprite.Sprite.__init__(self)
		img = pygame.image.load('img/lava.png')
		self.image = pygame.transform.scale(img, (tile_size, tile_size // 2))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
  
class Coin(pygame.sprite.Sprite):
	def __init__(self, x, y, tile_size = 40):
		pygame.sprite.Sprite.__init__(self)
		img = pygame.image.load('img/moneta.png')
		self.image = pygame.transform.scale(img, (tile_size//2, tile_size // 2))
		self.rect = self.image.get_rect()
		self.rect.center = (x,y)
  
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/platform.png')
        self.image = pygame.transform.scale(self.image, (40,40))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0
  	

    def update(self):
        self.rect.x += self.move_direction
        self.move_counter += 1
        if abs(self.move_counter) > 50:
            self.move_direction *= -1
            self.move_counter *= -1
  

class World():
    def __init__ (self, data, tile_size, screen, blob_group, dirt_img, grass_img, lava_group, coin_group, platform_group):
        self.tile_list = []
        self.tile_size = tile_size
        self.screen = screen
        self.blob_group = blob_group
        self.dirt_img = dirt_img
        self.grass_img = grass_img
        self.lava_group = lava_group
        self.coin_group = coin_group
        self.platform_group = platform_group
        
        row_count =0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(self.dirt_img, (self.tile_size, self.tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * self.tile_size
                    img_rect.y = row_count * self.tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(self.grass_img, (self.tile_size, self.tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * self.tile_size
                    img_rect.y = img_rect.y = row_count * self.tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                
                if tile == 3:
                    blob = Enemy(col_count * self.tile_size, row_count * self.tile_size + 8)
                    self.blob_group.add(blob)
                    
                if tile == 4:
                    platform = Platform(col_count * self.tile_size, row_count * self.tile_size )
                    platform_group.add(platform)
                    
                if tile == 5 :
                    coin = Coin(col_count * self.tile_size, row_count * self.tile_size )
                    self.coin_group.add(coin)
                if tile == 6:
                    lava = Lava(col_count * self.tile_size, row_count * self.tile_size + (self.tile_size // 2))
                    self.lava_group.add(lava)
                    
                col_count += 1
            row_count += 1
    
    def draw( self):
        for tile in self.tile_list:
            self.screen.blit(tile[0], tile[1])
            
    def reset(self):
        self.blob_group.empty()
        self.lava_group.empty()
        self.blob_group = pygame.sprite.Group()
        self.lava_group = pygame.sprite.Group()
            
    
        
        
                    
                    
					
					
