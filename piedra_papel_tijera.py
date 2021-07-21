import random

def jugar():
    user = input("Escoge una opción: 'pi' para piedra, 'pa' para papel y 'ti' para tijera.\n").lower()
    computadora = random.choice(['pi', 'pa', 'ti'])

    if user == computadora:
        return '¡Empate!'
    
    if gano_jugador(user, computadora):
        return '¡Ganaste!'
    
    return '¡Perdiste!'


def gano_jugador(jugador, oponente):
    # Retornar Valor True (verdadero) si gana el jugador.
    # Piedra gana a Tijeras (pi > ti)
    # Tijera gana a Papel (Ti > pa)
    # Papel gana a Piedra (pa > pi)
    if ((jugador == 'pi' and oponente == 'ti')
        or (jugador == 'ti' and oponente == 'pa')
        or (jugador == 'pa' and oponente == 'pi')):
        return True
    else:
        return False


print(jugar())