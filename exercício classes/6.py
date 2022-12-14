#Crie uma calculadora

class Calculadora:
    def __init__(self):
        self.valor = ""

    def calcular(self, numero2, operador):

        try:
            numero2 = float(numero2)
            self.valor = float(self.valor)

        except ValueError:
            print("Você digitou algum valor inválido. Tente novamente")
            return "Error na conversão de valor para float"

        if (operador == "+"):
            print(self.somar(numero2))
        elif (operador == "-"):
            print(self.subtrair(numero2))
        elif (operador == "/"):
            print(self.dividir(numero2))
        elif (operador == "*"):
            print(self.multiplicar(numero2))
        else:
            print("O usuário digitou um operador inválido. Tente novamente")
        return "Deu tudo certo"

    def somar(self, numero2):
        resultado = self.valor + numero2
        self.valor = resultado
        return resultado

    def subtrair(self, numero2):
        resultado = self.valor - numero2
        self.valor = resultado
        return resultado

    def multiplicar(self, numero2):
        resultado = self.valor * numero2
        self.valor = resultado
        return resultado

    def dividir(self, numero2):

        if (numero2 == 0):
            return "Tento dividir por 0"
        else:
            resultado = self.valor / numero2
            self.valor = resultado
            return resultado


calculadora = Calculadora()

while (True):
    if (not(calculadora.valor.replace('.','',1).isdigit())):
        calculadora.valor = input("Insira o numero 1: ")

    operador = input("Insira o operador: ")
    n2 = input("Insira o numero 2: ")

    print(calculadora.calcular(n2, operador))