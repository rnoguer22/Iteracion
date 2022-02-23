# Iteración
La dirección de nuestro repositorio es: [GitHub](https://github.com/rnoguer22/Iteracion)

## Ejercicio 7
``` python3
#Funcion que devuelve la mayor potencia de la base pero que sea menor o igual al número pasado como parámetro
def encuentra_potencia(numero, base):
    #Funciona muy parecido a un factorial
    factor = 1
    while factor <= numero:
        #Multiplicamos el numero por la base, hasta que factor > numero
        factor *= base
    return factor//base

#Funcion que nos imprime directamente el numero en la base que introducimos por teclado
def imprime_digito_en_base(digito):
  if digito < 10:
    #Hacemos uso de end="" para que no imprima los digitos con salto de linea
    print("{:d}".format(digito), end="")
  else:
    #Transoformamos el digito en una letra, ya que solo disponemos de numeros del 0 al 9
    digito_transformado = chr(digito - 10 + ord('A'))
    #Imprimimos la letra, que en realidad es un caracter del codigo ASCII
    print("{}".format(digito_transformado), end="")

def imprime_en_otra_base(numero, base):
  #La variable factor es la clave para que este codigo sea iterativo
    factor = encuentra_potencia(numero, base)
    while True:
        digito = numero // factor
      #Vamos imprimiendo los digitos uno por uno
        imprime_digito_en_base(digito)
        numero %= factor
      #De esta manera, la variable factor es realmente el cociente de dividir factor entre la base, tal y como se hace para cambiar de base matematicamente en un folio
        factor = factor//base;
        if factor == 0:
            break 

def flujo_programa():
  numero = int(input("Introduzca un numero entero: "))
  while True:
    base = int(input("Introduzca la base: "))
    if base >= 2:
      #Llamamos a la funcion que nos imprime el numero en la base deseada
      imprime_en_otra_base(numero, base)
      break
    else:
      print("Debe ingresar una base entre 2 y 36")

if __name__ == "__main__":

  flujo_programa()
```

## Ejercicio 11
```python3
"Primera parte del ejercicio"
def mcd_euclides (a,b):
  #Vamos a resolver el algoritmo de euclides utilizando iteracion
  while b != 0:
    # Hacemos uso de la siguiente propiedad: mcd(a,b) = mcd(a−b,b)
    aux = b
    b = a%b
    a = aux
    #De esta manera vamos reduciendo a hasta que este sea el mcd
  return a

"Segunda parte del ejercicio"
def mcd_sumas_restas (a,b):
  #Ahora tenemos un handicap; solo podemos usar sumas y restas
  while b != 0:
    aux = b-a
    b -= aux
    a = aux
    return a

def iniciar():

  num1 = 6
  num2 = 8
  print ("Por el algoritmo de Euclides: {}".format(mcd_euclides(num1, num2)))
  print ("Usando sumas y restas: ", mcd_sumas_restas(num1,num2))
```

## Ejercicio 12
```python3
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

if __name__ == "__main__":

  n = int(input("Introduzca un numero entero: "))
  calcular_cuadrados_perf(n)
```
