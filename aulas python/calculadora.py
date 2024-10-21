from time import sleep
print("   *** CALCULADORA ***  ")

while True:
    try: 
        print("Adição = 1 \nSubtração = 2 \nMultiplicação = 3\nDivisão = 4 ")
        entrada = int(input("Escolha sua opção: ").strip())
        if entrada < 1 or entrada > 4:
            print("Escolha inválida, por favor selecione entre 1 e 4.")
            sleep(0.5)
            continue
        
        print("Digite dois números: ")
        x = float(input().strip())
        y = float(input().strip())
        
        if entrada == 1:
            operacao = "+"
            resultado = x + y
            
        elif entrada == 2:
            operacao = "-"
            resultado = x - y
            
        elif entrada == 3:
            operacao = "x"
            resultado = x * y
            
        elif entrada == 4:
            if y != 0:  
                operacao = "/"
                resultado = x / y
            else:
                print("Erro: Divisão por zero não é permitida.")
                sleep(0.5)
                continue
            
        else:
            print("Escolha inválida:")
            sleep(2)
            continue
            
        print(f"Resultado: {x} {operacao} {y} = {resultado:.1f}")
        sleep(0.5)
        sair = input("Quer sair?[S]im: ").lower().strip().startswith("s")
        if sair is True:
            sleep(0.5)
            break
    except ValueError:
        print("Erro: Por favor, insira uma entrada válida.")
        sleep(0.5)
        continue

        
    
    
    
        

