class Calculator:
    def __init__(self, a: int, b: int) -> None:
        self.a = a
        self.b = b
    
    def suma(self):
        return self.a + self.b

    def resta(self):
        return self.a - self.b

    def multiplicacion(self):
        return self.a * self.b

    def division(self):
        try:
            return self.a / self.b
        except ZeroDivisionError:
            return('No se puede dividir entre cero')

    def potencia(self):
        return self.a ** self.b

    def raiz(self):
        if(self.a < 0):
            return('No se puede sacar raiz a un numero negativo')
        else:
            return self.a ** 1/self.b