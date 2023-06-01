import pygame

class Player():
	def __init__(self, x, y, world, screen, blob_group, lava_group, platform_group):
		self.reset(x,y)
		self.world = world
		self.screen = screen
		self.blob_group = blob_group
		self.lava_group = lava_group
		self.platform_group = platform_group

	def update(self, game_over):
		dx = 0
		dy = 0
		walk_cooldown = 5
		con = 20

		if game_over == 0:
			key = pygame.key.get_pressed()
			if key[pygame.K_SPACE] and self.jumped == False and self.in_air == False:
				self.vel_y = -16
				self.jumped = True
			if key[pygame.K_SPACE] == False:
				self.jumped = False
			if key[pygame.K_LEFT]:
				dx -= 3
				self.counter += 1
				self.direction = -1
			if key[pygame.K_RIGHT]:
				dx += 3
				self.counter += 1
				self.direction = 1
			if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False:
				self.counter = 0
				self.index = 0
				if self.direction == 1:
					self.image = self.images_right[self.index]
				if self.direction == -1:
					self.image = self.images_left[self.index]


			if self.counter > walk_cooldown:
				self.counter = 0	
				self.index += 1
				if self.index >= len(self.images_right):
					self.index = 0
				if self.direction == 1:
					self.image = self.images_right[self.index]
				if self.direction == -1:
					self.image = self.images_left[self.index]


			
			self.vel_y += 1
			if self.vel_y > 10:
				self.vel_y = 10
			dy += self.vel_y

			
			self.in_air = True
			for tile in self.world.tile_list:
				
				if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
					dx = 0
				
				if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
					
					if self.vel_y < 0:
						dy = tile[1].bottom - self.rect.top
						self.vel_y = 0
					
					elif self.vel_y >= 0:
						dy = tile[1].top - self.rect.bottom
						self.vel_y = 0
						self.in_air = False
      
      
			if pygame.sprite.spritecollide(self, self.blob_group, False):
				game_over = -1

			if pygame.sprite.spritecollide(self, self.lava_group, False):
				game_over = -1
    
			for platform in self.platform_group:
				
				if platform.rect.colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
					dx = 0
				
				if platform.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
					
					if abs((self.rect.top + dy) - platform.rect.bottom) < con:
						self.vel_y = 0
						dy = platform.rect.bottom - self.rect.top
					
					elif abs((self.rect.bottom + dy) - platform.rect.top) < con:
						self.rect.bottom = platform.rect.top - 1
						self.in_air = False
						dy = 0
    
     
			
		 

			
			self.rect.x += dx
			self.rect.y += dy


		elif game_over == -1:
			self.image = self.dead_image
			self.rect.y -= 5

		
		self.screen.blit(self.image, self.rect)

		return game_over

	def reset(self, x, y):
		self.images_right = []
		self.images_left = []
		self.index = 0
		self.counter = 0
		for num in range(1, 5):
			img_right = pygame.image.load(f'img/guy{num}.png')
			img_right = pygame.transform.scale(img_right, (30, 60))
			img_left = pygame.transform.flip(img_right, True, False)
			self.images_right.append(img_right)
			self.images_left.append(img_left)
		self.dead_image = pygame.image.load('img/ghost.png')
		self.dead_image = pygame.transform.scale(self.dead_image, (100,180))
		self.image = self.images_right[self.index]
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.width = self.image.get_width()
		self.height = self.image.get_height()
		self.vel_y = 0
		self.jumped = False
		self.direction = 0
		self.in_air = True

		