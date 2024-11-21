 #Definindo classe pessoa

class Pessoa:

    def __init__(self,nome,idade,altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura 
     
    def exibir_informacoes(self):
        print(f"Nome:{self.nome}")
        print(f"Idade:{self.idade}")
        print(f"Altura:{self.altura}") 


nome = input("Digite seu nome:")
idade = int(input("Digite sua idade:"))
altura = float(input("Digite sua altura:"))


pessoa1 = Pessoa(nome , idade , altura)


pessoa1.exibir_informacoes()



