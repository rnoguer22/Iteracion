import tabulate

def descomponer():

  separador = str(input("Introduce el separador que desea utilizar: "))
  cadena = str(input("Introduce un texto para analizar: "))

  ca = cadena.split(separador)
  
  lista = []
  for i in range(0, len(ca)):
    lista.append(list(ca[i:i+1]))

  table = lista
  headers = ["nº", "Cadena"]
  print(tabulate.tabulate(table, headers, tablefmt = "fancy_grid", showindex = True))


  

