ancho,alto=15
def grilla(ancho,alto):
    return ([[0 for _ in range(ancho)] for _ in range(alto)],[],[1],[],[1])

def agregar_comida(State_game,decrement):
    if decrement:
        State_game[4]+=1
    else:
        State_game[4]-=1
    return State_game


def cambiar_tamaño(N_ancho,N_alto):
    global ancho, alto
    ancho = N_ancho
    alto = N_alto
    return grilla(ancho,alto)
