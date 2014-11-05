import pygame
from pygame import gfxdraw
from pygame.locals import *
import numpy
	
class Rectangle(pygame.sprite.Sprite):
	
	def __init__(self, x, y, width, height,color):
        
        	pygame.sprite.Sprite.__init__(self)
 
        	# Make the Rect
        	self.image = pygame.Surface([width, height])
        	self.image.fill(color)
 
        	# Make our top-left corner the passed-in location.
        	self.rect = self.image.get_rect()
        	self.rect.y = y
        	self.rect.x = x 

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
n = 100
cellsize = 5
size = (cellsize*n, cellsize*n)

# create boards fo the game
array_one = numpy.ndarray(size)
array_two = numpy.ndarray(size)

# create pygame window
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Prisoner's World")

# set the boards' function
current = array_one
history = array_two




# create a deflector, hard coded for now
current[[n/2],[n/2]] = 1


# main loop that calculate all iteractions of the game
#must be put in a thread so the window will stop freezing
for bob in range(generations):
    rect_list = pygame.sprite.Group()    

    temp = current
    current = history
    history = temp
    
    #print history
    #print current
    print bob
    for i in range(n):
        for j in range(n):
            flag_defector = 0
            c = 0.0
            d = 0.0
			# test possible results, must add diagonals
			# yes, it's hard coded no fucking loop
            #adjacent            
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
            #diagonal
            if i-1 >= 0 and j-1 >= 0 :
                if history[i-1][j-1] == 0:
                    c += r
                    d += t
                else:
                    flag_defector +=1
                    c += s
                    d += p
            if i-1 >= 0 and j+1 < n :
                if history[i-1][j+1] == 0:
                    c += r
                    d += t
                else:
                    flag_defector +=1
                    c += s
                    d += p
            if i+1 < n and j-1 >= 0 :
                if history[i+1][j-1] == 0:
                    c += r
                    d += t
                else:
                    flag_defector +=1
                    c += s
                    d += p
            if i+1 < n and j+1 < n :
                if history[i+1][j+1] == 0:
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
                bluerect = Rectangle(i*cellsize,j*cellsize,cellsize ,cellsize,BLUE)          
                rect_list.add(bluerect)               
                # gfxdraw.pixel(screen, i , j , BLUE)
            if current[i][j] == 0 and history[i][j] == 1:
                greenrect = Rectangle(i*cellsize,j*cellsize,cellsize,cellsize,GREEN)                 
                rect_list.add(greenrect)               
                # screen.set_at((i, j), GREEN)
            if current[i][j] == 1 and history[i][j] == 0:
                yellowrect = Rectangle(i*cellsize,j*cellsize,cellsize,cellsize,YELLOW)                    
                rect_list.add(yellowrect)               
                # screen.set_at((i, j), YELLOW)
            if current[i][j] == 1 and history[i][j] == 1:
                redrect = Rectangle(i*cellsize,j*cellsize,cellsize,cellsize,RED)              
                rect_list.add(redrect)                
                # screen.set_at((i, j), RED)
            
                        
    # Update Screen
    rect_list.update()
    rect_list.draw(screen)
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
