import pygame, sys, time, random, os

from pygame.locals import *

pygame.init()
FPSCLOCK = pygame.time.Clock()

#Colors:
yellow = (216,196,10)
red = (183,18,18)
green =(12,176,23)
blue = (10,44,158)
brightYellow = (255,255,107)
brightRed = (255,43,43)
brightGreen = (112,255,112)
brightBlue = (94,175,255)
black = (0,0,0)
white = (255,255,255)
#Sizes:
boxSize = 100
margin = 50

#Color variables
ye = pygame.Rect(boxSize,boxSize,boxSize,boxSize)
r = pygame.Rect(boxSize,boxSize+boxSize+margin,boxSize,boxSize)
g = pygame.Rect(boxSize+boxSize+margin,boxSize+boxSize+margin,boxSize,boxSize)
b = pygame.Rect(boxSize+boxSize+margin,boxSize,boxSize,boxSize)

#various variables
sequence = []
playerSequence = []
turn = "player"
first = True
flashColor = (0 ,0 ,0)
locationTurple = ye.topleft
clickedButton = ()
clicks = 0
clicky = 0
sClick = 1

#Sounds:
BEEP1 = pygame.mixer.Sound('beep1.ogg')
BEEP2 = pygame.mixer.Sound('beep2.ogg')
BEEP3 = pygame.mixer.Sound('beep3.ogg')
BEEP4 = pygame.mixer.Sound('beep4.ogg')

screen = pygame.display.set_mode((600,400))
screen.fill(white)

#Buttons:
pygame.draw.rect(screen,blue,(boxSize+boxSize+margin,boxSize,boxSize,boxSize))
pygame.draw.rect(screen,green,(boxSize+boxSize+margin,boxSize+boxSize+margin,boxSize,boxSize))
pygame.draw.rect(screen,red,(boxSize,boxSize+boxSize+margin,boxSize,boxSize))  
pygame.draw.rect(screen,yellow,(boxSize,boxSize,boxSize,boxSize))


def drawButtons():
  pygame.draw.rect(screen,blue,(boxSize+boxSize+margin,boxSize,boxSize,boxSize))
  pygame.draw.rect(screen,green,(boxSize+boxSize+margin,boxSize+boxSize+margin,boxSize,boxSize))
  pygame.draw.rect(screen,red,(boxSize,boxSize+boxSize+margin,boxSize,boxSize))  
  pygame.draw.rect(screen,yellow,(boxSize,boxSize,boxSize,boxSize))

def checkSeq(sequence, playerSequence,turn,first,clicks,clicky,sClick):
  if playerSequence[clicky] != sequence[clicky]:
      sequence.clear()
      playerSequence.clear()
      turn = "player"
      first = True
      clicks = 0
      clicky = 0
      sClick = 0
  elif len(playerSequence) == len(sequence):
    turn = "Simon"
    sequence.append(random.choice((yellow,blue,green,red)))
    clicks = 0
    playerSequence.clear()
  return sequence, playerSequence,turn,first,clicks,clicky,sClick,turn

def getButtonClicked(x,y, first, sequence, playerSequence, turn, clicks,clicky,sClick):
  clicks = clicks + 1
  clicky = clicks - 1
  if ye.collidepoint((x,y)):
    if first == True:
      sequence.append(yellow)
      first = False
    playerSequence.append(yellow)
    turn,first = checkSeq(sequence, playerSequence,turn,first,clicks,clicky,sClick)
    return yellow, sequence, playerSequence, turn, first
  elif b.collidepoint((x,y)):
    if first == True:
      sequence.append(blue)
      first = False
    playerSequence.append(blue)
    turn,first = checkSeq(sequence, playerSequence,turn,first,clicks,clicky,sClick)
    return blue, sequence, playerSequence, turn, first
  elif r.collidepoint((x,y)):
    if first == True:
      sequence.append(red)
      first = False
    playerSequence.append(red)
    turn,first = checkSeq(sequence, playerSequence,turn,first,clicks,clicky,sClick)
    return red, sequence, playerSequence, turn, first
  elif g.collidepoint((x,y)):
    if first == True:
      sequence.append(green)
      first = False
    playerSequence.append(green)
    turn,first = checkSeq(sequence, playerSequence,turn,first,clicks,clicky,sClick)
    return green, sequence, playerSequence, turn, first
  return None, None, None, None

def flashButtonAnimation(color, flashColor, locationTurple):
  if color == yellow:
    locationTurple = ye.topleft
    flashColor = brightYellow
    sound = BEEP1
  elif color == red:
    locationTurple = r.topleft
    flashColor = brightRed
    sound = BEEP2
  elif color == green:
    locationTurple = g.topleft
    flashColor = brightGreen
    sound = BEEP3
  elif color == blue:
    locationTurple = b.topleft
    flashColor = brightBlue
    sound = BEEP4
  pygame.draw.rect(screen, flashColor, (locationTurple[0],locationTurple[1], boxSize,boxSize))
  pygame.display.update()
  sound.play()
  pygame.time.wait(250)
  drawButtons()
  pygame.display.update

def playSimonsSequence (sequence, sClick):
  for color in sequence:
    if color == yellow:
      sClick = sClick + 1
      locationTurple = ye.topleft
      flashColor = brightYellow
      sound = BEEP1
    elif color == red:
      sClick = sClick + 1
      locationTurple = r.topleft
      flashColor = brightRed
      sound = BEEP2
    elif color == green:
      sClick = sClick + 1
      locationTurple = g.topleft
      flashColor = brightGreen
      sound = BEEP3
    elif color == blue:
      sClick = sClick + 1
      locationTurple = b.topleft
      flashColor = brightBlue
      sound = BEEP4
    pygame.draw.rect(screen, flashColor, (locationTurple[0],locationTurple[1], boxSize,boxSize))
    pygame.display.update()
    sound.play()
    pygame.time.wait(500)
    drawButtons()
    pygame.display.update
    return sClick

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if turn == "player":
      if event.type == pygame.MOUSEBUTTONUP:
        mousex, mousey = event.pos
        clickedButton, sequence, playerSequence, turn, first = getButtonClicked(mousex,mousey, first, sequence, playerSequence, turn,clicks,clicky,sClick)
        flashButtonAnimation(clickedButton, flashColor, locationTurple)
        print(sequence)
  if turn == "Simon":
    print("simon's turn")
    pygame.time.wait(500)
    playSimonsSequence(sequence, sClick)
    turn = "player"
#make screen.blit  
  fontObj = pygame.font.SysFont('tahoma',30)
  fontSurfaceObj = fontObj.render("Click to begin the pattern then copy:",True,blue,yellow)
  screen.blit(fontSurfaceObj,(10,10))
  pygame.display.update()
  FPSCLOCK.tick(40)