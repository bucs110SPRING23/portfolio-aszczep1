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
    screen_size = (600, 500)
    screen = pygame.display.set_mode(screen_size)
    graph_size = (150, 100)
    graph = pygame.Surface(graph_size)
    screen.fill("blue")
    graph.fill("purple")
    inters_dict = threenplus1_inters_dict.items()
    print(inters_dict)
    max_so_far = 0 
    #max_value = 0
    points = [ ]
    for v, k in inters_dict:
        point = (v, k)
        points.append(point)
        if k > max_so_far: 
            max_so_far = k
            #max_value = v

    

    print(points)
  
    lines = pygame.draw.lines(graph, "red", False, points)
    new_display = pygame.transform.flip(graph, False, True) 
    width, height = new_display.get_size()
    print(width, height)
    new_display = pygame.transform.scale(new_display, (width * 16, height * 16))
    
    screen.blit(new_display, (0,0))

    
    
    

    words = [
        f"The max so far is {max_so_far}"
    ]

    for m in words:
        font = pygame.font.Font(None, 48)
        msg = font.render(m, False, "red") 
        pos = (10, 10)
        screen.blit(msg, pos) 
    pygame.display.flip() 
    pygame.time.wait(20000)


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
