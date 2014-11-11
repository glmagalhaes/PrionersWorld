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
p = 0.0

candidatex = 0.0
candidatey = 0.0


# game settings hard coded for now
generations = 20
n = 50
cellsize = 5
matrix_size = (n, n)
size = (cellsize*n, cellsize*n)

# create boards fo the game
array_one = numpy.ndarray(matrix_size)
array_two = numpy.ndarray(matrix_size)
array_three = numpy.ndarray(matrix_size)

# create pygame window
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Prisoner's World")

# set the boards' function
current = array_one
history = array_two
score = array_three

# create a defector, hard coded for now
for i in range(n):
        for j in range(n):
                score[i][j] = 0.0
                current[i][j] = 0.0
                history[i][j] = 0.0

current[[n//2],[n//2]] = 1

print history
print current


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
                        if history[i][j] == 0:#you cooperate
                                if i-1 >= 0:
                                        if history[i-1][j] == 0:
                                                score[i][j] += r
                                        else:
                                                score[i][j] += s
                                if i+1 < n:
                                        if history[i+1][j] == 0:
                                                score[i][j] += r
                                        else:
                                                score[i][j] += s
                                if j-1 >= 0:
                                        if history[i][j-1] == 0:
                                                score[i][j] += r                                                
                                        else:
                                                score[i][j] += s
                                if j+1 < n:
                                        if history[i][j+1] == 0:
                                                score[i][j] += r
                                        else:
                                                score[i][j] += s
                                if i-1 >= 0 and j-1 >= 0 :
                                        if history[i-1][j-1] == 0:
                                                score[i][j] += r
                                        else:
                                                score[i][j] += s
                                if i-1 >= 0 and j+1 < n :
                                        if history[i-1][j+1] == 0:
                                                score[i][j] += r
                                        else:
                                                score[i][j] += s
                                if i+1 < n and j-1 >= 0 :
                                        if history[i+1][j-1] == 0:
                                                score[i][j] += r                                
                                        else:
                                                score[i][j] += s                    
                                if i+1 < n and j+1 < n :
                                        if history[i+1][j+1] == 0:
                                                score[i][j] += r
                                        else:
                                                score[i][j] += s
                        else:
                                if i-1 >= 0:
                                        if history[i-1][j] == 0:
                                                score[i][j] += t
                                        else:
                                                score[i][j] += p
                                if i+1 < n:
                                        if history[i+1][j] == 0:
                                                score[i][j] += t
                                        else:
                                                score[i][j] += p
                                if j-1 >= 0:
                                        if history[i][j-1] == 0:
                                                score[i][j] += t                                                
                                        else:
                                                score[i][j] += p
                                if j+1 < n:
                                        if history[i][j+1] == 0:
                                                score[i][j] += t
                                        else:
                                                score[i][j] += p
                   #diagonal
                                if i-1 >= 0 and j-1 >= 0 :
                                        if history[i-1][j-1] == 0:
                                                score[i][j] += t
                                        else:
                                                score[i][j] += p
                                if i-1 >= 0 and j+1 < n :
                                        if history[i-1][j+1] == 0:
                                                score[i][j] += t
                                        else:
                                                score[i][j] += p
                                if i+1 < n and j-1 >= 0 :
                                        if history[i+1][j-1] == 0:
                                                score[i][j] += t                                
                                        else:
                                                score[i][j] += p                    
                                if i+1 < n and j+1 < n :
                                        if history[i+1][j+1] == 0:
                                                score[i][j] += t
                                        else:
                                                score[i][j] += p
                
        for i in range(n):
                for j in range(n):
                        candidatex=i
                        candidatey=j
                        if i-1 >= 0:
                                if score[i-1][j] >= score[candidatex][candidatey]:
                                        candidatex=i-1
                                        candidatey=j
                        if i+1 < n:
                                if score[i+1][j] >= score[candidatex][candidatey]:
                                        candidatex=i+1
                                        candidatey=j
                        if j-1 >= 0:
                                if score[i][j-1] >= score[candidatex][candidatey]:
                                        candidatex=i
                                        candidatey=j-1
                        if j+1 < n:
                                if score[i-1][j+1] >= score[candidatex][candidatey]:
                                        candidatex=i
                                        candidatey=j+1
                        if i-1 >= 0 and j-1 >= 0 :
                                if score[i-1][j-1] >= score[candidatex][candidatey]:
                                        candidatex=i-1
                                        candidatey=j-1
                        if i-1 >= 0 and j+1 <n:
                                if score[i-1][j+1] >= score[candidatex][candidatey]:
                                        candidatex=i-1
                                        candidatey=j+1
                        if i+1 < n and j-1 >= 0:
                                if score[i+1][j-1] >= score[candidatex][candidatey]:
                                        candidatex=i+1
                                        candidatey=j-1
                        if i+1 < n and j+1 < n:
                                if score[i+1][j+1] >= score[candidatex][candidatey]:
                                        candidatex=i+1
                                        candidatey=j+1
                        if history[candidatex][candidatey] == 0:
                                current[i][j] = 0
                        elif history[candidatex][candidatey] == 1:
                                current[i][j] = 1

                                # test possible results, must add diagonals
                                # yes, it's hard coded no fucking loop
                    #adjacent
 

                                # Paint the right color for the pixel on screen
        #            if c >= d:
        #                current[i][j] = 0
        #            elif history[i][j] == 1 or flag_defector == 1:
        #            if history[i][j] == 1 or flag_defector == 1:
        #                current[i][j] = 1
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
