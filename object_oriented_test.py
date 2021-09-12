import pygame
import sys

pygame.init()


size = width, height = (400, 600)

pygame.display.set_caption("繪製圖形")
screen = pygame.display.set_mode(size) # 要塞一個元素(500,500)
#頻速率
FPS = 60
clock = pygame.time.Clock()

class Player:
    def __init__(self):
        x,y = (width/2,height/2)
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect(center = (x,y))#預設(0,0)

    def move(self):
        #self.rect.y-=1
        #self.rect = self.rect.move(0,-1)#變化結果返回rect
        self.rect.move_ip(0,-2)

backgroud = pygame.image.load("AnimatedStreet.png")

player = Player()

while True:
    screen.blit(backgroud,(0,0))
    screen.blit(player.image,player.rect)
    player.move()

    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
            sys.exit()  #如在pygame.quit()前終止，IDLE會掛起

    pygame.display.update()
    clock.tick(FPS)