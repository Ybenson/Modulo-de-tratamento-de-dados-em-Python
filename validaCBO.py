
def cbo(cbo):
    if cbo in lista_cbo:
        return cbo
    else:
        return None

path = 'C:/Users/ybenson.augustave/Desktop/'
file_read = 'Modulo_DataLoad/cbo.txt'
ref_arquivo = open(path + file_read, 'r')
lista_cbo = ref_arquivo.read().splitlines()

print(cbo("10315"))
