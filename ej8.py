import tabulate

def descomponer():

  separador = str(input("Introduce el separador que desea utilizar: "))
  cadena = str(input("Introduce un texto para analizar: "))

  ca = cadena.split(separador)

  n = len(ca)

  table = [["nº", int(n)], ["Cadena", str(ca)]]
  
  print(tabulate(table, tablefmt = "fancy_grid"))

 

descomponer()
