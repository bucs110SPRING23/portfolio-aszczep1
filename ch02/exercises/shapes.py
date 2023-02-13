import pygame

pygame.init()
screen = pygame.display.set_mode()
screen.fill("purple")
pygame.display.flip()

screen_size = screen.get_size()

pygame.draw.circle(screen, "red", [960, 150], 50)
pygame.draw.circle(screen, "blue", [960, 300], 100)
pygame.draw.circle(screen, "green", [960, 600], 200)

pygame.display.flip()
input()