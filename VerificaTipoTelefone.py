

def qual_tipo(numero):

    if (numero[0:4] in lista_rdio):
        return 'Rádio'

    elif (numero[0]=='7') or (numero[0]=='8') or (numero[0]=='9'):
            return 'Celular'

    elif numero[0]=='2' or numero[0]=='3' or numero[0]=='4' or numero[0]=='5':
        return 'Fixo'
    else:
        None

path = 'C:/Users/ybenson.augustave/Desktop/'
file_read = 'Modulo_DataLoad/PrefixRadio.txt'
ref_arquivo = open(path + file_read, 'r')
lista_rdio = ref_arquivo.read().splitlines()

print(qual_tipo("700083265804"))
