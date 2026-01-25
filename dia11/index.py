#dicionarios
#bjetos em outras linguagens
pessoa = {
    "nome": "Ana",
    "idade": 28,
    "cidade": "São Paulo",
    "profissao": "Engenheira",
    "hobbies": ["leitura", "viagem", "fotografia"]
}

#"nome da chave" : valor

print(pessoa["nome"])
print(f"A {pessoa['nome']} tem {pessoa['idade']} anos e mora em {pessoa['cidade']}.")
print(f"A {pessoa['nome']} gosta de {pessoa['hobbies'][2]}")

#remocao

del pessoa["idade"]
print(pessoa)

#criar uma funçcao que vai adicionar a nota da prova para um aluno

def adicionarNota(aluno):
    aluno["prova_a"] = int(input("Digite a nota da prva A:"))

aluno_teste = {
    "nome":"João"
}

adicionarNota(aluno_teste)
print(aluno_teste)