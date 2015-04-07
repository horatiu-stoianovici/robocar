from carcontrol import CarController
import pygame, sys
from pygame.locals import *
import time


pygame.init()

DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello WORLD!')

time_interval = 0.2

try:
    with CarController() as controller:
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        controller.startLeft()
                    if event.key == pygame.K_RIGHT:
                        controller.startRight()
                    if event.key == pygame.K_UP:
                        controller.startForward()
                    if event.key == pygame.K_DOWN:
                        controller.startBackward()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        controller.stopLeft()
                    if event.key == pygame.K_RIGHT:
                        controller.stopRight()
                    if event.key == pygame.K_UP:
                        controller.stopForward()
                    if event.key == pygame.K_DOWN:
                        controller.stopBackward()
                    
            pygame.display.update()

            #sleep 5ms for better processor usage
            time.sleep(5.0/1000.0)
            
            #c = stdscr.getch()
            #if c == curses.KEY_UP:
            #    stdscr.addstr(0, 0, "UP   ")
            #    controller.forward(time_interval)
            #if c == curses.KEY_DOWN:
            #    stdscr.addstr(0, 0, "DOWN ")
            #    controller.backward(time_interval)
            #if c == curses.KEY_LEFT:
            #    stdscr.addstr(0, 0, "LEFT ")
            #    controller.left(time_interval)
            #if c == curses.KEY_RIGHT:
            #	stdscr.addstr(0, 0, "RIGHT")
            #	controller.right(time_interval)

            #if c == ord('q'):
	    #	break;
except BaseException as ex:
    print ex

    

