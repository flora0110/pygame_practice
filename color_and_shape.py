import pygame
import sys

pygame.init()
pygame.display.set_caption("繪製圖形")
size = width, height = 300, 300
screen = pygame.display.set_mode(size) # 要塞一個元素(500,500)

WHITE = pygame.color.Color(255,255,255)
BLACK = pygame.color.Color(0,0,0,a=255)
BLUE = (0,0,255)
BLUE = (0,0,255)
screen.fill(WHITE)
while True:
    pygame.draw.circle(screen,BLACK,(100,50),30)
    #左上,右上
    pygame.draw.circle(screen, BLACK,(200, 50), 30,3,False,False,True,True)
    pygame.draw.line(screen,BLUE,(150,130),(130,170))
    pygame.draw.line(screen, BLUE, (150, 130), (170, 170),1)
    pygame.draw.line(screen, BLUE, (130, 170), (170, 170),5)

    #起始座標(100,200)(左上方座標點) 寬100 高50 邊寬2的矩形
    pygame.draw.rect(screen, BLUE, (100,200,100,50),2)
    pygame.draw.rect(screen, BLACK, (110, 260, 80, 5))
    pygame.display.update() #不斷重新繪製畫面的過程
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
            sys.exit()  #如在pygame.quit()前終止，IDLE會掛起