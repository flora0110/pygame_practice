import random

import pygame
import sys
from pygame.locals import *
import time
import random

class Constant:
    # 頻速率
    FPS = 60
    clock = pygame.time.Clock()

    BLACK = (0, 0, 0)
    RED = "#FF0000"

    SCORE = 0
    SPEED = 1
    # 字體
    font_big = pygame.font.SysFont("Verdana", 60)
    font_small = pygame.font.SysFont("Verdana", 20)
    game_over = font_big.render("game over", True, BLACK)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        #super(Player,self).__init__()
        super().__init__()
        x,y =(random.randint(22,378),0)
        self.image = pygame.image.load("Enemy.png")
        self.surf = pygame.Surface((42, 70))
        self.rect = self.surf.get_rect(center=(x,y))#預設(0,0)

    def move(self):
        #global SCORE
        self.rect.move_ip(0,Constant.SPEED)
        if self.rect.top>Constant.height:
            Constant.SCORE+=1
            self.rect.top=0
            self.rect.left = random.randint(22,378)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        #super(Player,self).__init__()
        super().__init__()
        x,y = (Constant.width/2,Constant.height/2)
        self.image = pygame.image.load("Player.png")
        self.surf = pygame.Surface((40,75))
        self.rect = self.surf.get_rect(left=178,bottom=Constant.height-21)
        #self.rect = self.image.get_rect(center = (x,y))#預設(0,0)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_DOWN] and self.rect.bottom <= Constant.height-21:
            self.rect.move_ip(0, 5)
        if pressed_keys[pygame.K_UP] and self.rect.top>=0:
            self.rect.move_ip(0, -5)

        if pressed_keys[pygame.K_LEFT] and self.rect.left>=0:
            self.rect.move_ip(-5, 0)
        if pressed_keys[pygame.K_RIGHT]and self.rect.right<=Constant.width-4:
            self.rect.move_ip(5, 0)




class Game:
    def __init__(self):

        pygame.init()

        size = width, height = (400, 600)

        pygame.display.set_caption("逆行超車")
        self.screen = pygame.display.set_mode(size)  # 要塞一個元素(500,500)
        # 定義事件
        self.SPEED_UP = pygame.USEREVENT + 1
        pygame.time.set_timer(self.SPEED_UP, 1000)

        self.OUT_OF_RANGE = pygame.USEREVENT + 1
        self.backgroud = pygame.image.load("AnimatedStreet.png")

        self.player = Player()
        self.enemy = Enemy()
        # 定義精靈組
        self.enemies = pygame.sprite.Group()
        self.enemies.add(self.enemy)
        # 所有精靈
        self.all_sprite = pygame.sprite.Group()
        self.all_sprite.add(self.player)
        self.all_sprite.add(self.enemy)
        # 字體
        font_big = pygame.font.SysFont("Verdana", 60)
        font_small = pygame.font.SysFont("Verdana", 20)      # 音樂
        game_over = font_big.render("game over", True, BLACK)# pygame.mixer.Sound("background.wav").play(-1) #默認執行一遍,loop莫認為0,-1表示無限循環

        while True:
            self.screen.blit(self.backgroud, (0, 0))
            scores = Constant.font_small.render(str(Constant.SCORE), True, Constant.BLACK)
            self.screen.blit(scores, (10, 10))
            for sprite in self.all_sprite:
                self.screen.blit(sprite.image, sprite.rect)
                sprite.move()

            # 從事件列中提取事件對象，根據類型進行事件處理
            for event in pygame.event.get():
                if event.type == Constant.SPEED_UP:
                    Constant.SPEED += 0.5

                # print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()  # 如在pygame.quit()前終止，IDLE會掛起

                # 處理
                if event.type == self.OUT_OF_RANGE:
                    print("超過邊界")
            if pygame.sprite.spritecollideany(self.player, self.enemies):  # 把敵人從所有組內消除
                # pygame.mixer.Sound("crash.wav").play()
                # time.sleep(1)

                self.screen.fill(Constant.RED)
                self.screen.blit(Constant.game_over, (80, 150))

                pygame.display.update()
                time.sleep(2)

                pygame.quit()
                sys.exit()

            pygame.display.update()
            self.clock.tick(Constant.FPS)
if  __name__ =='__main__':
    game = Game()
    game.run()