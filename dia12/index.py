#treatmento de erros e exceções
#criar progrtas, que precuisa estra a prova de falhas

#try, except, ele, finally

#execept => tratar o erro
# else => executa quando não há erro
# finally => sempre executa


arquivo = open("dados.txt", "r" )
conteudo = arquivo.read()

try:
    arquivo = open("dados.txt", "r")
    conteudo = arquivo.read()
except FileNotFoundError:
    print("O arquivo não existe.")
else:
    print("Arquivo lido.")
    print(conteudo)
finally:
    print("Operação finalizada.")
    if 'arquivo' in locals():
        arquivo.close()
        print("Arquivo fechado.")
try:
    numero = int(input("Digite um número: "))
    resultwado = 100 / numero
except ValueError:
    print("Valor inválido! Por favor, digite um número inteiro.")
except ZeroDivisionError:
    print("Divisão por zero não é permitida.")
else:
    print("Número digitado com sucesso.", resultwado)