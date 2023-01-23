class Algoritmo:
  def algoritmoMejorable(self, n):
    a = 1
    b = 10
    salida = ""
    for i in range(1, n+1):
      b = 5 * i
      while a < 100:
        b = 10 *i
        a = a*b
      salida = salida + "{0}-".format(a)
    c = b + 1
    salida = salida + "{0:.1f}{1:.1f}".format(b,c)
    print(salida)