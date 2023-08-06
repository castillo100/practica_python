# preguntarle al usuario si necesita enviar un paquete (si o no)
# user_response = input("necesitas enviar un paquete?(responde sí o no)")

# si el usuario responde afirmativamente, imprimir "podemos enviar el paquete"
""" si el usuario responde negativamente, imprimir el mensaje  'por favor vuelve 
cuando necesites enviar un paquete. Gracias'  """
""" if user_response == 'si':
    print("podemos enviar el paquete")
else:
    print('por favor vuelve cuando necesites enviar un paquete. Gracias')
 """

""" preguntar al usuario: Quieres comprar estampillas,un sobre o hacer una copia? (escribe 
'estampilla', 'sobre' o 'copia')
    si la respuesta es estampilla, imprimir el mensaje: 'tenemos muchos tipos de diseños 
    de estampillas para escoger
    si la respuesta es sobre, imprimir el mensaje: 'tenemos muchos tamaños de sobres  para escoger 
    si la respuesta es copiar, preguntar al usuario: 'cuantas copias quieres (introduce el número) y
     y responder "aquí tienes x copias"
    si la respuesta está en blanco, imprimir el mensaje: 'gracias, por favor regresa pronto  
    
"""
user_response = input(
    "Quieres comprar estampillas,un sobre o hacer una copia? (escribe 'estampilla', 'sobre' o 'copia'")
if user_response == "estampilla":
    print("tenemos muchos tipos de diseños de estampillas para escoger")
elif user_response == 'sobre':
    print("tenemos muchos tamaños de sobres  para escoger")
elif user_response == 'copia':
    number_of_copies = input("cuantas copias quieres (introduce el número)")
    print("Aquí tienes {} copias".format(number_of_copies))
    # print(f"Aquí tienes {number_of_copies} copias")
else:
    print("gracias, por favor regresa pronto")
