import pygame, sys
from pygame.locals import *
import random, time 
import psycopg2

pygame.init()

#creating display
screen = pygame.display.set_mode((600, 300))
screen.fill((0, 0, 0))
w, h = screen.get_size()
img = pygame.image.load("/Users/dariga/Desktop/PP2/lab_10/snake_font.png") 
img1 = pygame.transform.scale(img,(600,300)) 

#general class for any snake
class Snake(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.coordinates = [[x, y]]
        self.radius = 10
        self.size = 1
        self.dy = -1
        self.dx = 0
        self.add = False
        self.speed = 100
    def draw(self):
        for coord in self.coordinates:
            pygame.draw.circle(screen, (100, 255, 0), coord, self.radius)
    def adding(self):
        self.size += 1
        self.coordinates.append([0, 0])
        self.add = False

    def move(self):
        if self.add:
            self.adding()
        for i in range(self.size-1, 0, -1):
            self.coordinates[i][0] = self.coordinates[i-1][0]
            self.coordinates[i][1] = self.coordinates[i-1][1]
        
        self.coordinates[0][0] += self.dx
        self.coordinates[0][1] += self.dy
    def eat(self, food_x, food_y, stage):
        x = self.coordinates[0][0]
        y = self.coordinates[0][1]
        if stage % 5 == 0:
            self.speed += 0.01
        if food_x - 15 <= x <= food_x + 15 and food_y - 15 <= y <= food_y + 15:
            return True
        return False
    def self_collision(self):
        return self.coordinates[0] in self.coordinates[1:]
    # wall collision
    def wall_collision(self, stage):
        if (d - 10 < self.coordinates[0][0] < d + 10 + f and e - 10 < self.coordinates[0][1] < e + 10 + g) or (390<self.coordinates[0][0]<510 and 85< self.coordinates[0][1]<125):
            return True
        return False

# general class for any food
class Food(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = random.randint(5, 595)
        self.y = random.randint(5, 295)
    #generating position for food
    def gen(self, stage):
        self.x = random.randint(5, 595)
        self.y = random.randint(5, 295)
        if 195 < self.x < 215+150+stage*5 and 85 < self.y < 105+105+stage*5:
            while 195 < self.x < 215+150+stage*5 or 85 < self.y < 105+105+stage*5:
                self.x = random.randint(5, 595)
                self.y = random.randint(5, 295)  
    def draw(self):
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), 8)
    
    
snake = Snake(550, 210)

food = Food()
#step = dx and dy
step = 1

#controlling speed
clock = pygame.time.Clock()

pressed = pygame.key.get_pressed()
points = 0
done = False
level = 1
level_add = False
name = input()
conn = psycopg2.connect(host='localhost', port = 5432, database='postgres', user='postgres', password='6587009dkssnv')
cursor = conn.cursor()
sql = "select exists(select 1 from snake_exam where name=%s)"
cursor.execute(sql, (name,))
ans = cursor.fetchone()
if(ans[0]):
    sql = "select score from snake_exam where name = %s"
    cursor.execute(sql, (name,))
    t = cursor.fetchone()
    score = t[0]
else:
    sql = "insert into snake_exam (name, score) values(%s, %s);"
    cursor.execute(sql, (name, points))
    conn.commit()

d, e, f, g = 205, 95, 20, 105
#main code
while not done:
    clock.tick(snake.speed)
    screen.blit(img1,(0,0)) 
    # screen.fill((0, 0, 0))
    # pygame.draw.rect(screen, (a, b, c), (400, 95, 20+level*5, 105+level*5))
    pygame.draw.rect(screen, (128,128,128), (d, e, f, g))
    pygame.draw.rect(screen, (128,128,128), (e, d, g, f))
    pygame.draw.rect(screen, (128,128,128), (400, 95, 100, 20))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and not snake.dy == step:
                snake.dx = 0
                snake.dy = -step
            if event.key == pygame.K_DOWN and not snake.dy == -step:
                snake.dx = 0
                snake.dy = step
            if event.key == pygame.K_LEFT and not snake.dx == step:
                snake.dx = -step
                snake.dy = 0
            if event.key == pygame.K_RIGHT and not snake.dx == -step:
                snake.dx = step
                snake.dy = 0
            if event.key == pygame.K_SPACE:
                snake.speed -= 1
            if event.key == pygame.K_LSHIFT:
                snake.speed += 1

    # screen.blit(img1,(0,0))            
    #score
    pat = pygame.font.Font(None, 35)
    lvl = pat.render('Level: '+str(level), True, (255, 255, 255))
    screen.blit(lvl, (495,0))
    text = pat.render('Score: '+str(points), True, (255, 255, 255))
    screen.blit(text, (10, 0))
  
  
    if snake.eat(food.x, food.y, level):
        #levels and increasing speed
        points += 10
        if points % 20 == 0:
            level_add = True
        snake.speed += 1
        snake.add = True
        food.gen(level)

        if level_add:
            level += 1
            level_add = False
            d, e, g = random.randint(10,500), random.randint(10,250), random.randint(100,300)

        if [food.x, food.y] in snake.coordinates:
            while not [food.x, food.y] in snake.coordinates:
                food.gen(level)

        
    snake.move()
    snake.draw()
    food.draw()
    #leaving play area
    if snake.coordinates[0][0] > 600:
      snake.coordinates[0][0] = 0
    if snake.coordinates[0][0] < 0:
      snake.coordinates[0][0] = 600
    if snake.coordinates[0][1] > 300:
      snake.coordinates[0][1] = 0
    if snake.coordinates[0][1] < 0:
      snake.coordinates[0][1] = 300 
    #game over situations
    if snake.self_collision() or snake.wall_collision(level):
        temp = pygame.font.Font(None, 100)
        over = temp.render('Game over', True, (255, 255, 255))
        
        while not done:
            screen.blit(over, (100, 100))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True


    pygame.display.update()
    pygame.display.flip()

    
sql = """
    update snake_exam
    set score = %s
    where name = %s;
    """
cursor.execute(sql, (points, name))
conn.commit()

pygame.quit()