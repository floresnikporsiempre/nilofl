from tkinter import * 
from tkinter import messagebox
import tkinter as tk
from math import sqrt
#ecuacion de secgundo grado aX^2+bX+c
def espacios(a,b,c):
 a = float(a)
 b = float(b)
 c = float(c)

 d = (b*b-4*a*c)
 if a!=0:
    #dos soluciones 
    if d>=0:
        x1 = (-1*b + sqrt(d))/(2*a)
        x2 = (-1*b - sqrt(d))/(2*a)
        l6 = Label(root,text=f'{"soluciones reales"}',bg='#DDD',fg='#000',font=('Helvetica', 14, 'italic'))
        l6.place(x=200,y=290)
        l4 = Label(root,text=f'X1 = {round(x1,6)}',bg='#DDD',fg='#000',font=('Helvetica', 25, 'italic'))
        l4.place(x=100,y=335)
        l5 = Label(root,text=f'X2 = {round(x2,6)}',bg='#DDD',fg='#000',font=('Helvetica', 25, 'italic'))
        l5.place(x=100,y=385)
    else:
        x = (-1*b)/(2*a)
        x1 = sqrt(-d)/(2*a)
        l6 = Label(root,text=f'{"soluciones complejas"}',bg='#DDD',fg='#000',font=('Helvetica', 14, 'italic'))
        l6.place(x=200,y=290)
        l4 = Label(root,text=f'X1 = {round(x,6)} + {round(x1,6)}i',bg='#DDD',fg='#000',font=('Helvetica', 25, 'italic'))
        l4.place(x=100,y=335)
        l5 = Label(root,text=f'X1 = {round(x,6)} + {round(x1,6)}i',bg='#DDD',fg='#000',font=('Helvetica', 25, 'italic'))
        l5.place(x=100,y=385)
 else:
    #unica solucion
    x1 = -(c)/b
    l6 = Label(root,text=f'{"unica solucion real"}',bg='#DDD',fg='#000',font=('Helvetica', 14, 'italic'))
    l6.place(x=200,y=290)
    l4 = Label(root,text=f'X1 = {x1}',bg='#DDD',fg='#000',font=('Helvetica', 25, 'italic'))
    l4.place(x=100,y=335)

root = Tk()
root.title("FLORES QUISPE NILO")
l = Label(root,text="ECUACION DE SEGUNDO GRADO ",fg='#1C2833',bg='#CCD1D1',font=('Helvetica', 14, "italic"))
l.place(x=250,y=5)
root.configure(background='#CCD1D1') 
root.geometry('750x500')
l1 = Label(root,text='Forma: ax²+bx+c',fg='#000',bg='#DDD',font=('Helvetica', 14, 'italic'))
l1.place(x=300,y=100)
#primer valor a introducir
l1 = Label(root,text='x²',fg='#000',bg='#DDD',font=('Helvetica', 14, 'italic'))
l1.place(x=200,y=150)
a = StringVar()
a1 = Entry(textvar=a)
a1.place(x=150,y=150,width=50,height=27)
#segundo valora a introducir 
l1 = Label(root,text=' x ',fg='#000',bg='#DDD',font=('Helvetica', 14, 'italic'))
l1.place(x=300,y=150)
b = StringVar()
b1 = Entry(textvar=b)
b1.place(x=250,y=150,width=50,height=27)
#tercer valor a introducir 
l1 = Label(root,text='  ',fg='#000',bg='#DDD',font=('Helvetica', 14, 'italic'))
l1.place(x=400,y=150)
c = StringVar()
c1 = Entry(textvar=c)
c1.place(x=350,y=150,width=50,height=27)
btn = Button(root,text='Calcular',fg='#000',bg='#439C0C',font=('Helvetica', 12, 'italic'),command=lambda: espacios(a1.get(),b1.get(),c1.get()))
btn.place(x=500,y=200)


root.mainloop()
