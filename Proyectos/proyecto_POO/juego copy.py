import apple_clases as Apple
import serpiente_clases as Snake
import time as tm
from random import randint as rn
import pygame
pygame.init()
screen = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()
alto,ancho=10,10
d_Cubos=50
time=0
movimientos_L={
            49: {
                97: (0, -1),
                100: (0, 1),
                115: (1, 0),
                119: (-1, 0)
            },
            50: {
                1073741904: (0, -1),
                1073741903: (0, 1),
                1073741905: (1, 0),
                1073741906: (-1, 0)
            }
        }

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
            pygame.draw.rect(screen,snake.color,cubozz,100)
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
        normal_apple= pygame.transform.scale(pygame.image.load(apple.available_tipes.get(apple.actual_type)[1]), (d_Cubos, d_Cubos))
        screen.blit(normal_apple , (y,x))


def main():
    running = True
    apples=[]
    snakes=[]
    startgame=False
    quantity_chose=0
    # for _ in range(2):
    snakes.append(Snake.snake(alto,ancho,"red"))
    snakes.append(Snake.snake(alto,ancho,"green"))
    for _ in range(5):
        apples.append(Apple.apple(alto,ancho))
    contador_habilidad=tm.perf_counter()

    while running:
        counter_result=tm.perf_counter() - contador_habilidad
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                for snake in snakes:
                    if not snake.eligio_comando:
                        if event.key in movimientos_L and len(snakes)==2:
                            snake.elegir_comandos(movimientos_L.get(event.key))
                            movimientos_L.pop(event.key)
                            quantity_chose+=1
                        
                    else:
                        if event.key in snake.comando_elegido:
                            snake.cambiar_sentido(snake.comando_elegido.get(event.key)) 

        startgame=True if quantity_chose==len(snakes) else startgame
        if startgame:
            if counter_result > 3:     
                apples[rn(0,len(apples))-1].change_apple_tipe()
                contador_habilidad=tm.perf_counter()
            screen.fill("black")
            Cambios_dimensionales_pantalla = pygame.display.get_surface().get_size()
            mostrar_grilla(Cambios_dimensionales_pantalla)
            mostrar_manzanas(apples,Cambios_dimensionales_pantalla)
            mostrar_serpent(snakes,Cambios_dimensionales_pantalla)
            for snake in snakes:  
                    snake.mover(apples)

            pygame.display.flip()

            clock.tick(10) 

    pygame.quit()
main()
