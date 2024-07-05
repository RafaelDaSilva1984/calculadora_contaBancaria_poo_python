

def mostrar_menu():
    print("\n********************Calculadora_Python_********************")
    print("""
    Escolha uma Opção Matemática:
        [1]= Soma,
        [2]= Subtração,
        [3]= Multiplicação,
        [4]= Divisão\n
    """)
    opcao = int(input("Digite a opção: "))
    while opcao not in [1, 2, 3, 4]:
        print("Erro na escolha de Opção, deve ser: 1, 2, 3, 4 ")
        opcao = int(input("Digite a opção correta: "))
    return opcao

def executar_operacao(opcao, n1, n2):
    if opcao == 1:
        result = n1 + n2
        print(f"Soma: {n1} + {n2} = {result}")
    elif opcao == 2:
        result = n1 - n2
        print(f"Subtração: {n1} - {n2} = {result}")
    elif opcao == 3:
        result = n1 * n2
        print(f"Multiplicação: {n1} * {n2} = {result}")
    elif opcao == 4:
        if n2 != 0:
            result = n1 / n2
            print(f"Divisão: {n1} / {n2} = {result}")
        else:
            while n2 == 0:
                print("Erro de divisor, deve ser maior que zero '0'")
                n2 = float(input("Digite Novamente o valor 2: "))
            result = n1 / n2
            print(f"Divisão: {n1} / {n2} = {result}")
            
def loop_iteracao():
    continuar_calculadora = input("Deseja continuar usando Calculadora? S = 'Sim' e N = 'Não'").upper()
    while continuar_calculadora not in ["S", "N"]:
        print("Erro: Resposta inválida. Deve ser 'S' para Sim ou 'N' para Não.")
        continuar_calculadora = input("Deseja continuar usando Calculadora? S = 'Sim' e N = 'Não'").upper()
    return continuar_calculadora

# Uso das funções em loop
continuar_calculadora = "S"
while continuar_calculadora == "S":
    opcao = mostrar_menu()
    valor1 = float(input("Digite valor 1: "))
    valor2 = float(input("Digite valor 2: "))
    executar_operacao(opcao, valor1, valor2)
    continuar_calculadora = loop_iteracao()
print("Finalizado pelo Usuário..")
