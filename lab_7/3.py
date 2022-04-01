import pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))
running = True
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
clock = pygame.time.Clock()
FPS = 40
color = RED
x = 35
y = 35
x1 = 500//2
y1 = 500//2
a = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if a == True:
            screen.fill(WHITE)
            f1 = pygame.font.Font(None, 48)
            text1 = f1.render('Tap to start', True, (255, 0, 0))
            screen.blit(text1, (162, 245))
            pygame.draw.rect(screen, (255, 0, 0), (150,240,205,50), 3)
            # pygame.draw.circle(screen, color, (245, 310), 10)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                a = False
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        y -= 20
    if pressed[pygame.K_DOWN]:
        y += 20
    if pressed[pygame.K_LEFT]:
        x -= 20
    if pressed[pygame.K_RIGHT]:
        x += 20
    if x + 25 >= 500:
        x = 475
    if x <= 25:
        x = 25
    if y + 25 >= 500:
        y = 475
    if y <= 25:
        y = 25
    if x == 475 or x == 25 or y == 475 or y == 25:
        color = BLUE
    else:
        color = RED
    if a == False:
        screen.fill(WHITE)
        pygame.draw.circle(screen, color, (x, y), 25)
        pygame.draw.circle(screen, RED, (x1, y1), 5)
        pygame.draw.rect(screen, (0,0,255), (0,0,500,500), 5)
    pygame.display.flip()
    clock.tick(FPS)
