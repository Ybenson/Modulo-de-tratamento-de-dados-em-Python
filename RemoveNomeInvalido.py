
import pandas as pd

def remove_nome_invalido(nome):
    verification = any([i in black_list for i in nome.split()])

    if verification == True:
        return None
    else:
        return nome

path = 'C:/Users/ybenson.augustave/Desktop/'
file_read = 'Modulo_DataLoad/DOM_DQ_NOME_INVALIDO.txt'
arquivo = pd.read_csv(path + file_read, sep = ',', encoding='utf8',
                          dtype = {'ID':str, 'DS_NOME':str, 'DS_TIPOPESSOA':str, 'CD_LOCALIZACAO':str, 'DS_ATIVO':str, 'DS_TIPO':str})
black_list = arquivo.loc[:,"DS_NOME"]
black_list = list(black_list)

print(remove_nome_invalido("YBENSON AUGUSTAVE"))









