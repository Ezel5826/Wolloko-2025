from copy import deepcopy as dp

class snake:
    def __init__(self,cordenadas:list,ancho,alto):
        self.cordenadas=cordenadas
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
            for i in range(len(self.cordenadas)-1):
                self.cordenadas[i] = dp(self.cordenadas[i+1])

            for i in range(2):
                self.cordenadas[len(self.cordenadas)-1][i] += self.sense[i]

            for x in range(len(self.cordenadas)):
                for y in range(len(self.cordenadas[0])):
                    if self.cordenadas[x][y] > self.alto-1:
                        self.cordenadas[x][y] = 0

                    if self.cordenadas[x][y] < 0:
                        self.cordenadas[x][y] = self.alto-1
        return

    def elegir_comandos(self,eleccion):
        self.comando_elegido = self.movimientos_L.get(eleccion)
    
    def elegir_tipo_serpent(self,tipo):
        self.tipe_serpent = tipo

    def cambiar_sentido(self,nueva_cord):
        self.sense=nueva_cord

    def eat_appl(self,apples):
        Bool,i=self.its_apple_on_snake(apples)
        if Bool:
            apples[i].reroll_coords(self,apples)
            self.dencrement_size(apples[i])

    def its_apple_on_snake(self,apples):
        i=0
        for apple in apples:
            if apple.coords in self.cordenadas:
                return True,i
            i+=1
        return False,i

    def dencrement_size(self,apple):
        increment=apple.increment_size
        if increment>=1:
            for i in range(increment):
                self.cordenadas.insert(0,[self.cordenadas[0][0]-self.sense[0], self.cordenadas[0][1]-self.sense[1]])
        else:
            self.cordenadas.pop(0)


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
         