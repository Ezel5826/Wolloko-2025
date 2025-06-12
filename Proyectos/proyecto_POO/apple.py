from random import randint as rn

ancho=15
alto=15
def create_apple(snake,count_apple=5,feed_increment_size = 1,tipe="normal",state=True,apple=[]) -> list[(int,int),bool,int]:
    state_apple=[]
    j=0
    while count_apple !=j:
        _new_apple = [rn(0,alto-1), rn(0,ancho-1)]
        if not len(apple)==0:
            if not (repeatable_apple(apple,_new_apple) or apple_in_snake(snake,_new_apple)):

                state_apple.append([_new_apple,state,feed_increment_size,tipe])
                j+=1
        else:
            state_apple.append([_new_apple,state,feed_increment_size,tipe])
            j+=1
        _new_apple=[]
        
    return state_apple
    
def increment_apple(increment:bool, apple):    
    if increment and len(apple) < 3:
        apple=add_apple(apple)
    if not (increment) and not len(apple) == 1:
            apple=pop_apple(apple,0)

    return apple

def check_state(apple:list,snake):
    for i in range(len(apple)):
        if not all(apple[i]):
            apple=pop_apple(apple,i)
            apple=add_apple(apple,snake)
    return apple

def pop_apple(apple,i):
    apple.pop(i)
    return apple

def add_apple(apple,snake):
    apple.extend(create_apple(snake, 1, feed_increment_size=1, tipe="normal", state=True, apple=apple))
    return apple

def repeatable_apple(apple,new_apple):
    for i in range(len(apple)):
        if apple[i][0]==new_apple:
            return True
    return False

def apple_in_snake(snake,new_apple):
    for i in range(len(snake[0])):
        if snake[0][i]==new_apple:
            return True
    return False


def convert_tipe_apple(apple):
    tipes=["gold","rotten"]

    actual_tipe=tipes[rn(0,len(tipes)-1)]
    print(actual_tipe)
    j=0
    print(tipos_disponibles(apple))
    if tipos_disponibles(apple):
        print(actual_tipe)
        while j==0:
            apple_choised=rn(0,len(apple)-1)
            print(apple,apple_choised)
            if actual_tipe=="gold" and (apple[apple_choised][3]=="normal" or apple[apple_choised][3]=="rotten"):
                apple[apple_choised][2] = 2
                apple[apple_choised][3]=actual_tipe
                print("soy gold")
                j+=1
            else:
                if actual_tipe=="rotten" and (apple[apple_choised][3]=="normal" or apple[apple_choised][3]=="gold"):
                    apple[apple_choised][2]= -1
                    apple[apple_choised][3]=actual_tipe
                    print("soy rotten")
                    j+=1
        apple[apple_choised][3]=actual_tipe
        print(apple)
    return apple


def tipos_disponibles(apple):
    j=0
    for i in range(len(apple)):
        if apple[i][3]=="gold" or apple[i][3]=="rotten":
            j+=1
    if j==len(apple):
        return False
    return True
