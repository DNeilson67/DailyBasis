import pygame 

class nextbutton():
    def __init__(self):
        self.N1image = pygame.image.load("images/red_button_next.png")
        self.N1x = 100
        self.N1y = 600
        self.N1pos = pygame.Rect(100,600,109,111)
        self.N2image = pygame.image.load("images/blue_button_next.png")
        self.N2x = 1100
        self.N2y = 600
        self.N2pos = pygame.Rect(1100,600,109,111)

class plusbutton():
    def __init__(self):
        self.goalgoldspos = pygame.Rect(355, 210, 85, 100)
        self.p1coinpos = pygame.Rect(1085,167,65,75)
        self.p1goldpos = pygame.Rect(1085,247,65,75)
        self.p2coinpos = pygame.Rect(1085,417,65,75)
        self.p2goldpos = pygame.Rect(1085,497,65,75)

class minusbutton():
    def __init__(self):
        self.goalgoldspos = pygame.Rect(155, 210, 80, 100)
        self.p1coinpos = pygame.Rect(950,167,65,75)
        self.p1goldpos = pygame.Rect(950,247,65,75)
        self.p2coinpos = pygame.Rect(950,417,65,75)
        self.p2goldpos = pygame.Rect(950,497,65,75)

class startbutton():
    def __init__(self):
        self.pos = pygame.Rect(485,530,310,115)
        self.setpos = pygame.Rect(515,605,250,80)

class quitbutton():
    def __init__(self):
        self.pos = pygame.Rect(90,528,310,115)
        self.setpos = pygame.Rect(25,10,165,60)

class settingbutton():
    def __init__(self):
        self.pos = pygame.Rect(900,530,310,115)

class onmusicbutton():
    def __init__(self):
        self.pos = pygame.Rect(270,415,103,85)

class offmusicbutton():
    def __init__(self):
        self.pos = pygame.Rect(160,415,103,85)
