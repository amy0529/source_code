import os
from tkinter import *
t1= Tk()

c1= Canvas(t1, width=200, height=200)
c1.pack()
img=PhotoImage(file=os.path.abspath(os.path.curdir)+'\\home.gif')
c1.create_image((95,70),image=img) 
c1.create_rectangle(50, 20, 150, 80, fill="Blue")
c1.create_rectangle(65, 35, 135, 65, fill="yellow")
c1.create_line(0, 21, 50, 21, fill="Black", width=3)
c1.create_line(0, 40, 50, 21, fill="#476042", width=3)
canvas_width = 200
canvas_height = 100
c1.create_text(canvas_width / 2,
              canvas_height / 2,
              text="三酷猫")
c1.create_arc(151,20,190,80,start=0,extent=90,width=2,fill="red",tags="arc")
c1.create_polygon(111,140,151,100,190,100,151,180,fill="Purple",tags="polygon")

t1=c1.create_text(20,6,text="三酷猫")
c1.delete(t1)
mainloop()
