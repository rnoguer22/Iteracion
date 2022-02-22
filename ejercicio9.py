import tabulate

def palabra():
  diccionario =  ["Patata", "Fotos", "Ancla", "Cucaracha"]
  
  print("Las palabras de este diccionario son: ")
  for i in range(0, len(diccionario)):
    print(diccionario[i])
  
  diccionario.sort()

  table = []
  for i in range(0, len(diccionario)):
    
    table.append(list(diccionario[i:i+1]))
  
  headers = ["i", "diccionario", "anterior", "siguiente"]
  print(tabulate.tabulate(table, headers, tablefmt = "fancy_grid", showindex = True))

palabra()