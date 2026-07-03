menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: R$"))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f}\n"
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("Valor inválido para depósito.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: R$"))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação não foi realizada seu saldo é insuficiente.")
        elif excedeu_limite:
            print("Operação não pode ser realizada pois o limite máximo por saque é R$500.")
        elif excedeu_saques:
            print("Operação incocluida pois o Limite diário de 3 saques ja foi atingido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            numero_saques += 1
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
        else:
            print("Valor inválido para saque.")

    elif opcao == "e":
        print("\n--- Extrato ---")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo atual: R${saldo:.2f}")
        print("----------------")

    elif opcao == "q":
        print("\nEncerrando o sistema bancário...")
        print("\n--- Extrato Final ---")
        print("Não foram concluída as movimentações." if not extrato else extrato)
        print(f"Saldo final: R${saldo:.2f}")
        print("----------------")
        break

    else:
        print("não foi possível concluir a operação, tente novamente.")
