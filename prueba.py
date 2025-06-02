import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

# Lista de serpientes, cada una con su propia velocidad
serpientes = [
    {
        "color": (255, 0, 0),
        "sense": (1, 0),
        "cant_serp": 1,
        "vida": 100,
        "state": True,
        "velocidad": 5,  # movimientos por segundo
        "x": 50,
        "y": 100,
        "timer": 0
    },
    {
        "color": (0, 255, 0),
        "sense": (1, 0),
        "cant_serp": 1,
        "vida": 100,
        "state": True,
        "velocidad": 2,
        "x": 50,
        "y": 200,
        "timer": 0
    }
]

def mover_serpiente(serp):
    dx, dy = serp["sense"]
    serp["x"] += dx * 10
    serp["y"] += dy * 10

def dibujar_serpiente(serp):
    pygame.draw.rect(screen, serp["color"], (serp["x"], serp["y"], 20, 20))
# Bucle principal
while True:
    dt = clock.tick(60) / 1000  # tiempo entre frames en segundos

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))

    for serp in serpientes:
        serp["timer"] += dt
        if serp["timer"] >= 1 / serp["velocidad"]:
            serp["timer"] = 0
            mover_serpiente(serp)
        dibujar_serpiente(serp)

    pygame.display.flip()
