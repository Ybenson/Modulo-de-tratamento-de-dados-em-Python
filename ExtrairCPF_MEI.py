from ValidaCPF import validate_cpf
import re

def extrairCPF(CPF_MEI):
    CPF_MEI = re.sub('[^0-9]','',CPF_MEI)
    if validate_cpf(CPF_MEI) ==True:
        return CPF_MEI
    else:
        return None
print(extrairCPF("Ybenson$#%¨¨¨&&&*(&¨%#!@# Augustave 71027943128"))



