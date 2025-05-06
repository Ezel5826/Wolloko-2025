#atributos = coordenadas, tamaño, color, avance
#conportamientos = mover, incrementar tamaño, obtener longitud

def crear_serpiente(color:int=1, avance:int=1):
    longitud=[[0,0],[0,1]]
    return [sorted(longitud,reverse=True),len(longitud),color,avance]

def move_serpent(stategame):
    for i in range(stategame[1]):
        stategame[0][i] = stategame[0][i][0],stategame[0][i][1]+stategame[3]
    return stategame

def increment_size(stategame):
    x,y=stategame[0][0]
    stategame.append(x,y-1)
    return stategame

def grilla():
    return [[0 for i in range(100)] for _ in range(2)]

def put_serpent(grid,serpent):
    print(serpent[0][0][1])
    if serpent[0][0][1] == len(grid)-1:
        serpent[0][0][0] + 1
        serpent[0][0][1] = 0

    for i in range(1,serpent[1]):
        grid[serpent[0][i][0]][serpent[0][i][1]]=1
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