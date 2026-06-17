'''
Arquivo que armazena e cria o banco de dados em jason
'''

import json
import os
from funcoes import Conta

ARQUIVO = "contas.json"

def salvar_contas(contas):
    with open(ARQUIVO, "w") as f:
        json.dump({nome: conta.to_dict() for nome, conta in contas.items()}, f, indent=4)

def carregar_contas():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r") as f:
            data = json.load(f)
            return {nome: Conta.from_dict(conta) for nome, conta in data.items()}
    return {}