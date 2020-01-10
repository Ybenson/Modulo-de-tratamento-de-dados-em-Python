
def valida_porte_empresa(porte):

    porte = porte.upper()

    if porte == 'EMPRESA DE GRANDE PORTE':
        return porte
    elif porte == 'EMPRESA DE MEDIO PORTE':
        return porte
    elif porte=='EPP' or porte== 'EMPRESA DE PEQUENO PORTE':
        return porte
    elif porte == 'MICROEMPRESA':
        return porte
    elif porte == 'MICROEMPREENDEDOR INDIVIDUAL':
        return porte
    else:
        return None

print(valida_porte_empresa('MiCroempreendedor indiVidUal'))
