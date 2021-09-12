import pygame
import sys
from pygame.locals import *
import time
pygame.init()


size = width, height = (400, 600)

pygame.display.set_caption("逆行超車")
screen = pygame.display.set_mode(size) # 要塞一個元素(500,500)
#頻速率
FPS = 60
clock = pygame.time.Clock()

OUT_OF_RANGE = pygame.USEREVENT+1
BLACK = (0,0,0)
RED = "#FF0000"

SCORE = 0
#字體
font_big = pygame.font.SysFont("Verdana",60)
font_small = pygame.font.SysFont("Verdana",20)
game_over = font_big.render("game over",True,BLACK)
#音樂
pygame.mixer.Sound("background.wav").play(-1) #默認執行一遍,loop莫認為0,-1表示無限循環

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        #super(Player,self).__init__()
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect(left=100 ,top=0)#預設(0,0)

    def move(self):
        global SCORE
        self.rect.move_ip(0,5)
        if self.rect.top>height:
            SCORE+=1
            self.rect.top=0

class Player(pygame.sprite.Sprite):
    def __init__(self):
        #super(Player,self).__init__()
        super().__init__()
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
enemy = Enemy()
#定義精靈組
enemies = pygame.sprite.Group()
enemies.add(enemy)
#所有精靈
all_sprite = pygame.sprite.Group()
all_sprite.add(player)
all_sprite.add(enemy)


while True:
    screen.blit(backgroud,(0,0))
    scores = font_small.render(str(SCORE),True,BLACK)
    screen.blit(scores,(10,10))
    for sprite in all_sprite:
        screen.blit(sprite.image,sprite.rect)
        sprite.move()

    #從事件列中提取事件對象，根據類型進行事件處理
    for event in pygame.event.get():

        #print(event)
        if event.type ==pygame.QUIT:
            pygame.quit()
            sys.exit()  #如在pygame.quit()前終止，IDLE會掛起

        #處理
        if event.type == OUT_OF_RANGE:
            print("超過邊界")
    if pygame.sprite.spritecollideany(player,enemies):#把敵人從所有組內消除
        pygame.mixer.Sound("crash.wav").play()
        time.sleep(1)

        screen.fill(RED)
        screen.blit(game_over,(80,150))

        pygame.display.update()
        time.sleep(2)

        pygame.quit()
        sys.exit()

    pygame.display.update()
    clock.tick(FPS)