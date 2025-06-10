from random import randint as rn
class apple:
    def __init__(self,alto,ancho):
        self.coords=[rn(0,ancho-1),rn(0,alto-1)]
        self.ancho=ancho
        self.alto=alto
        self.feed_increment_size = 1
        self.type = "normal"
        self.state = True

    def reroll_coords(self,snake,apples):
        while True:
            coords_nuevas=[rn(0, self.ancho-1), rn(0, self.alto-1)]
            if not self.apple_in_apples(apples,coords_nuevas) and not self.apple_in_snake(snake,coords_nuevas):
                self.coords = coords_nuevas
                break
    
    def apple_in_snake(self,snake,apple_):
        return apple_ in snake
    
    def apple_in_apples(self,apples,new_apple):
        for apple_ in apples:
             if new_apple==apple_.coords:
                return True
        return False