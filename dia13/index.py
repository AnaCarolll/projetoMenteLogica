# como trabalhar com arquivo e, python

#uyma forma de ler o arquivo todo

with open("dados.txt", "r") as arquivo:
    conteudo = arquivo.read( )
    print(conteudo)

#ler arquivo linha por linha
with open('dados.txt', 'r') as arquivo:
    for linha in arquivo:
        print(linha.strip())  # strip() remove espaços em branco extras e quebras de linha
        break
#escrever em um arquivo
with open("saida.txt", "w") as arquivo:
    arquivo.write("Esta é uma nova linha no arquivo.\n")
    arquivo.write("Outra linha adicionada ao arquivo.\n")

#r - read - ler
#w - write - escrever (apaga o conteudo anterior)
#a - append - adicionar conteudo ao final do arquivo
#x - create - criar um arquivo (gera erro se o arquivo ja existir)

with open("contatos.csv", "w") as arquivo:
    arquivo.write("nome,telefone,email\n")
    arquivo.write("João Silva,123456789,jooao@email.com\n")


import json

dados = {
    "nome": "Ana Maria",
    "idade": 28,
    "cidade": "São Paulo"
}

with open("dados.json", "w") as arquivo_json:
    json.dump(dados, arquivo_json, indent=2)
