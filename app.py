
import random
opciones = ["piedra", "papel", "tijeras"]
jugador = input("Elige piedra, papel o tijeras: ").lower()
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