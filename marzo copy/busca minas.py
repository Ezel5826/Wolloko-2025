from random import randrange

ancho=8
alto=10
minas=7
def crear_grilla(ancho,alto):
    grilla=[]
    for i in range(alto):
        lista_aux=[]
        for j in range(ancho):
           lista_aux.append(0)
        grilla.append(lista_aux)
    return grilla 

def colocar_minas(cord_mina,grilla):
    x,y=coord_mina(cord_mina)
    grilla[y][x]=5
    return grilla
def comprobar_repetidas(lista_minas,mina):
    for i in range(len(lista_minas)):
        if lista_minas[i] == mina:
            mina=cambiar_repetidas(lista_minas,mina)

def cambiar_repetidas(lista_minas,mina):
    while True:
        mina=[randrange(0,ancho),randrange(0,alto)]
        if mina not in lista_minas:
            return mina,lista_minas
def coord_mina(mina):
    return mina[0],mina[1]

def paso_limite(grilla,mina):
    x,y=coord_mina(mina)
    return 0 < x < len(grilla[0]) and 0 < y < len(grilla)

def main():
    while True:
        grilla= crear_grilla(ancho,alto)
        lista_minas=[]
        for i in range(minas):
            mina=[randrange(0,ancho),randrange(0,alto)]
            if paso_limite(grilla,mina) and mina not in lista_minas:
                lista_minas.append(mina)
                grilla=colocar_minas(mina,grilla)
        for columnas in grilla:
            print(columnas)
        print(lista_minas)
        break
main()