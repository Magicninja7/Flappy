import displayio
from blinka_displayio_pygamedisplay import PyGameDisplay
import pygame
import time

pygame.init()
display = PyGameDisplay(width=128, height=128)
splash = displayio.Group()
display.show(splash)


forest_background = displayio.OnDiskBitmap("flappy-back-1_3.bmp")

bg_sprite = displayio.TileGrid(
	forest_background, 
	pixel_shader=forest_background.pixel_shader
)
splash.append(bg_sprite)



#birdie
cat_sheet = displayio.OnDiskBitmap("cat-Sheet.bmp")

cat_sprite = displayio.TileGrid(
	cat_sheet,
	pixel_shader=cat_sheet.pixel_shader,
	width=1,
	height=1,
	tile_width=32,
	tile_height=32,
	default_tile=0,
	x=(display.width - tile_width) // 2,
	y=display.height - tile_height - 10
)

splash.append(cat_sprite)







#run game
frame = 0

while True:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
		pygame.quit()
		exit()
	
	cat_sprite[0] = frame
    frame = (frame + 1) % (cat_sheet.width // tile_width)

	time.sleep(0.01)