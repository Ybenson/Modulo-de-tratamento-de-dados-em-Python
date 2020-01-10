import re
def remove_espaco(dado):
    dado = " ".join(re.split("\s+", dado, flags=re.UNICODE))
    return (dado)
print(remove_espaco('bruno         faustino    amorim 132456798'))