import tabulate

diccionario =  ["Patata", "Fotos", "Ancla",                             "Cucaracha"]

def palabra(dicccionario):

  palabra = []

  for i in range(0, len(diccionario)):
    diccionario.sort()
    z = [i + 1, diccionario[i], i, i + 2]
    palabra.append(z)
  
  tabla = palabra

  headers = ["i", "diccionario", "anterior", "siguiente"]

  print("Este es el diccionario:")
  print(tabulate.tabulate(tabla, headers, tablefmt = "fancy_grid"))


def añadir():

  n = str(input("Introduce la palabra que quieres añadir al diccionario: "))
  diccionario.append(n)

  palabra(diccionario)
  
def delete():
  n = str(input("Introduce la palabra que quieres quitar del diccionario: "))
  diccionario.remove(n)

  palabra(diccionario)
  
def inicio():
  palabra(diccionario)
  añadir()
  delete()