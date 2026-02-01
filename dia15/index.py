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
