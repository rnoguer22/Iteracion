# Iteración
La dirección de nuestro repositorio es: [GitHub](https://github.com/rnoguer22/Iteracion)

## Ejercicio 6 
```python
cuenta = str(input("¿Quiere abrir una cuenta en el banco?: "))
saldo = 0
d = []

class banco:
  
  def __init__(self, cuenta, saldo):
    self.cuenta = cuenta
    self.saldo = saldo
  
  def respuesta(self):
    if self.cuenta == "no":
      print("De acuerdo, gracias")
    if self.cuenta == "si":
      self.saldo = 0
      abono = float(input("Introduce el dinero que desea ingresar: "))
      self.saldo = abono
      print("Su cuenta se ha abierto correctamente")
      print("Su saldo es:", self.saldo, "€")
  
  def accion(self):
    act = str(input("¿Quiere ingresar, retirar, o consultar dinero?: "))
    d.append(act)
    if act == "ingresar":
      ingreso = float(input("Introduce la cantidad que desea ingresar: "))
      self.saldo = self.saldo + ingreso
      print("Su saldo es ahora de: ", self.saldo, "€")

    if act == "retirar":
      retirada = float(input("Introduce la cantidad que desea retirar: "))
      if self.saldo < retirada:
        print("Error, no tiene suficiente saldo")
      else: 
        self.saldo = self.saldo - retirada
        print("Su saldo es ahora de: ", self.saldo, "€")

    if act == "consultar":
      print("Su saldo es de:", self.saldo, "€")

  def algo_mas(self):
    pregunta = str(input("¿Quiere hacer alguna operación más?: "))
    if pregunta == "si":
      banco.accion(self)
      banco.algo_mas(self)
    if pregunta == "no":
      print("Como usted quiera")

  def historial(self):
    hist = str(input("¿Quiere consultar su historial?: "))
    if hist == "si":
      for i in d:
        print(i)
    
    

cliente = banco(cuenta, saldo)
print(cliente.respuesta())
print(cliente.algo_mas())
print(cliente.historial())
```


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

## Ejercicio 8
```python
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
```

## Ejercicio 9
```python
import tabulate

diccionario =  ["Patata", "Fotos", "Ancla", "Cucaracha"]

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
  ```

## Ejercicio 10
#### Sin terminar :(
```python
class Persona:
  #Constructor
  def __init__(self, identidad, edad, padre, madre):
    self.identidad = identidad
    self.edad = edad
    self.padre = padre
    self.madre = madre

  def lista_edad_20_30(self):
    r = []
    for i in range(numero de personas):
      if 20 < self.edad < 30:
        r.append(self.nombre)
    return r

  def numero_huerfanos(self):
    #Lista vacia donde se almacenaran la identidad de los niños huerfanos
    r = []
    for i in range (1000)
    if self.padre == 0 and self.madre == 0:
      if self.edad < 15:
        r.append(self.identidad)
    return r
  
  def envejecer_1_año(self):
    for i in range (numero de personas):
      self.edad[i] += 1

  def identidad_padre_jaime(self):
    if self.identidad = "Jaime MARTIN"
      return self.padre

if __name__ == "__main__":

  familias = []
  for i in range (1000):
    r = Persona(identidad, padre, madre, edad)
    familias.append(r)
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
