#atributos = coordenadas, tamaño, color, avance
#conportamientos = mover, incrementar tamaño, obtener longitud

def crear_serpiente(color:int=1, avance:int=1):
    longitud=[[0,0],[0,1]]
    return (sorted(longitud),len(longitud),color,avance)

def move_serpent(stategame):
    for i in range(stategame[1]):
        stategame[0][i] = stategame[0][i][0],stategame[0][i][1]+stategame[3]
    return stategame

def increment_size(stategame):
    x,y=stategame[0][0]
    stategame.append(x,y-1)
    return stategame

def grilla():
    return [[0 for i in range(100)] for _ in range(1)]

def put_serpent(grid,stategame):
    for i in range(stategame[1]):
        grid[stategame[0][i][0]][stategame[0][i][1]]=1
    if serpiente[1]
    
    return grid
def main():
    grid=grilla()
    serpiente=crear_serpiente()
    i=0
    while True:
        grid=put_serpent(grid,serpiente)
        serpiente=move_serpent(serpiente)
        i+=1
        print(f"esta es la serpiente{serpiente} en ciclo {i}")
        for j in grid:
            print(j)
        
main()