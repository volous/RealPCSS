import pygame_menu as pgm
from Character import Character
from Mlevel import Level


class Menu:

    def __init__(self, menuW, menuH, screen, game_screen):
        self.menuW = menuW
        self.screen = screen
        self.game_screen = game_screen
        self.menu_draw = pgm.Menu(self.menuW, self.menuH, 'Welcome', theme=pgm.themes.THEME_SOLARIZED)
        self.level = Level(0, 0, 0, 0, self.game_screen)
        self.level.level()
        self.level.impassible_blocks()
        self.char1 = Character(1, 1, 249, 149, self.game_screen, self.level.walkable)


    def mainMenu(self):
        self.mainMenu_draw.add_text_input('Name: ')
        self.mainMenu_draw.add_button('Play', self.playButton)
        self.mainMenu_draw.add_button('Item shop', self.itemShop)
        self.mainMenu_draw.add_button('Settings', self.settings)
        self.mainMenu_draw.add_button('Quit', self.exit)
        self.mainMenu_draw.mainloop(self.screen)

    def playButton(self):
        self.menu_draw.disable()
        self.game_screen.fill((0, 0, 0))
        self.level.draw_level()
        self.char1.player_actions()
        self.char1.draw_char()
    def itemShop(self):
        pass

    def settings(self):
        self.mainMenu_draw.disable()




    def exit(self):
        # Quits displaying on the surface
        pg.display.quit()
        # Quits the surface
        pg.quit()

