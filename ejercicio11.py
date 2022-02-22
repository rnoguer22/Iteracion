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

  num1 = int(input("Introduce un número: "))
  num2 = int(input("Introduce otro número: "))
  print ("Por el algoritmo de Euclides: {}".format(mcd_euclides(num1, num2)))
  print ("Usando sumas y restas: ", mcd_sumas_restas(num1,num2))