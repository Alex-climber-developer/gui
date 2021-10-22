import pygame
import os
orderX=700
orderY=700
pygame.init()
win=pygame.display.set_mode((orderX , orderY))
pygame.display.set_caption("Смещение")
width=20
height=60
run=True
x=orderX//2-(1/2*width)
y=orderY//2-(1/2*height)
player=pygame.image.load('.\python\gui\pygame\\figure\idle.png')
def eachPixel():
  global x,y,width,height
  for yi in range(int(y),int(y)+height+1):
    for xi in range(int(x),int(x)+width+1):
      color=tuple(win.get_at((int(xi), int(yi))))
      pygame.draw.rect(win, color,(xi,yi, 1, 1))

def updateFrame():
  win.blit(player, (x,y))
  # pygame.draw.rect(win, (1,255,255),(x,y, width, height))
  pygame.display.update()


while run:
  
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