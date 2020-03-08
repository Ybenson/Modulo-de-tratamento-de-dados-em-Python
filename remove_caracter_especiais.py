# -*- coding: utf-8 -*-
"""
@author: ybenson.augustave
"""
import re
def remove_caracter_especial(dado):
    dado_limpa = re.sub('[^A-Za-z0-9]+', '', dado)
    return (dado_limpa)

print(remove_caracter_especial("bru@#$%¨&*()no!@#$%¨&*()_"))