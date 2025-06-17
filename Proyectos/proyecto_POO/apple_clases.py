from random import randint as rn
class apple:
    def __init__(self,alto,ancho):
        self.coords=[rn(0,ancho-1),rn(0,alto-1)]
        self.ancho=ancho
        self.alto=alto
        self.feed_increment_size = 1
        self.actual_type = "normal"
        self.state = True
        self.available_tipes={
            "normal":[1,"Proyectos/proyecto_POO/images/manza_normal.png"],
            "gold":[2,"Proyectos/proyecto_POO/images/manzana_de_oro.png"],
            "rotten":[-1,"Proyectos/proyecto_POO/images/manzana_podrida.png"],
            "thunderbolt":[1,"Proyectos/proyecto_POO/images/imagen azul (1).png"]
            }


    def reroll_coords(self,snake,apples):
        while True:
            coords_nuevas=[rn(0, self.ancho-1), rn(0, self.alto-1)]
            if not self.apple_in_apples(apples,coords_nuevas) and not self.apple_in_snake(snake,coords_nuevas):
                self.coords = coords_nuevas
                break
    
    def apple_in_snake(self,snake,apple_):
        return apple_ in snake.coords
    
    def apple_in_apples(self,apples,new_apple):
        for apple_ in apples:
             if new_apple==apple_.coords:
                return True
        return False
    def change_apple_tipe(self):
        tipes=list(self.available_tipes.keys())
        print(tipes)
        while True:
            select_tipe=tipes[rn(0,len(tipes)-1)]
            if select_tipe!=self.actual_type:
                self.feed_increment_size=self.available_tipes.get(select_tipe)[0]
                self.actual_type=select_tipe
                break

    