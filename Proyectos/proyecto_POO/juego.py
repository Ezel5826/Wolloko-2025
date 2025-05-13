import pygame
import serpiente
valores=(600,700)
pygame.init()
screen = pygame.display.set_mode(valores,pygame.RESIZABLE)
clock = pygame.time.Clock()
d_Cubos=10

def grilla(grilla,dimensiones):
    alto_g = len(grilla)*d_Cubos
    ancho_g = len(grilla[0])*d_Cubos
    centrado = (dimensiones[0] - (alto_g))/2
    centrado_1 = ( dimensiones[1] - (ancho_g))/2
    for alto in range(len(grilla)):
        for ancho in range(len(grilla[0])):
            y = alto*d_Cubos+centrado_1
            x = ancho*d_Cubos+centrado
            if grilla[alto][ancho] == 0:
                cubozz=pygame.Rect(x,y,d_Cubos,d_Cubos)
                pygame.draw.rect(screen,"violet",cubozz,100)
            elif grilla[alto][ancho] == 1:
                cubozz=pygame.Rect(x,y,d_Cubos,d_Cubos)
                pygame.draw.rect(screen,"green",cubozz,100)
def main():
    Serpiente=serpiente.crear_serpiente()
    grilla_=serpiente.grilla()
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_4:
                    Serpiente=serpiente.increment_size(Serpiente)

        screen.fill("black")
        Cambios_dimensionales_pantalla = pygame.display.get_surface().get_size()
        grilla(grilla_,Cambios_dimensionales_pantalla)
        Serpiente,grilla_=serpiente.move_serpent(Serpiente,grilla_)
        grilla_,Serpiente=serpiente.put_serpent(grilla_,Serpiente) 
        pygame.display.flip()

        clock.tick(10)  

    pygame.quit()
main()