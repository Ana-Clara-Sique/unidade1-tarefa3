#Definindo classe calculadora

class Calculadora:
    def soma(self, a,b):
        return a + b
    def sub(self, a,b):
        return a - b
    def multi(self , a ,b):
        return a * b
    def div(self, a ,b):
        if b != 0:
            return a/b
        else:
            return "Erro.Divisão por zero."

calc = Calculadora()

num1 = float(input("Digite um número:"))
num2 = float(input("Digite um número:"))

print(f"Soma:{calc.soma(num1 , num2)}")
print(f"Subtraçao:{calc.sub(num1, num2)}")
print(f"Multiplicação: {calc.multi(num1 , num2)}")
print(f"Divisão:{calc.div(num1, num2)}")
