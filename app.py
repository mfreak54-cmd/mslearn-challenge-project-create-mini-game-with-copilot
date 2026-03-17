
import random
opciones = ["piedra", "papel", "tijeras"]

def obtener_jugada():
    while True:
        jugador = input ("Elige piedra, papel o tijeras: ").lower()
        if jugador in opciones:
            return jugador
        else:
            print("Opcion Invalida.")

jugador = obtener_jugada()
computadora = random.choice(opciones)
victorias_jugador = 0
victorias_computadora = 0
while True:
    print("La Computadora eligió:", computadora)
    if jugador == computadora:
        print("¡Empate!")
    elif jugador == "piedra" and computadora == "tijeras":
        print("¡Ganaste! La piedra aplasta las tijeras.")
        victorias_jugador += 1
    elif jugador == "papel" and computadora == "piedra":
        print("¡Ganaste! El papel envuelve la piedra.")
        victorias_jugador += 1
    elif jugador == "tijeras" and computadora == "papel":
        print("¡Ganaste! Las tijeras cortan el papel.")
        victorias_jugador += 1
    else:
        print("¡Perdiste! La computadora gana.")
        victorias_computadora += 1

    print("Puntuación del jugador:", victorias_jugador)
    print("Puntuación de la computadora:", victorias_computadora)

    respuesta = input("¿Quieres volver a jugar? Sí/No: ").lower()
    if respuesta == "sí" or respuesta == "si":
        jugador = obtener_jugada()
        computadora = random.choice(opciones) 
    else: 
        print("¡Gracias por jugar! ¡Hasta luego!")

        if victorias_jugador > victorias_computadora:
            print("El ganador de esta ronda fue: El jugador con", victorias_jugador)
        elif victorias_computadora > victorias_jugador:
            print("El ganador de esta ronda fue: La computadora con", victorias_computadora)
        else:
            print("¡La ronda terminó en empate con", victorias_jugador, "victorias cada uno!")
        break
