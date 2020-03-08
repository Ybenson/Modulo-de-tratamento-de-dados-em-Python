# -*- coding: utf-8 -*-
"""
@author: ybenson.augustave
"""

def valida_cnpj(cnpj):

    if len(cnpj) != 14 or not cnpj.isnumeric():
        return False

    verificadores = cnpj[-2:]
    lista_validacao_um = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    lista_validacao_dois = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    'Calcular o primeiro digito verificador'
    soma = 0
    for numero, ind in zip(cnpj[:-1], range(len(cnpj[:-2]))):
        soma += int(numero) * int(lista_validacao_um[ind])

    soma = soma % 11
    digito_um = 0 if soma < 2 else 11 - soma

    soma = 0
    for numero, ind in zip(cnpj[:-1], range(len(cnpj[:-1]))):
        soma += int(numero) * int(lista_validacao_dois[ind])

    soma = soma % 11
    digito_dois = 0 if soma < 2 else 11 - soma

    return verificadores == str(digito_um) + str(digito_dois)

print(valida_cnpj('04276921000132'))