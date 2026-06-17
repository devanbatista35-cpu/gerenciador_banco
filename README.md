# 🏦 Devan's Bank

O **Devan's Bank** é uma aplicação de simulação de sistema bancário baseada em terminal desenvolvida em Python. O projeto foca na persistência de dados local de forma leve e em boas práticas de modularização de código, ideal para demonstrar habilidades em lógica de programação, manipulação de arquivos e Orientação a Objetos.

---

## 🎯 Funcionalidades Principais

* **Gestão de Contas:** Criação, autenticação de segurança e exclusão definitiva de contas de utilizadores.
* **Operações Bancárias:** Consulta de saldo atualizado, depósitos e levantamentos.
* **Regras de Negócio Implementadas:** Restrição rígida de um limite máximo de até 3 levantamentos diários por sessão, além da validação de fundos insuficientes.
* **Extrato Detalhado:** Registo em tempo real com data e hora exata de todas as movimentações da conta.
* **Exportação de Dados:** Opção de exportar o extrato completo da conta em formato de ficheiro de texto (`.txt`).

---

## 💪 Pontos Fortes do Projeto

1. **Persistência de Dados Inteligente (NoSQL JSON):** Em vez de redefinir o estado da aplicação sempre que o programa fecha, o sistema guarda e carrega dinamicamente as informações das contas num ficheiro local `contas.json` utilizando serialização de dicionários.
2. **Arquitetura Modular Limpa:** O código foi dividido cirurgicamente seguindo o princípio da responsabilidade única:
   * `main.py`: Controla o fluxo de navegação e os menus de interação.
   * `funcoes.py`: Centraliza a regra de negócio e abstração da entidade `Conta` através de Programação Orientada a Objetos (POO).
   * `validacoes.py`: Camada de segurança dedicada a validar inputs e acessos.
   * `banco.py`: Camada de persistência (I/O de dados).
   * `utils.py`: Auxiliares de interface visual e estilização do terminal.
3. **Segurança de Inputs:** Mecanismo robusto contra inserções vazias ou espaços em branco que poderiam quebrar o fluxo (`validar_campos`), além da formatação automática de nomes com a capitalização correta (`.capitalize()`).
4. **UX no Terminal:** Interface amigável utilizando elementos visuais dinâmicos (como linhas delimitadoras, centralização de títulos e emojis de feedback) para melhorar a experiência do utilizador na consola.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.x
* **Módulos Nativos:** `json` (persistência), `os` (verificação de ficheiros) e `datetime` (carimbo de data/hora).

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
Ter o Python 3 instalado na sua máquina.

### Passos para Execução
1. Faça o clone deste repositório ou descarregue os ficheiros.
2. Certifique-se de que todos os ficheiros (`main.py`, `funcoes.py`, `validacoes.py`, `banco.py`, `utils.py` e `contas.json`) estão na mesma diretoria.
3. Abra o terminal na diretoria do projeto e execute o comando:
   ```bash
   python main.py
