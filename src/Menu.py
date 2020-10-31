import pygame_menu as pgm

class Menu:

    def __init__(self, menuX, menuY, screen):
        self.menuX = menuX
        self.menuY = menuY
        self.screen = screen

    def menu(self):
        menu = pgm.Menu(self.menuX, self.menuY, 'Welcome', theme=pgm.themes.THEME_SOLARIZED)
        menu.mainloop(self.screen)


    def playButton(self):
        pass

    def itemShop(self):
        pass

    def settings(self):
        pass

    def exit(self):
        exit()
