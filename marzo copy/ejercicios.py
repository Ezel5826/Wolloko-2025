#conceptos importantes que debemos sabes - deberiamos saber.
#
#adecuacion de la ecuacion de un problema. 
#criterio de temas - dependiendo de los temas que nosotros tengamos para hacerlo va a depender de los ejercicios 
#programa computacional: un texto escrito en un formato formal, es lo que es una "aplicacion", producto inacabado. 
#con lo algoritmos escribimos programas
#algoritmos: estrategia de roslucion de un problema

#rutinas
#   procedimientos: hacen cosas 
#   funcion: devuelven valores #declaracion: nombre, paramtro, y tipo.
#funcion: hay que saber dos cosas:
#         return acepta una expresion - return n+n
#         composicion de de funcion   - return doble(doble(n))
#efecto lateral. ocurre sin ser el proposito. algo distinto ademas de lo que te pide.
#cuestión importante - al escribir el nombre de algo, tiene que ser compresible

#expresiones - valores.
#   2+2           1
#expresion para llegar a un valor - tipos: aritmetica(+, -), relacionales(<, >, <=, <=), logicas(or, and, not)
#se pueden usar funciones donde van expresiones.
#if exprecion booleana, espera una exprecion booleana. puede recibir expreciones relacionales y logicas.


#en principio que la grilla sea de valor opcional n*m y por otro lado, hay que ubicar c cantidad de elementros de manera aleatoria condiciones. dos elementos no pueden compartir ubicacion adyacente la cantidad de cosa para meter en el tablero tiene que ser menor al tablero.

lista=[(1,2),(5,6),(7,8)]
barco=((1,3),(3,6),(7,8))
print(barco in lista)
print((7,8) in lista)

for j in range(len(barco)):
    print(barco[j])
    if barco[j] in lista:
        print("esta")
        
    else:
        print("no esta")
        
print("fin")
