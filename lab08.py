import random
# Vamos a crear el juego "Adivina el número"
# Damos la bienvenida al usuario "Bienvenido al juego Adivina el número!"
print("Bienvenido al juego Adivina el número!")
""" 
 Indicar las reglas al usuario: 'Las reglas son sencillas: Pensaré en un número y
 tú intentarás hasta que adivines'

 """
print("Las reglas son sencillas: Pensaré en un número y tú intentarás hasta que adivines")
# definir el número aleatorio
frutas = ["fresa", "melon", "mango"]
random_fruit = random.choice(frutas)
random_number = random.randint(1, 10)

status = True
while status == True:
    # pedir al usuario que adivine
    user_guess = int(input("Dime un número entre 1 y 10 "))
 # Si el usuario adivina, indicarle el número y dale la enhorabuena
    if user_guess == random_number:
        print(f"Enhorabuena, haz adivinado el número que era {random_number}")
        status = False
    else:
     # si el usuario no adivina, indicarle que intente otra vez hasta que adivine
        print("Número incorrecto, intenta de nuevo")
