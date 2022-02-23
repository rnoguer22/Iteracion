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
    
    
def inicio():
  cliente = banco(cuenta, saldo)
  print(cliente.respuesta())
  print(cliente.algo_mas())
  print(cliente.historial())



      