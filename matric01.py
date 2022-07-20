import numpy as np
suma = 0

filas = int(input('introduce el nuemro de filas = '))
columnas = int(input('introduce el numero de columnas = '))

def matriz(filas, columnas):
 suma = 0
 fil = []
 for i in range (0,filas):
    col = []
    for j in range (0,columnas):
        elem = int (input(f'Elemento {i},{j} de la matriz = '))
        col.append(elem)
    fil.append(col)
 return fil
 

matrizA = matriz(filas,columnas) 
print (matrizA)

for i in range (0,filas):
    for j in range(0,columnas):
        if i==j:
            suma = suma+matrizA[i][j]

print(suma )





