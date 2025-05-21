from random import randint as rn
import Grilla
import serpiente

def create_apple(grid:list[list,int,int], count_apple=5) -> list[(int,int),bool,int]:
    state = True
    cords = [] 
    state_apple=[]
    feed_increment_size = -1
    tipe="normal"
    j=0
    while count_apple!=j:
        cords = [rn(0,Grilla.alto-1), rn(0,Grilla.ancho-1)]
        if not (grid[0][cords[0]][cords[1]] == 1):
            state_apple.append([cords,state,feed_increment_size,tipe])
            cords=[]
            j+=1
    return state_apple
    
def increment_apple(increment:bool, apple, grid):    
    if increment and len(apple) < 5:
        apple=add_apple(apple,grid)

    if not (increment) and len(apple) > 1:
            grid[0][apple[0][0][0]][apple[0][0][1]] = 0
            apple=pop_apple(apple,0)

    return apple

def check_state(apple:list,grid):
    for i in range(len(apple)):
        if not all(apple[i]):
            grid[0][apple[i][0][0]][apple[i][0][1]] = 0
            apple=pop_apple(apple,i)
            apple=add_apple(apple,grid)
    return apple,grid

def pop_apple(apple,i):
    apple.pop(i)
    return apple

def add_apple(apple,grid):
    apple.extend(create_apple(grid,1))
    return apple