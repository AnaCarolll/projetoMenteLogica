# como trabalhar com arquivo e, python

#uyma forma de ler o arquivo todo

with open("dados.txt", "r") as arquivo:
    conteudo = arquivo.read( )
    print(conteudo)