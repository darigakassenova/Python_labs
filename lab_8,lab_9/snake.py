import sys
import pygame
import random
import datetime

from pygame.time import Clock
pygame.init()

# display size
BLACK = (0, 0, 0)
LINE_COLOR = (50, 50, 50)
HEIGHT = 400
WIDTH = 400
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()
SCREEN.fill(BLACK)
game=True

BLOCK_SIZE = 20
step=5

# img load
img = pygame.image.load("/Users/dariga/Desktop/PP2/lab_8/img/snake_font.png") 
img1 = pygame.transform.scale(img,(400,400)) 

# text
score_font = pygame.font.SysFont("Times New Roman", 20) 
level_font=pygame.font.SysFont("Times New Roman", 20)

# variables
score=0
Level=1
bf=False


class Point:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y


# wall:
class Wall:
    def __init__(self, level):
        self.body = []
        f = open("level1.txt".format(level), "r")
    
        for y in range(0, HEIGHT//BLOCK_SIZE + 1):
            for x in range(0, WIDTH//BLOCK_SIZE + 1):
                if f.read(1) == '#':
                    self.body.append(Point(x, y))

    def draw(self):
        for point in self.body:
            rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, (128,128,128), rect)
    def check_collision(self, snake,): 
        for point in self.body:
                if snake.body[0].x == point.x:
                    if snake.body[0].y == point.y:
                        pygame.quit()
    
            
# food: 
class Food:
    def __init__(self):
        self.location = Point( round(random.randrange(0, 20)),  round(random.randrange(0, 20))) 

    def draw(self):
        point = self.location
        rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(SCREEN, (128, 0, 0), rect)
    def check_collision(self, snake): 
        if snake.body[0].x == self.location.x:
            if snake.body[0].y == self.location.y:
                self.location = Point( round(random.randrange(0, 20)),  round(random.randrange(0, 20)))
                point = self.location
                rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
                pygame.draw.rect(SCREEN, (128, 0, 0), rect) 
    def check_new(self,wall): 
        for point in wall.body:
            if point.x == self.location.x:
                if point.y == self.location.y:
                    self.location = Point( round(random.randrange(0, 20)),  round(random.randrange(0, 20)))
                    point = self.location
                    rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
                    pygame.draw.rect(SCREEN, (128, 0, 0), rect) 


# Randomly generating food with different weights
class Big_food:
    def __init__(self):
        self.location = Point( round(random.randrange(0, 20)),  round(random.randrange(0, 20))) #

    def draw(self):
        point = self.location
        rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(SCREEN, (128, 0, 0), rect)
    def check_collision(self, snake): 
        if snake.body[0].x == self.location.x:
            if snake.body[0].y == self.location.y:
                self.location = Point( round(random.randrange(0, 20)),  round(random.randrange(0, 20)))
                point = self.location
                rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
                pygame.draw.rect(SCREEN, (128, 0, 0), rect) 
    def check_new(self,wall): 
        for point in wall.body:
            if point.x == self.location.x:
                if point.y == self.location.y:
                    self.location = Point( round(random.randrange(0, 20)),  round(random.randrange(0, 20)))
                    point = self.location
                    rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
                    pygame.draw.rect(SCREEN, (128, 0, 0), rect)
    def check_food(self,food):
        if self.location.x == food.location.x:
            if self.location.y == food.location.y:
                self.location = Point( round(random.randrange(0, 20)),  round(random.randrange(0, 20)))
                point = self.location
                rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
                pygame.draw.rect(SCREEN, (128, 0, 0), rect)



# snake
class Snake():
    def __init__(self):
        self.body = [Point(10, 11)]
        self.dx = 0
        self.dy = 0
        self.level = 1

    def move(self):    
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i-1].x
            self.body[i].y = self.body[i-1].y

        self.body[0].x += self.dx 
        self.body[0].y += self.dy 
        if self.body[0].x * BLOCK_SIZE > WIDTH:

           pygame.quit()
        
        if self.body[0].y * BLOCK_SIZE > HEIGHT:
           pygame.quit()

        if self.body[0].x < 0:
           pygame.quit()
        
        if self.body[0].y < 0:
           pygame.quit()
    def draw(self):
        point = self.body[0]
        rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, 20, BLOCK_SIZE)
        pygame.draw.rect(SCREEN, (0, 128, 0), rect)


        for point in self.body[1:]:
            rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, (0, 128, 0), rect)

    def check_collision(self, food): 
        global score,step,Level
        if self.body[0].x == food.location.x:
            if self.body[0].y == food.location.y:
                self.body.append(Point(food.location.x, food.location.y))
                score+=1
                # increase speed:
                if score % 4 == 0:
                    step+=3
                    Level+=1

# game start 
    # global SCREEN, CLOCK,step,score,bf
    # pygame.init()
    # SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    # CLOCK = pygame.time.Clock()
    # SCREEN.fill(BLACK)

snake = Snake()
food = Food()
wall = Wall(snake.level)
big_food= Big_food()

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RIGHT:
                snake.dx = 1
                snake.dy = 0

            if event.key == pygame.K_LEFT:
                snake.dx = -1
                snake.dy = 0

            if event.key == pygame.K_UP:
                snake.dx = 0
                snake.dy = -1

            if event.key == pygame.K_DOWN:
                snake.dx = 0
                snake.dy = 1
                
    snake.move()
    SCREEN.blit(img1,(0,0))

    snake.check_collision(food)
    food.check_collision(snake)
    food.check_new(wall)
    wall.check_collision(snake)
    if score%3==0 and score>0:
        bf=True
    if bf==True:
        big_food.check_collision(snake)
        big_food.check_food(food)
        big_food.check_new(wall)
        big_food.draw()
        
    snake.draw()
    food.draw() 
    wall.draw()

    score_img = score_font.render(f'SCORE: {str(score)}', True, pygame.Color('white'))
    SCREEN.blit(score_img, (0, 0))
    score_img1 = score_font.render(f'LEVEL: {str(Level)}', True, pygame.Color('white'))
    SCREEN.blit(score_img1, (0, 20))

    pygame.display.update()
    CLOCK.tick(step)
