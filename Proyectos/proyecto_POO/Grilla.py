ancho=20
alto=20
import apple as ap
import serpiente as sp
from random import randint as rn

def crear_grilla(ancho,alto,long_serp=1,cant_food=1)->list[list,int,int]:
    return [[[0 for _ in range(ancho)] for _ in range(alto)],long_serp,cant_food]

def put_serpent(grid,serpent):
    for i in range(serpent[1]):
        if in_grid(serpent[0][i],grid):
            if thers_nothing(serpent[0][i],grid):
                grid[0][serpent[0][i][0]][serpent[0][i][1]] = 1
    return grid

def put_apple(grid:list[list,int,int],apple:list[(int,int),bool,int]):
    for i in range(len(apple)):
        grid[0][apple[i][0][0]][apple[i][0][1]] = 3
    return grid

def in_grid(cords,grid):
    return 0 <= cords[1] <= len(grid[0])-1 

def thers_nothing(serpent,grid):
    return grid[0][serpent[0]][serpent[1]] == 0