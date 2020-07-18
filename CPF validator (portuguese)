cpf  = input('Digite o cpf apenas com números: ')
if len(cpf) == 11:
    def calculo(cpf):
        cpf_por_numero = [int(numero) for numero in cpf]
        d1,d2,d3,d4,d5,d6,d7,d8,d9,*outra_lista = cpf_por_numero
        digito1 = 11 - (d1*10 + d2*9 + d3*8 + d4*7 + d5*6 + d6*5 + d7*4 + d8*3 + d9*2) % 11
        if digito1>9:
            digito1 = 0
        digito2 = 11 - (d1*11 + d2*10 + d3*9 + d4*8 + d5*7 + d6*6 + d7*5 + d8*4 + d9*3 + digito1*2) % 11
        if digito2>9:
            digito2 = 0
        return [digito1, digito2]
    def validacao(digito10,digito11, cpf):
        cpf_por_numero = [int(numero) for numero in cpf]
        if digito10 == cpf_por_numero[9] and digito11 == cpf_por_numero[10]:
            return True
        else:
            return False
    l = calculo(cpf)
    digito1, digito2 = l
    sequencia = cpf == str(cpf[0]) * 11
    if validacao(digito1,digito2,cpf) and not sequencia:
        print('O CPF é válido')
    else:
        print('O CPF é inválido')
else:
    print('Digite um cpf válido')
