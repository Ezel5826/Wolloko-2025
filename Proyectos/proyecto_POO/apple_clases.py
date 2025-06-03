from random import randint as rn
class apple:
    def __init__(self,alto,ancho):
        self.coords=[rn(0,ancho-1),rn(0,alto-1)]
        self.ancho=ancho
        self.alto=alto
        self.init_count_apples = 5
        self.feed_increment_size = 1
        self.type = "normal"
        self.state = True
        self.names = {}

    def increment_apple(self,increment:bool,apples):    
        if increment and len(apples) < 3:
            apples=self.add_apple(apples)
        if not (increment) and not len(apples) == 1:
                apples.pop(apples[rn(0,len(apples))])
        return apples
    
    def pop_apple(apple:object):
        del apple
    
    def add_apple(names):
        while True:
            #  objet-pool
            pass
              
         
