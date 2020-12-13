
def azul(palavra):
    print(f'\u001b[34m {palavra} \u001b[0m')
def amarelo(palavra):
    print(f'\u001b[33m {palavra} \u001b[0m')
def verde(palavra):
    print(f'\u001b[32m {palavra} \u001b[0m')
def vermelha(palavra):
    print(f'\u001b[31m {palavra} \u001b[0m')

def separa_por_linha():
    print('-'*82)

def apresenta_programa():
    '''
    CORES ANSII
    vermelha \u001b[31m
    verde \u001b[32m
    amarela \u001b[33m
    azul \u001b[34m

    \u001b[0m'
    '''
    
    azul(separa_por_linha())
    print("""\u001b[32m
        ██ ███    ██ ██    ██ ██ ███████ ████████  █████        ███    ███ ███████ 
        ██ ████   ██ ██    ██ ██ ██         ██    ██   ██       ████  ████ ██      
        ██ ██ ██  ██ ██    ██ ██ ███████    ██    ███████ █████ ██ ████ ██ █████
        ██ ██  ██ ██  ██  ██  ██      ██    ██    ██   ██       ██  ██  ██ ██
        ██ ██   ████   ████   ██ ███████    ██    ██   ██       ██      ██ ███████\u001b[0m""")
    print(' '*35 + 'Pronto para investir?')
    azul(separa_por_linha())

    
