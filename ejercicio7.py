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