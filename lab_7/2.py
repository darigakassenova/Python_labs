import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
running = True
songs = ['riles.mp3', 'riles2.mp3', 'mj.mp3']
pygame.mixer.music.load(songs[0])
pygame.mixer.music.play(-1)
img = pygame.image.load('img.JPG')
music = True
k = 0
k1 = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if music==True:
                    pygame.mixer.music.pause()
                    music = False
                else:
                    pygame.mixer.music.unpause()
                    music = True 
            if event.key == pygame.K_RIGHT:
                k+=1
                if k>=len(songs):
                    k=0
                pygame.mixer.music.load(songs[0+k])
                pygame.mixer.music.play(-1)
            if event.key == pygame.K_LEFT:
                k1+=1
                if k1>len(songs):
                    k1=0
                pygame.mixer.music.load(songs[0-k1])
                pygame.mixer.music.play(-1)
    screen.blit(img, (0, 0))
    pygame.display.flip() 