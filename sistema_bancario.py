limite_de_saques_diarios = 3
VALOR_LIMITE_DE_SAQUE = 500
saldo = 0
extrato = ''

menu = """
===============SISTEMA BANCÁRIO DIO================
Escolha uma opção:
1 - Saque
2 - Depósito
3 - Extrato
0 - Sair
:"""

while True:
    opcao = int(input(menu))
    if opcao == 1:
        if limite_de_saques_diarios > 0:
            valor = float(input("Insira o valor que deseja sacar: "))
            if valor > 500:
                print("O limite de valor de saque foi atingido\nOperação Cancelada!")
            elif valor <= saldo:
                saldo -= valor
                extrato += f"SAQUE: R$ {valor: .2f}. Saldo {saldo: .2f}\n"
                limite_de_saques_diarios -= 1
                print("A operação foi realizada com sucesso")
            else:
                print("Saldo insuficiente!")
        else:
            print("""O limite diário de Saques foi atingido.
                  Operação Cancelada!
""")
    elif opcao == 2:
        valor_deposito = float(input("Insira o valor que deseja depositar: "))
        if valor_deposito < 0:
            print("""
                  Você não pode depositar um valor negativo!
                  Operação cancelada!
""")
        elif valor_deposito == 0:
            print('''
                  Operação Inválida!
                  Você não pode depositar 0 reais
                  Operação cancelada!
''')
        else:
            saldo += valor_deposito
            extrato += f"DEPÓSITO: R$ {valor_deposito: .2f}. Saldo {saldo: .2f}\n"
            print("Operação realizada com sucesso!")
    elif opcao == 3:
        if extrato == "":
            print("Nenhuma operação realizada")
        else:
            print(extrato)
            pausa = input("aperte qualquer botão para continuar... ")
    elif opcao == 0:
        break
    else:
        print('''
            Opção Inválida!
            Tente novamente.
              ''')
    