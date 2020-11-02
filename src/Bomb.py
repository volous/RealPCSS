import time
import pygame


class Bomb:

    # bRad is blastRadius
    def __init__(self, bRadX, bRadY, bState, bSecs, bReload, screen):
        self.bRadX = bRadX
        self.bRadY = bRadY
        self.bState = bState
        self.bSecs = bSecs
        self.bReload = bReload
        self.timer_start = False
        self.bomb_state_one = pygame.image.load("Res/bomb1.png")
        pygame.transform.scale(self.bomb_state_one, (32, 32))
        self.bomb_state_two = pygame.image.load("Res/bomb2.png")
        self.bomb_state_three = pygame.image.load("Res/bomb3.png")
        self.bomb_state = [self.bomb_state_one, self.bomb_state_two, self.bomb_state_three]
        self.screen = screen


    def bomb(self):
        # sets secs to be equal to bSecs
        bomb_state = self.bomb_state
        secs = self.bSecs
        # same timer as in timer method
        while secs > 0 and self.timer_start:
            # if statements that check for the timer position and prints the corespondent state
            if secs == 4:
                self.screen.blit(bomb_state[0])
            if secs == 3:
                self.screen.blit(bomb_state[1])
            if secs == 2:
                self.screen.blit(bomb_state[2])
        secs -= 1
        time.sleep(1)


    # timer method
    def timer(self):
        # sets secs to be equal to bSecs
        secs = self.bSecs
        # while secs is greater than 0 and timer_start is true secs is -1 per second
        while secs > 0 and self.timer_start:
            secs -= 1
            # sleeps for 1 second and stops the while loop continuing for 1 second
            time.sleep(1)
            # of secs is = to 0 code is executed
            if secs == 1:
                print("boom")
                # resets secs to start point
                secs = self.bSecs
                # timer_start is set to false again
                self.timer_start = False