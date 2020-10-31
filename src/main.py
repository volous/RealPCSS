import pygame as pg
import pygame_menu as pgm
from Menu import Menu
from Bomb import Bomb
from Character import Character
from Mlevel import Level

# initialize the pygame
pg.init()
# setting screen height, width and accessible size
size = width, height = 900, 700
# create screen
screen = pg.display.set_mode((width, height))
bRadX, bRadY = 10, 10
# instantiating Bomb class
bomb_player_one = Bomb(bRadX, bRadY, True, 5, True)
# instantiating Char class
char1 = Character(249, 149, screen)
level = Level(0, 0, 0, 0, screen)
running = True
# game loop-ish
while running:
    screen.fill((0, 0, 0))
    level.level()
    level.positional_grid()
    level.impassible_blocks()
    char1.draw_char()
    pg.time.delay(100)
    # timer is available from start, but when an event type of keydown on space, timer_start from bomb class is set
    # to true and begins countdown
    bomb_player_one.timer()
    # checks if there are events in the pygame window
    for event in pg.event.get():
        # if the window closes, it gets closed properly
        if event.type == pg.QUIT:
            running = False
        # if a key is pressed down event is triggered
        if event.type == pg.KEYDOWN:
            # if key pressed is space the timer_start is set to true
            if event.key == pg.K_SPACE:
                bomb_player_one.timer_start = True
                bomb_player_one.bomb(screen)
        trigger = pg.key.get_pressed()
    if trigger[pg.K_w] and char1.posY > char1.vel:
        char1.posY -= char1.vel
    if trigger[pg.K_s] and char1.posY + char1.vel + char1.height < height:
        char1.posY += char1.vel
    if trigger[pg.K_a] and char1.posX > char1.vel:
        char1.posX -= char1.vel
    if trigger[pg.K_d] and char1.posX + char1.vel + char1.width < width:
        char1.posX += char1.vel
        # if the window closes, it gets closed properly
        if event.type == pg.QUIT:
            running = False
        # if a key is pressed down event is triggered
        if event.type == pg.KEYDOWN:
            # if key pressed is space the timer_start is set to true
            if event.key == pg.K_SPACE:
                bomb_player_one.timer_start = True
                bomb_player_one.bomb(screen)
        if level.positional_array[0] + level.block_size is char1.posX is level.positional_array[0]:
            print("hit")