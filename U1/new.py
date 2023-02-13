import random


def crear_matriz(n):
    matriz = []
    filas = n
    columnas = n
    for f in range(filas):
        matriz.append([0]*columnas)
    return matriz

def rellenar(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            matriz[f][c] = random.randint(0, orden**2)
            
            
    return matriz


def imprimir(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas):
        for c in range (columnas):
            print("%3d" %matriz[f][c], end= "")
        print()


orden = int(input("Ingrese el orden de la matriz: "))

matriz = crear_matriz(orden)

rellenar(matriz)

imprimir(matriz)