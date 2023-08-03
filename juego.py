import random


def adivina_el_numero(x):

    print("-------------------")
    print("bienvenido al juego")
    print("-------------------")
    print("tu meta es adivinar el número generado por la computadora.")

    número_aleatorio = random.randint(1, x)  # Número aleatorio entre 1 y x.

    predicción = 0

    while predicción != número_aleatorio:
        # el usuario ingresa un número
        predicción = int(
            input(f"Adivina un número entre 1 y {x}: "))  # f-string

        if predicción < número_aleatorio:
            print("intenta otra vez. este número es muy pequeño.")
        elif predicción > número_aleatorio:
            print("Intenta otra vez. Este número es muy grande.")

    print(
        f"¡Felicitaciones! Adivinaste el número {número_aleatorio} correctamente.")


adivina_el_numero(10)
