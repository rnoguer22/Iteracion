def descomponer():

  separador = str(input("Introduce el separador que desea utilizar: "))
  cadena = str(input("Introduce un texto para analizar: "))

  ca = cadena.split(separador)

  info = {"Cadena" : ca}

  print(tabulate(info, headers = "keys", tablefmt = "fancy_grid", showindex = True))

descomponer()
