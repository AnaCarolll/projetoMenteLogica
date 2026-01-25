#manipulação de strings

mensagem = "Olá, mundo!"
print(mensagem.upper())  # transforma em maiúsculas
print(mensagem.lower())  # transforma em minúsculas
print(mensagem.replace("mundo", "Python"))  # substitui uma parte da string
print(mensagem.split(","))  # divide a string em uma lista
print("mundo" in mensagem)  # verifica se uma substring está presente
print("Python" not in mensagem)  # verifica se uma substring não está presente
print(mensagem.find("mundo"))  # encontra a posição de uma substring
print(mensagem.index("mundo"))  # encontra a posição de uma substring (levanta erro se não encontrar)
print(mensagem.count("o"))  # conta quantas vezes uma substring aparece
print(mensagem.startswith("Olá"))  # verifica se a string começa com uma substring