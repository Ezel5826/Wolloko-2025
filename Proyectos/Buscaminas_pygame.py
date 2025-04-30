import pygame
import buscaminas
valores=(600,700)
pygame.init()
screen = pygame.display.set_mode(valores,pygame.RESIZABLE)
clock = pygame.time.Clock()
d_Cubos=40

def color_1(D_Pantalla,grilla):
    alto_g = len(grilla)*d_Cubos
    ancho_g = len(grilla[0])*d_Cubos
    centrado = (D_Pantalla[0] - (alto_g))/2
    centrado_1 = ( D_Pantalla[1] - (ancho_g))/2
    for alto in range(len(grilla)):
        for ancho in range(len(grilla[0])):
            y = alto*d_Cubos+centrado_1
            x = ancho*d_Cubos+centrado
            if grilla[alto][ancho] == 8:
                cubozz=pygame.Rect(x,y,d_Cubos,d_Cubos)
                pygame.draw.rect(screen,"gray",cubozz,100)
            elif grilla[alto][ancho] == 1:
                cubozz=pygame.Rect(x,y,d_Cubos,d_Cubos)
                pygame.draw.rect(screen,"red",cubozz,100)
            elif grilla[alto][ancho] == 0:
                cubozz=pygame.Rect(x,y,d_Cubos,d_Cubos)
                pygame.draw.rect(screen,"blue",cubozz,100)
            else:
                cubozz=pygame.Rect(x,y,d_Cubos,d_Cubos)
                pygame.draw.rect(screen,"green",cubozz,100)

def main():
    hola=0
    running=True
    grilla=buscaminas.grilla_logica_2()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")
        Cambios_dimensionales_pantalla = pygame.display.get_surface().get_size()

        color_1(Cambios_dimensionales_pantalla,grilla)
        pygame.display.flip()

        clock.tick(60)  

    pygame.quit()
main()