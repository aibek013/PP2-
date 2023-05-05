import pygame as pg

pg.init()

pg.mixer.init()

WIDTH = 800
HEIGHT = 600
FPS = 50

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE=(0,0,225)

musiclist = ["./playlist/m1.mp3", "./playlist/m2.mp3", "./playlist/m3.mp3"]
i = 0
screen = pg.display.set_mode((WIDTH,HEIGHT))
clock = pg.time.Clock()

background = pg.image.load("./images/player.jpg")

pg.mixer.music.load(musiclist[i])
pg.mixer.music.play(1)
running = True
while running:
    clock.tick(FPS)
    screen.fill(WHITE)
    #keys = pg.key.get_pressed()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key ==pg.K_SPACE:
                pg.mixer.music.pause()
            if event.key ==pg.K_z:
                pg.mixer.music.unpause()
            if event.key ==pg.K_RIGHT:
                pg.mixer.music.stop()
                i += 1
                pg.mixer.music.load(musiclist[i])
                pg.mixer.music.play(1)    
            if event.key ==pg.K_LEFT:
                pg.mixer.music.stop
                i -= 1
                pg.mixer.music.load(musiclist[i])
                pg.mixer.music.play(1) 
    pg.mixer.music.queue(musiclist[(i+1) % len(musiclist)])
    screen.blit(background,(100,0))
    pg.display.flip()
pg.quit()