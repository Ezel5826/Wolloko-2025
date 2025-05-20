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
    
    if not serpent[3] == (0,0):
        for i in range(serpent[1]):
            if i + 1 <= serpent[1]-1:
                serpent[0][i] = dp(serpent[0][i+1])

    for i in range(2):
        serpent[0][serpent[1]-1][i] += serpent[3][i]

    print(f"esta es la serpiente {serpent[0]}")
    
    if in_grid(tail,grid):
        if not serpent[1]==1:
            grid[0][tail[0]][tail[1]] = 0
        else:
            print(tail)
            print(serpent[3])
            grid[0][tail[0] - serpent[3][0]][tail[1] - serpent[3][1]] = 0

    for _ in range(serpent[1]):
        if serpent[0][_][1] == len(grid[0]):
            serpent[0][_][1] = 0
            break
        if serpent[0][_][1] == 0:
            serpent[0][_][1] = len(grid[0])-1
            break
        if serpent[0][_][0] == len(grid[0])-1:
            serpent[0][_][0] = 0
            break
        if serpent[0][_][0] == 0:
            serpent[0][_][0] = len(grid[0])-1
            break
    return serpent, grid

def dincrement_size(serpent,apple):
    if apple[2]>=1:
        for i in range(apple[2]):
            serpent[0].insert(0,[serpent[0][0][0],serpent[0][0][1] -1])
            serpent[1]+=1
    else:
        if not len(serpent[0])==1:
            for i in range(-2,apple[2]):
                serpent[0].pop(0)
                serpent[1]-=1
    return serpent


def eat_appl(serpent,apple):
    for i in range(len(apple)):
        if apple[i][0] == serpent[0][serpent[1]-1] or apple[i][0] == serpent[0][0]:
            print(serpent)
            apple[i][1] = False
            serpent=dincrement_size(serpent,apple[i])
    return serpent,apple


def in_grid(cords,grid):
    return 0 <= cords[1] <= len(grid[0])-1 and 0 <= cords[0] <= len(grid[0])-1 

def thers_nothing(serpent,grid):
    return grid[0][serpent[0]][serpent[1]] == 0