import pygame
import random
import math 

pygame.init()
screen = pygame.display.set_mode()
screen_size = screen.get_size()
#print(screen_size)
pos_1 = (screen_size[0] // 2)
pos_2 = (screen_size[1] // 2)
screen.fill("black")


hitbox_width = pos_1
hitbox_height = pos_2

hitboxes = {
   "white": pygame.Rect(0, 0, hitbox_width, hitbox_height),
   "purple": pygame.Rect(0, 0, hitbox_width, hitbox_height)
   }
hitboxes["purple"].topright = hitboxes["white"].bottomright
msg = "Pick which color you think will win."
done = False
font = pygame.font.Font(None, 48) 
text = font.render(msg, True, "white") 
screen.blit(text, (pos_1, pos_2))
for c, hb in hitboxes.items():
    pygame.draw.rect(screen, c, hb)
pygame.display.flip()
pygame.time.wait(1000)
while not done: 
  for event in pygame.event.get():
       mouseX, mouseY = pygame.mouse.get_pos() 
       if event.type == pygame.MOUSEBUTTONDOWN:
            if hitboxes["purple"].collidepoint(event.pos):
                selected = "purple"
            elif hitboxes["white"].collidepoint(event.pos):
                selected = "white"
            done = True

pygame.display.flip()
screen.fill("green")
pygame.draw.circle(screen, "red", (pos_1, pos_2), pos_2, 0)
pygame.draw.line(screen, 'black', (pos_1, 0), (pos_1, screen_size[1]), width = 5 )
pygame.draw.line(screen, 'black', ( 0 , pos_2), (screen_size[0] , pos_2), width = 5 )
pygame.display.flip()
pygame.time.wait(2000)

x1 = pos_1 
y1 = pos_2 
white_score = 0 
purple_score = 0
for i in range(21): 
    pygame.display.flip()
    pygame.time.wait(1000)
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
            pygame.draw.circle(screen, "red", [x2, y2], 10)
        
pygame.display.flip()
pygame.time.wait(1000)



if purple_score < white_score: 
    winner = [
        f"White is the winner! This player scored {white_score} points",
    ]
    if selected == "white":
        winner.append("You chose the correct player.")
    else: 
        winner.append("You chose the incorrect player.")
elif white_score < purple_score: 
    winner =  [
        f"Purple is the winner! This player scored {purple_score} points",
    ]
    if selected == "purple":
        winner.append("You chose the correct player.")
    else: 
        winner.append("You chose the incorrect player.")
else: 
    winner = [
        f"It was a tie! Both players scored {white_score} points",
        f"You kinda chose the correct player."
    ]


for m in winner:
    font = pygame.font.Font(None, 48) 
    text = font.render(m, True, "white") 
    screen.blit(text, (pos_1, pos_2))
    pos_2 += 100

pygame.display.flip()
pygame.time.wait(3000)

            


