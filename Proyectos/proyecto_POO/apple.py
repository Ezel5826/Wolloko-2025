from random import randint as rn
import Grilla
import serpiente

def apple(grid:list[list,int,int]) -> list[(int,int),bool,int]:
    state = True
    cords = [] 
    state_apple=[]
    feed_increment_size = 1
    j=0
    while grid[2]!=j:
        cords = [rn(0,Grilla.alto-1), rn(0,Grilla.ancho-1)]
        if not (grid[0][cords[0]][cords[1]] == 1):
            state_apple.append([cords,state,feed_increment_size])
            cords=[]
            j+=1
    return state_apple
    
def increment_apple(grid:list,increment:bool):
    if increment:
        grid[2]+=1
    else:
        if not grid[2]==1:
            grid[2]-=1
    return grid
    
def put_apple(grid:list[list,int,int],apple:list[(int,int),bool,int]):
    for i in range(grid[2]):
        grid[0][apple[i][0][0]][apple[i][0][1]] = 3
    return grid