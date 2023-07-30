
"""  UMPIRE
Understand
Match
Plan
Implement
Review
Evaluate
"""

# 4 Typos de datos: Listas, Tuplas y Diccionarios

# 4.1 listas

miListadefrutas = ["manzanas", "bananas", "cerezas"]
print(miListadefrutas, type(miListadefrutas))
print(miListadefrutas[0])
print(miListadefrutas[1])
print(miListadefrutas[2])
miListadefrutas.append("piñas")
print(miListadefrutas, type(miListadefrutas))
miListadefrutas[2] = "naranjas"
print(miListadefrutas, type(miListadefrutas))
print(len(miListadefrutas))

# 4.2 Tuplas
miListadefrutasTupla = ("manzanas", "bananas", "cerezas")
print(miListadefrutasTupla, type(miListadefrutasTupla))
print(miListadefrutasTupla[0])

# 4.3 Diccionarios
miListadefrutasDic = {
    "Ana": "manzana", "Juana": 'banana', "Petra": "piña"

}
print(miListadefrutasDic)
print(miListadefrutasDic["Ana"])
miListadefrutasDic["Ana"] = "uvas"
print(miListadefrutasDic["Ana"])
