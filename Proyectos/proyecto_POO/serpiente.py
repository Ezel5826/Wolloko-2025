#atributos = coordenadas, tamaño, color, avance
#conportamientos = mover, incrementar tamaño, obtener longitud
from copy import deepcopy as dp
from random import randint as rd
ancho=15
alto=15

def crear_serpientes(color:int=1, sense:int=(0,0),cant_serp=1,vida=100,state=True,velocidad=20):
    j=0
    serpent=[]
    while j!=cant_serp:
        cords=[rd(2,ancho-3),rd(2,alto-3)]
        if j==0:
            serpent.append(cords,color,sense,)

    return [cordenadas,len(cordenadas),color,sense]

def move_serpent(serpent):

    if not serpent[3] == (0,0):
        for i in range(len(serpent[0])):
            if i + 1 <= len(serpent[0])-1:
                serpent[0][i] = dp(serpent[0][i+1])

    for i in range(2):
        serpent[0][len(serpent[0])-1][i] += serpent[3][i]

    for _ in range(len(serpent[0])):
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
    if apple[2]>=1:
        for i in range(apple[2]):
            serpent[0].insert(0,[serpent[0][0][0],serpent[0][0][1] -1])
    else:
        if not len(serpent[0]) == 2:
            for i in range(-2,apple[2]):
                serpent[0].pop(0)
    return serpent


def eat_appl(serpent,apple):
    for i in range(len(apple)):
        if apple[i][0] == serpent[0][len(serpent[0])-1]:
            apple[i][1] = False
            serpent=dencrement_size(serpent,apple[i])
            # serpent[6]+=apple[i][4]
    return serpent,apple
