#atributos = coordenadas, tamaño, color, avance
#conportamientos = mover, incrementar tamaño, obtener longitud
from copy import deepcopy as dp

def grilla():
    return [[0 for i in range(20)] for _ in range(20)]

def crear_serpiente(color:int=1, sense:int=(0,0)):
    cordenadas=[[10,4],[10,5]]
    return [cordenadas,len(cordenadas),color,sense]

def move_serpent(serpent,grid):
    grid[3][1] = 3
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
def eat_appl(apple,serpent,grid):
    if apple[0]== serpent[0][1]-1:
        increment_size(serpent)

def in_grid(cords,grid):
    return 0 <= cords[1] <= len(grid[0])-1 

def thers_nothing(serpent,grid):
    return grid[serpent[0]][serpent[1]] == 0