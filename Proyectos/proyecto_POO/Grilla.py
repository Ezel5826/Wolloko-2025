ancho=10
alto=10
from random import randint as rn
def grilla(ancho,alto,long_serp=1,cant_food=1)->list[list,int,int]:
    return [[[0 for _ in range(ancho)] for _ in range(alto)],long_serp,cant_food]

def increment_apple(grid:list,increment:bool):
    
    if increment:
        grid[2]+=1
    else:
        if not grid[2]==1:
            grid[2]-=1
    return grid

def apple(grid:list[list,int,int]) -> list[(int,int),bool,int]:
    state = True
    cords = [] 
    state_apple=[]
    feed_increment_size = 1
    j=0
    while grid[2]!=j:
        cords = [rn(0,alto-1), rn(0,alto-1)]
        if not (grid[0][cords[0]][cords[1]] == 1):
            state_apple.append([cords,state,feed_increment_size])
            cords=[]
            j+=1
    return state_apple
    
def put_apple(grid:list[list,int,int],apple:list[(int,int),bool,int]):
    for i in range(grid[2]):
        grid[0][apple[i][0][0]][apple[i][0][1]] = 3
    return grid

def cambiar_tamaño(N_ancho,N_alto):
    global ancho, alto
    ancho = N_ancho
    alto = N_alto
    return ancho,alto

grid=grilla(ancho,alto)
grid=increment_apple(grid,True)
apple_=apple(grid)
grid=put_apple(grid,apple_)
for hola in grid[0]:
    print(hola)
