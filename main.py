import pygame

pygame.init()
win = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("PAINT")



def DrowMainWin():   
    ## main selection bar
    pygame.draw.rect(win, (255, 255, 255), (10, 620, 980, 70))
    ## clear button
    pygame.draw.rect(win, (255, 0, 0), (930, 630, 50, 50))

    ## size mate
    pygame.draw.rect(win, (0, 255, 255), (870, 630, 50, 50))
    pygame.draw.circle(win, (0,0,0), (895, 655), 15)
    pygame.draw.rect(win, (0, 255, 255), (810, 630, 50, 50))
    pygame.draw.circle(win, (0,0,0), (835, 655), 12)
    pygame.draw.rect(win, (0, 255, 255), (750, 630, 50, 50))
    pygame.draw.circle(win, (0,0,0), (775, 655), 9)
    pygame.draw.rect(win, (0, 255, 255), (690, 630, 50, 50))
    pygame.draw.circle(win, (0,0,0), (715, 655), 6)
    pygame.draw.rect(win, (0, 255, 255), (630, 630, 50, 50))
    pygame.draw.circle(win, (0,0,0), (655, 655), 3)

    ## color mate main win
    pygame.draw.rect(win, (0, 255, 255), (20, 630, 125, 50))

    ## 10 colors
    pygame.draw.rect(win, (0, 0, 0), (20, 630, 25, 25))
    pygame.draw.rect(win, (255, 0, 0), (45, 630, 25, 25))
    pygame.draw.rect(win, (0, 255, 0), (70, 630, 25, 25))
    pygame.draw.rect(win, (0, 0, 255), (95, 630, 25, 25))
    pygame.draw.rect(win, (255,255,0), (120, 630, 25, 25))
    pygame.draw.rect(win, (255,255,255), (20, 655, 25, 25))
    pygame.draw.rect(win, (255, 0, 255), (45, 655, 25, 25))
    pygame.draw.rect(win, (0, 255, 255), (70, 655, 25, 25))
    pygame.draw.rect(win, (128,128,128), (95, 655, 25, 25))
    pygame.draw.rect(win, (127, 0, 255), (120, 655, 25, 25))



def paint(r,g,b,re):
    d = True
    while d:
        x, y = pygame.mouse.get_pos()
        if x in range(10, 980) and y in range(10, 600):
        # pygame.draw.rect(win, (r,g,b), (x, y, 10, 10))
            pygame.draw.circle(win, (r,g,b), (x,y), re)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                d = False
            if e.type == pygame.MOUSEBUTTONUP:
                d = False
                break
        pygame.display.update()

## drawing the main canvas
pygame.draw.rect(win, (255, 255, 255), (10, 10, 980, 600))
#### GAME LOOP ######## 
run = True
r,g,b,re = 255,0,0,9
while run:
    DrowMainWin()

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        if e.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if x in range(10, 980) and y in range(10, 600):
                paint(r,g,b,re)
            if x in range(930, 980) and y in range(630, 680):
                pygame.draw.rect(win, (255, 255, 255), (10, 10, 980, 600))
            elif x in range(20, 45) and y in range(630, 655):
                r,g,b = 0,0,0
            elif x in range(45, 70) and y in range(630, 655):
                r,g,b = 255, 0, 0
            elif x in range(70, 95) and y in range(630, 655):
                r,g,b = 0, 255,0
            elif x in range(95, 120) and y in range(630, 655):
                r,g,b = 0,0,255
            elif x in range(120, 145) and y in range(630, 655):
                r,g,b = 255,255,0
            elif x in range(20, 45) and y in range(655, 680):
                r,g,b = 255,255,255
            elif x in range(45, 70) and y in range(655, 680):
                r,g,b = 255,0,255
            elif x in range(70, 95) and y in range(655, 680):
                r,g,b = 0,255,255
            elif x in range(95, 120) and y in range(655, 680):
                r,g,b = 128,128,128
            elif x in range(120, 145) and y in range(655, 680):
                r,g,b = 127,0,255
            elif x in range(630, 680) and y in range(630, 680):
                re = 3
            elif x in range(690, 740) and y in range(630, 680):
                re = 6
            elif x in range(750, 800) and y in range(630, 680):
                re = 9
            elif x in range(810, 860) and y in range(630, 680):
                re = 12
            elif x in range(870, 920) and y in range(630, 680):
                re = 15
        

    

    pygame.display.update()

pygame.quit()