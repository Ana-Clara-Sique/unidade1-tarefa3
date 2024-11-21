# Definindo a classe media

class Media:
    def mediaSimples(self, a,b):
         return (a + b)/2
    
    def mediaPonderada(self, a , b):
         peso_a = 3
         peso_b =4
         return (a * peso_a + b * peso_b)/(peso_a + peso_b)
    
media_calculadora  = Media()

nota1 = float(input("Digite sua nota:"))
nota2 = float(input("Digite sua nota:"))

print(f"Média Simples: {media_calculadora.mediaSimples(nota1 , nota2)}")
print(f"Média Ponderada: {media_calculadora.mediaPonderada(nota1 , nota2)}")

