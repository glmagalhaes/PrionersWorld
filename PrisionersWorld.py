import pygame
from pygame import gfxdraw
from pygame.locals import *
import numpy


# 0 - C
# 1 - D

#number of lines and rows of players

pygame.init()

BLUE     = (   0,   0, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
YELLOW   = ( 255, 255,   0)

# T > R > P > S
t = 1.8
r = 1.0
s = 0.0
p = 0.00001

# score holders
c = 0.0
d = 0.0

# game settings hard coded for now
generations = 100
n = 200

size = (n, n)

# create boards fo the game
array_one = numpy.ndarray(size)
array_two = numpy.ndarray(size)

# create pygame window
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Priosiner's World")

# set the boards' function
current = array_one
history = array_two

# clean boards
for i in range(n):
    for j in range(n):
        array_one[[i],[j]] = 0
        array_two[[i],[j]] = 0


# create a deflector, hard coded for now
current[[n/2],[n/2]] = 1


# main loop that calculate all iteractions of the game
#must be put in a thread so the window will stop freezing
for bob in range(generations):
    temp = current
    current = history
    history = temp

    #print history
    #print current
    print bob
    for j in range(n):
        for i in range(n):
            flag_defector = 0
            c = 0.0
            d = 0.0
			# test possible results, must add diagonals
			# yes, it's hard coded no fucking loop
            if i-1 >= 0:
                if history[i-1][j] == 0:
                    c += r
                    d += t
                else:
                    flag_defector +=1
                    c += s
                    d += p
            if i+1 < n:
                if history[i+1][j] == 0:
                    c += r
                    d += t
                else:
                    flag_defector +=1
                    c += s
                    d += p
            if j-1 >= 0:
                if history[i][j-1] == 0:
                    c += r
                    d += t
                else:
                    flag_defector +=1
                    c += s
                    d += p
            if j+1 < n:
                if history[i][j+1] == 0:
                    c += r
                    d += t
                else:
                    flag_defector +=1
                    c += s
                    d += p
			# Paint the right color for the pixel on screen
            if c >= d:
                current[[i],[j]] = 0
            elif history[i][j] == 1 or flag_defector == 1:
                current[i][j] = 1
            if current[i][j] == 0 and history[i][j] == 0:
                gfxdraw.pixel(screen, i , j , BLUE)
            if current[i][j] == 0 and history[i][j] == 1:
                screen.set_at((i, j), GREEN)
            if current[i][j] == 1 and history[i][j] == 0:
                screen.set_at((i, j), YELLOW)
            if current[i][j] == 1 and history[i][j] == 1:
                screen.set_at((i, j), RED)
	# Update Screen
    pygame.display.flip()
#print history
#print current

#event loop
done = False
while not done:
    for event in pygame.event.get():
		#quit program event
        if event.type == pygame.QUIT:
            done = True
