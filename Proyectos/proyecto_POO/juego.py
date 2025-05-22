import pygame
import serpiente
import apple
import time as tm
valores=(600,700)
ancho=20
alto=20

pygame.init()
screen = pygame.display.set_mode(valores,pygame.RESIZABLE)
clock = pygame.time.Clock()
d_Cubos=25

def mostrar_grilla(dimensiones):
    alto_g = alto*d_Cubos
    ancho_g = ancho*d_Cubos
    centrado = (dimensiones[0] - (alto_g))/2
    centrado_1 = (dimensiones[1] - (ancho_g))/2
    for alto_ in range(alto):
        for ancho_ in range(ancho):
            x = alto_*d_Cubos+centrado_1
            y = ancho_*d_Cubos+centrado
            cubozz=pygame.Rect(y,x,d_Cubos,d_Cubos)
            pygame.draw.rect(screen,"violet",cubozz,100)
                
def mostrar_serpent(serpent,dim):
    alto_g = alto*d_Cubos
    ancho_g = ancho*d_Cubos
    centrado = (dim[0] - (alto_g))/2
    centrado_1 = (dim[1] - (ancho_g))/2
    for _ in range(len(serpent[0])):
        serpent_x =serpent[0][_][0]*d_Cubos+centrado_1
        serpent_y =serpent[0][_][1]*d_Cubos+centrado
        cubozz=pygame.Rect(serpent_y,serpent_x,d_Cubos,d_Cubos)
        pygame.draw.rect(screen,"green",cubozz,100)

def mostrar_manzanas(apple_,dim):
    alto_g = alto*d_Cubos
    ancho_g = ancho*d_Cubos
    centrado = (dim[0] - (alto_g))/2
    centrado_1 = (dim[1] - (ancho_g))/2
    for _ in range(len(apple_)):
        apple_x=apple_[_][0][0]*d_Cubos+centrado_1
        apple_y=apple_[_][0][1]*d_Cubos+centrado
        print(apple_)
        if apple_[_][3] == "normal":
            cubozz=pygame.Rect(apple_y,apple_x,d_Cubos,d_Cubos)
            pygame.draw.rect(screen,"red",cubozz,100)
def main():
    contador_habilidad=tm.perf_counter()
    Serpiente=serpiente.crear_serpiente()
    apple_=apple.create_apple()
    running=True
    while running:
        counter_result=tm.perf_counter() - contador_habilidad
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_a:
                    Serpiente[3] = (0,-1)#IZQUIERDA
                    
                if event.key == pygame.K_d:
                    Serpiente[3] = (0,1)#DERECHA
                    
                if event.key == pygame.K_s:
                    Serpiente[3] = (1,0)#ARRIBA

                if event.key == pygame.K_w:
                    Serpiente[3] = (-1,0)#ABAJO
           
                if event.key == pygame.K_4:
                    Serpiente=serpiente.increment_size(Serpiente)

                if event.key == pygame.K_1:
                    apple_=apple.increment_apple(True,apple_,grilla_)

                if event.key == pygame.K_2:
                    apple_=apple.increment_apple(False,apple_,grilla_)

        # print(counter_result)
        if counter_result > 10:
            # print("hii")
            apple_=apple.increment_apple(True,apple_)
            contador_habilidad=tm.perf_counter()
        screen.fill("black")
        Cambios_dimensionales_pantalla = pygame.display.get_surface().get_size()
        mostrar_grilla(Cambios_dimensionales_pantalla)
        mostrar_manzanas(apple_,Cambios_dimensionales_pantalla)
        mostrar_serpent(Serpiente,Cambios_dimensionales_pantalla)
        Serpiente=serpiente.move_serpent(Serpiente)
        Serpiente,apple_=serpiente.eat_appl(Serpiente,apple_)
        apple_ =apple.check_state(apple_)
        pygame.display.flip()

        clock.tick(10)  

    pygame.quit()
main()