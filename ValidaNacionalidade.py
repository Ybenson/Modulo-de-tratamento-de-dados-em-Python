
def valida_nacionalidade(nacionalidade):
    nacionalidade = nacionalidade.upper()
    if nacionalidade in lista_nacionalidade:
        return nacionalidade
    else:
        return None

path = 'C:/Users/ybenson.augustave/Desktop/'
file_read = 'Modulo_DataLoad/cd_nacionalidade.txt'
ref_arquivo = open(path + file_read, 'r')
lista_nacionalidade = ref_arquivo.read().splitlines()
lista_nacionalidade = ([w.upper() for w in lista_nacionalidade])

print(valida_nacionalidade("Brasileiro"))





