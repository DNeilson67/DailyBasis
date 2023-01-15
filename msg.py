import sys
import pygame
from settings import Settings
import gamefunctions as gf

class msg():
    #player 1 turn msg
    def p1turnmsg(self,screen):
        font1 = pygame.font.SysFont("comicsansms",60)
        msg1 = "Player 1 Turn!"
        message = font1.render(msg1, True, (255,87,87))
        time_clock = pygame.time.get_ticks()
        while pygame.time.get_ticks() - time_clock < 1000:        
            screen.blit(message, (450,85))
            pygame.display.flip()

    #player 2 turn msg
    def p2turnmsg(self,screen):
        font2 = pygame.font.SysFont("comicsansms",60)
        msg2 = "Player 2 Turn!"
        message = font2.render(msg2, True, (140,85,255))
        time_clock = pygame.time.get_ticks()
        while pygame.time.get_ticks() - time_clock < 1000:        
            screen.blit(message, (450,85))
            pygame.display.flip()