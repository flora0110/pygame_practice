import pygame
import sys
from pygame.locals import *
pygame.init()


size = width, height = (400, 600)

pygame.display.set_caption("繪製圖形")
screen = pygame.display.set_mode(size) # 要塞一個元素(500,500)
#頻速率
FPS = 60
clock = pygame.time.Clock()

OUT_OF_RANGE = pygame.USEREVENT+1


class Player:
    def __init__(self):
        x,y = (width/2,height/2)
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect(center = (x,y))#預設(0,0)

    def move(self):
        mouseX, mouseY = pygame.mouse.get_pos()

        # 自定義事件
        if self.rect.left<40 or self.rect.right>360:
            pygame.event.post(pygame.event.Event(OUT_OF_RANGE))

        if player.rect.width/2 <= mouseX <= width-player.rect.width/2 \
                and player.rect.height/2 <= mouseY <= height - player.rect.height/2:
            player.rect.center = mouseX, mouseY

        pass

backgroud = pygame.image.load("AnimatedStreet.png")

player = Player()

while True:
    screen.blit(backgroud,(0,0))
    screen.blit(player.image,player.rect)
    player.move()


    #從事件列中提取事件對象，根據類型進行事件處理
    for event in pygame.event.get():

        #print(event)
        if event.type ==pygame.QUIT:
            pygame.quit()
            sys.exit()  #如在pygame.quit()前終止，IDLE會掛起

        #處理
        if event.type == OUT_OF_RANGE:
            print("超過邊界")
    #每次畫面刷新都會檢測
    #pressed_keys = pygame.key.get_pressed()
    #if pressed_keys[pygame.K_DOWN]:
    #    player.rect.move_ip(0,5)

    pygame.display.update()
    clock.tick(FPS)