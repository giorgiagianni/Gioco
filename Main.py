import pygame
from pygame.locals import *
from bottoni import Button
# from lava import Lava
from player import Player
from mondo import World
from mondo import Coin

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width = 800
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Platformer')

#variabili
tile_size = 40
game_over = 0
main_menu = True
score = 0
white=(255,255,255)
red=(255,0,0)


font=pygame.font.SysFont('Bauhaus 93',70)
font_score=pygame.font.SysFont('Bauhaus 93',70)

def draw_text(text,font,text_col,x,y):
	img=font.render(text,True,text_col)
	screen.blit(img,(x,y))

#immagini

sfondo_img = pygame.image.load("img/sfondo.jpg")
sfondo_img= pygame.transform.scale(sfondo_img, (screen_width, screen_height))
restart_img = pygame.image.load('img/restart.png')
restart_img = pygame.transform.scale(restart_img, (200, 100))
start_img = pygame.image.load('img/start.png')
start_img = pygame.transform.scale(start_img, (200, 100))
exit_img = pygame.image.load('img/exit.png')
exit_img = pygame.transform.scale(exit_img, (200, 100))
dirt_img = pygame.image.load("img/dirt.png")
grass_img = pygame.image.load("img/grass.png")
lev1_img = pygame.image.load("img/lev1.jpg")
lev1_img = pygame.transform.scale(lev1_img, (70,70))
porta_img=pygame.image.load('img/porta.png.jpg')
porta_img=pygame.transform.scale(porta_img,(40,40))


with open ("level1_data.txt") as f:
    world_data = [list(map(int, riga.strip().split())) for riga in f]
     

blob_group = pygame.sprite.Group()
lava_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()
platform_group = pygame.sprite.Group()


score_coin=Coin(tile_size//2,tile_size//2)
coin_group.add(score_coin)

world = World(world_data, tile_size, screen, blob_group, dirt_img, grass_img, lava_group, coin_group, platform_group )
player =Player(100, screen_height - 130, world, screen, lava_group, blob_group, platform_group)


restart_button = Button(screen_width // 2 - 300, screen_height // 2, restart_img, screen)
start_button = Button(screen_width // 2 - 300, screen_height // 2, start_img, screen)
exit_button = Button(screen_width // 2 + 100, screen_height // 2, exit_img, screen)
porta_button = Button(720, 100, porta_img, screen)




num=1
run = True
while run:


	clock.tick(fps)

	screen.blit(sfondo_img, (0, 0))
 

	if main_menu == True:
		if exit_button.draw():
			run = False
		if start_button.draw():
			main_menu = False
	
	else:
		
		world.draw()

		if game_over == 0:
			blob_group.update()
			platform_group.update()
			if pygame.sprite.spritecollide(player,coin_group,True):
				score+=1
			draw_text('x'+str(score),font_score,white,tile_size-10,10)
			porta_button.draw()
		
		blob_group.draw(screen)
		lava_group.draw(screen)
		coin_group.draw(screen)
		platform_group.draw(screen)
        

		game_over = player.update(game_over)


		if game_over == -1:
			if restart_button.draw():
				player.reset(100, screen_height - 130)
				game_over = 0
				score=0
				blob_group.empty()
				platform_group.empty()
				blob_group.update()
				platform_group.update()
				blob_group.draw(screen)
				platform_group.draw(screen)
				world = World(world_data, tile_size, screen, blob_group, dirt_img, grass_img, lava_group, coin_group, platform_group )
				world.draw()
		
    			
   
				
			if exit_button.draw():
				run=False

				

	for event in pygame.event.get():
		if event.type == QUIT:
			run = False
		if event.type == MOUSEBUTTONDOWN and event.button == 1:
			pos = pygame.mouse.get_pos()
			if  porta_button.rect.collidepoint(pos) and player.rect.collidepoint(pos):
				if num==4:
					draw_text('WIN',font_score,white,400,400)
					num=1
					with open (f"level{num}_data.txt") as f:
						world_data = [list(map(int, riga.strip().split())) for riga in f]
					blob_group = pygame.sprite.Group()
					lava_group = pygame.sprite.Group()
					coin_group = pygame.sprite.Group()
					platform_group = pygame.sprite.Group()

					world = World(world_data, tile_size, screen, blob_group, dirt_img, grass_img, lava_group, coin_group, platform_group )
					player = Player(100, screen_height - 130, world, screen, lava_group, blob_group, platform_group)
					main_menu=True
                    
                    
				else:   
					num+=1
					with open (f"level{num}_data.txt") as f:
						world_data = [list(map(int, riga.strip().split())) for riga in f]
					blob_group = pygame.sprite.Group()
					lava_group = pygame.sprite.Group()
					coin_group = pygame.sprite.Group()
					platform_group = pygame.sprite.Group()

					world = World(world_data, tile_size, screen, blob_group, dirt_img, grass_img, lava_group, coin_group, platform_group )
					player = Player(100, screen_height - 130, world, screen, lava_group, blob_group, platform_group)
					main_menu=False
		
	
	pygame.display.update()

