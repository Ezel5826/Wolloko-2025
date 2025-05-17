#atributos = coordenadas, tamaño, color, avance
#conportamientos = mover, incrementar tamaño, obtener longitud
from copy import deepcopy as dp
from random import randint as rd
import Grilla

def crear_serpiente(color:int=1, sense:int=(0,0)):
    cordenadas=[[10,4],[10,5]]
    return [cordenadas,len(cordenadas),color,sense]

def move_serpent(serpent,grid):
    
    tail=serpent[0][0]
    print(serpent)
    if not serpent[3] == (0,0):
        for i in range(serpent[1]):
            if i + 1 <= serpent[1]-1:
                serpent[0][i] = dp(serpent[0][i+1])

    for i in range(2):
        serpent[0][serpent[1]-1][i] += serpent[3][i]

    if in_grid(tail,grid):
        grid[0][tail[0]][tail[1]] = 0

    for _ in range(serpent[1]):
        if serpent[0][_][1] > len(grid[0])-1:
            serpent[0][_][1] = 0
        if serpent[0][_][1] < 0:
            serpent[0][_][1] = 19

        if serpent[0][_][0] > len(grid[0])-1:
            serpent[0][_][0] = 0
        if serpent[0][_][0] < 0:
            serpent[0][_][0] = 19

    return serpent, grid

def increment_size(serpent):
    serpent[0].insert(0,[serpent[0][0][0],serpent[0][0][1] -1])
    serpent[1]+=1
    return serpent

def eat_appl(serpent,apple):
    for i in range(len(apple)):
        if apple[i][0] == serpent[0][serpent[1]-1] or apple[i][0] == serpent[0][0]:
            serpent=increment_size(serpent)
            apple[i][1] = False
    return serpent,apple


def in_grid(cords,grid):
    return 0 <= cords[1] <= len(grid[0])-1 

def thers_nothing(serpent,grid):
    return grid[0][serpent[0]][serpent[1]] == 0