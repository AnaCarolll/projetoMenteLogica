#orientação a objetos
#paradigma procedural: códi objeto 
#classe é o molde do objeto
#instancio um objeto(criar um objeto)

class Pessoa:
    #caracteres e ações do objeto
    #nome = caracteristica do objeto => propriedades, atributos
    #apresentar = ação => método

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos.")

#Pessoa => joaozinho, 33
#self => os valores no objeto
# varivel = Classe()
p1 = Pessoa("Joaozinho", 33)

#metodo => função dentro de uma classe
p1.apresentar()

#Retangulo 
#atributos: largura e altura
#metodos: calcular_area e calcular_perimetro
class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura

    def calcular_perimetro(self):
        return 2 * (self.largura + self.altura)