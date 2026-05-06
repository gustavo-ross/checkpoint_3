# 🏦 Terminal Bank - Checkpoint 3

O **Terminal Bank** é um sistema de simulação bancária robusto operado via linha de comando (CLI). O projeto foi desenvolvido como parte do Checkpoint 3 da trilha de Python, aplicando conceitos avançados de **Programação Orientada a Objetos (POO)**, persistência de dados e tratamento de exceções.

---

## 🚀 Funcionalidades

- **Persistência de Dados:** Todas as contas, clientes e saldos são salvos em um arquivo `banco.json`, permitindo que os dados sejam mantidos mesmo após fechar o programa.
- **Sistema de Login:** Acesso seguro através de CPF e Senha.
- **Contas Segregadas:** Cada cliente possui automaticamente uma **Conta Corrente** (com taxas de saque) e uma **Conta Poupança** (com rendimentos).
- **Área PIX:** Transferência de valores entre diferentes clientes usando o CPF como chave.
- **Movimentação Interna:** Transferência simplificada de saldo entre a própria Conta Corrente e Poupança do usuário.
- **Rendimento Automático:** Função para simular a passagem de um mês e aplicar o rendimento de 1% (base CDI) sobre o saldo da poupança.
- **Interface Amigável:** Menus numerados e organizados, arte ASCII para o logo e sistema de limpeza de tela para melhor navegação.

---

## 🛠️ Arquitetura do Projeto

O projeto segue os princípios de modularização e os pilares da POO:

1.  **Encapsulamento:** O saldo das contas é protegido (usando `_saldo`), sendo acessado apenas por métodos específicos.
2.  **Herança:** `ContaCorrente` e `ContaPoupanca` herdam a lógica base da classe `Conta`.
3.  **Polimorfismo:** A `ContaCorrente` sobrescreve o método de saque para aplicar uma taxa administrativa de R$ 1,00.

### Estrutura de Arquivos

| Arquivo | Descrição |
| :--- | :--- |
| `main.py` | Ponto de entrada do sistema. Gerencia os menus e o fluxo de interação com o usuário. |
| `Banco.py` | Gerenciador central que controla a lista de contas e a comunicação com o arquivo JSON. |
| `Cliente.py` | Define o molde para os dados do usuário (Nome, CPF e Senha). |
| `Conta.py` | Superclasse que contém as operações financeiras básicas (Depósito, Saque, Transferência). |
| `ContaCorrente.py` | Subclasse de Conta com regra de taxa de saque aplicada. |
| `ContaPoupanca.py` | Subclasse de Conta com lógica para rendimento mensal. |
| `funcoes.py` | Funções utilitárias de sistema (limpar tela, logo ASCII e pausas). |
| `banco.json` | Arquivo onde os dados são armazenados permanentemente. |

---

## ⚙️ Pré-requisitos

- **Python:** Versão 3.12.10 ou superior.
- **Bibliotecas:** O projeto utiliza apenas bibliotecas nativas (`os`, `json`), não sendo necessária a instalação de dependências externas.

---

## 🏃 Como Executar

1.  Certifique-se de que todos os arquivos `.py` estão na mesma pasta.
2.  Abra o seu terminal ou prompt de comando.
3.  Navegue até a pasta do projeto.
4.  Execute o comando:
    ```bash
    python main.py
    ```

---

## 🛡️ Tratamento de Erros e Validações

O sistema foi blindado para evitar interrupções indesejadas:
- **Try/Except:** Utilizado para validar entradas numéricas (valores de depósito/saque), impedindo que o programa quebre caso o usuário digite letras.
- **Verificações de Saldo:** O sistema impede saques ou transferências superiores ao saldo disponível, considerando taxas.
- **Fluxo de Segurança:** Verificação de CPFs duplicados no cadastro e validação de existência de conta no login.

---

## 📝 Exemplo de Uso do Menu Logado
```text
[ 1 ] 📥 Depositar
[ 2 ] 📤 Sacar (Conta Corrente)
[ 3 ] 💸 Fazer um PIX (Para outro CPF)
[ 4 ] 🔄 Transferência Interna (Corrente <-> Poupança)
[ 5 ] 📅 Simular fim do mês (Render Poupança)
[ 0 ] 🚪 Sair da conta
```

---

### Autor
Desenvolvido por **Gustavo Ross**.

--- 

*Dica: Caso você precise resetar o banco de dados para testes, basta deletar o arquivo `banco.json` da pasta do projeto.*