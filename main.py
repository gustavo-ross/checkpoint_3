from funcoes import limpar_tela, enter_time, imprimir_logo
from Cliente import Cliente
from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupanca
from Banco import Banco

def ler_valor_monetario(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            print("⚠️ ERRO: Por favor, digite um valor numérico válido (ex: 50.50).")

def menu_logado(banco, cc, cp):
    while True:
        limpar_tela()
        imprimir_logo()
        print(f"Bem-vindo(a), {cc.cliente.nome} | CPF: {cc.cliente.cpf}\n")
        print("=" * 45)
        print("💰 SALDOS:")
        print(f"Corrente: R$ {cc.get_saldo():.2f} | Poupança: R$ {cp.get_saldo():.2f}")
        print("=" * 45)
        print("[ 1 ] 📥 Depositar")
        print("[ 2 ] 📤 Sacar (Conta Corrente)")
        print("[ 3 ] 💸 Fazer um PIX (Para outro CPF)")
        print("[ 4 ] 🔄 Transferência Interna (Corrente <-> Poupança)")
        print("[ 5 ] 📅 Simular fim do mês (Render Poupança)")
        print("[ 0 ] 🚪 Sair da conta")
        print("=" * 45)

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            limpar_tela()
            print("\nOnde deseja depositar?")
            print("[ 1 ] Conta Corrente\n[ 2 ] Conta Poupança")
            destino = input("Escolha: ")
            if destino in ["1", "2"]:
                valor = ler_valor_monetario("Valor do depósito: R$ ")
                if destino == "1": cc.depositar(valor)
                else: cp.depositar(valor)
                banco.salvar_dados()
            else:
                limpar_tela()
                print("\n⚠️ Opção inválida.")
            enter_time()

        elif opcao == "2":
            limpar_tela()
            valor = ler_valor_monetario("\nValor do saque: R$ ")
            if cc.sacar(valor):
                banco.salvar_dados()
            enter_time()

        elif opcao == "3":
            limpar_tela()
            print("\n--- 💸 ÁREA PIX ---")
            num_destino = input("Digite a Chave PIX (CPF do destinatário): ")
            conta_dest = banco.buscar_conta(num_destino + "-CC")
            
            if conta_dest and conta_dest != cc:
                print(f"Destinatário encontrado: {conta_dest.cliente.nome}")
                valor = ler_valor_monetario("Qual o valor do PIX? R$ ")
                # Passamos is_pix=True para ativar a mensagem na classe Conta
                if cc.transferir(valor, conta_dest, is_pix=True):
                    banco.salvar_dados()
            elif conta_dest == cc:
                print("❌ Você não pode fazer um PIX para sua própria Conta Corrente!")
            else:
                print("❌ Chave PIX não encontrada ou inválida.")
            enter_time()

        elif opcao == "4":
            limpar_tela()
            print("\n--- 🔄 TRANSFERÊNCIA INTERNA ---")
            print("De onde o dinheiro vai sair?")
            print("[ 1 ] Conta Corrente -> Para -> Conta Poupança")
            print("[ 2 ] Conta Poupança -> Para -> Conta Corrente")
            sentido = input("Escolha: ")
            
            if sentido in ["1", "2"]:
                valor = ler_valor_monetario("Valor a transferir: R$ ")
                if sentido == "1":
                    # Passamos is_pix=False para a mensagem padrão
                    if cc.transferir(valor, cp, is_pix=False): 
                        banco.salvar_dados()
                else:
                    if cp.transferir(valor, cc, is_pix=False): 
                        banco.salvar_dados()
            else:
                print("⚠️ Opção inválida.")
            enter_time()

        elif opcao == "5":
            limpar_tela()
            print("⏳ Simulando passagem de tempo...")
            cp.render_juros()
            banco.salvar_dados()
            enter_time()

        elif opcao == "0":
            limpar_tela()
            print("Saindo da conta...")
            enter_time()
            break
        else:
            limpar_tela()
            print("⚠️ Opção inválida!")
            enter_time()

def main():
    banco = Banco()

    while True:
        limpar_tela()
        imprimir_logo()
        print("=" * 45)
        print("[ 1 ] 📝 Criar Nova Conta")
        print("[ 2 ] 🔑 Fazer Login")
        print("[ 0 ] ❌ Desligar Sistema")
        print("=" * 45)

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            limpar_tela()
            print("--- ABERTURA DE CONTA ---")
            nome = input("Digite seu nome completo: ")
            cpf = input("Digite seu CPF (apenas números): ")

            if banco.cpf_ja_cadastrado(cpf):
                print("\n❌ Este CPF já possui conta em nosso banco!")
            elif not cpf.isdigit() or len(cpf) < 3:
                print("\n❌ CPF inválido.")
            else:
                senha = input("Crie uma senha de acesso: ")
                
                cli = Cliente(nome, cpf, senha)
                cc = ContaCorrente(numero=f"{cpf}-CC", cliente=cli)
                cp = ContaPoupanca(numero=f"{cpf}-CP", cliente=cli)
                
                banco.adicionar_conta(cc)
                banco.adicionar_conta(cp)
                print(f"\n✅ Parabéns {nome}! Contas criadas com sucesso.")
            enter_time()

        elif opcao == "2":
            limpar_tela()
            print("--- LOGIN ---")
            cpf = input("Digite seu CPF: ")
            
            cc = banco.buscar_conta(f"{cpf}-CC")
            cp = banco.buscar_conta(f"{cpf}-CP")

            if cc and cp:
                # Pede e valida a senha
                senha = input("Digite sua senha: ")
                if cc.cliente.senha == senha:
                    menu_logado(banco, cc, cp)
                else:
                    print("\n❌ Senha incorreta!")
                    enter_time()
            else:
                print("\n❌ Conta não encontrada. Verifique o CPF.")
                enter_time()

        elif opcao == "0":
            limpar_tela()
            print("Sistema encerrado. Obrigado por usar o Terminal Bank!")
            break
            
        else:
            print("\n⚠️ Opção inválida!")
            enter_time()

if __name__ == "__main__":
    main()