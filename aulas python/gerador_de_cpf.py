from random import randint
# Solicita os primeiros nove dígitos do CPF
nove_digitos ='' 
for i in range(9):
    nove_digitos += str(randint(0,9)) 


# Verifica se a entrada contém apenas números e tem 9 dígitos
if not nove_digitos.isdigit() or len(nove_digitos) != 9:
    print("Por favor, insira exatamente 9 dígitos numéricos.")
else:
    contador_regressivo_2 = 10
    resultado_digito1 = 0
    
    # Calcula o primeiro dígito verificador
    for numero_cpf in nove_digitos:
        resultado_digito1 += int(numero_cpf) * contador_regressivo_2  
        contador_regressivo_2 -= 1
        
    digito_1 = (resultado_digito1 * 10) % 11 
    digito_1 = digito_1 if digito_1 <= 9 else 0

    novos_digitos_2 = nove_digitos + str(digito_1)
    contador_regressivo_2 = 11
    resultado_digito_2 = 0
    
    # Calcula o segundo dígito verificador
    for numero_cpf in novos_digitos_2:
        resultado_digito_2 += int(numero_cpf) * contador_regressivo_2  
        contador_regressivo_2 -= 1

    digito_2 = (resultado_digito_2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0

    cpf_gerado_calculo = f'CPF GERADO: {nove_digitos}{digito_1}{digito_2}'
    print(cpf_gerado_calculo)

