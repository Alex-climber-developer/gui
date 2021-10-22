import pygame
orderX=700
orderY=700
import os
print(os.environ["PATH"])
os.environ["PATH"] = r"c:\...\pywin32_system32;" + os.environ["PATH"]
from win32.win32api import GetSystemMetrics
clock= pygame.time.Clock()

realWidth=GetSystemMetrics(0)
realHeight=GetSystemMetrics(1)
pygame.init()
win=pygame.display.set_mode((realWidth , realHeight))
pygame.display.set_caption("Смещение")

run=True
while run:
  clock.tick(5)
  def color_change(start_color,count_change,change_size,simvol):
    do=True
    while do:
      r,g,b=start_color[0],start_color[1],start_color[2]
      surf=pygame.Surface((realWidth,realHeight))
      surf.fill(r,g,b)
      win.blit(surf,((GetSystemMetrics(0)-realWidth)//2,(GetSystemMetrics(1)-realHeight)//2))
      if b>=count_change:b-=count_change
      elif g>=count_change:g-=count_change; b=0
      elif r>=count_change:r-=count_change;g=0
      if simvol==-1:
        if realHeight<=change_size[0]:do=False;break
        else:
          realWidth-=change_size[0]
          realHeight-=change_size[1]
      else:
        if realHeight>=GetSystemMetrics(1)-change_size[1]:do=False;break
        else:
          realWidth+=change_size[0]
          realHeight+=change_size[1]
  color_change((255,255,255),3,1,-1)
  pygame.display.update()
  