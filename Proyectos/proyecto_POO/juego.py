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
screen = pygame.display.set_mode(valores,pygame.RESIZABLE| pygame.FULLSCREEN)
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
    imagenes_manzanas = {
    "normal": pygame.transform.scale(normal_apple, (d_Cubos, d_Cubos)),
    "gold": pygame.transform.scale(gold_apple, (d_Cubos, d_Cubos)),
    "rotten": pygame.transform.scale(rotten_apple, (d_Cubos, d_Cubos))}
    alto_g = alto * d_Cubos
    ancho_g = ancho * d_Cubos
    centrado = (dim[0] - alto_g) / 2
    centrado_1 = (dim[1] - ancho_g) / 2
    font = pygame.font.SysFont(None, 20)
    for i in range(len(apple_)):
        x = apple_[i][0][0] * d_Cubos + centrado_1
        y = apple_[i][0][1] * d_Cubos + centrado

        tipo = apple_[i][3]
        imagen = imagenes_manzanas.get(tipo)
        if imagen:
            screen.blit(imagen, (y, x))

def main():
    contador_habilidad=tm.perf_counter()
    serpientes=[[[[2,2],[2,3]],1,1,(0,1),100,True,10,0],[[[4,4],[4,5]],1,1,(0,1),100,True,8,0]]
    apple_=apple.create_apple(serpientes[0])
    running=True
    while running:
        dt = clock.tick(60) / 1000
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

        if counter_result > 5:     
            apple.convert_tipe_apple(apple_)
            contador_habilidad=tm.perf_counter()
        screen.fill("black")

        Cambios_dimensionales_pantalla = pygame.display.get_surface().get_size()

        mostrar_grilla(Cambios_dimensionales_pantalla)
        mostrar_manzanas(apple_,Cambios_dimensionales_pantalla,normal_apple,gold_apple,rotten_apple)
        
        for Serpiente in serpientes:
            Serpiente[7]+=dt
            if Serpiente[7] >= 1 / Serpiente[6]:
                Serpiente[7] = 0
                Serpiente=serpiente.move_serpent(Serpiente)
                Serpiente,apple_=serpiente.eat_appl(Serpiente,apple_)
                apple_ =apple.check_state(apple_,Serpiente)
            mostrar_serpent(Serpiente,Cambios_dimensionales_pantalla,serpent_body,serpent_head,Serpiente[3])
        pygame.display.flip()


    pygame.quit()
main()