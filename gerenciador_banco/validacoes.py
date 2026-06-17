'''
Arquivo que realiza as verificações
'''

from funcoes import Conta
from banco import salvar_contas


def validar_campos(*campos):
    for campo in campos:
        if campo.strip() == "":
            return False
    return True

def criar_conta(contas, nome, senha):
    if not validar_campos(nome, senha):
        return "❌ Erro: nome e senha não podem ser vazios."
    if nome in contas:
        return "Já existe uma conta com esse nome."
    contas[nome] = Conta(nome, senha, 0)
    salvar_contas(contas)
    return f"\nConta criada para {nome}.✅"

def autenticar(contas, nome, senha):
    if not validar_campos(nome, senha):
        print("❌ Erro: nome e senha não podem ser vazios.")
        return None
    if nome in contas and contas[nome].senha == senha:
        return contas[nome]
    print("⛔ Conta não encontrada ou senha incorreta.")
    return None

def deletar_conta(contas, nome, senha):
    if not validar_campos(nome, senha):
        return "❌ Erro: nome e senha não podem ser vazios."
    if nome in contas and contas[nome].senha == senha:
        confirmacao = input(f"\n⚠️ Tem certeza que deseja deletar a conta de {nome}? (S/N): ")
        if confirmacao.strip().lower() == "s":
            del contas[nome]
            salvar_contas(contas)
            return f"\nConta de {nome} deletada.✅"
        else:
            return "Operação cancelada. A conta não foi deletada."
    return None