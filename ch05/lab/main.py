import pygame


def threenp1(n): 
    count = 0 
    while n > 1.0: 
        count += 1
        if n % 2 == 0: 
            n = int(n/2) 
        else: 
            n = int(3 * n + 1)
        return count
    

def threenp1range(upper_limit): 
    objs_in_sequence = {n => inters}
    threenplus1_inters_dict = { }


# Part B

def graph_coordinates(threenplus1_inters_dict): 
    new_display = pygame.transform.flip(display, Flase, True) 
    width, height = new_display.get_size()
    new_display = pygame.transform.scale(new_dsiplay, (width * <factor>, height * <factor>))
    display.blit(flipped_screen, (0,0))

    font = pygame.font.Font(font_name, size) 
    msg = font.render(msg, antialias, color) 

    display.blit(msg, pos) 
    