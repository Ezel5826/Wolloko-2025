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
    if not serpent[3]== (0,0):
        for i in range(serpent[1]):
            if i + 1 <= serpent[1]-1:
                serpent[0][i] = dp(serpent[0][i+1])

    for i in range(2):
        serpent[0][serpent[1]-1][i] += serpent[3][i]

    if in_grid(tail,grid):
        grid[tail[0]][tail[1]] = 0

    return serpent, grid

def increment_size(serpent):
    print(serpent[0])   
    serpent[0].insert(0,[serpent[0][0][0],serpent[0][0][1] -1])
    print(serpent[0])
    serpent[1]+=1
    print(serpent[1])
    return serpent


def eat_appl(serpent,grid,apple):
    print(apple)
    if apple == serpent[0][serpent[1]-1]:
        serpent=increment_size(serpent)
        grid[apple[0]][apple[1]] = 0
    return grid,serpent


def in_grid(cords,grid):
    return 0 <= cords[1] <= len(grid[0])-1 

def thers_nothing(serpent,grid):
    return grid[serpent[0]][serpent[1]] == 0