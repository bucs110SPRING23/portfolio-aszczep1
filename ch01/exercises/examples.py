
## Pygame 
# framework 
import pyame

pyame.init()

screen = pygame.display.set_mode()

# screen: variable 
# pygame:modules that contain modules are called frameworks 
# display: submodule of pygame 
# set mode 

screen.fill("red")
pygame.display.flip()
pygame.time.wait(2000)
screen.fill("green")
pygame.display.flip()
pygame.time.wait(2000)

# [x, y, width, height (y inreaases downward)](negative coordinantes are always offscreen) 
dimensions = [ 0, 0, 250, 250]