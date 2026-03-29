class Ropa:
    def __init__(self):
        self.marca = 'willow'
        self.talla = 'M'
        self.color = 'rojo'

camisa = Ropa()
print(camisa.marca)
print(camisa.talla)
print(camisa.color)

class Calculadora:
    def __init__(self, n1, n2):
        self.suma = n1 + n2
        self.resta = n1 - n2
        self.multiplicacion = n1 * n2
        self.division = n1 / n2

calc = Calculadora(3, 4)
print(calc.suma)
print(calc.resta)
print(calc.multiplicacion)
print(calc.division)
