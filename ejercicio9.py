import tabulate

def palabra():
  diccionario = {1 : "Patata", 2 : "Fotos", 3 : "Ancla", 4 : "Cucaracha"}
  
  print("Las palabras de este diccionario son: ")
  for i in diccionario:
    print("{}".format(diccionario[i]))

  

palabra()