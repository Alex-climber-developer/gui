### Ты играешь за определенный тип рыбок со своим приемуществом,ты можешь переключаться между экземплярами своего вида и управлять отдельно каким то из них,другие в это время будут упавляться встроенными функциями(боты),изначально  есть 1 рыба каждого типа ,ты должен есть еду или если ты хищник-обычных рыб, каждую секунду твоя сытость уменьшается и как только тыт ешь,ты ее пополняешь ,если она у  какой нибудь из рыбок станет 0- то она погибнет .Партия длится опр. колво времени . Кто по ее истечеии будет иметь больше всего рыб и сытости в каждой.ты можешь изначально настроить игровое поолле ,цвет ,уровень сложности,размеры и тд.
# from tkinter import *
# from tkinter import messagebox
#! Цвета (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
ORANGE = (230, 150, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPOSE = (255, 0, 255)


from random import *
import time
import pygame
import math
from win32.win32api import GetSystemMetrics

realWidth=GetSystemMetrics(0)
realHeight=GetSystemMetrics(1)

ordX=810
ordY=710
run=True
clock=pygame.time.Clock()
win=pygame.display.set_mode((ordX,ordY))
pygame.display.set_caption("Добро пожаловать в мир выживания,РЫБЫ")
clock=pygame.time.Clock()
pygame.init()
keys= pygame.key.get_pressed()
class game:
  def __init__(self,hardLevel,colorFish, colorGame,gameSize):
    self.hardLevel=hardLevel
    self.colorFish=colorFish
    self.colorGame=colorGame
    self.gameSize=gameSize
  def isClear(self):
    if realWidth<self.gameSize[0]<300:
      message=f'Не корректные размеры игрового поля. Размер вашего экрана{realWidth}x{realHeight}, и поле должно быть более 300х300 '
      self.gameSize=input(' размеры игрового поля ')
      if realWidth<self.gameSize[0]<300:
        self.gameSize=(realWidth, realHeight)

firstGame=game(1,[RED,GREEN,BLUE,PURPOSE],(0,112,90),[ordX,ordY])


class fish:
  
  def __init__(self,isDanger,speed,delSpeed ):
    self.isDanger=isDanger     #*проверка наи хищника
    self.speed=speed     #*скорость коэфф
    self.delSpeed=delSpeed     #*коэфф размножения
    self.foodLevel=100     #*уровень сытости(понижается с течением времени)
    self.isMyControl=False#* управляю ли я в данный момент этой рыбой
    self.transportable=[]    #* динамический массив всех рыб в которые можно телепортнуться
    self.seable=[]      #* динамический массив всех рыб которых видет эта
    self.dictMove={}    #* пары предыдущих коордитнат рыбы
    global fishs
    fish.count1=0
    fish.count2=0
    fish.count3=0
    fish.count4=0

  def __del__(self):
    if self in fishs: fishs[fishs.index(self)].remove(self)
  def append(self):
    if self is not fishs:
      fishs.append(self) #!
  def whoIs(self):
    if self.isDanger==True:#*ХИЩНИК
      self.radius_see=30#*как далеко в процентах от поля рыба может обнаружить противника (хищника\жертву)
      self.lifeTime=10#*время жизни в секундах(пополняется от съеденой еды)
      self.healthPerTime=15#* кол-во здоровья на секунду уходит
      self.w=self.h=20 #*размеры рыб
      self.x=randint((ordX//2)+self.w//2,ordX-self.w//2)#* расположение рандомно каждого в своей квадранте
      self.y=randint((ordY//2)+self.h//2,ordY-self.h//2)
      self.color=firstGame.colorFish[0]#*Цвет рыбы из массива в объекте игры КРАСНАЯ!!
      fish.count1+=1
      self.intelect=self.radius_see//2 #* дальность видения своих друзей(рыб своего типа)
      # self.speed- 90~100
      # self.delSpeed=30


      
    elif self.speed<30:#*бЫСТРО РАЗМНОЖАЕТСЯ , МАКС РАДИУС(В ПРОЦЕНТАХ ОТ РАЗМЕРОВ ПОЛЯ)
      self.radius_see=40
      self.lifeTime=30
      self.healthPerTime=10
      self.w=self.h=10
      self.x=randint(self.w//2,(ordX//2)-self.w//2)
      self.y=randint((ordY//2)+self.h//2,ordY-self.h//2)
      self.color=firstGame.colorFish[1] #*ЖЕЛТАЯ
      fish.count2+=1
      self.intelect=self.radius_see//2 #* дальность видения своих друзей(рыб своего типа)

    elif 30<=self.speed<=60:#* МЕДЛ РАЗМНОЖАЕТСЯ ,МИН РАДИУС
      self.radius_see=20
      self.lifeTime=30
      self.healthPerTime=5
      self.w=self.h=15
      self.x=randint(self.w//2, (ordX//2)-self.w//2)
      self.y=randint(self.h//2, (ordY//2)-self.h//2)
      self.color=firstGame.colorFish[2]#*ГОЛУБАЯ
      fish.count3+=1
      self.intelect=self.radius_see//2 #* дальность видения своих друзей(рыб своего типа)


    else:#* БЫСТРАЯ, РАЗМНОЖЕНИЕ СРЕДНИЕ ,РАДИУС СРЕДНИЙ
      self.radius_see=30
      self.lifeTime=5
      self.healthPerTime=15
      self.w=self.h=15
      self.x=randint((ordX//2)+self.w//2,ordX-self.w//2)
      self.y=randint(self.h//2, ordY//2-self.h//2)
      self.color=firstGame.colorFish[3]#*ФИОЛЕТОВАЯ
      fish.count4+=1    
      self.intelect=self.radius_see//2 #* дальность видения своих друзей(рыб своего типа)

  def myMove(self):
    # global fishs
    
    # def isControl(self):
    #   if  keys[pygame.K_a] 
    # if keys[pygame.K_SPACE]
    self.dictMove[x]=y
    if self.isMyControl==True:
      if ( keys[pygame.K_LEFT]) and self.x>0:
        
        self.x-=self.speed
        # left=True;right=False
      elif (keys[pygame.K_RIGHT] or keys[pygame.K_d] ) and self.x<ordX-self.w:
        self.x+=self.speed 
      # right=True;left=False
    # else:right=False;left=False;animCount=0
      if (keys[pygame.K_UP] or keys[pygame.K_w] ) and self.y>0 : self.y-=self.speed

      if (keys[pygame.K_DOWN] or keys[pygame.K_s] ) and self.y<ordY-self.h : self.y+=self.speed
    else:
      #сделать 2 функции отдельно- движение на клавиши 
      # global fishs
      for f in fishs:
        if f.x!=self.x and f.y!=self.y:
          dist=(f.x-self.x)**2+(f.y-self.y)**2
          if f.isDanger!=True:    #? Другая рыба не хищник
            if self.isDanger==True:      #!  Я ХИЩНИК
              def iamDanger():   
                if math.sqrt(dist)<=self.radius_see:
                  self.seable.append(f)
                else:
                  try:self.seable.remove(f)
                  except: None
              iamDanger()  
            else:     #!  Я не хищник
              def iamNOTDanger():  
                if math.sqrt(dist)<=self.intelect:
                  self.transportable.append(f)
                else:
                  try: self.transportable.remove(f)
                  except: None
              iamNOTDanger()
          else:             #? Другая рыба ХИЩНИК
            if self.isDanger==True:    #!  Я ХИЩНИК
              iamDanger()  
            else:           #!  Я не хищник
              iamNOTDanger()


fish0=fish(True,90,10)
fish2=fish(False,50,40)
fish1=fish(False,20,80)
fish3=fish(False,70,60)
fishs=[fish0,fish1,fish2,fish3] #!
# for i in fishs:
#   i.whoIs()
#   i.myMove()
#   pygame.draw.circle(win,i.color, (i.x, i.y), i.w)
# pygame.display.update()
def strela(self):
  i=0
  global keys 
  if self.isMyControl==True:
    if keys[pygame.K_a]:
        angle = i * 3.14 / 180
        l = math.acos((self.x - 400) / math.sqrt(self.y** 2 - 400 **2))
        int(l)
        a = (100 * math.cos(angle + l)) + 400
        b = (100 * math.sin(angle + l))  + 400
        i -= 1
    elif keys[pygame.K_d]:
        angle = i * 3.14 / 180
        l = math.acos((a - 400) / math.sqrt(500 ** 2 - 400 **2))
        int(l)
        a = (100 * math.cos(angle + l))  + 400 # 400 - начальная точка по х и по у
        b = (100 * math.sin(angle + l))  + 400
        i += 1
def updateFrame():
  win.fill(firstGame.colorGame)

  for i in fishs: #!ЦИКЛ ВСЕХ СОБЫТИЙ ДЛЯ КАЖДОЙ! РЫБЫ
    if i.foodLevel>=30 and :
    i.whoIs()
    i.myMove()
    #! тут функция чтоб стрелка во время движения тоже меняла направление
    # i.append() 
    # l=360
    # a=
    # if l <= 360: # здесь мы ставим ограничения, что-бы питон не выдал нам ошибку. 
    #     angle = l * (3.14 / 180) # перевод из градусов в радианы
    #     a = 100 * math.cos(angle) + 300
    #     b = 100 * math.sin(angle) + 300
    #     l+= 3 # здесь мы увеличиваем угол перемещения. 
        
    # else:
    #     l = 0
    
    if time.time()-t==1.0:#*если прошла секунда(кажд сек)
      i.lifeTime-= 1
      i.foodLevel-=i.healthPerTime
      countDelSpeed=i.delSpeed
      if i.delSpeed > 0 : i.delSpeed -=  1
      else: 
    
    if i.lifeTime<=0 or i.foodLevel<=0: i.__del__()

    pygame.draw.circle(win, i.color, (i.x,i.y), i.w)
    pygame.draw.rect(win, WHITE, (a,b))
  pygame.display.update()

while run:
  clock.tick(5)
  events=pygame.event.get()
  for event in events:
    if event.type==pygame.QUIT:
      exit()
      run=False
  t=time.time()
  pygame.draw.rect(win, (0,0,0), (0,0,ordX,ordY),5)

  updateFrame()

  # text.update(events)
  # text.draw(win)
