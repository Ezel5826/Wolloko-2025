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
        if grilla[fila][columna] != 8: 
            grilla[fila][columna] = 8
            bombas_colocadas += 1  
    return grilla   

def contar_bombas(grilla):
    x=len(grilla[0]) #8
    y=len(grilla) #11
    for i in range(y):
        for j in range(x):
            pass

def grilla_logica_2():
    grilla = grilla_logica_1()
    num_bombas = 6
    grilla = poner_bombas(grilla, num_bombas)
    #grilla = contar_bombas(grilla)
    for i in grilla:
        print(i)
    return grilla
