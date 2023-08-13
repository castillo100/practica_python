
def es_primo(numero):
    """Evalúa si un número es primo o no

    Args:
        numero (int): el número a ser evaluado

    Returns:
        bool: True si es primo, False si no
    """
    if(numero == 0 or numero == 1): return False
    if(numero == 2): return True
    if(not isinstance(numero, int)): return False
    if(numero > 0):
        interruptor = True
        
        while interruptor == True:
            for i in range(2, numero - 1):
                es_multiplo = numero % i == 0
                if es_multiplo == True: 
                    interruptor = False
                    return False
            interruptor = False
            return True
    else:
        return False
            
# Test-driven development: red, green, refactor
# Usar Arrange, Act, Assert (Preparar, Ejecutar, Comprobar)
def test():
    
    # Primer caso: 0 == False
    # Arrange
    numero = 0
    # Act
    resultado = es_primo(numero)
    # Assert
    print(f"primer caso: {resultado == False}")
    # Segundo caso: 1 == True
    # Arrange
    numero = 1
    # Act
    resultado = es_primo(numero)
    # Assert
    print(f"segundo caso: {resultado == False}")
    # Tercer caso: 2 == True
    # Arrange
    numero = 2
    # Act
    resultado = es_primo(numero)
    # Assert
    print(f"tercer caso: {resultado == True}")
    # Cuarto caso: 3 == True
    # Arrange
    numero = 3
    # Act
    resultado = es_primo(numero)
    # Assert
    print(f"cuarto caso: {resultado == True}")
    # Quinto caso: 4 == False
    # Arrange
    numero = 4
    # Act
    resultado = es_primo(numero)
    # Assert
    print(f"quinto caso: {resultado == False}")
    # Sexto caso: 0.6 == False
    # Arrange
    numero = 0.6
    # Act
    resultado = es_primo(numero)
    # Assert
    print(f"sexto caso: {resultado == False}")
    # Séptimo caso: -3 == False
    # Arrange
    numero = -6
    # Act
    resultado = es_primo(numero)
    # Assert
    print(f"séptimo caso: {resultado == False}")
    
# Review
# Evaluate




def escribir_a_archivo(lista, nombre_archivo):
    """Crea un archivo txt con los datos y nombre facilitados por el usuario

    Args:
        lista (list): lista de enteros a ser guardada en el archivo
        nombre_archivo (str): nombre que tendrá el archivo
    """
    with open(f"{nombre_archivo}.txt", 'w') as f:
        f.write(",".join(map(str,lista)))

def main(n, nombre_archivo):
    """Obtiene la lista de números primos entre 1 y el número determinado
    por el usuario y lo graba en un archivo con el nombre determinado por el usuario
    

    Args:
        n (int): número máximo del rango que va a ser evaluado
        nombre_archivo (str): nombre del archivo determinado por el usuario
    """
    numeros_primos = []
    for i in range(1, n+1):
        if es_primo(i) == True:
            numeros_primos.append(i)
    escribir_a_archivo(numeros_primos, nombre_archivo)
    print(len(numeros_primos))

test()
main(250, "numeros_primos")