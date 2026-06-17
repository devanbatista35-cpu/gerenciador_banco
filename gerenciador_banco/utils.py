'''
Funções para estilizar os titulos, ja que o programa roda somente no terminal
'''

def linha():
    print("-" * 30)

def titulo(txt):
    linha()
    print(txt.center(30))
    linha()
    print()