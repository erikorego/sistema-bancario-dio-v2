def menu():
    menu = """
            ===============SISTEMA BANCÁRIO DIO================
            Escolha uma opção:
            1 - Saque
            2 - Depósito
            3 - Extrato
            4 - Cadastrar Cliente
            5 - Listar Clientes
            6 - Cadastrar Nova Conta
            7 - Listar Contas
            0 - Sair
            :"""
    return int(input(menu))

def saque(*, saldo, extrato, limite_saque, numero_saque):
    if numero_saque > 0:
        valor = float(input("Insira o valor que deseja sacar: "))
        if valor > limite_saque:
            print("O limite de valor de saque foi atingido\nOperação Cancelada!")
        elif valor <= saldo:
            saldo -= valor
            extrato += f"SAQUE: R$ {valor: .2f}. Saldo {saldo: .2f}\n"
            numero_saque -= 1
            print("A operação foi realizada com sucesso")
        else:
            print("Saldo insuficiente!")
    else:
        print("""O limite diário de Saques foi atingido.
                  Operação Cancelada!
              """)
    return saldo, extrato, numero_saque

def deposito (saldo, extrato ,/):
    valor = float(input("Insira o valor que deseja depositar: "))
    if valor < 0:
        print("""
              Você não pode depositar um valor negativo!
              Operação cancelada!
              """)
    elif valor == 0:
        print('''
              Operação Inválida!
              Você não pode depositar 0 reais
              Operação cancelada!
              ''')
    else:
        saldo += valor
        extrato += f"DEPÓSITO: R$ {valor: .2f}. Saldo {saldo: .2f}\n"
        print("Operação realizada com sucesso!")
    return saldo, extrato

def exibir_extrato(saldo,/,*,extrato):
    if extrato == "":
        return print("Nenhuma operação realizada")
    else:
        return print(extrato)    

def criar_cliente(lista_de_clientes):
    cpf = int(input("Insira seu CPF (somente números): "))
    cliente = check_cpf(cpf, lista_de_clientes)

    if cliente:
        print("\nUm cliente com esse CPF já está cadastrado!!")
        return
    
    nome = input("Insira seu nome completo: ")
    print("Insira sua data de nascimento: ")
    dia = int(input("\ndia: "))
    mes = int(input("\nmês: "))
    ano = int(input("\nano: "))
    data_de_nascimento = f'{dia}/{mes}/{ano}'
    print("Agora informe seu endereço: ")
    logradouro = input("\nQual o seu logradouro?\n")
    numero = input("\nE o número da sua casa/apartamento?\n")
    bairro = input("\nEm que bairro você mora?\n")
    cidade = input("\nQual a cidade que você mora?\n")
    estado = input("\n Em que estado você mora (apenas a sigla)?\n")
    endereco = f'{logradouro},{numero} - {bairro} - {cidade}/{estado}'

    lista_de_clientes.append({"nome": nome, "data_de_nascimento": data_de_nascimento, "cpf": cpf, "endereco": endereco})
    print("Cliente cadastrado com sucesso!")

def check_cpf(cpf, lista_de_clientes):
    lista_filtrada = [cliente for cliente in lista_de_clientes if cliente["cpf"] == cpf]
    return lista_de_clientes[0] if lista_filtrada else None

def main():

    limite_de_saques_diarios = 3
    VALOR_LIMITE_DE_SAQUE = 500
    saldo = 0
    extrato = ''
    lista_de_clientes = []
    contas = []

    while True:
        opcao = menu()
        if opcao == 1:
            saldo, extrato, limite_de_saques_diarios = saque(saldo=saldo, limite_saque=VALOR_LIMITE_DE_SAQUE, numero_saque=limite_de_saques_diarios, extrato=extrato)
        elif opcao == 2:
            saldo, extrato = deposito(saldo, extrato)
        elif opcao == 3:
            exibir_extrato(saldo, extrato=extrato)
        elif opcao == 4:
            criar_cliente(lista_de_clientes)

        elif opcao == 0:
            break
        else:
            print('''
                Opção Inválida!
                Tente novamente.
                ''')

main()