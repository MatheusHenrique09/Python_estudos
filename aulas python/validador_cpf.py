import re

# Solicita o CPF ao usuário
cpf_enviado_usuario = input("Digite o CPF (apenas números): ")

# Verifica se a entrada contém exatamente 11 dígitos numéricos
if not cpf_enviado_usuario.isdigit() or len(cpf_enviado_usuario) != 11:
    print("Por favor, insira exatamente 11 dígitos numéricos.")
else:
    # Remove qualquer caractere não numérico (embora já tenha verificado)
    cpf_enviado_usuario = re.sub(r'[^0-9]', '', cpf_enviado_usuario)
    
    # Extrai os primeiros 9 dígitos
    nove_digitos = cpf_enviado_usuario[:9]
    
    # Cálculo do primeiro dígito verificador
    contador_regressivo_2 = 10
    resultado_digito1 = 0
    for numero_cpf in nove_digitos:
        resultado_digito1 += int(numero_cpf) * contador_regressivo_2  
        contador_regressivo_2 -= 1
    digito_1 = (resultado_digito1 * 10) % 11 
    digito_1 = digito_1 if digito_1 <= 9 else 0

    # Cálculo do segundo dígito verificador
    novos_digitos_2 = nove_digitos + str(digito_1)
    contador_regressivo_2 = 11
    resultado_digito_2 = 0
    for numero_cpf in novos_digitos_2:
        resultado_digito_2 += int(numero_cpf) * contador_regressivo_2  
        contador_regressivo_2 -= 1
    digito_2 = (resultado_digito_2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0

    # CPF gerado com dígitos verificadores
    cpf_gerado_calculo = f'{nove_digitos}{digito_1}{digito_2}'

    # Verifica se o CPF gerado é igual ao CPF enviado pelo usuário
    if cpf_gerado_calculo == cpf_enviado_usuario:
        print(f'{cpf_enviado_usuario} é válido')
    else:
        print('CPF inválido')


