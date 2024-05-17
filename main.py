menu = """

[d] Depositar 
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 0
valor = 0
limite = 500
extrato = []
numero_de_saques = 0
LIMITE_DE_SAQUES = 3

while True:
    escolha = input(menu)

    if escolha == "d":
        while True:
            valor = float(input("Digite o valor que deseja inserir\n"))
            
            if valor < 0:
                print("O valor não pode ser negativo, digite outro valor.\n")
            
            elif valor == 0:
                print("Não tem como adicionar R$0,00. Por vaor, escolha outro valor.\n")
            else:
                saldo += valor
                extrato.append(f"Valor depositado de R${valor}")
                break 
        
         

    
    elif escolha == "s":
        if numero_de_saques == 3:
            print("Você atingiu seu limite de saques.\n")
            
        else:
            while True:
                valor = float(input("Digite o valor que deseja sacar\n"))

                if valor > 500:
                    print("Só é possível sacar no maximo R$500,00. Por favor, escolha outro valor.\n")

                elif valor == 0:
                    print("Não é possível sacar R$0,00. Escolha outro valor.\n")
                
                elif valor < 0:
                    print("Não é possível sacar um valor negativo. Escolha outro valor.\n")
                
                elif valor > saldo:
                    print("você não tem saldo suficiente.\n")
                    
                else:
                    saldo -= valor 
                    numero_de_saques += 1 
                    extrato.append(f"Valor sacado de R${valor}")  
                    break   

    
    elif escolha == "e":
        print(*extrato, sep="\n")
        print("saldo total:", saldo)
    
    elif escolha == "q":
        break 
    
    else:
        print("opção invalida, escolha novamente.")