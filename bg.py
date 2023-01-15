import pygame

class bg():
    def __init__(self):
        self.board = pygame.image.load("images/board.png")
        self.menu = pygame.image.load("images/mainmenu.png")
        self.settings = pygame.image.load("images/settings.png")