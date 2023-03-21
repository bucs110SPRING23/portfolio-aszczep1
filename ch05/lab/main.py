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
    objs_in_sequence = {}
    for i in range(2, upper_limit + 1): 
         inters = threenp1(i)
         objs_in_sequence[i] = inters
    threenplus1_inters_dict = objs_in_sequence
    return threenplus1_inters_dict


# Part B

def graph_coordinates(threenplus1_inters_dict): 
    screen = pygame.display.set_mode()
    screen_size = screen.get_size()
    pygame.screen_fill("blue")
    
    inters_dict = threenplus1_inters_dict.items()
    pygame.draw.lines(screen, "red", False, inters_dict)


    new_display = pygame.transform.flip(screen, False, True) 
    width, height = new_display.get_size()
    new_display = pygame.transform.scale(new_display, (width * 5, height * 5))
    screen.blit(new_display, (0,0))

    font = pygame.font.Font(font_name, size) 
    msg = font.render(msg, antialias, color) 

    screen.blit(msg, pos) 



def main(): 
    n = int(input("Enter a number greater than 1:"))
    count = threenp1(n)
    print(count)
    upper_limit = int(input("Enter an upper limit for the three n plus 1 process:"))
    rangdict = threenp1range(upper_limit)
    print(rangdict)
    pygame.init()
    
main()
