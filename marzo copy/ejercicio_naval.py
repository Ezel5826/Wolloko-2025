#en principio que la grilla sea de valor opcional n*m y por otro lado, hay que ubicar c cantidad de elementros de manera aleatoria condiciones. dos elementos no pueden compartir ubicacion adyacente la cantidad de cosa para meter en el grilla tiene que ser menor al grilla.
from random import randint

ancho=10
alto=10
cantidad_barcos=[1,2,2,3,3,4]

def grilla_juego(alto:int,ancho:int)-> list:
    """crear y devuelve la grilla del juego"""
    
    juego=[]
    for i in range(ancho):
        lista_aux=[]
        for j in range(alto):
            lista_aux.append(0)
        juego.append(lista_aux)
    return juego

def insertar_barco(barco:list[list[int]],grilla:list) -> list[list[int]]:
    """inserta el barco en la grilla y devuelve la grilla modificada"""
    for i in range(len(barco)):
        grilla[barco[i][0]][barco[i][1]]=1
    return grilla

def crear_barcos_hor(long:list,cord_piv:tuple[int],grilla:list,lista:list)-> list[list[int]]:
    """crea barcos de manera horizontal y añade sus cordenadas en una lista"""
    barco=[cord_piv]
    for i in range(1,long):
        barco.append([cord_piv[0],cord_piv[1]+i])
    if deteccion_limite(barco,grilla):
        lista=almacenar_barco(barco,lista,grilla)
        return barco,lista
    else:
        barco,lista=reeleccion_barco(lista,grilla,long,1)
        return barco,lista
    
def crear_barcos_vert(long:int,cord_piv:tuple[int],grilla:list,lista:list)-> list[list[int]] | list[int]:
    """crea barcos de manera horizontal y añade sus cordenadas en una lista"""
    barco=[cord_piv]
    for i in range(1,long):
        barco.append([cord_piv[0]+i,cord_piv[1]])
    if deteccion_limite(barco,grilla):
        lista=almacenar_barco(barco,lista,grilla)
        return barco,lista
    else:
        barco,lista=reeleccion_barco(lista,grilla,long)
        return barco,lista
    
def barco_con_sentido(long:int,cord_piv:tuple[int],grilla:list,lista:list, sent:int)-> list[list[int]] | list[int]:
    """elige la forma de crear el barco, horizontal o vertical y devuelve el barco creado"""
    long1=long[0]
    long.pop(0)
    if sent:
        return crear_barcos_hor(long1,cord_piv,grilla,lista)
    else:
        return crear_barcos_vert(long1,cord_piv,grilla,lista)

def reeleccion_barco(lista_barcos:list[int],grilla:list,long:int,H_sen:int=0)-> list[list[int]] | list[int]:
    """reelige la forma de crear el barco, horizontal o vertical y devuelve el barco creado"""
    j=0
    while True:
        if j > 100:
            return None,lista_barcos
        barco=[[randint(0,ancho-1),randint(0,alto-1)]]
        x,y=coordenadas_barco(barco)
        for i in range(1,long):
            if H_sen:
                barco.append([ x, y + i])
            else:
                barco.append([ x + i, y ])      
        if deteccion_limite(barco,grilla) and not_barco_in_lista(barco,lista_barcos):
            lista_barcos=almacenar_barco(barco,lista_barcos,grilla)
            return barco,lista_barcos
        j+=1
            
def not_barco_in_lista(barco:list[list[list]],lista:list)->bool:
    """verifica si el barco no se encuentra en la lista de barcos"""
    for i in range(len(barco)):
        if barco[i] in lista:
            return False
    return True

def almacenar_barco(barco:tuple,lista:list,grilla:list)->list:
    """almacena el barco en la lista de barcos"""
    x,y=coordenadas_barco(barco)
    for k in range(x-1,x+2):
        for l in range(y-1,y+2):
            if deteccion_limite([[k,l]],grilla):
                lista.append((k,l))
    return lista


def agregar_adyacentes(barco:list[list[int]], grilla:list)->list:
    """agrega las coordenadas adyacentes a la grilla"""
    for i in range(len(barco)):
        x,y=coordenadas_barco([barco[i]])
        for k in range(x-1,x+2):
            for l in range(y-1,y+2):
                if deteccion_limite([[k,l]],grilla):
                        grilla[k][l]=2
    return grilla


# funciones relacionadas con el disparo
def elegir_disparo(lista:list):
    """elige un disparo aleatorio y verifica que no se repita"""
    while True:
        disparo=(randint(0,ancho-1), randint(0,alto-1))
        if disparo_diferente(disparo,lista):
            return disparo

def enviar_disparos(disparo:tuple[int],grilla:list)->list:
    """envia el disparo y devuelve la grilla modificada"""
    x,y=coordenadas_disparo(disparo)
    if grilla_ocupada(x,y,grilla):
            grilla[x][y]=3
    else:
        return grilla

def disparo_diferente(disparo:tuple,lista_disparos:list)->bool:
    """verifica que el disparo no se repita"""
    for i in range(len(lista_disparos)):
        if disparo==lista_disparos[i]:
            return False
    return True

def almacenar_disparos(disparo:tuple,grilla:list,lista_disparos:list)->list[int]:
    """almacena los disparos en una lista"""
    x,y=coordenadas_disparo(disparo)
    if grilla_ocupada(x,y,grilla):
        for k in range(x-1,x+2):
            for l in range(y-1,y+2):
                if no_pasa_limite(k,l,grilla) and not(grilla_ocupada(k,l,grilla)) and disparo_diferente((k,l),lista_disparos):
                        lista_disparos.append((k,l))
    else:
        lista_disparos.append((x,y))
    return lista_disparos
    
def deteccion_limite(barco:list[list[int]],grilla:list)->bool:
    """verifica si el barco no se pasa del limite de la grilla y si la  grilla en las cordenadas del barco está vacia"""
    contador=0
    for i in range(len(barco)):
        x,y=coordenadas_barco([barco[i]])
        if no_pasa_limite(x,y,grilla) and grilla_vacia(x,y,grilla):
            contador+=1
    if contador == len(barco):
        return True
    else:
        return False
    
def coordenadas_barco(barco:list[list[int]])->tuple[int,int]:
    """devuelve las coordenadas del barco"""
    return barco[0][0], barco[0][1]

def coordenadas_disparo(disparo:list[list[int]])->tuple[int,int]:
    """devuelve las coordenadas del disparo"""
    return disparo[0], disparo[1]

def grilla_vacia(x:int,y:int,grilla:list)->bool:
    """verifica si la grilla está vacia"""
    return grilla[x][y]==0

def grilla_ocupada(x:int,y:int,grilla:list)->bool:
    """verifica si la grilla está ocupada"""
    return grilla[x][y]==1

def no_pasa_limite(x:int,y:int,grilla:list)->bool:
    """verifica si el barco no se pasa del limite de la grilla"""
    return 0 <= x <= len(grilla[0])-1 and 0 <= y <= len(grilla)-1

def contador_barcos(grilla:list):
    """cuenta la cantidad de barcos en la grilla"""
    contador=0
    for i in range(len(grilla[0])):
        for j in range(len(grilla)):
            if grilla[i][j]==1:
                contador+=1
    return contador

def limite_de_barcos(barcos:tuple,cantidad:int)->bool:
    """verifica si se ha alcanzado el limite de barcos"""
    return barcos==cantidad


def main():
    grilla=grilla_juego(alto,ancho)
    lista_cord_barcos=[]
    lista_cord_disp=[]
    cantidad=0
    esperados=len(cantidad_barcos)
    none=True
    while True:
        if  not (limite_de_barcos(cantidad,esperados)) and none:
            barco,lista_cord_barcos=barco_con_sentido(cantidad_barcos,[9,9],grilla,lista_cord_barcos,randint(0,1))
            if barco==None:
                none=False
                continue
            grilla=insertar_barco(barco,grilla)
            grilla=agregar_adyacentes(barco,grilla)
            cantidad+=1
            
        else:
            disparo=elegir_disparo(lista_cord_disp)
            grilla=enviar_disparos(disparo,grilla)
            lista_cord_disp=almacenar_disparos(disparo,grilla,lista_cord_disp)
        
        for file in  grilla:
            print(file)
        print("\n")
        if contador_barcos(grilla)==0:
            return

main()