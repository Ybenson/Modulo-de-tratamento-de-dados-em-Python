def cd_cnae(cnae):
    if cnae in lista_cnae:
        return cnae
    else:
        return None

path = 'C:/Users/ybenson.augustave/Desktop/'
file_read = 'Modulo_DataLoad/cd_cnae.txt'
ref_arquivo = open(path + file_read, 'r')
lista_cnae = ref_arquivo.read().splitlines()

print(cd_cnae("6421200"))








