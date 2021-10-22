import time ,pygame
pygame.init()
orderX = 500
orderY = 500
win = pygame.display.set_mode((orderX,orderY))

#! Colors (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
ORANGE = (230, 150, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPOSE = (255, 0, 255)

pygame.display.set_caption("Cube game")
run = True
x = 0
y = 450
width = 30
height = 60
speed = 7
face=1
isJump = False
jumpCount = 10
jumps =2

left =False; right = False
animCount=0
clock=pygame.time.Clock()
bullets=[]

class bullet:
  def __init__(self,x,y,color,radius,face_direct,speed_bul):
    self.x=x
    self.y=y
    self.color=color
    self.radius=radius
    self.face_direct=face_direct
    self.speed_bul=speed_bul
    self.vel=self.speed_bul*face_direct
  def draw(self,surf):
    pygame.draw.circle(surf,self.color, (self.x,self.y), self.radius)
walkL=[]    
for i in range(1,7):
  walkL.append(pygame.image.load('.\python\gui\pygame\\1lesson\left_'+str(i)+'.png'))
walkR=[]
for i in range(1,7):
  walkR.append(pygame.image.load('.\python\gui\pygame\\1lesson\\right_'+str(i)+'.png'))
  
stand=pygame.image.load('.\python\gui\pygame\\1lesson\idle.png')
bg=pygame.image.load('.\python\gui\pygame\\1lesson\\bg.jpg')

def draw():
  global animCount
  win.blit(bg,(0,0))
  if animCount+1 >= 30:animCount=0
  if left:
    win.blit(walkL[animCount//5], (x,y))
    animCount+=1
  elif right:
    win.blit(walkR[animCount//5], (x,y))
    animCount+=1
  else: win.blit(stand, (x,y))

  for bullet in bullets: 
    bullet.draw(win)
  # win.fill(BLACK)c
  # pygame.draw.rect(win, GREEN,(x,y,width,height))
  pygame.display.update()


while run:
  clock.tick(30)
  for event in pygame.event.get():
    if event.type==pygame.QUIT:
      run=False
  
  keys= pygame.key.get_pressed()
  
  
  if (keys[pygame.K_LEFT] or keys[pygame.K_a] ) and x>0:
    x-=speed
    face= -1
    left=True;right=False
  elif (keys[pygame.K_RIGHT] or keys[pygame.K_d] ) and x<orderX-width:
    face= 1
    x+=speed 
    right=True;left=False

  else:right=False;left=False;animCount=0

  if (keys[pygame.K_c] ) and len(bullets)<=5:
    bullets.append(bullet(x+width//2, y+height//2, RED, 10-len(bullets), face,8 ))

  
  for bullet in bullets:
    if bullet.x>orderX or bullet.x<0:
      bullets.pop(bullets.index(bullet))
    else: bullet.x+=bullet.vel

  if not(isJump):
    if (keys[pygame.K_UP] or keys[pygame.K_w] ) and y>0 : y-=speed
    if (keys[pygame.K_DOWN] or keys[pygame.K_s] ) and y<orderY-height : y+=speed
    if keys[pygame.K_SPACE] and y>height//2+(jumpCount**2)//6:
      isJump=True
      jumps-=1
      
  if isJump:
    if jumpCount>=-10 :
      if keys[pygame.K_SPACE] and y>height//2+(jumpCount**2)//6:
        jumpCount=10
        jumps-=1
      if jumpCount>=0:
        y-=(jumpCount**2)//6
      else:
        y+=(jumpCount**2)//6
      jumpCount-=1
    else: 
      isJump=False
      jumpCount=10
      jumps=2

  draw()
  
pygame.quit()