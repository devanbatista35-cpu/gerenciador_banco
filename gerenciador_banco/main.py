'''
Arquivo principal do projeto, responsável por iniciar a aplicação e definir as rotas.
'''
from banco import carregar_contas, salvar_contas
from validacoes import criar_conta, autenticar, deletar_conta
from utils import titulo

contas = carregar_contas()


def menu():
    print()
    titulo("🏦 Devan's Bank")
    print("Aqui você pode criar uma conta,acessar sua conta, realizar transações e muito mais!\n")
    print("Escolha uma opção para começar:")
    print("1. Acessar Conta")
    print("2. Criar conta")
    print("3. Deletar conta")
    print("0. Sair\n")

def sub_menu():
    print(f"\n--- Conta de {nome} ---")
    print("1 - Mostrar saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Ver extrato")
    print("5 - Salvar extrato em TXT")
    print("0 - Voltar")



while True:
    menu()
    opcao = input("Escolha a opção desejada: ")

 # Acessando uma conta existente
    if opcao == "1":
        nome = input("Nome do titular: ")
        nome = nome.capitalize()
        senha = input("Senha: ")
        conta = autenticar(contas, nome, senha)
        if conta:
            while True:
                sub_menu()
                opcao = input("Escolha: ")
                if opcao == "1":
                    print(conta.mostrar_saldo())
                elif opcao == "2":
                    valor = float(input("Valor Depósito: "))
                    conta.depositar(valor)
                    salvar_contas(contas)
                    print("Depósito realizado.✅")
                elif opcao == "3":
                    valor = float(input("Valor Saque: "))
                    if conta.sacar(valor):
                        print("Saque realizado.✅")
                    else:
                        print("Saldo insuficiente.")
                    salvar_contas(contas)
                elif opcao == "4":
                    conta.ver_extrato()
                elif opcao == "5":
                    conta.salvar_extrato_txt()
                elif opcao == "0":
                    break
        else:
            print("Conta não encontrada ou senha incorreta.")
    
 # Criando uma conta
    elif opcao == "2":
        nome = input("Nome do titular: ")
        nome = nome.capitalize()
        senha = input("Senha da conta: ")
        print(criar_conta(contas, nome, senha))

 # Deletar conta
    elif opcao == "3":
        nome = input('Digite o seu nome: ')
        nome = nome.capitalize()
        senha = input('Digite a sua senha: ')
        print(deletar_conta(contas, nome, senha))

 # Sair do sistema
    elif opcao == "0":
        print('Encerrando o programa...')
        break

    else:
        print('Escolha um opção válida!')



    
