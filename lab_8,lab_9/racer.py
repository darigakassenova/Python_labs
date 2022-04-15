import pygame
import random,time
pygame.init()

# main
dis = [400,600]
enemy_step = 3
SPEED = 5
screen = pygame.display.set_mode(dis)
pygame.display.set_caption("RACER")
timer = pygame.time.Clock()
screen.fill('white')

# img load
game_background = pygame.image.load('/Users/dariga/Desktop/PP2/lab_8/img/AnimatedStreet.png').convert()


text = pygame.font.SysFont('ariel',40)

# variables
score = 0
coin_collision =False
w = 0

# enemy
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("/Users/dariga/Desktop/PP2/lab_8/img/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, dis[0]-40), 50) 

      def move(self):
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
  
# player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("/Users/dariga/Desktop/PP2/lab_8/img/Car.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        self.score = 0
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_UP]:
                self.rect.move_ip(0, -5)
        if pressed_keys[pygame.K_DOWN]:
                self.rect.move_ip(0,5)
        if self.rect.left > 0:
              if pressed_keys[pygame.K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < dis[0]:        
              if pressed_keys[pygame.K_RIGHT]:
                  self.rect.move_ip(5, 0)

# coin
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        image = pygame.image.load("/Users/dariga/Desktop/PP2/lab_8/img/Coin.png")
        self.image = pygame.transform.scale(image, (40,40))
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(200,dis[0]-30),0)

    def move(self):
        global coin_collision, w
        self.rect.move_ip(0,enemy_step)
        if coin_collision == True:
            coin_collision = False
            # Randomly generating coins with different weights on the road
            w = random.randrange(5, 15)
            image = pygame.image.load("/Users/dariga/Desktop/PP2/lab_8/img/Coin.png")
            self.image = pygame.transform.scale(image, (40+w,40+w))
            self.rect = self.image.get_rect()
            self.rect.center=(random.randint(20,dis[0]-30),0) 

        if(self.rect.bottom>dis[1]):
            self.top=0
            self.rect.center = (random.randint(20,dis[0]-30),0)
 
P1 = Player()
E1 = Enemy()
C1 = Coin()
 
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
while True:     
    screen.blit(game_background,(0,0))
    for event in pygame.event.get():
        # Increase the speed of Enemy when the player earns N coins
        if event.type == INC_SPEED:
            if score % 3 == 0:
              SPEED += 1
        # quit   
        if event.type == pygame.QUIT:
            pygame.quit()
    # Showing the number of collected coins in the top right corner
    text_score=text.render(f"SCORE: {score}",0,'black')
    screen.blit(text_score,(10,10))

    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()
    
    # collecting coins
    if pygame.sprite.spritecollideany(P1, coins):
        score+=1
        coin_collision = True

    # enemy vs player
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()   
          
    pygame.display.update()
    timer.tick(60)