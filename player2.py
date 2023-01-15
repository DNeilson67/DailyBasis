import pygame
import sys

class player2():
    def __init__ (self):
        self.p2x = 1100
        self.p2y = 450
        self.p2image = pygame.image.load("images/p2.png")
        #Currency
        self.coin = 10
        self.gold = 0

