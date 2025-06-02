from copy import deepcopy as dp
class snake:
    def __init__(self,cordenadas,color,ancho,alto):
        self.cordenada=cordenadas
        self.color=color
        self.sense=(0,0)
        self.ancho=ancho
        self.alto=alto 
        self.movimientos_L={
            "p1": {
                "K_a": (0, -1),
                "K_d": (0, 1),
                "K_s": (1, 0),
                "K_w": (-1, 0)
            },
            "p2": {
                "K_LEFT": (0, -1),
                "K_RIGHT": (0, 1),
                "K_DOWN": (1, 0),
                "K_UP": (-1, 0)
            }
        }

    def mover(self):
        if not self.sense == (0,0):
            for i in range(len(self.cordenada)):
                if i + 1 <= len(self.cordenada)-1:
                    self.cordenada[i] = dp(self.cordenada[i+1])

            for i in range(2):
                self.cordenada[len(self.cordenada)-1][i] += self.sense[i]

            for x in range(len(self.cordenada)):
                for y in range(len(self.cordenada[0])):
                    if self.cordenada[x][y] > self.alto-1:
                        self.cordenada[x][y] = 0

                    if self.cordenada[x][y] < 0:
                        self.cordenada[x][y] = self.alto-1

    def elegir_comandos(self,eleccion):
        self.comando_elegido = self.movimientos_L.get(eleccion)

    def cambiar_sentido(self,nueva_cord):
        self.sense=nueva_cord

    def eat_appl(self,apple):
        for i in range(len(apple.cantidad)):
            if apple.cantidad[i][0] == self.cordenada[len(self.cordenada)-1]:
                apple.state = False
                self.dencrement_size(apple.cantidad[i])

    def dencrement_size(self,apple):

        if apple.increment_size>=1:
            for i in range(apple[2]):
                self.cordenada[0].insert(0,[self.cordenada[0][0][0]-self.sense[0], self.cordenada[0][0][1]-self.sense[1]])
        else:
            if not len(self.cordenada) == 2:
                for i in range(-2,apple[2]):
                    self.cordenada[0].pop(0)
                    self.cordenada[1]-=1
 


s=snake([[10,11],[10,12]],"red",15,15)

for i in range(3):
    print(s.sense)
    s.cambiar_sentido(input("ingrese una tupla"))
    print(s.sense)
    print(s.cordenada,"antes")
    s.mover()
    print(s.cordenada,"despues")


        # PARA AÑADIR
        # if event.type == pygame.KEYDOWN:
        # for comando in s.comando_elegido:
        #     if event.key == pygame.comando:
        #         s.cambiar_sentido(s.comando_elegido.get(comando))

        # hay que usar dos for que cada uno itere en cada elemento, el elemento 1 y 2. con el for voy a preguntar que sea ==19 o ==0, para cada uno de los casos voy a tocar los elementos respectivos de cada ciclo, por ejemplo, si es 
         