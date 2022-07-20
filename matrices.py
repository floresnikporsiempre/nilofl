"""from cmath import sqrt
from tkinter import*
import  tkinter as tk
from tkinter import messagebox
from math import sqrt

interfaz = Tk()
interfaz.title('MATRICES')
interfaz.geometry('400x400')
interfaz.configure(bg='#D4E6F1')
l = Label(interfaz,text="DETERMINANTE ",fg='#2874A6',bg='#D4E6F1',font=('Helvetica', 20, "italic"))
l.place(x=100,y=5)
interfaz.mainloop() 
 edad = 0
while edad<18:
    edad = edad +1
    print ("felicidades, tienes "+ str(edad))"""
filas = int (input("inroduce el numero de filas "))
columnas = int(input("Introdusca el numero de columnas"))

matriz = []
for i in range(filas):
    matriz.append([])
    for j in range(columnas):
        valor = float (input("Filas {}, Columnas {} :".format(i+1, j+1 )))
        matriz[i]. append(valor)

print()
for fila in matriz:
    print(" ", end =" ")
    for elemento in fila:
        print(" {: 8.2f}". format(elemento), end =" ")
    print(" ")    
print()
