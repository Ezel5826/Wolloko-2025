#atributos = coordenadas, tamaño, color, avance
#conportamientos = mover, incrementar tamaño, obtener longitud
from copy import deepcopy as dp
from random import randint as rd
ancho=20
alto=20

def crear_serpiente(color:int=1, sense:int=(0,0)):
    cordenadas=[[10,4],[10,5]]
    return [cordenadas,len(cordenadas),color,sense]

def move_serpent(serpent):

    if not serpent[3] == (0,0):
        for i in range(serpent[1]):
            if i + 1 <= serpent[1]-1:
                serpent[0][i] = dp(serpent[0][i+1])

    for i in range(2):
        serpent[0][serpent[1]-1][i] += serpent[3][i]

    for _ in range(serpent[1]):
        if serpent[0][_][1] > ancho-1:
            serpent[0][_][1] = 0

        if serpent[0][_][1] < 0:
            serpent[0][_][1] = ancho-1

        if serpent[0][_][0] > alto-1:
            serpent[0][_][0] = 0
        if serpent[0][_][0] < 0:
            serpent[0][_][0] = alto-1
    return serpent

def dencrement_size(serpent,apple):
    print(f"esta es la manzana que entra a dencrement{apple}")
    print(f"esta es la cantidad de serpiente que rellena{apple[2]}")
    if apple[2]>=1:
        for i in range(apple[2]):
            serpent[0].insert(0,[serpent[0][0][0],serpent[0][0][1] -1])
            serpent[1]+=1
    else:
        if not len(serpent[0]) == 2:
            for i in range(-2,apple[2]):
                serpent[0].pop(0)
                serpent[1]-=1
    return serpent


def eat_appl(serpent,apple):
    for i in range(len(apple)):
        if apple[i][0] == serpent[0][serpent[1]-1]:
            apple[i][1] = False
            serpent=dencrement_size(serpent,apple[i])
    return serpent,apple
