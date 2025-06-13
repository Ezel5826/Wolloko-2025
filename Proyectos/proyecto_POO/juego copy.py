import apple_clases as Apple
import serpiente_clases as Snake
import time as tm
from random import randint as rn
import pygame
pygame.init()
screen = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()
alto,ancho=15,15
d_Cubos=35
time=0

imagenes={
        "normal":pygame.image.load("Proyectos/proyecto_POO/images/manza_normal.png"),
        "gold":pygame.image.load("Proyectos/proyecto_POO/images/manzana_de_oro.png"),
        "rotten":pygame.image.load("Proyectos/proyecto_POO/images/manzana_podrida.png"),
        "thunderbolt":pygame.image.load("Proyectos/proyecto_POO/images/snake_head.png")}

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

def mostrar_serpent(snakes,dim):
    alto_g = alto*d_Cubos
    ancho_g = ancho*d_Cubos
    centrado = (dim[0] - (alto_g))/2
    centrado_1 = (dim[1] - (ancho_g))/2 
    for snake in snakes:
        for i in range(len(snake.coords)):
            x =snake.coords[i][0]*d_Cubos+centrado_1
            y =snake.coords[i][1]*d_Cubos+centrado
            cubozz=pygame.Rect(y,x,d_Cubos,d_Cubos)
            pygame.draw.rect(screen,"green",cubozz,100)
        # if _==len(serpent[0])-1:
        #     snake_head= pygame.transform.scale(snake_head, (d_Cubos, d_Cubos))

        #     if direccion == (-1,0): #arriba
        #         snake_head = pygame.transform.rotate(snake_head,90)
        #         screen.blit(snake_head, (y,x)) 

        #     if direccion == (1,0): #abajo
        #         snake_head = pygame.transform.rotate(snake_head,-90)
        #         screen.blit(snake_head, (y,x)) 

        #     if direccion == (0,-1): #izquierda
        #         snake_head = pygame.transform.flip(snake_head, True, False)
        #         screen.blit(snake_head, (y,x)) 
        #     if direccion == (0,1): #izquierda
        #         snake_head = pygame.transform.rotate(snake_head, 0)
        #         screen.blit(snake_head, (y,x))
        # else:
        #     snake_body= pygame.transform.scale(snake_body, (d_Cubos, d_Cubos))
        #     screen.blit(snake_body, (y,x))

def mostrar_manzanas(apples, dim):
    alto_g = alto * d_Cubos
    ancho_g = ancho * d_Cubos
    centrado = (dim[0] - alto_g) / 2
    centrado_1 = (dim[1] - ancho_g) / 2
    font = pygame.font.SysFont(None, 20)
    for apple in apples:
        x = apple.coords[0] * d_Cubos + centrado_1
        y = apple.coords[1] * d_Cubos + centrado
        normal_apple= pygame.transform.scale(imagenes.get(apple.actual_type), (d_Cubos, d_Cubos))
        screen.blit(normal_apple , (y,x))




def main():
    running = True
    apples=[]
    snakes=[]
    for _ in range(1):
        snakes.append(Snake.snake(alto,ancho))
    for _ in range(5):
        apples.append(Apple.apple(alto,ancho))
    snakes[0].elegir_comandos(input("ingrese p1 o p2 "))
    contador_habilidad=tm.perf_counter()
    print(snakes[0].comando_elegido)
    while running:
        counter_result=tm.perf_counter() - contador_habilidad
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                for snake in snakes:
                    if event.key in snake.comando_elegido:
                        snake.cambiar_sentido(snake.comando_elegido.get(event.key))
        print(counter_result)
        if counter_result > 3:     
            for apple in apples:
                print(apple.actual_type)
            apples[rn(0,len(apples))-1].change_apple_tipe()
            contador_habilidad=tm.perf_counter()
        screen.fill("black")
        Cambios_dimensionales_pantalla = pygame.display.get_surface().get_size()
        mostrar_grilla(Cambios_dimensionales_pantalla)
        mostrar_manzanas(apples,Cambios_dimensionales_pantalla)
        mostrar_serpent(snakes,Cambios_dimensionales_pantalla)
        for snake in snakes:  
                snake.mover()
                snake.eat_appl(apples)

        pygame.display.flip()

        clock.tick(10) 

    pygame.quit()
main()

# class game:
#     def __init__(self):
#         self.