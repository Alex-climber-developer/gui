from tkinter import *
from random import *
import time
organics=[]
# for j in range(0,50):
#   organics[j]=[]
#   for i in range(0,50):
#     organics[j].append(randint(0,1))
for j in range(0,2500):
  organics.append(randint(0,1))
run= True
ordX=610;ordY=620

win= Tk()
win.title("Добро пожаловать в мир микроорганизмов")
c=Canvas(win, width=ordX, height=ordY, bg='white')
c.pack()
def change():
  global organics
  change_mas=organics
  count=0
  for el in range(0,2500):
    for i in 1,-1,24,-24,25,-25,26,-26:
      try:
          count+=organics[el+i]
      except:continue
    if count <2 or count >7:
      change_mas[el]=0
    if count==4: change_mas[el]=1
    count=0
  organics=change_mas

def draw():
  x=10
  y=10
  for el in range(0,2500):
    if (el)%50==0:
      y+=12
      x=10
    c.create_rectangle(x,y,x+9,y+9)
    if organics[el]==1: 
      c.create_oval(x,y,x+9,y+9 ,fill='red' )
      # time.sleep(1)
    else: 
      c.create_oval(x,y,x+9,y+9 ,fill='white', outline='black',width=1)
      # time.sleep(1)
    x+=12
while run:
  change()
  draw()
  time.sleep(1/2)
  # c.create_rectangle(0,0,620,620 ,fill='white')
  win.update()



