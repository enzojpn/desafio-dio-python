menu = """
    
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUES = 3

def depositar(valor , saldo , extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito = {valor:.2f}\n"
        print(f"saldo {saldo}" )
    else:
        print("valor negativo - deposito invalido")
    return saldo , extrato

def sacar(saldo ,limite ,extrato, numero_saque , LIMITE_SAQUES ):
    if numero_saque == LIMITE_SAQUES:
        print("limite de saque diario estourou")
    elif valor > 500:
        print("ultrapassou o limite de 500 reais por saque")
    elif valor > saldo:
        print("saldo insuficiente")
    else:
        saldo -= valor
        numero_saque += 1            
        extrato += f"Saque = {valor:.2f}\n"
        print(f"valor {saldo}")
    return saldo , extrato , numero_saque

while True :
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("digite o valor do deposito: "))
        saldo , valor = depositar(valor, saldo, extrato)
        

    elif opcao == "s": 
        valor = float(input("digite o valor do saque: "))
        saldo , extrato, numero_saque=  sacar(saldo ,limite ,extrato, numero_saque , LIMITE_SAQUES )
   
    elif opcao == "e":
        print("\n============Extrato Bancario============")
        print("Não existe lancamento no extrato" if not extrato else extrato)
        print(f"SALDO TOTAL:  R$ {saldo:.2f}")
        print("\n============END============")
    elif opcao == "q":
        break
    else:
        print("operacao invalida, por favor selecionar uma das opcoes do menu")