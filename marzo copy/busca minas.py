from random import randrange

ancho=9
alto=14
def grilla(ancho,alto):
    grilla=[]
    for i in range(alto):
        lista_aux=[]
        for j in range(ancho):
           lista_aux.append(0)
        grilla.append(lista_aux)
    return grilla 

def minas(cord_mina,grilla):
    x,y=coord_mina(cord_mina)
    grilla[y][x]=1
    return grilla

def coord_mina(mina):
    return mina[0],mina[1]

def paso_limite(grilla,mina):
    x,y=coord_mina(mina)
    return 0 < x < grilla[0] and 0 < y < grilla
dic={
    "hola":(10,10),
    15:"hola",
}
saber=dic.get("hola")
comida=saber[0]+5
print(comida)
print(saber)

hola=[3,4]
pepe=[1,1]
print(hola[0]+pepe[0])