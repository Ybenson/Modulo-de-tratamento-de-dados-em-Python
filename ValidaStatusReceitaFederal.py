def valida_status_RC(status):

    status = status.upper()

    if status == 'CANCELADA':
        return status
    elif status == 'NULA':
        return status
    elif status == 'PENDENTE DE REGULARIZAÇÃO':
        return status
    elif status == 'SUSPENSA':
        return status
    elif status == 'REGULAR':
        return status
    else:
        return None
print(valida_status_RC('PenDENTe DE REGULARIZAÇÃO'))
