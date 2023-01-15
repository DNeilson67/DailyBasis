import pygame
import sys

class player1():
    def __init__ (self):
        self.p1x = 100
        self.p1y = 450
        self.p1image = pygame.image.load("images/p1.png")
        #Currency
        self.coin = 10
        self.gold = 0

