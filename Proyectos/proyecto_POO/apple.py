from random import randint as rn
import serpiente
ancho=20
alto=20
def create_apple(count_apple=5,feed_increment_size = 1,tipe="normal",) -> list[(int,int),bool,int]:
    state = True
    cords = [] 
    state_apple=[]
    j=0
    while count_apple!=j:
        cords = [rn(0,alto-1), rn(0,ancho-1)]
        # if not repeatable_apple():
        state_apple.append([cords,state,feed_increment_size,tipe])
        cords=[]
        j+=1
    return state_apple
    
def increment_apple(increment:bool, apple):    
    if increment and len(apple) < 6:
        apple=add_apple(apple)
    if not (increment) and not len(apple) == 1:
            apple=pop_apple(apple,0)

    return apple

def check_state(apple:list):
    for i in range(len(apple)):
        if not all(apple[i]):
            apple=pop_apple(apple,i)
            apple=add_apple(apple)
    return apple

def pop_apple(apple,i):
    apple.pop(i)
    return apple

def add_apple(apple):
    apple.extend(create_apple(1))
    return apple

def repeatable_apple(apple,new_apple):
    return apple[0]==new_apple