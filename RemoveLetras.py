# -*- coding: utf-8 -*-
"""
@author: ybenson.augustave
"""

import re
def removeletras(dado):
    dado_limpa = re.sub('[^0-9]+', '', dado)
    return (dado_limpa)

print(removeletras("burno12$%¨&*()_3456$%    ¨&*()789bryuno"))