import pygame
from pygame import mixer
import random as rand
import sys
import time
from settings import Settings

import gamefunctions as gf
from player1 import player1
from player2 import player2
from bg import bg
from dice import dice as dices

#inputs imports
from inputs import startbutton
from inputs import nextbutton
from inputs import settingbutton
from inputs import quitbutton
from inputs import onmusicbutton
from inputs import offmusicbutton
from inputs import plusbutton
from inputs import minusbutton

#initialize the game
pygame.init()
screen = pygame.display.set_mode((Settings().screen_width,Settings().screen_height))
pygame.display.set_caption("Daily Basis")
pygame.time.Clock().tick(60)

#BGM Music
music = mixer.music.load("sound/BGM.wav")
mixer.music.play(-1)
mixer.music.set_volume(0.3)

#Font General Settings
font1 = pygame.font.SysFont("comicsansms", 60)
font2 = pygame.font.SysFont("comicsansms", 40)
p1fontcolor = (255, 87, 87)
p2fontcolor = (140, 85, 255)

#First Turn MSG
messageft = font1.render(f"First Turn: {gf.turn}", True, (0,0,0))
    
#Backgrounds
mmbg = bg().menu
sbg = bg().settings
board = bg().board

#players
p1 = player1().p1image
p2 = player2().p2image

#start button
startpos = startbutton().pos
startsetpos = startbutton().setpos

#quit button
quitpos = quitbutton().pos
quitsetpos = quitbutton().setpos

#settings button
setpos = settingbutton().pos
onmusicpos = onmusicbutton().pos
offmusicpos = offmusicbutton().pos
plusp1coinpos = plusbutton().p1coinpos
plusp1goldpos = plusbutton().p1goldpos
plusp2coinpos = plusbutton().p2coinpos
plusp2goldpos = plusbutton().p2goldpos
plusgoalgoldspos = plusbutton().goalgoldspos
minusp1coinpos = minusbutton().p1coinpos
minusp1goldpos = minusbutton().p1goldpos
minusp2coinpos = minusbutton().p2coinpos
minusp2goldpos = minusbutton().p2goldpos
minusgoalgoldspos = minusbutton().goalgoldspos

#next turn P1 button
N1image = nextbutton().N1image
N1pos = nextbutton().N1pos

#next turn P2 button
N2image = nextbutton().N2image
N2pos = nextbutton().N2pos

#Main Menu
def mainmenu():
    while True:
        if gf.mainmenu == False:
            break
        gf.updatemainmenuscreen(screen, mmbg)
        gf.checkeventsmainmenuscreen(quitpos, startpos, setpos)
        if gf.settings == True:
            while True:
                p1gstats = font2.render(f"{gf.p1g}", True, p1fontcolor)
                p1cstats = font2.render(f"{gf.p1c}", True, p1fontcolor)
                p2gstats = font2.render(f"{gf.p2g}", True, p2fontcolor)
                p2cstats = font2.render(f"{gf.p2c}", True, p2fontcolor)
                goalgolds = font2.render(f"{gf.goalgolds}", True, (0,0,0))
                gf.updatesettingscreen(screen,sbg,p1cstats, p1gstats, p2cstats, p2gstats, goalgolds)
                gf.checkeventssettingsscreen(quitsetpos, startsetpos, onmusicpos, offmusicpos,plusp1coinpos,plusp1goldpos,plusp2coinpos,plusp2goldpos,minusp1coinpos,minusp1goldpos,minusp2coinpos,minusp2goldpos,plusgoalgoldspos,minusgoalgoldspos)
                if gf.back == True:
                    gf.settings = False
                    gf.back = False
                    break
#The Main Game
def rungame():
    mixer.music.set_volume(0.1)
    time_clock = pygame.time.get_ticks()
    while True:
    #Updating screen and control everytime
        p1gstats = font2.render(f"{gf.p1g}", True, p1fontcolor)
        p1cstats = font2.render(f"{gf.p1c}", True, p1fontcolor)
        p2gstats = font2.render(f"{gf.p2g}", True, p2fontcolor)
        p2cstats = font2.render(f"{gf.p2c}", True, p2fontcolor)
        messaget = font2.render(f"{gf.turn}", True, (0,0,0))

        gf.checkevents(screen,N1pos, N2pos)
        gf.updatemainscreen(screen,board,p1,p2,N1image,N2image,messaget,p1gstats,p1cstats,p2gstats,p2cstats)
        gf.gameover(screen)
    
        #Display the first turn for 3 seconds

        while pygame.time.get_ticks() - time_clock < 3000:
            screen.blit(messageft, (370, 85))
            pygame.display.flip()

if __name__ == "__main__":
    mainmenu()
    rungame()