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
    screen.fill("blue")
    new_display = pygame.transform.flip(screen, False, True) 
    width, height = new_display.get_size()
    new_display = pygame.transform.scale(new_display, (width * 5, height * 5))
    screen.blit(new_display, (0,0))

    
    inters_dict = threenplus1_inters_dict.items()
    print(inters_dict)
    max_so_far = 0 
    cor_1 = (0, 0)
    for v, k in inters_dict:
        cor_2 = (v, k)
        pygame.draw.lines(screen, "red", cor_1, cor_2)
        cor_1 = (v, k)

    
    font = pygame.font.Font(None, 48)
    words = [
        f"The max so far is", {max_so_far}
         ]
    msg = font.render(words, False, "red") 
    pos = (10, 10)
    screen.blit(msg, pos) 



def main(): 
    n = int(input("Enter a number greater than 1:"))
    count = threenp1(n)
    print(count)
    upper_limit = int(input("Enter an upper limit for the three n plus 1 process:"))
    rangdict = threenp1range(upper_limit)
    print(rangdict)
    pygame.init()
    graph_coordinates(rangdict)
    
main()
