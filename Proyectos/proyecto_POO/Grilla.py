ancho=10
alto=10
import apple as ap
import serpiente as sp
from random import randint as rn

def crear_grilla(ancho,alto,long_serp=1,cant_food=1)->list[list,int,int]:
    return [[[0 for _ in range(ancho)] for _ in range(alto)],long_serp,cant_food]

def put_serpent(grid,serpent):
    print(serpent[0])
    for _ in range(serpent[1]):
        if serpent[0][_][1] > len(grid[0])-1:
            serpent[0][_][1] = 0
        if serpent[0][_][1] < 0:
            serpent[0][_][1] = 19
        if serpent[0][_][0] > len(grid[0])-1:
            serpent[0][_][0] = 0
    for i in range(serpent[1]):
        if in_grid(serpent[0][i],grid):
            if thers_nothing(serpent[0][i],grid):
                grid[serpent[0][i][0]][serpent[0][i][1]] = 1
    return grid,serpent
