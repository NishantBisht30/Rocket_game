import pygame,sys
import random
import math


class bgEnemey():

    def __init__(self,black_holes,enemeyha,pos_x,pos_y):
        self.bh = pygame.image.load(black_holes)
        self.enemeyImg1 = pygame.image.load(enemeyha)
        self.enemeyImg2 = pygame.image.load(enemeyha)
        self.enemeyImg3 = pygame.image.load(enemeyha)
        self.enemeyImg4 = pygame.image.load(enemeyha)
        self.enemeyImg5 = pygame.image.load(enemeyha)
        self.enList = [self.enemeyImg1,self.enemeyImg2,self.enemeyImg3,self.enemeyImg4,self.enemeyImg5]
        self.enemeyX = pos_x
        self.enemeyY = pos_y
        self.distance = 0
        # self.score_value = 0
        self.font = pygame.font.Font("freesansbold.ttf",32)
        self.hitSound = pygame.mixer.Sound("mixkit-space-coin-win-notification-271.wav")


    def drawB(self,screen):
        screen.blit(self.bh,(10,0))
        screen.blit(self.bh,(180,0))
        screen.blit(self.bh,(350,0))
        screen.blit(self.bh,(520,0))
        screen.blit(self.bh,(690,0))

    def drawE(self,screen):
        screen.blit(self.enemeyImg1,(self.enemeyX,self.enemeyY))

    def draw_score(self,screen,scoreV):
        self.score = self.font.render("Score: " +str(scoreV),True,(255,0,0))
        screen.blit(self.score,(5,608))

    def update(self,screen,playerX,playerY,scoreV):
        self.enemeyY += 10
        self.distance = math.sqrt((pow(playerX - self.enemeyX, 2)) + (pow(playerY - self.enemeyY, 2)))

        if self.enemeyY > 650:
            self.enemeyY = 0
            # list1 = [15, 185, 355, 525, 685]
            self.enemeyX = random.choice(list1)
        else:
            if self.distance < 27:
                scoreV += 1
                self.enemeyY = 0
                self.enemeyX = random.choice(list1)
                self.hitSound.play()

        self.drawE(screen)
        return scoreV


class player():
    def __init__(self,pla):
        self.img = pygame.image.load(pla)
        self.img = pygame.transform.scale(self.img,(64,64))
        self.imgX = 760 / 2
        self.imgY = 530
        self.img_rect = self.img.get_rect(center = (self.imgX,self.imgY))



    def draw(self,screen):
        screen.blit(self.img,(self.imgX,self.imgY))

    def update(self,screen,changeX):
        self.imgX = self.imgX - changeX
        if self.imgX <= 0:
            self.imgX = 0
        if self.imgX >= 696:
            self.imgX = 696
        self.draw(screen)
        return self.imgX,self.imgY


class gameState():
    def __init__(self):
        self.state = 'intro'
        self.readyImg = pygame.image.load("text_ready.png")
        self.x = 300
        self.y = 550
        self.x_change = 0
        self.y_change = 0
        self.score_value =0

    def intro(self):

            screen.fill((255, 255, 255))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.state = 'main_game'
            screen.blit(bgimage, (0, 0))
            screen.blit(self.readyImg, (290, 280))
            pygame.display.flip()



    def main_game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.x_change += 10
                elif event.key == pygame.K_RIGHT:
                    self.x_change -= 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    self.x_change = 0

        screen.blit(bgimage, (0, 0))

        tempX, tempY = pl.update(screen,self.x_change)
        self.score_value = enem1.update(screen, tempX, tempY, self.score_value)
        enem1.draw_score(screen, int(self.score_value))
        enem1.drawB(screen)
        pygame.display.flip()




    def game_manager(self):
        if self.state == 'intro':
            self.intro()
        elif self.state == 'main_game':
            self.main_game()


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((760,650))
pygame.mixer.music.load("space-chillout-14194.wav")
pygame.display.set_caption("Fill The Fuel!!")
pygame.mixer.music.play(-1,0,0)
bgimage = pygame.image.load("vectorstock_3071038.png")
bgimage = pygame.transform.scale(bgimage,(760,650))

pygame.mouse.set_visible(False)

tempX=0
tempY=0
#setting value for enemy

list1 = [15, 185, 355, 525, 685]
enemey_x = random.choice(list1)
enemey_y=0



enem1 = bgEnemey("black-hole.png" ,"petrol-can.png",enemey_x,enemey_y)
pl= player("spaceship (1).png")

obj = gameState()

while True:
    obj.game_manager()
    clock.tick(30)