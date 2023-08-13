lista = [1,34, 11, 28, 50, 100, 29, 7, 71, 55, 33]
def busqueda_binaria(lista, objetivo):
    """
    Busca un número dentro de una lista y devuelve booleano con resultado
    Args:
        lista (list): Lista de números sobre la que se realizará la búsqueda
        objetivo (int): Número objetivo
    Returns: 
        (bool): Si hay o no match
    """
    lista_ordenada = sorted(lista)
    loops = 0
        
    for _ in range(len(lista)):
        if objetivo not in lista_ordenada:
            resultado = False
            return resultado
        biseccion = len(lista_ordenada) // 2
        if objetivo == lista_ordenada[biseccion]: 
            loops += 1
            print(loops)
            return True
        if objetivo > lista_ordenada[biseccion]:
            lista_ordenada[:] = lista_ordenada[biseccion+1:]
            loops += 1
        else:
            lista_ordenada[:] = lista_ordenada[0:biseccion]
            loops += 1
    
    return False
def test():
    # Arrange
    objetivo = 55
    # Act
    resultado = busqueda_binaria(lista, objetivo)
    print(resultado)
    # Assert
    print(f"{objetivo} es {resultado == True}\n")
    # Arrange
    objetivo = 54
    # Act
    resultado = busqueda_binaria(lista, objetivo)
    print(resultado)
    # Assert
    print(f"{objetivo} es {resultado == False}\n")
    # Arrange
    objetivo = 100
    # Act
    resultado = busqueda_binaria(lista, objetivo)
    print(resultado)
    # Assert
    print(f"{objetivo} es {resultado == True}\n")
    # Arrange
    objetivo = 1
    # Act
    resultado = busqueda_binaria(lista, objetivo)
    print(resultado)
    # Assert
    print(f"{objetivo} es {resultado == True}\n")
    # Arrange
    objetivo = 28
    # Act
    resultado = busqueda_binaria(lista, objetivo)
    print(resultado)
    # Assert
    print(f"{objetivo} es {resultado == True}\n")
    
test()
