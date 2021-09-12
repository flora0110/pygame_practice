import pygame
import sys
from pygame.locals import *
pygame.init()


size = width, height = (400, 600)

pygame.display.set_caption("逆行超車")
screen = pygame.display.set_mode(size) # 要塞一個元素(500,500)
#頻速率
FPS = 60
clock = pygame.time.Clock()

OUT_OF_RANGE = pygame.USEREVENT+1

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        #super(Player,self).__init__()
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect(left=width/2 ,top=0)#預設(0,0)

    def move(self):
        self.rect.move_ip(0,5)

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
    #都存在
    #if pygame.sprite.spritecollide(player,enemies,False):
    #    print("撞車啦")
    #敵人消失
    #if pygame.sprite.spritecollide(player,enemies,True):#把敵人從所有組內消除
    #    print("撞車啦")
    #玩家消失
    #if pygame.sprite.spritecollide(player,enemies,True):#把敵人從所有組內消除
    #    player.kill()
    #    print("撞車啦")
    if pygame.sprite.spritecollideany(player,enemies):#把敵人從所有組內消除
        player.kill()
        print("撞車啦")

    if player not in all_sprite:
        all_sprite.add(player)
    pygame.display.update()
    clock.tick(FPS)