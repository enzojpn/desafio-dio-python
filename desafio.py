menu = """
    
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [u] Criar usuario
    [c] Criar conta    
    [l] Listar contas
    [q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUES = 3
AGENCIA = "0001"
usuarios = [] 
contas  = []

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

def consultar_extrato():
    print("\n============Extrato Bancario============")
    print("Não existe lancamento no extrato" if not extrato else extrato)
    print(f"SALDO TOTAL:  R$ {saldo:.2f}")
    print("\n============END============")

def cadastrar_usuario(usuarios):
    cpf = input("informe o CPF somente numeros: ")
    usuario = filtrar_usuario(cpf , usuarios)

    if usuario:
        print("usuario ja cadastrado com este cpf")
        return
    
    nome = input("digite o nome: ")
    data_nascimento = input("digite a data de nascimento (dd-mm-aaa): ")
    endereco = input("digite o endereco (logradouro , numero - bairro - municipio e UF ): ")

    usuarios.append({"nome":nome, "data_nascimento": data_nascimento , "cpf": cpf , "endereco": endereco})
    print("usuario criado com sucesso!!" )

def filtrar_usuario(cpf , usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta , usuario):
    cpf = input("informe o CPF somente numeros: ")
    usuario = filtrar_usuario(cpf , usuarios)

    if usuario:
        print("conta criada com sucesso!!")
        return {"agencia" : agencia, "numero_conta": numero_conta , "usuario" : usuario}

    print("usuario nao encontrado, favor cadastrar usuario !!")

def listar_contas():
    for conta in contas:
        linha = f"""\
        Agencia:\t{conta['agencia']} 
        C/C:\t{conta['numero_conta']}       
        Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)

while True :
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("digite o valor do deposito: "))
        saldo , valor = depositar(valor, saldo, extrato)
        

    elif opcao == "s": 
        valor = float(input("digite o valor do saque: "))
        saldo , extrato, numero_saque=  sacar(saldo ,limite ,extrato, numero_saque , LIMITE_SAQUES )
   
    elif opcao == "e":
        consultar_extrato()
    
    elif opcao == "u":
        cadastrar_usuario(usuarios)

    elif opcao == "c":
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)

        if conta:
            contas.append(conta)

    elif opcao == "l":
        print("lista de contas")
        listar_contas()

    elif opcao == "q":
        break
    else:
        print("operacao invalida, por favor selecionar uma das opcoes do menu")