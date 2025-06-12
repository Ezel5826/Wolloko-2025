from copy import deepcopy as dp
from random import randint as rn
class snake:
    def __init__(self,ancho,alto):
        self.coords=[[4,4],[4,5]]
        self.sense=(0,0)
        self.ancho=ancho
        self.alto=alto 
        self.movimientos_L={
            "p1": {
                97: (0, -1),
                100: (0, 1),
                115: (1, 0),
                119: (-1, 0)
            },
            "p2": {
                1073741904: (0, -1),
                1073741903: (0, 1),
                1073741905: (1, 0),
                1073741906: (-1, 0)
            }
        }
        
    def mover(self):
        if not self.sense == (0,0):
            for i in range(len(self.coords)-1):
                self.coords[i] = dp(self.coords[i+1])

            for i in range(2):
                self.coords[len(self.coords)-1][i] += self.sense[i]

            for x in range(len(self.coords)):
                for y in range(len(self.coords[0])):
                    if self.coords[x][y] > self.alto-1:
                        self.coords[x][y] = 0

                    if self.coords[x][y] < 0:
                        self.coords[x][y] = self.alto-1
        return

    def elegir_comandos(self,eleccion):
        print(eleccion)
        self.comando_elegido = self.movimientos_L.get(eleccion)
    
    def elegir_tipo_serpent(self,tipo):
        self.tipe_serpent = tipo

    def cambiar_sentido(self,nueva_cord):
        self.sense=nueva_cord

    def eat_appl(self,apples):
        Bool,i=self.its_apple_on_snake(apples)
        if Bool:
            print(i)
            apples[i].reroll_coords(self,apples)
            self.dencrement_size(apples[i])

    def its_apple_on_snake(self,apples):
        i=0
        for apple in apples:
            if apple.coords in self.coords:
                return True,i
            i+=1
        return False,i

    def dencrement_size(self,apple):
        increment=apple.feed_increment_size
        if increment>=1:
            for i in range(increment):
                self.coords.insert(0,[self.coords[0][0]-self.sense[0], self.coords[0][1]-self.sense[1]])
        else:
            self.coords.pop(0)


        # pruebas
        
        # s=snake([[10,11],[10,12]],15,15)
        # for i in range(5):
        #     print(s.sense)
        #     s.cambiar_sentido((0,1))
        #     print(s.sense)
        #     print(s.cordenada,"antes")
        #     s.mover()
        #     print(s.cordenada,"despues")

        # PARA AÑADIR
        # if event.type == pygame.KEYDOWN:
        # for comando in s.comando_elegido:
        #     if event.key == pygame.comando:
        #         s.cambiar_sentido(s.comando_elegido.get(comando))

        # hay que usar dos for que cada uno itere en cada elemento, el elemento 1 y 2. con el for voy a preguntar que sea ==19 o ==0, para cada uno de los casos voy a tocar los elementos respectivos de cada ciclo, por ejemplo, si es 
         