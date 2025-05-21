import pygame
import serpiente
import Grilla
import apple
import time as tm
valores=(600,700)
pygame.init()
screen = pygame.display.set_mode(valores,pygame.RESIZABLE)
clock = pygame.time.Clock()
d_Cubos=25

def grilla(grilla,dimensiones):
    alto_g = len(grilla[0])*d_Cubos
    ancho_g = len(grilla[0][0])*d_Cubos
    centrado = (dimensiones[0] - (alto_g))/2
    centrado_1 = (dimensiones[1] - (ancho_g))/2
    for alto in range(len(grilla[0])):
        for ancho in range(len(grilla[0][0])):
            x = alto*d_Cubos+centrado_1
            y = ancho*d_Cubos+centrado
            if grilla[0][alto][ancho] == 0:
                cubozz=pygame.Rect(y,x,d_Cubos,d_Cubos)
                pygame.draw.rect(screen,"violet",cubozz,100)
            elif grilla[0][alto][ancho] == 1:
                cubozz=pygame.Rect(y,x,d_Cubos,d_Cubos)
                pygame.draw.rect(screen,"green",cubozz,100)
            elif grilla[0][alto][ancho] == 3:
                cubozz=pygame.Rect(y,x,d_Cubos,d_Cubos)
                pygame.draw.rect(screen,"red",cubozz,100)

def mostrar_manzanas(apple,dim):
    cubozz=pygame.Rect(apple[0][0][0],apple[0][0][1],d_Cubos,d_Cubos)
    pygame.draw.rect(screen,"purple",cubozz,100)
def main():
    contador_habilidad=tm.perf_counter()
    Serpiente=serpiente.crear_serpiente()
    grilla_=Grilla.crear_grilla(Grilla.alto,Grilla.ancho,len(Serpiente),1)
    apple_=apple.create_apple(grilla_)
    
    running=True
    while running:
        counter_result=tm.perf_counter() - contador_habilidad
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                   

                    Serpiente[3] = (0,-1)#IZQUIERDA
                    
                    # Serpiente,grilla_ = serpiente.move_serpent(Serpiente,grilla_)
                if event.key == pygame.K_d:

                    Serpiente[3] = (0,1)#DERECHA
                    


                if event.key == pygame.K_s:

                    Serpiente[3] = (1,0)#ARRIBA

                    
                if event.key == pygame.K_w:

                    Serpiente[3] = (-1,0)#ABAJO

                    # Serpiente,grilla_=serpiente.move_serpent(Serpiente,grilla_)
           
                if event.key == pygame.K_4:
                    Serpiente=serpiente.increment_size(Serpiente)
                if event.key == pygame.K_1:
                    apple_=apple.increment_apple(True,apple_,grilla_)
                if event.key == pygame.K_2:
                    apple_=apple.increment_apple(False,apple_,grilla_)
        # print(counter_result)
        if counter_result > 10:
            # print("hii")
            apple_=apple.increment_apple(True,apple_,grilla_)
            contador_habilidad=tm.perf_counter()
        screen.fill("black")
        Cambios_dimensionales_pantalla = pygame.display.get_surface().get_size()
        mostrar_manzanas(apple,Cambios_dimensionales_pantalla)
        grilla(grilla_,Cambios_dimensionales_pantalla)
        Serpiente,grilla_=serpiente.move_serpent(Serpiente,grilla_)
        grilla_ = Grilla.put_serpent(grilla_,Serpiente) 
        grilla_ = Grilla.put_apple(grilla_,apple_)
        Serpiente,apple_=serpiente.eat_appl(Serpiente,apple_)
        apple_,grilla_ =apple.check_state(apple_,grilla_)
        pygame.display.flip()

        clock.tick(10)  

    pygame.quit()
main()