import math
import random
import pygame
pygame.init()  
pygame.display.set_caption("COOKIE CLICKER")  
screen = pygame.display.set_mode((1000, 1000))  
screen.fill((255,190,130))
clock = pygame.time.Clock() #set up clock
gameover = False #variable to run our game loop

n = 0
#set up variable to hold mouse position
xpos=0
ypos=0
mousePos = (xpos, ypos)


while not gameover: #GAME LOOP############################################################
    clock.tick(60) #FPS

#event queue (bucket that holds stuff that happens in game and passes to one of the sections below)
    event = pygame.event.wait()    


#Input Section------------------------------------------------------------

    if event.type == pygame.MOUSEBUTTONDOWN:#CLICK
        mousePos = event.pos


    if event.type == pygame.QUIT: #close game window
        break        
  
    #physics section-----------------------------------------
    if mousePos[0] > 133 and mousePos[0] < 233 and mousePos[1] > 439 and mousePos[1] < 489:
        n = 3
    
    if mousePos[0] > 437 and mousePos[0] < 537 and mousePos[1] > 439 and mousePos[1] < 489:
        n = 5
        
    if mousePos[0] > 767 and mousePos[0] < 867 and mousePos[1] > 439 and mousePos[1] < 489:
        n = 10
    
    if mousePos[0] > 233 and mousePos[0] < 723 and mousePos[1] > 639 and mousePos[1] < 689:
        n = 60
        
    print(mousePos)
    #Render Section ---------------------------
    screen.fill((0,0,0)) #wipes screen black
    pygame.draw.rect(screen, (0, 255, 255), (133,439, 100, 50))
    pygame.draw.rect(screen, (255, 255, 0), (437,439, 100, 50))
    pygame.draw.rect(screen, (0, 255, 0), (767,439, 100, 50))
    pygame.draw.rect(screen, (255, 0, 0), (233,639, 490, 50))
    font = pygame.font.Font(None, 65)
    text = font.render(str("How fast would you like to go?"),1, (255,255,255))
    screen.blit(text, (200,250))
    text = font.render(str("slow"),1, (0, 250, 250))
    screen.blit(text, (133,390))
    text = font.render(str("normal"),1, (250, 250, 0))
    screen.blit(text, (415,390))
    text = font.render(str("fest"),1, (0, 250, 0))
    screen.blit(text, (778,390))
    text = font.render(str("extrememe"),1, (250, 0, 0))
    screen.blit(text, (360,590))
    pygame.display.flip()  

pygame.quit() 
