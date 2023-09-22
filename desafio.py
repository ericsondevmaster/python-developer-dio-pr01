menu = """
_____________________________________
Bem vindo ao autoatendimento DevBank!

[1] - Depositar
[2] - Sacar
[3] - Extrato
[0] - Sair
_____________________________________

Por favor, selecione uma das opções acima: """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor_deposito = float(input("\nInforme o valor que deseja depositar: R$"))

        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: + R${valor_deposito:.2f}\n"
            print("\nDepósito realizado com sucesso!")
        else:
            print("\nValor inválido!")

    elif opcao == "2":
        valor_saque = float(input("\nInforme o valor que deseja sacar: R$"))

        if valor_saque <= 0:
            print("\nValor inválido!")
        elif valor_saque > saldo:
            print("\nSaque não permitido. Saldo insuficiente!")
        elif numero_saques >= LIMITE_SAQUES:
            print("\nNúmero máximo de saques excedido!")
        elif valor_saque > limite:
            print("\nOperação não autorizada! Valor máximo permitido por saque: R$500,00.")
        else:
            saldo -= valor_saque
            numero_saques += 1
            extrato += f"Saque: - R${valor_saque:.2f}\n"
            print("\nSaque realizado com sucesso! Retire o seu dinheiro no local indicado.")

    elif opcao == "3":
        print("\n================ EXTRATO ================")
        if not extrato:
            print("\nNão foram realizadas movimentações!\n")
            print("==========================================")
        else:
            print(extrato)
            print(f"\nSaldo disponível: R$ {saldo:.2f}")
            print("==========================================")

    elif opcao == "0":
        print("\nObrigado por utilizar nosso autoatendimento. Até logo! \n")
        break

    else:
        print("\nOpção inválida!")