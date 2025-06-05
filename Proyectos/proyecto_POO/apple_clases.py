from random import randint as rn
import serpiente_clases as snake
class apple:
    def __init__(self,alto,ancho):
        self.coords=[rn(0,ancho-1),rn(0,alto-1)]
        self.ancho=ancho
        self.alto=alto
        self.count_apples = 5
        self.feed_increment_size = 1
        self.type = "normal"
        self.state = True

    def reroll_coords(self,snake=0,apples=0):
        self.coords = [rn(0, self.ancho-1), rn(0, self.alto-1)]

manzanas=[]
a1=apple(15,15)
a2=apple(15,15)
a3=apple(15,15)
a4=apple(15,15)
a5=apple(15,15)
serpiente=snake.snake([10,10],a1.alto,a1.alto)
manzanas.append((a1,a2,a3,a4,a5))
print(manzanas)
i=0
flag=True
while flag:
    coords_nuevas=[10,10]
    print(coords_nuevas) if coords_nuevas==serpiente.cordenada else print()
    for manzana in manzanas[0]:
        if manzana.coords!=coords_nuevas and coords_nuevas!=serpiente.cordenada:
            print("yayyy")
            
        else:
            flag=False
    i+=1    
print(i)