'''
Arquivo que armazena as funçoes do sistema
'''
from utils import titulo
from datetime import datetime

class Conta:
    def __init__(self, titular, senha, saldo=0.00):
        self.titular = titular
        self.senha = senha
        self.saldo = saldo
        self.extrato = []
        self.saques_realizados = 0 
    
    # Mostrar saldo
    def mostrar_saldo(self):
        return f"Saldo atual de {self.titular}: {self.saldo:.2f}"

    # Registrar hora exata das movimentações usando o datetime
    def registrar_operacao(self, tipo, valor):
        agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.extrato.append(f"\n{agora} - {tipo} de {valor:.2f} | Saldo: {self.saldo:.2f}")
    
    # Depositar
    def depositar(self, valor):
        valor = float(input('Digite o valor que deseja depositar: '))
        self.saldo += valor
        self.registrar_operacao("Depósito" ,valor)
    
    # Sacar e delimitar que sejam realizados somente 3 saques, mesmo tendo saldo
    def sacar(self, valor):
        if self.saques_realizados >= 3:
            print("Limite de 3 saques atingido. Não é possível sacar mais.")
            return False
        if valor <= self.saldo:
            self.saldo -= valor
            self.saques_realizados += 1
            self.registrar_operacao("Saque", valor)
            return True
        else:
            print("❌ Saldo insuficiente.💰")
            return False
    
    # Ver extrato
    def ver_extrato(self):
        print("Extrato da conta")
        if not self.extrato:
            print("⛔Nenhuma movimentação registrada.")
        else:
            for operacao in self.extrato:
                print(operacao)
        print(f"Saldo final: {self.saldo:.2f}")

    # Gerar um arquivo .txt para enviar o extrato
    def salvar_extrato_txt(self):
        nome_arquivo = f"extrato_{self.titular}.txt"
        with open(nome_arquivo, "w") as f:
            f.write(f"Extrato da conta de {self.titular}\n")
            f.write("="*60 + "\n")
            if not self.extrato:
                f.write("⛔Nenhuma movimentação registrada.\n")
            else:
                for operacao in self.extrato:
                    f.write(operacao + "\n")
            f.write("="*60 + "\n")
            f.write(f"Saldo final: {self.saldo:.2f}\n")
        print(f"Extrato salvo em {nome_arquivo} ✅")

    # Dicionario para guardar as informações
    def to_dict(self):
        return {
            "titular": self.titular,
            "senha": self.senha,
            "saldo": self.saldo,
            "extrato": self.extrato
        }

    @staticmethod
    def from_dict(data):
        conta = Conta(data["titular"], data["senha"], data["saldo"])
        conta.extrato = data["extrato"]
        return conta


    

    
    
