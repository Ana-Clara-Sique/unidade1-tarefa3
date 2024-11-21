 # Definindo a classe Produto

class Produto:
    def __init__(self,nome,marca,peso,quantidade,valor):
        self.nome = nome
        self.marca = marca
        self.peso = peso 
        self.quantidade = quantidade
        self.preco = preco 


    def exibir_informacoes(self):
       print(f"\nProduto:{self.nome}")
       print(f"\nMarca:{self.marca}")
       print(f"\nPeso:{self.peso} Kg")
       print(f"\nQuantidade:{self.quantidade}unidades")
       print(f"\nPreço(R$):{self.nome}")


produtos = []
for i in range (3):
    print(f"Digite as informações do produto{i + 1}")
    nome =input("Nome:")
    marca =input("Marca:")
    peso = float(input("Peso(em Kg):"))
    quantidade = int(input("Quantidade:"))
    preco = float(input("Digite o Preço(R$):"))     

for produto in produtos:
    produto.exibir_informacoes()     
        