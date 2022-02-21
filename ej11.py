#Primera parte del ejercicio

def mcd_euclides (a,b):
  #Vamos a resolver el algoritmo de euclides utilizando iteracion
  while b =! 0:
    # Hacemos uso de la siguiente propiedad: mcd(a,b) = mcd(a−b,b)
    b = a%b
    #De esta manera vamos reduciendo a hasta que este sea el mcd
    return a

if __name__ == "__main__":

  print (mcd_euclides(105, 70))