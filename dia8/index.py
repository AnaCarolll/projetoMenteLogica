#funções 
#são a maneira de criar blocos de código reutilizáveis

def saudacao():
    print("Olá, seja bem vindo!")
    print("Espero que você tenha um ótimo dia!")

saudacao()

#paramos de função => de configurar a função para executar a função

def saudacao_com_nome(nome):
    print(f"Olá, {nome}, seja bem vindo!")
    print("Espero que você tenha um ótimo dia!")

saudacao_com_nome("Maria")

#return => retornar valores de dentro da função

def soma(a, b):
    resultado = a + b
    return resultado

soma(3, 5)

x = 10 

soma_x = x +soma(5,5)
print(soma_x)

resultado_soma = soma(20,30)

soma_y = resultado_soma + 100
print(soma_y)
