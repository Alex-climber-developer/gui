# Pygame шаблон - скелет для нового проекта Pygame
import pygame
import random

WIDTH = 1920  # ширина игрового окна
HEIGHT = 1080 # высота игрового окна
FPS = 30 # частота кадров в секунду



# создаем игру и окно
pygame.init()
pygame.mixer.init()  # для звука
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()



# Цикл игры
running = True
while running:
  
  pygame.time.delay(10)
  for event in pygame.event.get():
    if event.type==pygame.QUIT:
      run=False
  keys= pygame.key.get_pressed()

  k=0
  fill=False
  stop=0
  l,r,u,d=False,False,False,False

  
  if keys[pygame.K_q]:
    stop+=1;fill=True
    if stop%2==0: fill=False
  if fill:
    new_serf=win
    win.blit(new_serf,(0,0))
    new_serf.blit(player, (x,y))
    # eachPixel()
    # pygame.draw.rect(win, (0,0,0),(x,y, width, height))
  if keys[pygame.K_SPACE]:k +=1
  if keys[pygame.K_LEFT]:
    x-=2+k
    l=True
    if (d or r or u)!= False: k=0
    d,r,u=False,False,False
  if keys[pygame.K_RIGHT]:
    x+=2+k
    r=True
    if (l or d or u)!= False: k=0
    l,d,u=False,False,False
  if keys[pygame.K_UP]:
    y-=2+k
    u=True
    if (l or r or d)!= False: k=0
    l,r,d=False,False,False
  if keys[pygame.K_DOWN]:
    y+=2+k
    d=True
    if (l or r or u)!= False : k=0
    l,r,u=False,False,False
  updateFrame()
  # if fill:
  

    # win.fill(0,0,0)
    # pygame.draw.rect(win, (0,0,0),(x,y, width, height))
  # else:pygame.draw.rect(win, (1,255,255),(x,y, width, height))
  
 
pygame.quit()
    # Ввод процесса (события)
    # Обновление
    # Визуализация (сборка)


    # Цвета (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


# Рендеринг
screen.fill(BLACK)
# после отрисовки всего, переворачиваем экран
pygame.display.flip()