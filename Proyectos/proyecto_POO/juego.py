import pygame
import serpiente
import apple
import time as tm
valores=(600,700)
ancho=20
alto=20
d_Cubos=30

pygame.init()
normal_apple = pygame.image.load("Proyectos/proyecto_POO/images/manza_normal.png")
gold_apple = pygame.image.load("Proyectos/proyecto_POO/images/manzana_de_oro.png")
rotten_apple=pygame.image.load("Proyectos/proyecto_POO/images/manzana_podrida.png")
serpent=pygame.image.load("Proyectos/proyecto_POO/images/serpiente-removebg-preview.png")
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
            if ancho_%2==0 and alto_%2==0:           
                cubozz=pygame.Rect(y,x,d_Cubos,d_Cubos)
                pygame.draw.rect(screen,"violet",cubozz,100)
            else:
                cubozz=pygame.Rect(y,x,d_Cubos,d_Cubos)
                pygame.draw.rect(screen,"violet",cubozz,100)

                
def mostrar_serpent(serpent,dim,snake):
    alto_g = alto*d_Cubos
    ancho_g = ancho*d_Cubos
    centrado = (dim[0] - (alto_g))/2
    centrado_1 = (dim[1] - (ancho_g))/2
    for _ in range(len(serpent[0])):
        x =serpent[0][_][0]*d_Cubos+centrado_1
        y =serpent[0][_][1]*d_Cubos+centrado

        snake= pygame.transform.scale(snake, (d_Cubos, d_Cubos))
        screen.blit(snake , (y,x))

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
    apple_=apple.create_apple(Serpiente)
    running=True
    while running:
        counter_result=tm.perf_counter() - contador_habilidad
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_a or event.key ==pygame.K_LEFT:
                    Serpiente[3] = (0,-1)#IZQUIERDA
                    
                if event.key == pygame.K_d or event.key ==pygame.K_RIGHT:
                    Serpiente[3] = (0,1)#DERECHA
                    
                if event.key == pygame.K_s or event.key ==pygame.K_DOWN:
                    Serpiente[3] = (1,0)#ARRIBA

                if event.key == pygame.K_w or event.key ==pygame.K_UP:
                    Serpiente[3] = (-1,0)#ABAJO
           
                if event.key == pygame.K_4:
                    Serpiente=serpiente.increment_size(Serpiente)

                if event.key == pygame.K_1:
                    apple_=apple.increment_apple(True,apple_)

                if event.key == pygame.K_2:
                    apple_=apple.increment_apple(False,apple_)
        print(Serpiente[1])
        # print(int(counter_result))
        if counter_result > 10:     
            apple.convert_tipe_apple(apple_)
            contador_habilidad=tm.perf_counter()
        screen.fill("black")
        Cambios_dimensionales_pantalla = pygame.display.get_surface().get_size()
        mostrar_grilla(Cambios_dimensionales_pantalla)
        mostrar_manzanas(apple_,Cambios_dimensionales_pantalla,normal_apple,gold_apple,rotten_apple)
        mostrar_serpent(Serpiente,Cambios_dimensionales_pantalla,serpent)
        Serpiente=serpiente.move_serpent(Serpiente)
        Serpiente,apple_=serpiente.eat_appl(Serpiente,apple_)
        apple_ =apple.check_state(apple_,Serpiente)
        pygame.display.flip()

        clock.tick(10)  

    pygame.quit()
main()