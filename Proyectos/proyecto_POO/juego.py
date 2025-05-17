import pygame
import serpiente
import Grilla
import apple
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

def main():
    Serpiente=serpiente.crear_serpiente()
    grilla_=Grilla.crear_grilla(Grilla.alto,Grilla.ancho,len(Serpiente),1)
    # print(grilla_)
    # print(Serpiente)
    apple_=apple.create_apple(grilla_)
    print(apple_)
    running=True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    print(f"antes del desastre {Serpiente[3]}")

                    Serpiente[3] = (0,-1)#IZQUIERDA
                    
                    print(f"despues del desastre {Serpiente[3]}")
                    # Serpiente,grilla_ = serpiente.move_serpent(Serpiente,grilla_)
                if event.key == pygame.K_d:
                    print(f"antes del desastre {Serpiente[3]}")

                    Serpiente[3] = (0,1)#DERECHA
                    
                    print(f"despues del desastre {Serpiente[3]}")


                if event.key == pygame.K_s:
                    print(f"antes del desastre {Serpiente[3]}")

                    Serpiente[3] = (1,0)#ARRIBA

                    print(f"despues del desastre {Serpiente[3]}")
                    
                if event.key == pygame.K_w:
                    print(f"antes del desastre {Serpiente[3]}")

                    Serpiente[3] = (-1,0)#ABAJO

                    print(f"despues del desastre {Serpiente[3]}")
                    # Serpiente,grilla_=serpiente.move_serpent(Serpiente,grilla_)
           
                if event.key == pygame.K_4:
                    Serpiente=serpiente.increment_size(Serpiente)
                if event.key == pygame.K_1:
                    print(f"la manzana antes de añadirse {apple_}")
                    apple_=apple.increment_apple(True,apple_,grilla_)
                    print(f"la manzana despeus de añadirse {apple_}")
                if event.key == pygame.K_2:
                    apple_=apple.increment_apple(False,apple_,grilla_)
        screen.fill("black")
        Cambios_dimensionales_pantalla = pygame.display.get_surface().get_size()
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