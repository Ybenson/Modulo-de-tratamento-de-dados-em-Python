
import re
def so_letras(onlyLeters):
    return re.sub("[^A-Za-z]",'',onlyLeters)

print(so_letras("123Ybenson@#$%¨&*()_)(*¨%$AU@#$%¨&*()(*&¨%GUSTAVE1234"))

