
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

print("La Computadora eligió:", computadora)
if jugador == computadora:
    print("¡Empate!")
elif jugador == "piedra" and computadora == "tijeras":
    print("¡Ganaste! La piedra aplasta las tijeras.")
elif jugador == "papel" and computadora == "piedra":
    print("¡Ganaste! El papel envuelve la piedra.")
elif jugador == "tijeras" and computadora == "papel":
    print("¡Ganaste! Las tijeras cortan el papel.")
else:
    print("¡Perdiste! La computadora gana.")