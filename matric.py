matriz = [[1,2,2],[3,5,6],[5,6,5,]]
print(matriz[0][0])
print(matriz[1][1])
print(matriz[2][2])
#sumar una matriz 
suma = 0
for i in range(len(matriz)):
    for j in range(len(matriz)):
        #suma = suma + matriz[i][j]
        if i==j:
            suma = suma + matriz[i][j]

print(suma)
