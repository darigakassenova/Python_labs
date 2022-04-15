import pygame
pygame.init()

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (230, 0, 0)
RED_DARK = (139, 0 ,0)
GREEN = (34, 139, 34)
BLUE = (0, 0, 230)
# display
size = WIDTH,HEIGHT = (800, 600)
pygame.display.set_caption('PAINT')
img = pygame.image.load("/Users/dariga/Desktop/PP2/lab_8/img/eraser.png")
img_=pygame.transform.scale(img, (50,50))
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()
running = False
dir, mouse = None, None
screen.fill(WHITE)
color = BLACK
pen = 1
done = True 
shape = 0
check = 0
save_screen = None
points = []

# start
while not running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = True 
    # mouse--->draw line
    if event.type == pygame.MOUSEBUTTONDOWN:
      dir = pygame.mouse.get_pos()

    if event.type == pygame.MOUSEMOTION:
      mouse = pygame.mouse.get_pos()

      if dir:
        pygame.draw.line(screen, color, dir, mouse, pen)
        dir = mouse
    # dir = 0 ---> no line
    if event.type == pygame.MOUSEBUTTONUP:
      dir = None
      points = []
      done = True  
    
    if event.type == pygame.MOUSEBUTTONDOWN:
      # choose color:
      if 25<=mouse[0]<=55 and 35<=mouse[1]<=65:
        color = RED

      elif 65<=mouse[0]<=95 and 35<=mouse[1]<=65:
        color = BLUE

      elif 25<=mouse[0]<=55 and 75<=mouse[1]<=105:
        color = GREEN

      elif 66<=mouse[0]<=96 and 76<=mouse[1]<=106:
        color = BLACK
      # eraser:
      elif 40<=mouse[0]<=90 and 500<=mouse[1]<=550:
        color = WHITE  
        check = 0 
      # geometric figures
      elif 41<=mouse[0]<=96 and 130<=mouse[1]<=175:
        # rect
        check = 1
        shape = 0
        
      elif 60<=mouse[0]<=90 and 200<=mouse[1]<=230:
        # circle
        check = 1
        shape = 1

      elif 50<=mouse[0]<=65 and 300<=mouse[1]<=340:
        # right triangle
        check = 1
        shape = 2
        
      elif 41<=mouse[0]<=86 and 360<=mouse[1]<=405:
        # square
        check = 1
        shape = 3

      elif 50<=mouse[0]<=65 and 260<=mouse[1]<=305:
        # equilateral triangle
        check = 1
        shape = 4
      
      if check != 0 and color == WHITE:
        color = BLACK

      if check == 1:
        done = False
        x1,y1 = event.pos
        save_screen = screen.copy()

    if event.type == pygame.KEYDOWN:
      # rhombus
      if event.key == pygame.K_1:
        check = 1
        shape = 5
     
    # size of figures
    if event.type == pygame.MOUSEMOTION and (0,0) < event.pos < size and pygame.mouse.get_pressed()[0]:
      
      if not done:
          x2,y2 = event.pos
          width, height = abs(x1-x2), abs(y1-y2)
          screen.blit(save_screen, (0,0))

          if shape==0:
              pygame.draw.rect(screen, color, (x1 - width*(x2<x1),y1 - height*(y2<y1),width, height),pen) 

          if shape==1:
              pygame.draw.ellipse(screen, color, (x1 - width*(x2<x1),y1 - height*(y2<y1),width, height),pen) 

          if shape==2:
              if x2 > x1 and y2 > y1:
                  pygame.draw.polygon(screen, color, ((x1, y1), (x2, y2), (x1, y2)), pen)

              if y2 > y1 and x1 > x2:
                  pygame.draw.polygon(screen, color, ((x1, y1), (x2, y2), (x1, y2)), pen)

              if x1 > x2 and y1 > y2:
                  pygame.draw.polygon(screen, color, ((x1, y1), (x2, y2), (x2, y1)), pen)

              if x2 > x1 and y1 > y2:
                  pygame.draw.polygon(screen, color, ((x1, y1), (x2, y2), (x2, y1)),  pen)

          if shape==3:
            pygame.draw.rect(screen, color, (x1 - width*(x2<x1),y1 - height*(y2<y1),height, height),pen)

          if shape==4:
              width_b = abs(x2 - x1)
              height = (3**0.5) * width_b / 2

              if y2 > y1:
                  pygame.draw.polygon(screen, color, ((x1, y2), (x2, y2), ((x1 + x2) / 2, y2 - height)), pen)
              else:
                  pygame.draw.polygon(screen, color, ((x1, y1), (x2, y1), ((x1 + x2) / 2, y1 - height)), pen)
          if shape==5:
              pygame.draw.lines(screen, pygame.Color(color), True, (((x1 + x2) / 2, y1), (x1, (y1 + y2) / 2), ((x1 + x2) / 2, y2), (x2, (y1 + y2) / 2)), pen)
              

    pygame.mouse.get_pos()
    # pencil thickness
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP:
        pen+=1
      elif event.key == pygame.K_DOWN:
        pen-=1
        if pen <= 0:
          pen = 1  

    # design
    pygame.draw.rect(screen, (192,192,192), (2,2,120,598)) 
    pygame.draw.line(screen, (0,0,0), (122,0),(122,600), 10)
    pygame.draw.rect(screen, (0,0,0), (0,0,800,600), 10)
    pygame.draw.rect(screen, RED, (25,35,30,30))
    pygame.draw.rect(screen, BLUE, (65, 35, 30, 30))
    pygame.draw.rect(screen, GREEN, (25, 75, 30, 30))
    pygame.draw.rect(screen, BLACK, (66, 76, 30, 30))
    pygame.draw.rect(screen, (0,0,0), (24,34,32,32), 3)
    pygame.draw.rect(screen, (0,0,0), (64,34,32,32), 3)
    pygame.draw.rect(screen, (0,0,0), (24,74,32,32), 3)
    pygame.draw.rect(screen, (0,0,0), (39,499,52,52), 3)
    pygame.draw.rect(screen, (0,0,0), (40,130,55,45), 2)
    pygame.draw.circle(screen, (0,0,0), (63,210), 23, 2)
    pygame.draw.rect(screen, (255,255,255), (40,500,50,50))
    pygame.draw.rect(screen, (0,0,0), (41,360,45,45), 2)
    pygame.draw.polygon(screen, BLACK, [(35,285), (62,245), (91, 285)], 2)
    pygame.draw.polygon(screen, BLACK, [(35,340), (35,300), (91, 340)], 2)
    
  screen.blit(img_,(40,499))
  pygame.display.flip()
  clock.tick(30)
pygame.quit()