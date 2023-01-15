import sys
import pygame
import random
import pygame.font
from pygame import mixer
from bg import bg
from player1 import player1
from player2 import player2
from inputs import quitbutton as qb
from inputs import nextbutton
from dice import dice as dices
from msg import msg
from event import event as events
from settings import Settings
import time
import movement

# Main Menu States
mainmenu = True
music = True
settings = False
back = False

#Determine the first turn
team = ["Player 1","Player 2"]
turn = team[random.randint(0,1)]
goalgolds = Settings().goalgolds

#Calling the initial stats for player 1 and 2
p1p, p1c, p1g = [(player1().p1x, player1().p1y)], player1().coin, player1().gold
p2p, p2c, p2g= [(player2().p2x, player2().p2y)], player2().coin, player2().gold

#Convert everything to integer
def convertInt():
    global p1c, p2c, p1g, p2g
    p1c, p2c, p1g, p2g = int(p1c), int(p2c), int(p1g), int(p2g)

#No Negative Numbers
def nonegativenumber():
    global p1c, p2c, p1g, p2g, goalgolds
    if p1c < 0:
        p1c = 0
    elif p1g < 0:
        p1g = 0
    elif p2c < 0:
        p2c = 0
    elif p2g < 0:
        p2g = 0
    elif goalgolds < 1:
        goalgolds = 1

# No more than goal golds
def notexceedgoalgolds():
    global p1g, p2g, goalgolds
    if p1g >= goalgolds:
        p1g = goalgolds - 1
    elif p2g >= goalgolds:
        p2g = goalgolds - 1

# Limit 100 coins and golds
def coinsgolds100():
    global p1c, p2c, p1g, p2g, goalgolds
    if p1c > 100:
        p1c = 100
    elif p2c > 100:
        p2c = 100
    elif p1g > 100:
        p1g = 100
    elif p2g > 100:
        p2g = 100
    elif goalgolds > 100:
        goalgolds = 100

#Index value of position
a = 0
b = 0

#Updating the main menu screen every event happens
def updatemainmenuscreen(screen, mmbg):
    screen.blit(mmbg, (0,0))
    pygame.display.flip()

def checkeventsmainmenuscreen(quitpos, startpos, setpos):
    global mainmenu, settings
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            quitpos_clicked = quitpos.collidepoint(mouse_pos)
            startpos_clicked = startpos.collidepoint(mouse_pos)
            setpos_clicked = setpos.collidepoint(mouse_pos)
            if quitpos_clicked:
                pygame.quit()
                exit()
            elif startpos_clicked:
                mainmenu = False
            elif setpos_clicked:
                settings = True

#Update the settings screen every event happens

def updatesettingscreen(screen,sbg,p1cstats, p1gstats, p2cstats, p2gstats,goalgolds):
    screen.blit(sbg, (0,0))
    screen.blit(p1cstats,(1025,175))
    screen.blit(p1gstats,(1025,255))
    screen.blit(p2cstats,(1025,425))
    screen.blit(p2gstats,(1025,505))
    screen.blit(goalgolds,(280,230))
    pygame.display.flip()
    

def checkeventssettingsscreen(quitsetpos, startsetpos, onmusicpos, offmusicpos,plusp1coinpos,plusp1goldpos,plusp2coinpos,plusp2goldpos,minusp1coinpos,minusp1goldpos,minusp2coinpos,minusp2goldpos,plusgoalgoldspos,minusgoalgoldspos):
    global music, back, mainmenu
    global p1c, p2c, p1g, p2g,goalgolds
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            quitsetpos_clicked = quitsetpos.collidepoint(mouse_pos)
            onmusicpos_clicked = onmusicpos.collidepoint(mouse_pos)
            offmusicpos_clicked = offmusicpos.collidepoint(mouse_pos)
            startsetpos_clicked = startsetpos.collidepoint(mouse_pos)
            plusp1coinpos_clicked = plusp1coinpos.collidepoint(mouse_pos)
            plusp1goldpos_clicked = plusp1goldpos.collidepoint(mouse_pos)
            plusp2coinpos_clicked = plusp2coinpos.collidepoint(mouse_pos)
            plusp2goldpos_clicked = plusp2goldpos.collidepoint(mouse_pos)
            plusgoalgoldspos_clicked = plusgoalgoldspos.collidepoint(mouse_pos)
            minusp1coinpos_clicked = minusp1coinpos.collidepoint(mouse_pos)
            minusp1goldpos_clicked = minusp1goldpos.collidepoint(mouse_pos)
            minusp2coinpos_clicked = minusp2coinpos.collidepoint(mouse_pos)
            minusp2goldpos_clicked = minusp2goldpos.collidepoint(mouse_pos)
            minusgoalgoldspos_clicked = minusgoalgoldspos.collidepoint(mouse_pos)

            if onmusicpos_clicked:
                if music == True:
                    break
                else:
                    mixer.music.unpause()
                    music = True
            elif offmusicpos_clicked:
                mixer.music.pause()
                music = False
            elif startsetpos_clicked:
                mainmenu = False
                back = True
            elif quitsetpos_clicked:
                back = True
                goalgolds = 5
                p1c = 10
                p2c = 10
                p1g = 0
                p2g = 0
            elif plusgoalgoldspos_clicked:
                goalgolds += 1
            elif minusgoalgoldspos_clicked:
                goalgolds -= 1
            elif plusp1coinpos_clicked:
                p1c += 5
            elif plusp1goldpos_clicked:
                p1g += 1
            elif plusp2coinpos_clicked:
                p2c += 5
            elif plusp2goldpos_clicked:
                p2g += 1
            elif minusp1coinpos_clicked:
                p1c -= 5
            elif minusp1goldpos_clicked:
                p1g -= 1
            elif minusp2coinpos_clicked:
                p2c -= 5
            elif minusp2goldpos_clicked:
                p2g -= 1

            #No more than 100 coins and golds, must not be a negative number, and not exceeding goal golds
            coinsgolds100()
            nonegativenumber()
            notexceedgoalgolds()

#Updating the main screen every event happens
def updatemainscreen(screen, board, p1,p2, N1b, N2b, messaget,p1gstats,p1cstats,p2gstats,p2cstats):
    global p1x, p1y, p1c, p1g, p2x, p2y, p2c, p2g, turn
    screen.blit(board,(0,0))
    screen.blit(p1, p1p[0])
    screen.blit(p2, p2p[0])

    if turn == "Player 1":
        screen.blit(N1b, (nextbutton().N1x,nextbutton().N1y))
    elif turn == "Player 2":
        screen.blit(N2b, (nextbutton().N2x,nextbutton().N2y))

    screen.blit(messaget,(650,645))
    screen.blit(p1cstats,(150,120))
    screen.blit(p1gstats,(150,170))
    screen.blit(p2cstats,(1100,120))
    screen.blit(p2gstats,(1100,170))
    
    pygame.display.flip()

#Controls triggers

def check_keydown_events(event):
    if event.key == pygame.K_ESCAPE:
        sys.exit()

def checkevents(screen, N1pos, N2pos):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            global turn, red_button_clicked, blue_button_clicked
            if turn == "Player 1": 
                button_clicked = N1pos.collidepoint(mouse_pos)
            elif turn == "Player 2":
                button_clicked = N2pos.collidepoint(mouse_pos)

            if button_clicked:
                #When the button is pressed, it will call the dice img
                global a, b, p1p, p2p, p1c, p2c, p1g, p2g
                dice, diceroll = dices().picknumber()
                dices().loaddice(screen, dice)   

                #Triggering the movement and rotate the turn
                if turn == "Player 1":
                    a += diceroll
                    if a > 50:
                        a = 0 
                        p1p[0] = (100,450)
                    elif a <= 50:
                        p1p[0] = movement.m[a]
                        #Check space
                        checkspace(screen, turn, p1p)
                        p1p[0] = movement.m[a]
                    turn = "Player 2"
                    msg().p2turnmsg(screen)

                elif turn == "Player 2":
                    b += diceroll
                    if b > 50:
                        b = 0
                        p2p[0] = (1100,450)
                    elif b <= 50:
                        #Check space
                        p2p[0] = movement.m[b]
                        checkspace(screen, turn, p2p)
                        #Update latest movement
                        p2p[0] = movement.m[b]
                    turn = "Player 1"
                    msg().p1turnmsg(screen)
                #Making sure the numbers are not in negative or float type
                nonegativenumber()
                convertInt()


def checkspace(screen, turn, pos):
        for i in movement.c:
            if pos[0] == i:
                events().chance(screen, turn)
                break
        for i in movement.bl:
            if pos[0] == i:
                events().badluck(screen, turn)
                break
        for i in movement.gc:
            if pos[0] == i:
                events().gacha(screen, turn)
                break
        for i in movement.b:
            if pos[0] == i:
                events().bluespace(turn)
                break
        for i in movement.r:
            if pos[0] == i:
                events().redspace(turn)
                break
        if pos[0] == movement.g[0]:
            events().goldspace1(screen, turn)
        elif pos[0] == movement.g[1]:
            events().goldspace3(screen, turn)

def gameover(screen):
    global p1g, p2g, goalgolds
    font = pygame.font.SysFont("comicsansms", 60)
    if p1g >= goalgolds:
        message = font.render(f"Player 1 WINS!", True, (255, 87, 87),(0,0,0))
        time_clock = pygame.time.get_ticks()
        while pygame.time.get_ticks() - time_clock < 3000:
            screen.blit(message, (450, 300))
            pygame.display.flip()
        pygame.quit()
        exit()
    elif p2g >= goalgolds:
        message = font.render(f"Player 2 WINS!", True, (140, 85, 255),(0,0,0))
        time_clock = pygame.time.get_ticks()
        while pygame.time.get_ticks() - time_clock < 3000:
            screen.blit(message, (450, 300))
            pygame.display.flip()
        pygame.quit()
        exit()

