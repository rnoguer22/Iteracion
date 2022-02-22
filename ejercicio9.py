import tabulate

def tabla(diccionario):
  table = []
  for i in range(0, len(diccionario)):
    
    table.append(list(diccionario[i:i+1]))
  
  headers = ["i", "diccionario", "anterior", "siguiente"]
  print(tabulate.tabulate(table, headers, tablefmt = "fancy_grid", showindex = True))

def palabra():
  diccionario =  ["Patata", "Fotos", "Ancla", "Cucaracha"]
  
  tabla(diccionario)

  print("\n")
  
  diccionario.sort()

  print("Ordenadas alfabéticamente:")

  tabla(diccionario)

palabra()