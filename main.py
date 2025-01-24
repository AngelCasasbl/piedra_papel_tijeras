import random

def jugar_ronda():
    opciones = ["piedra", "papel", "tijeras"]
    jugador = input("Elige piedra, papel o tijeras: ").strip().lower()
    
    if jugador not in opciones:
        print("Opción no válida. Intenta nuevamente.")
        return None, None
    
    computadora = random.choice(opciones)
    print(f"La computadora eligió: {computadora}")
    
    if jugador == computadora:
        print("¡Empate!")
        return "empate"
    elif (jugador == "piedra" and computadora == "tijeras") or \
         (jugador == "papel" and computadora == "piedra") or \
         (jugador == "tijeras" and computadora == "papel"):
        print("¡Ganaste esta ronda!")
        return "jugador"
    else:
        print("La computadora ganó esta ronda.")
        return "computadora"

def piedra_papel_tijeras():
    print("¡Bienvenido a Piedra, Papel o Tijeras!")
    print("Gana el mejor de 3.")
    
    jugador_puntos = 0
    computadora_puntos = 0
    
    while True:
        resultado = jugar_ronda()
        
        if resultado == "jugador":
            jugador_puntos += 1
        elif resultado == "computadora":
            computadora_puntos += 1
        
        print(f"Puntaje -> Jugador: {jugador_puntos}, Computadora: {computadora_puntos}")
        
        # Verificar si alguien ya ganó 2 de 3
        if jugador_puntos == 2:
            print("¡Felicidades! Ganaste el juego.")
            break
        elif computadora_puntos == 2:
            print("La computadora ganó el juego. ¡Mejor suerte la próxima vez!")
            break

# Inicia el juego
piedra_papel_tijeras()
