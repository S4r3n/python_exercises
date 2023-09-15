saltoLinea = '\n'

class Category:
  name=''
  ledger = []
  

  def __init__(self, name):
    self.name = name
    self.ledger = []

  def __str__(self):
    objectString = ((self.name).center(30, '*')) + saltoLinea  
    for dict in self.ledger:
      objectString = (objectString 
                      + (str(dict['description'])[:23]).ljust(23)
                      + str("{:.2f}".format(float(dict['amount']))).rjust(7)
                      + saltoLinea)

    objectString = (objectString + 'Total: '
                    + str("{:.2f}".format(self.get_balance())))
    return objectString

  def deposit(self, amount, description=''):
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, description=''):
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": description})
      return True
    else:
      return False

  def get_balance(self):
    total = 0
    for dict in self.ledger:
      total += dict['amount']
    return total

  def transfer(self, amount, category):
    if self.check_funds(amount):
      category.deposit(amount, "Transfer from " + self.name)
      self.ledger.append(
        {"amount": -amount, "description": "Transfer to " + category.name})
      return True
    else:
      return False

  def check_funds(self, amount):
    return self.get_balance() >= amount


def create_spend_chart(listaCategorias):
  resultado = 'Percentage spent by category'
  porcentajes = [100,90,80,70,60,50,40,30,20,10,0]

  for p in porcentajes:
    resultado = (resultado 
                 + saltoLinea
                 + str(p).rjust(3) 
                 + '| ')

    for c in listaCategorias:
      categoryWithdraws = getlWithdrawsPercentage(c, listaCategorias)
      if  categoryWithdraws >= p:
        resultado = resultado + 'o' + '  '
      else:
        resultado = resultado + '   '
        

  resultado = (resultado
               + saltoLinea
               + '----------'.rjust(14) )

  for i in range(0,longestCategoryNameSize(listaCategorias)):
    lineaCategoria=''
    for c in listaCategorias:
      if len(c.name) > i:
        lineaCategoria = lineaCategoria + c.name[i:i+1] + '  ' 
      else:
        lineaCategoria = lineaCategoria + '   '
    resultado = (resultado
               + saltoLinea
               + lineaCategoria.rjust(14))  

  return resultado


def longestCategoryNameSize(listaCategorias):
  length=0
  for c in listaCategorias:
    if len(c.name)>length:
        length = len(c.name)
  return length

def getlWithdrawsPercentage(categoria, listaCategorias):
  totalGastos=0
  totalGastosCategoria=0

  for c in listaCategorias:
     for dict in c.ledger:
        if dict['amount'] < 0:
          totalGastos=totalGastos - dict['amount']
       
  for dict in categoria.ledger:
      if dict['amount'] < 0:
        totalGastosCategoria = totalGastosCategoria - dict['amount']
  return getPercentage(totalGastosCategoria, totalGastos)

def getPercentage(part, whole):
  #print("Part: " + str(part) + ', whole: ' + str(whole))
  return 100 * float(part)/float(whole)