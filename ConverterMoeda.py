import locale
import VerificarSeNumero
def converte_moeda(valor):
    VerificarSeNumero
    if True:
        if valor.isdecimal():
            valor= int(valor)
            locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
            valor = locale.currency(valor, grouping=True, symbol=None)
        else:
            return None

    else:
        return None
    return ('R$ %s' % valor)

print(converte_moeda("1077700098"))