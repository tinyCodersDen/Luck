import pygame
from pygame.locals import *
import random
import time
pygame.init()
screen=pygame.display.set_mode((600,600))
pygame.display.set_caption("Luck")
texts = [['RED',(255,0,0)],['GREEN',(0,255,0)],['BLUE',(0,0,255)],['YELLOW',(255,255,0)],['CYAN',(0,255,255)],['MAGENTA',(255,0,255)],['WHITE',(255,255,255)]]
colors = [['RED',(255,0,0)],['GREEN',(0,255,0)],['BLUE',(0,0,255)],['YELLOW',(255,255,0)],['CYAN',(0,255,255)],['MAGENTA',(255,0,255)],['WHITE',(255,255,255)]]
initial = False
def pick_random_color():
    r = random.choice(colors)
    return r
score = 0
font=pygame.font.Font('freesansbold.ttf', 30)
s = random.choice(texts)
text = font.render(s[0], False, s[1])
text2 = font.render('Score: {}'.format(score), False, (255,255,255))
count = 1
while True:
    if initial==False:
        d = pick_random_color()
        initial=True
    screen.blit(text,(260,100))
    screen.blit(text2,(0,0))
    pygame.draw.rect(screen,d[1],(275,400,50,50))
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        elif event.type==MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if 275<=pos[0]<=325 and 400<=pos[1]<=450:
                if count<3:
                    d = pick_random_color()
                    pygame.draw.rect(screen,d[1],(275,400,50,50))
                    if d[0]==s[0]:
                        score+=1
                        screen.fill((0,0,0))
                        s = random.choice(texts)
                        text = font.render(s[0], False, s[1])
                        text2 = font.render('Score: {}'.format(score), False, (255,255,255))
                        pygame.draw.rect(screen,d[1],(275,400,50,50))
                        count = 1
                    else:
                        count+=1
                else:
                    time.sleep(0.5)
                    text3 = font.render('Game Over', False, (255,0,0))
                    screen.fill((0,0,0))
                    screen.blit(text3,(250,300))
                    pygame.display.update()
                    time.sleep(2)
                    pygame.quit()
                    exit()
    pygame.display.update()