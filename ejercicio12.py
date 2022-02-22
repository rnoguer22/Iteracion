from math import sqrt

def calcular_cuadrados_perf(n):
  #Definimos una segunda lista donde se almacenaran los cuadrados perfectos
  r = []
  s = []
  #Bucle para generar los numeros enteros hasta n
  for i in range (n+1):
    s.append(i)
  #Bucle que nos calcula los cuadrados perfectos hasta n
  for t in s:
      if sqrt(t) in s:
        r.append(t)
  #Mostramos el resultado por pantalla
  print("Los cuadrados perfectos hasta {} son:".format(n))
  #Bucle para imprimir los cuadrados perfectos con salto de linea
  for x in r:
    print (x)

calcular_cuadrados_perf(45)