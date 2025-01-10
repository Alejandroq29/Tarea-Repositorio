import random

def adivina_el_numero():
    # Generar un número aleatorio entre 1 y 100
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinado = False

    print("¡Bienvenido al juego de Adivina el Número!")
    print("He elegido un número entre 1 y 100. ¡Intenta adivinarlo!")

    while not adivinado:
        # Solicitar al jugador que ingrese un número
        try:
            suposicion = int(input("Introduce tu suposición: "))
            intentos += 1

            # Comprobar la suposición
            if suposicion < numero_secreto:
                print("Demasiado bajo. Intenta de nuevo.")
            elif suposicion > numero_secreto:
                print("Demasiado alto. Intenta de nuevo.")
            else:
                adivinado = True
                print(f"¡Felicidades! Has adivinado el número {numero_secreto} en {intentos} intentos.")
        except ValueError:
            print("Por favor, introduce un número válido.")

# Llamar a la función para iniciar el juego
adivina_el_numero()