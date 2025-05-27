import pygame
import serpiente
import apple
import time as tm
valores=(1600,900)
ancho=15
alto=15
d_Cubos=50
time=0
pygame.init()
normal_apple = pygame.image.load("Proyectos/proyecto_POO/images/manza_normal.png")
gold_apple = pygame.image.load("Proyectos/proyecto_POO/images/manzana_de_oro.png")
rotten_apple=pygame.image.load("Proyectos/proyecto_POO/images/manzana_podrida.png")
serpent_body=pygame.image.load("Proyectos/proyecto_POO/images/snake_body.png")
serpent_head=pygame.image.load("Proyectos/proyecto_POO/images/snake_head.png")
screen = pygame.display.set_mode(valores,pygame.RESIZABLE)
clock = pygame.time.Clock()

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
           
def mostrar_serpent(serpent,dim,snake_body,snake_head,direccion):
    alto_g = alto*d_Cubos
    ancho_g = ancho*d_Cubos
    centrado = (dim[0] - (alto_g))/2
    centrado_1 = (dim[1] - (ancho_g))/2
    for _ in range(len(serpent[0])):
        x =serpent[0][_][0]*d_Cubos+centrado_1
        y =serpent[0][_][1]*d_Cubos+centrado
        if _==len(serpent[0])-1:
            snake_head= pygame.transform.scale(snake_head, (d_Cubos, d_Cubos))

            if direccion == (-1,0): #arriba
                snake_head = pygame.transform.rotate(snake_head,90)
                screen.blit(snake_head, (y,x)) 

            if direccion == (1,0): #abajo
                snake_head = pygame.transform.rotate(snake_head,-90)
                screen.blit(snake_head, (y,x)) 

            if direccion == (0,-1): #izquierda
                snake_head = pygame.transform.flip(snake_head, True, False)
                screen.blit(snake_head, (y,x)) 
            if direccion == (0,1): #izquierda
                snake_head = pygame.transform.rotate(snake_head, 0)
                screen.blit(snake_head, (y,x))
        else:
            snake_body= pygame.transform.scale(snake_body, (d_Cubos, d_Cubos))
            screen.blit(snake_body, (y,x))

def mostrar_manzanas(apple_, dim,normal_apple,gold_apple,rotten_apple):
    alto_g = alto * d_Cubos
    ancho_g = ancho * d_Cubos
    centrado = (dim[0] - alto_g) / 2
    centrado_1 = (dim[1] - ancho_g) / 2
    font = pygame.font.SysFont(None, 20)
    for i in range(len(apple_)):
        x = apple_[i][0][0] * d_Cubos + centrado_1
        y = apple_[i][0][1] * d_Cubos + centrado
        if apple_[i][3] == "normal":
            normal_apple= pygame.transform.scale(normal_apple, (d_Cubos, d_Cubos))
            screen.blit(normal_apple , (y,x))
        if apple_[i][3] == "gold":
            gold_apple= pygame.transform.scale(gold_apple, (d_Cubos, d_Cubos))
            screen.blit(gold_apple , (y,x))
        if apple_[i][3] == "rotten":
            rotten_apple= pygame.transform.scale(rotten_apple, (d_Cubos, d_Cubos))
            screen.blit(rotten_apple , (y,x))
        

def main():
    contador_habilidad=tm.perf_counter()
    Serpiente=serpiente.crear_serpiente()
    serpent_2=serpiente.crear_serpiente()
    apple_=apple.create_apple(Serpiente)
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


                if event.key ==pygame.K_LEFT:
                    serpent_2[3] = (0,-1)#IZQUIERDA
                                    
                if event.key ==pygame.K_RIGHT:
                    serpent_2[3] = (0,1)#DERECHA
                    
                if event.key ==pygame.K_DOWN:
                    serpent_2[3] = (1,0)#ARRIBA

                if event.key ==pygame.K_UP:
                    serpent_2[3] = (-1,0)#ABAJO
           
                # if event.key == pygame.K_4:
                #     Serpiente=serpiente.increment_size(Serpiente)

                # if event.key == pygame.K_1:
                #     apple_=apple.increment_apple(True,apple_)

                # if event.key == pygame.K_2:
                #     apple_=apple.increment_apple(False,apple_)
        print(Serpiente[1])

        if counter_result > 5:     
            apple.convert_tipe_apple(apple_)
            contador_habilidad=tm.perf_counter()
        screen.fill("black")

        Cambios_dimensionales_pantalla = pygame.display.get_surface().get_size()
        mostrar_grilla(Cambios_dimensionales_pantalla)
        mostrar_manzanas(apple_,Cambios_dimensionales_pantalla,normal_apple,gold_apple,rotten_apple)
        mostrar_serpent(Serpiente,Cambios_dimensionales_pantalla,serpent_body,serpent_head,Serpiente[3])
        mostrar_serpent(serpent_2,Cambios_dimensionales_pantalla,serpent_body,serpent_head,Serpiente[3])
        Serpiente=serpiente.move_serpent(Serpiente)
        serpent_2=serpiente.move_serpent(serpent_2)
        Serpiente,apple_=serpiente.eat_appl(Serpiente,apple_)
        serpent_2,apple_=serpiente.eat_appl(serpent_2,apple_)
        apple_ =apple.check_state(apple_,Serpiente)
        apple_ =apple.check_state(apple_,serpent_2)
        pygame.display.flip()

        clock.tick(10)  

    pygame.quit()
main()