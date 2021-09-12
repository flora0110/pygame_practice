import pygame
import sys

pygame.init()


size = width, height = (400, 600)

pygame.display.set_caption("繪製圖形")
screen = pygame.display.set_mode(size) # 要塞一個元素(500,500)
#頻速率
FPS = 60
clock = pygame.time.Clock()


player = pygame.image.load("Player.png")
backgroud = pygame.image.load("AnimatedStreet.png")


x,y = 178,504
while True:
    screen.blit(backgroud,(0,0))
    screen.blit(player,(x,y))
    y-=1

    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
            sys.exit()  #如在pygame.quit()前終止，IDLE會掛起

    pygame.display.update()
    clock.tick(FPS)