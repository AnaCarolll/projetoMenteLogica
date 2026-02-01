#gerenciador de tarefas
import os 
import json



#gerador de id unico
def gerar_id(tarefas):
    if tarefas:
        return max(tarefa['id'] for tarefa in tarefas) + 1
    else:
        return 1

# funcao para carregar tarefas
def carregar_tarefas():
    if os.path.exists('tarefas.json'):
        with open ('tarefas.json', 'r') as arquivo:
            return json.load(arquivo)
        return []

# funcao para listar tarefas
def listar_tarefas(tarefas):
    print("=== LISTA DE TAREFAS ===")
    for tarefa in tarefas:
        print(f"ID: {tarefa['id']}, Título: {tarefa['titulo']}, Concluída: {tarefa['concluida']}")


#adiconar tarefa 

def adcionar_tarefa(tarefas):
    print("Adiconar nova Tarefa")
    titulo = input("Título da tarefa: ")
    descricao = input("Descrição da tarefa: ")
    tarefa ={ 
        "id": gerar_id(tarefas),
        "titulo": titulo,
        "descricao": descricao,
        "concluida": False
    }
    tarefas.append(tarefa)
    salvar_tarefas(tarefas)
print("Tarefa adicionada com sucesso!")

# salvar tarefas em arquivo json
def salvar_tarefas(tarefas):
    with open('tarefas.json', 'w') as arquivo:
        json.dump(tarefas, arquivo, indent=4)


#menu principal
def menu():
    print("=== GERENCIADOR DE TAREFAS ===")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Concluir Tarefa")
    print("4. Remover Tarefa")
    print("5. Sair")
    return input("Escolha uma opção: ")

#concluir tarefa
def concluir_tarefa(tarefas):
    try:
        id_tarefa = int(input("Digite o ID da tarefa para concluir: "))
        for tarefa in tarefas:
            if tarefa['id'] == id_tarefa:
                if tarefa['concluida']:
                    print("Tarefa ja esta concluida.")
                else:
                    tarefa['concluida'] = True
                    salvar_tarefas(tarefas)
                    print("Tarefa concluida com sucesso!")
                    return
        print("Tarefa com o ID especificado nao encontrada.")
    except ValueError:
        print("ID invalido. Por favor, digite um numero inteiro.")

#remover tarefa
def remover_tarefa(tarefas):
    try:
        id_tarefa = int(input("Digite o ID da tarefa para remover: "))
        for i, tarefa in enumerate(tarefas):
            if tarefa['id'] == id_tarefa:
                tarefas.pop(i)
                salvar_tarefas(tarefas)
                print("Tarefa removida com sucesso!")
                return
        print("Tarefa com o ID especificado nao encontrada.")
    except ValueError:
        print("ID invalido. Por favor, digite um numero inteiro.")

#Loop
def main():
    tarefas = carregar_tarefas()
    while True:
        opcao = menu()
        if opcao == '1':
            adcionar_tarefa(tarefas)
        elif opcao == '2':
            listar_tarefas(tarefas)
        elif opcao == '3':
            concluir_tarefa(tarefas)
        elif opcao == '4':
            remover_tarefa(tarefas)
        elif opcao == '5':
            print("Saindo do gerenciador de tarefas.")
            break
        else:
            print("Opção inválida.")
            continue
        
        # Após a ação, perguntar se deseja continuar
        if opcao != '5':
            continuar = input("Deseja selecionar alguma outra opção? (s/n): ").lower()
            if continuar == 's':
                continue
            else:
                break
        
if __name__ == "__main__":
    main()
         