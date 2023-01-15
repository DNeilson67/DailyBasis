import pygame
from pygame import mixer
import gamefunctions as gf
import event as events
import movement
import random as rand

class event():
    def chance(self, screen, turn):
        mixer.Sound.play(mixer.Sound("sound/chance.wav"))
        chance = pygame.image.load("images/chance.png")
        time_clock = pygame.time.get_ticks()
        while pygame.time.get_ticks() - time_clock < 1000:        
            screen.blit(chance, (550,225))
            pygame.display.flip()
        random = rand.randint(1,27)
        chancecard = pygame.image.load(f"images/chances/{random}.png")
        time_clock2 = pygame.time.get_ticks()
        
        if random == 1:
            mixer.Sound.play(mixer.Sound("sound/coin.wav"))
            if turn == "Player 1":
                gf.p1c += 15 
                gf.p1g += 0
            elif turn == "Player 2":
                gf.p2c += 15
                gf.p2g += 0
        elif random == 9:
            mixer.Sound.play(mixer.Sound("sound/coin.wav"))
            if turn == "Player 1":
                gf.p1c += 5 
                gf.p1g += 0
            elif turn == "Player 2":
                gf.p2c += 5
                gf.p2g += 0
        elif random == 2:
            mixer.Sound.play(mixer.Sound("sound/coin.wav"))
            gf.p1c += rand.randint(1,20)
            gf.p2c += rand.randint(1,20)
        elif random == 3 or random == 19 or random == 24 or random == 6:
            mixer.Sound.play(mixer.Sound("sound/coin.wav"))
            if turn == "Player 1":
                gf.p1c += 10 
                gf.p1g += 0
            elif turn == "Player 2":
                gf.p2c += 10
                gf.p2g += 0
        elif random == 4 or random == 18:
            mixer.Sound.play(mixer.Sound("sound/coin.wav"))
            if turn == "Player 1":
                gf.p1c += 1 
                gf.p1g += 0
            elif turn == "Player 2":
                gf.p2c += 1
                gf.p2g += 0
        elif random == 5:
            mixer.Sound.play(mixer.Sound("sound/coin.wav"))
            if turn == "Player 1":
                gf.p1c += 3 
                gf.p1g += 0
            elif turn == "Player 2":
                gf.p2c += 3
                gf.p2g += 0
        elif random == 11:
            mixer.Sound.play(mixer.Sound("sound/lost.wav"))
            if turn == "Player 1":
                gf.p1c -= 4 
                gf.p1g += 0
            elif turn == "Player 2":
                gf.p2c -= 4
                gf.p2g += 0
        elif random == 12:
            mixer.Sound.play(mixer.Sound("sound/confirm.wav"))
            if turn == "Player 1":
                gf.a += 3
            if turn == "Player 2":
                gf.b += 3
        elif random == 13:
            mixer.Sound.play(mixer.Sound("sound/coin.wav"))
            if turn == "Player 1":
                gf.p1c += 0.05*gf.p1c
                gf.p1c //= 1
            elif turn == "Player 2":
                gf.p2c += 0.05*gf.p2c
                gf.p2c //= 1
        elif random == 14 or random == 23:
            mixer.Sound.play(mixer.Sound("sound/lost.wav"))
            if turn == "Player 1":
                gf.p1c -= 0.05*gf.p1c
                gf.p1c //= 1
            elif turn == "Player 2":
                gf.p2c -= 0.05*gf.p2c
                gf.p2c //= 1
        elif random == 15:
            mixer.Sound.play(mixer.Sound("sound/coin.wav"))
            if turn == "Player 1":
                gf.p1c += 20 
                gf.p1g += 0
            elif turn == "Player 2":
                gf.p2c += 20
                gf.p2g += 0
        elif random == 16:
            mixer.Sound.play(mixer.Sound("sound/lost.wav"))
            if turn == "Player 1":
                gf.p1c -= 10 
                gf.p1g += 0
            elif turn == "Player 2":
                gf.p2c -= 10
                gf.p2g += 0
        elif random == 17:
            mixer.Sound.play(mixer.Sound("sound/coin.wav"))
            if turn == "Player 1":
                gf.p1c += 25 
                gf.p1g += 0
            elif turn == "Player 2":
                gf.p2c += 25
                gf.p2g += 0
        elif random == 21:
            mixer.Sound.play(mixer.Sound("sound/gold.wav"))
            if turn == "Player 1": 
                gf.p1g += 1
            elif turn == "Player 2":
                gf.p2g += 1           
        elif random == 22:
            mixer.Sound.play(mixer.Sound("sound/coin.wav"))
            if turn == "Player 1":
                gf.p1c += 0.03*gf.p1c
                gf.p1c //= 0
            elif turn == "Player 2":
                gf.p2c += 0.03*gf.p2c
                gf.p2c //= 0
        elif random == 25:
            mixer.Sound.play(mixer.Sound("sound/lost.wav"))
            if turn == "Player 1":
                gf.a -= 1
            elif turn == "Player 2":
                gf.b -= 1
        elif random == 26:
            mixer.Sound.play(mixer.Sound("sound/confirm.wav"))
            if turn == "Player 1":
                gf.a += 5
            elif turn == "Player 2":
                gf.b += 5
        elif random == 27:
            mixer.Sound.play(mixer.Sound("sound/lost.wav"))
            gf.a -= 10
            gf.b -= 10
        while pygame.time.get_ticks() - time_clock2 < 3000:
            screen.blit(chancecard, (550,225))
            pygame.display.flip()
        

    def badluck(self, screen, turn):
        badluck = pygame.image.load("images/badluck.png")
        mixer.Sound.play(mixer.Sound("sound/cancel.wav"))
        time_clock = pygame.time.get_ticks()
        while pygame.time.get_ticks() - time_clock < 1000:        
            screen.blit(badluck, (550,225))
            pygame.display.flip()
        random = rand.randint(1,15)
        badluckcard = pygame.image.load(f"images/badluck/{random}.png")
        time_clock = pygame.time.get_ticks()
        if random == 10:
            mixer.Sound.play(mixer.Sound("sound/confirm.wav"))
        else:
            mixer.Sound.play(mixer.Sound("sound/lost.wav"))

        if random == 1:
            if turn == "Player 1":
                gf.a = 0 
                gf.p1g -= 1
            elif turn == "Player 2":
                gf.b = 0
                gf.p2g -= 1
        elif random == 2 or random == 9:
            if turn == "Player 1":
                gf.p1c -= 10
            elif turn == "Player 2":
                gf.p2c -= 10
        elif random == 3:
            if turn == "Player 1":
                gf.p1c -= 30
            elif turn == "Player 2":
                gf.p2c -= 30
        elif random == 4 or random == 7:
            if turn == "Player 1":
                gf.p1c -= 20
            elif turn == "Player 2":
                gf.p2c -= 20
        elif random == 5:
            if turn == "Player 1":
                gf.p1c -= 15
            elif turn == "Player 2":
                gf.p2c -= 15
        elif random == 6:
            if turn == "Player 1":
                gf.p1c *= 0.85
            elif turn == "Player 2":
                gf.p2c *= 0.85
        elif random == 8:
            if turn == "Player 1":
                gf.p1g -= 1
            elif turn == "Player 2":
                gf.p2g -= 1
        elif random == 11:
            if turn == "Player 1":
                gf.a = 0 
            elif turn == "Player 2":
                gf.b = 0
        elif random == 12:
            if turn == "Player 1":
                gf.a -= 3 
            elif turn == "Player 2":
                gf.b -= 3
        elif random == 13:
            if turn == "Player 1":
                gf.p1c *= 0.75
            elif turn == "Player 2":
                gf.p2c *= 0.75
        elif random == 14:
            if turn == "Player 1":
                gf.p1c -= 1
            elif turn == "Player 2":
                gf.p2c -= 1
        elif random == 15:
            if turn == "Player 1":
                gf.a -= 5 
            elif turn == "Player 2":
                gf.b -= 5
        while pygame.time.get_ticks() - time_clock < 3000:
            screen.blit(badluckcard, (550,225))
            pygame.display.flip()

    def gacha(self, screen, turn):
        mixer.Sound.play(mixer.Sound("sound/gacha.wav"))
        gacha =  pygame.image.load("images/gacha.png")
        time_clock = pygame.time.get_ticks()
        while pygame.time.get_ticks() - time_clock < 1000:        
            screen.blit(gacha, (550,225))
            pygame.display.flip()
        random = rand.randint(1,100)
        time_clock2 = pygame.time.get_ticks()
        if random in range (1,5):
            mixer.Sound.play(mixer.Sound("sound/gold.wav"))
            gachacard = pygame.image.load(f"images/gacha/1.png")
            if turn == "Player 1":
                gf.p1g += 1 
            elif turn == "Player 2":
                gf.p2g += 1
        if random in range (5,30):
            mixer.Sound.play(mixer.Sound("sound/coin.wav"))
            gachacard = pygame.image.load(f"images/gacha/2.png")
            if turn == "Player 1":
                gf.p1c += 5 
            elif turn == "Player 2":
                gf.p2c += 5
        if random in range (30,51):
            mixer.Sound.play(mixer.Sound("sound/coin.wav"))
            gachacard = pygame.image.load(f"images/gacha/3.png")
            if turn == "Player 1":
                gf.p1c += 10
            elif turn == "Player 2":
                gf.p2c += 10
        if random in range (51,76):
            mixer.Sound.play(mixer.Sound("sound/coin.wav"))
            gachacard = pygame.image.load(f"images/gacha/4.png")
            if turn == "Player 1":
                gf.p1c += 15
            elif turn == "Player 2":
                gf.p2c += 15
        if random in range (76,101):
            mixer.Sound.play(mixer.Sound("sound/coin.wav"))
            gachacard = pygame.image.load(f"images/gacha/5.png")
            if turn == "Player 1":
                gf.p1c += 20
            elif turn == "Player 2":
                gf.p2c += 20

        while pygame.time.get_ticks() - time_clock2 < 3000:
            screen.blit(gachacard, (550,225))
            pygame.display.flip()

    def bluespace(self, turn):
        mixer.Sound.play(mixer.Sound("sound/coin.wav"))
        if turn == "Player 1":
            gf.p1c += 5
        elif turn == "Player 2":
            gf.p2c += 5
    
    def redspace(self, turn):
        mixer.Sound.play(mixer.Sound("sound/lost.wav"))
        if turn == "Player 1":
            gf.p1c -= 5
        elif turn == "Player 2":
            gf.p2c -= 5

    def goldspace1(self, screen, turn):
        if turn == "Player 1":
            if gf.p1c >= 20:
                mixer.Sound.play(mixer.Sound("sound/gold.wav"))
                gf.p1c -= 20
                gf.p1g += 1
            elif gf.p1c < 20:
                mixer.Sound.play(mixer.Sound("sound/cancel.wav"))
                font = pygame.font.SysFont("comicsansms", 20)
                message = font.render("You do not have enough coins", True, (255,255,255))
                time_clock = pygame.time.get_ticks()
                while pygame.time.get_ticks() - time_clock < 1000:
                        screen.blit(message, (500,160))
                        pygame.display.flip()

        elif turn == "Player 2":
            if gf.p2c >= 20:
                mixer.Sound.play(mixer.Sound("sound/gold.wav"))
                gf.p2c -= 20
                gf.p2g += 1
            elif gf.p1c < 20:
                mixer.Sound.play(mixer.Sound("sound/cancel.wav"))
                font = pygame.font.SysFont("comicsansms", 20)
                message = font.render("You do not have enough coins", True, (255,255,255))
                time_clock = pygame.time.get_ticks()
                while pygame.time.get_ticks() - time_clock < 1000:
                        screen.blit(message, (500,160))
                        pygame.display.flip()

    def goldspace3(self, screen, turn):
        if turn == "Player 1":
            if gf.p1c >= 60:
                mixer.Sound.play(mixer.Sound("sound/gold.wav"))
                gf.p1c -= 60
                gf.p1g += 3
            elif gf.p1c >= 40:
                mixer.Sound.play(mixer.Sound("sound/gold.wav"))
                gf.p1c -= 40
                gf.p1g += 2
            elif gf.p1c >= 20:
                mixer.Sound.play(mixer.Sound("sound/gold.wav"))
                gf.p1c -= 20
                gf.p1g += 1
            elif gf.p1c < 20:
                mixer.Sound.play(mixer.Sound("sound/cancel.wav"))
                font = pygame.font.SysFont("comicsansms", 20)
                message = font.render("You do not have enough coins", True, (255,255,255))
                time_clock = pygame.time.get_ticks()
                while pygame.time.get_ticks() - time_clock < 1000:
                        screen.blit(message, (500,160))
                        pygame.display.flip()

        elif turn == "Player 2":
            if gf.p2c >= 60:
                mixer.Sound.play(mixer.Sound("sound/gold.wav"))
                gf.p2c -= 60
                gf.p2g += 3
            elif gf.p2c >= 40:
                mixer.Sound.play(mixer.Sound("sound/gold.wav"))
                gf.p2c -= 40
                gf.p2g += 2
            elif gf.p2c >= 20:
                mixer.Sound.play(mixer.Sound("sound/gold.wav"))
                gf.p2c -= 20
                gf.p2g += 1
            elif gf.p2c < 20:
                mixer.Sound.play(mixer.Sound("sound/cancel.wav"))
                font = pygame.font.SysFont("comicsansms", 20)
                message = font.render("You do not have enough coins", True, (255,255,255))
                time_clock = pygame.time.get_ticks()
                while pygame.time.get_ticks() - time_clock < 1000:
                        screen.blit(message, (500,160))
                        pygame.display.flip()
    
    
