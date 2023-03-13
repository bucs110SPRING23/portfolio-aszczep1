import pygame
import random
import math 

pygame.init()
screen = pygame.display.set_mode()
screen_size = screen.get_size()
print(screen_size)
#guess = input("Do you think player 1 or 2 will win?:")

# Part A
pos_1 = (screen_size[0] // 2)
pos_2 = (screen_size[1] // 2)
screen.fill("green")
pygame.draw.circle(screen, "red", (pos_1, pos_2), pos_2, 0)
pygame.draw.line(screen, 'black', (pos_1, 0), (pos_1, screen_size[1]), width = 5 )
pygame.draw.line(screen, 'black', ( 0 , pos_2), (screen_size[0] , pos_2), width = 5 )
pygame.display.flip()
pygame.time.wait(2000)

# Part B
x1 = pos_1 
y1 = pos_2 
for i in range(11): 
   x2 = random.randrange(screen_size[0] + 1)
   y2 = random.randrange(screen_size[1] + 1)
   distance_from_center = math.hypot(x1 - x2, y1 - y2)
   is_in_circle = distance_from_center <= pos_2
   if is_in_circle == True:
      pygame.draw.circle(screen, "white", [x2, y2], 10)
   else:
      pygame.draw.circle(screen, "black", [x2, y2], 10)

pygame.display.flip()
pygame.time.wait(1000)









input()