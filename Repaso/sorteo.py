import random


def imprimir_ganador (*participantes):
    if not participantes:
        return "No hay participantes"
    else:
        return random.choice(participantes)


personas = input("Introduce los nombres de los participantes: ").split()

ganador = imprimir_ganador(*personas)

print("El ganador es: ", ganador)