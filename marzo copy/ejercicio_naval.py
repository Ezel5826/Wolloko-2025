#en principio que la grilla sea de valor opcional n*m y por otro lado, hay que ubicar c cantidad de elementros de manera aleatoria condiciones. dos elementos no pueden compartir ubicacion adyacente la cantidad de cosa para meter en el grilla tiene que ser menor al grilla.
from random import randint

ancho=10
alto=10
cantidad_barcos=[1,2,2,3,3,4]


def grilla_juego(alto,ancho):
    juego=[]
    for i in range(ancho):
        lista_aux=[]
        for j in range(alto):
            lista_aux.append(0)
        juego.append(lista_aux)
    return juego

def insertar_barco(barco,grilla:list):
    for i in range(len(barco)):
        grilla[barco[i][0]][barco[i][1]]=1
    return grilla

def crear_barcos_hor(long:list,cord_piv,grilla,lista):
    barco=[cord_piv]
    print(barco)
    for i in range(1,long):
        barco.append([cord_piv[0],cord_piv[1]+i])
    print("after",barco)
    print(f"esto es el barco {barco} dentro de crear barco")
    print(deteccion_limite(barco,grilla))
    if deteccion_limite(barco,grilla):
        lista=almacenar_barco(barco,lista,grilla)
        return barco,lista
    else:
        print(f"se reeleccionará el barco mediante la funcion reeleccion_barco")
        barco,lista=reeleccion_barco(lista,grilla,long,1)
        return barco,lista
    
def crear_barcos_vert(long,cord_piv,grilla,lista):
    barco=[cord_piv]
    print(barco)
    for i in range(1,long):
        barco.append([cord_piv[0]+i,cord_piv[1]])
    print("after",barco)
    print(f"esto es el barco {barco} dentro de crear barco")
    print(deteccion_limite(barco,grilla))
    if deteccion_limite(barco,grilla):
        lista=almacenar_barco(barco,lista,grilla)
        return barco,lista
    else:
        print(f"se reeleccionará el barco mediante la funcion reeleccion_barco")
        barco,lista=reeleccion_barco(lista,grilla,long)
        return barco,lista
    

def barco_con_sentido(long,cord_piv,grilla,lista, sent):
    long1=long[0]
    long.pop(0)
    if sent:
        return crear_barcos_hor(long1,cord_piv,grilla,lista)
    else:
        return crear_barcos_vert(long1,cord_piv,grilla,lista)

# def crear_barcos(cord_pivote,grilla,lista_barco):    
#     longitud=int(input("ingrese un numero entre 1-4"))
#     vert_hori=randint(0,1)
#     barco_testeo=[]
#     if 0 < longitud < 5:
#         if vert_hori:
#             for i in range(1,longitud):
#                 barco=barco_testeo.append(cord_pivote[1]+i)
#         else:
#             for j in range(1,longitud):
#                 barco=barco_testeo.append(cord_pivote[0]+j)
#         lista_barcos=almacenar_barco(barco,lista_barco,grilla)
#         if deteccion_limite(barco,grilla):        
#             return barco,lista_barco
#         else:
#             #barco,lista_barcos = reeleccion_barco(sentido_obtenido,grilla,lista_barco)
    
#             return barco,lista_barcos
#     else:
#         raise IndexError("se fue de rango")

def reeleccion_barco(lista_barcos,grilla,long,H_sen=0):
    j=0
    while True:
        if j > 100:
            print("se cumple?")
            return None,lista_barcos
        barco=[[randint(0,ancho-1),randint(0,alto-1)]]
        print("esto es el barco dentro de reeleccion_barco",barco)
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
            
def not_barco_in_lista(barco,lista):
    for i in range(len(barco)):
        if barco[i] in lista:
            return False
    return True

def deteccion_limite(barco,grilla):
    contador=0
    for i in range(len(barco)):
        x,y=coordenadas_barco([barco[i]])
        print(f"esto es la coordenada {x} {y} y e I {i}")
        if no_pasa_limite(x,y,grilla) and grilla_vacia(x,y,grilla):
            contador+=1
    if contador == len(barco):
        return True
    else:
        print("no se puede colocar el barco")
        return False

def almacenar_barco(barco:tuple,lista:list,grilla:list):
    x,y=coordenadas_barco(barco)
    for k in range(x-1,x+2):
        for l in range(y-1,y+2):
            if deteccion_limite([[k,l]],grilla):
                lista.append((k,l))
    return lista

def agregar_adyacentes(barco, grilla):
    print(f"este es el barco antes de entrar al for {barco}")
    for i in range(len(barco)):
        print(f"estas son sus cordenadas enviadas al for{barco[i]}")
        x,y=coordenadas_barco([barco[i]])
        for k in range(x-1,x+2):
            for l in range(y-1,y+2):
                if deteccion_limite([[k,l]],grilla):
                        grilla[k][l]=2
    return grilla

def enviar_disparos(disparo,grilla:list):
    x,y=coordenadas_disparo(disparo)
    if grilla_ocupada(x,y,grilla):
            grilla[x][y]=3

    else:
        print("No se ha tocado ningún barco. agua")
    return grilla

def elegir_disparo(lista:list):
    while True:
        disparo=(randint(0,ancho-1), randint(0,alto-1))
        if disparo_diferente(disparo,lista):
            return disparo

def disparo_diferente(disparo:tuple,lista_disparos:list):
    for i in range(len(lista_disparos)):
        if disparo==lista_disparos[i]:
            return False
    return True

def almacenar_disparos(disparo:tuple,grilla:list,lista_disparos:list):
    x,y=coordenadas_disparo(disparo)
    if grilla_ocupada(x,y,grilla):
        for k in range(x-1,x+2):
            for l in range(y-1,y+2):
                if no_pasa_limite(k,l,grilla) and not(grilla_ocupada(k,l,grilla)) and disparo_diferente((k,l),lista_disparos):
                        lista_disparos.append((k,l))
    else:
        lista_disparos.append((x,y))
    return lista_disparos
    
def coordenadas_barco(barco):
    return barco[0][0], barco[0][1]

def coordenadas_disparo(disparo):
    return disparo[0], disparo[1]

def grilla_vacia(x:int,y:int,grilla:list):
    return grilla[x][y]==0

def grilla_ocupada(x:int,y:int,grilla:list):
    return grilla[x][y]==1

def no_pasa_limite(x:int,y:int,grilla:list):
    return 0 <= x <= len(grilla[0])-1 and 0 <= y <= len(grilla)-1

def contador_barcos(grilla:list):
    contador=0
    for i in range(len(grilla[0])):
        for j in range(len(grilla)):
            if grilla[i][j]==1:
                contador+=1
    return contador


def limite_de_barcos(barcos:tuple,cantidad:int):
    return barcos==cantidad

def main():
    lista_ayuda=[]
    almacen_barcos=[]
    almacen_disparos=[]
    grilla=grilla_juego(alto,ancho)
    i=1
    contador=0
    contador_2=0
    barcos=int(input(f"ingrese un numero menor a {(((len(grilla)**2) //9) * 2)+2} "))
    barco=(randint(0,ancho-1), randint(0,alto-1))
    x_barco,y_barco=coordenadas_barco(barco)
    while True:
        print("loop",i)
        if grilla_vacia(x_barco,y_barco,grilla) and not (limite_de_barcos(barcos,contador_2)):
            almacen_barcos=almacenar_barco(barco,almacen_barcos,grilla)
            grilla=insertar_barco(grilla,barco)
            grilla=agregar_adyacentes(barco,grilla)
            x_barco,y_barco=coordenadas_barco(barco)
            contador_2+=1

        print(f"contador de barcos pocisionados {contador_2}")
        
        #print(f"¿es igual? {limite_de_barcos(barcos,contador_2)}")
        
        if limite_de_barcos(barcos,contador_2):
            
            disparo=elegir_disparo(almacen_disparos)
            print(f"disparo actual: {disparo}")
            x_disparo,y_disparo=coordenadas_disparo(disparo)
            grilla=enviar_disparos(x_disparo,y_disparo,grilla)
            almacen_disparos=almacenar_disparos(disparo,grilla,almacen_disparos)
            print(f"esto es la lista que contiene las coordenadas: {sorted(almacen_disparos)}")
            contador+=1
        i+=1
        for hola in grilla:
            print(hola)
            
        if contador_2 == contador_destruidos(grilla):
            break
    print("\n")
    print("----------------------------------\n")

    for hola in grilla:
        print(hola)


def main_2():
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
"se terminó"

#main()
main_2()