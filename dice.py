import random
import pygame

class dice():
    def picknumber(diceroll):
        diceroll = random.randint(1,6)       
        if diceroll == 1:
            dice = pygame.image.load("images/dice1.png")
        elif diceroll == 2:
            dice = pygame.image.load("images/dice2.png")
        elif diceroll == 3:
            dice = pygame.image.load("images/dice3.png") 
        elif diceroll == 4:
            dice = pygame.image.load("images/dice4.png") 
        elif diceroll == 5:
            dice = pygame.image.load("images/dice5.png") 
        elif diceroll == 6:
            dice = pygame.image.load("images/dice6.png")
        return (dice, diceroll)
        
    def loaddice (self, screen, dice):
        time_clock = pygame.time.get_ticks()   
        while pygame.time.get_ticks() - time_clock < 1000:
            screen.blit(dice, (525,240))
            pygame.display.flip() 