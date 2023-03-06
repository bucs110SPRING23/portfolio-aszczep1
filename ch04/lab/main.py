import pygame
import random
import math 

pygame.init()
screen = pygame.display.set_mode()
screen_size = screen.get_size()
print(screen_size)
#guess = input("Do you think player 1 or 2 will win?:")

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
white_score = 0 
purple_score = 0
for i in range(21): 
   x2 = random.randrange(screen_size[0] + 1)
   y2 = random.randrange(screen_size[1] + 1)
   distance_from_center = math.hypot(x1 - x2, y1 - y2)
   is_in_circle = distance_from_center <= pos_2
   if i % 2 == 0: 
        if is_in_circle == True:
            pygame.draw.circle(screen, "white", [x2, y2], 10)
            white_score += 1
        else:
            pygame.draw.circle(screen, "black", [x2, y2], 10)
   else:
        if is_in_circle == True:
            pygame.draw.circle(screen, "purple", [x2, y2], 10)
            purple_score += 1
        else:
            pygame.draw.circle(screen, "blue", [x2, y2], 10)
        pygame.display.flip()
        pygame.time.wait(1000)

if purple_score < white_score: 
    winner = "White is the winner!"
elif white_score < purple_score: 
    winner = "Purple is the winner!"
else: 
    winner = "It was a tie!"

font = pygame.font.Font(None, 48) 
text = font.render(winner, True, "white") 
screen.blit(text, (pos_1, pos_2))
pygame.display.flip()
pygame.time.wait(2000)
#Part B

hitbox_width = pos_1
hitbox_height = pos_2

hitboxes = {
   "white": pygame.Rect(0, 0, hitbox_width, hitbox_height),
   "purple": pygame.Rect(0, 0, hitbox_width, hitbox_height)}
done = False
while not done: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True 
        elif event.type == pygame.KEYDOWN:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hitboxes["purple"].collidepoint(event.pos):
                    selected = "purple"
                elif hitboxes["white"].collidepoint(event.pos):
                    selected = "white"
        done = True
            


