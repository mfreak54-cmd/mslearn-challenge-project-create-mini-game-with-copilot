
import tkinter as tk
import random

opciones = ["piedra", "papel", "tijeras"]
victorias_jugador = 0
victorias_computadora = 0

window = tk.Tk()
window.title("Piedra, Papel o Tijeras")
window.geometry("400x260")
window.resizable(False, False)

bienvenida = tk.Label(window, text="Bienvenido a Piedra, Papel o Tijeras! Elige tu jugada:", font=("Arial", 12), pady=20)
bienvenida.config(fg="red")
bienvenida.pack()

marcador = tk.Label(window, text="Jugador: 0  PC: 0", font=("Arial", 12, "bold"), pady=10)
marcador.pack()

texto_resultado = tk.Label(window, text="Elige una opción para jugar.", font=("Arial", 12), pady=10)
texto_resultado.pack()

def jugar(jugador):
    global victorias_jugador, victorias_computadora
    computadora = random.choice(opciones)

    if jugador == computadora:
        resultado = "Empate"
    elif (
        (jugador == "piedra" and computadora == "tijeras")
        or (jugador == "papel" and computadora == "piedra")
        or (jugador == "tijeras" and computadora == "papel")
    ):
        resultado = "¡Ganaste!"
        victorias_jugador += 1
    else:
        resultado = "¡La computadora ganó!"
        victorias_computadora += 1

    texto_resultado.config(text=f"Tú: {jugador} | PC: {computadora}\n{resultado}")
    marcador.config(text=f"Jugador: {victorias_jugador}  PC: {victorias_computadora}")


frame_botones = tk.Frame(window)
frame_botones.pack(pady=10)

btn_piedra = tk.Button(frame_botones, text="🪨Piedra", width=10, command=lambda: jugar("piedra"))
btn_papel = tk.Button(frame_botones, text="📄Papel", width=10, command=lambda: jugar("papel"))
btn_tijeras = tk.Button(frame_botones, text="✂️Tijeras", width=10, command=lambda: jugar("tijeras"))

btn_piedra.grid(row=0, column=0, padx=5)
btn_papel.grid(row=0, column=1, padx=5)
btn_tijeras.grid(row=0, column=2, padx=5)

btn_salir = tk.Button(window, text="Salir", command=window.destroy)
btn_salir.pack(side="bottom", pady=8)

window.mainloop()
