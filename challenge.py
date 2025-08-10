import os
from datetime import datetime

def carregar_dados(arquivo):
    """Carrega dados de um arquivo"""
    if not os.path.exists(arquivo):
        return []
    with open(arquivo, 'r') as file:
        return [linha.strip().split('|') for linha in file.readlines()]

def salvar_dados(arquivo, dados):
    """Salva dados em um arquivo"""
    with open(arquivo, 'w') as file:
        for item in dados:
            file.write('|'.join(item) + '\n')

def adicionar_consulta():
    """Permite ao usuário adicionar uma nova consulta"""
    print("\n--- AGENDAR CONSULTA ---")
    data = input("Data (DD/MM/AAAA): ")
    horario = input("Horário (HH:MM): ")
    medico = input("Médico/Especialidade: ")
    
    consultas = carregar_dados('consultas.txt')
    consultas.append([data, horario, medico])
    salvar_dados('consultas.txt', consultas)
    print("Consulta agendada com sucesso!")

def listar_consultas():
    """Lista todas as consultas agendadas"""
    consultas = carregar_dados('consultas.txt')
    
    if not consultas:
        print("\nNenhuma consulta agendada.")
        return
    
    print("\n--- PRÓXIMAS CONSULTAS ---")
    for i, (data, hora, medico) in enumerate(consultas, 1):
        print(f"{i}. Data: {data} - Hora: {hora} - Médico: {medico}")

def adicionar_tarefa():
    """Permite ao usuário adicionar uma nova tarefa"""
    print("\n--- ADICIONAR TAREFA ---")
    descricao = input("Descrição da tarefa: ")
    prioridade = input("Prioridade (A-Alta, M-Média, B-Baixa): ").upper()
    
    tarefas = carregar_dados('tarefas.txt')
    tarefas.append([descricao, prioridade, 'Pendente'])
    salvar_dados('tarefas.txt', tarefas)
    print("Tarefa adicionada com sucesso!")

def listar_tarefas():
    """Lista todas as tarefas"""
    tarefas = carregar_dados('tarefas.txt')
    
    if not tarefas:
        print("\nNenhuma tarefa cadastrada.")
        return
    
    print("\n--- SUAS TAREFAS ---")
    for i, (descricao, prioridade, status) in enumerate(tarefas, 1):
        print(f"{i}. {descricao} - Prioridade: {prioridade} - Status: {status}")

def menu_principal():
    """Exibe o menu principal e gerencia as opções"""
    while True:
        print("\n" + "="*40)
        print(" SISTEMA DE GERENCIAMENTO ".center(40))
        print("="*40)
        print("1. Agendar Consulta")
        print("2. Ver Consultas")
        print("3. Adicionar Tarefa")
        print("4. Ver Tarefas")
        print("5. Sair")
        print("="*40)
        
        opcao = input("Escolha uma opção (1-5): ")
        
        if opcao == '1':
            adicionar_consulta()
        elif opcao == '2':
            listar_consultas()
        elif opcao == '3':
            adicionar_tarefa()
        elif opcao == '4':
            listar_tarefas()
        elif opcao == '5':
            print("\nObrigado por usar o sistema! Até logo!")
            break
        else:
            print("Opção inválida. Por favor, escolha de 1 a 5.")

if __name__ == "__main__":
    # Cria os arquivos se não existirem
    if not os.path.exists('consultas.txt'):
        open('consultas.txt', 'w').close()
    if not os.path.exists('tarefas.txt'):
        open('tarefas.txt', 'w').close()
    
    print("Bem-vindo ao Sistema de Gerenciamento!")
    menu_principal()