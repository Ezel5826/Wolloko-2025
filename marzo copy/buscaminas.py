import random
def grilla_logica_1():
    grilla=[]
    for i in range(11):
        grilla_aux=[]
        for j in range(8):
                grilla_aux.append(0) 
        grilla.append(grilla_aux)
    return grilla 

def poner_bombas(grilla, num_bombas):
    filas = len(grilla)
    columnas = len(grilla[0])
    bombas_colocadas = 0
    while bombas_colocadas < num_bombas:
        fila = random.randint(0, filas - 1)
        columna = random.randint(0, columnas - 1)
        if grilla[fila][columna] != 1: 
            grilla[fila][columna] = 1
            bombas_colocadas += 1
            
    return grilla   

def contar_bombas(grilla):
    filas = len(grilla)
    columnas = len(grilla[0])

    for fila in range(filas):
        for columna in range(columnas):
            if grilla[fila][columna] == 1:
                continue
            contador = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if (0 <= fila + i < filas) and (0 <= columna + j < columnas):
                        if grilla[fila + i][columna + j] == 1:
                            contador += 1
            grilla[fila][columna] = contador
    return grilla

def grilla_logica_2():
    grilla = grilla_logica_1()
    num_bombas = 6
    grilla = poner_bombas(grilla, num_bombas)
    for i in grilla:
        print(i)
    grilla = contar_bombas(grilla)
    return grilla
