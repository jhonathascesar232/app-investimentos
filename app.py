from utilidades import apresenta_programa, verde, separa_por_linha

from termcolor import colored
from pathlib import Path
from playsound import playsound

import json

def salvar_alteracao(investimentos):
    investimento_json = json.dumps(investimentos)
    Path('investimentos.json').write_text(investimento_json)

def cria_investimentos_iniciais():
    lista_de_investimentos = [
        {
            'id':1,
            'nome':'celular',
            'valor':1500
        },
        {
            'id':2,
            'nome':'geladeira',
            'valor':1300
        },
        {
            'id':3,
            'nome':'notbook',
            'valor':3500
        },
        {
            'id':4,
            'nome':'IPhone',
            'valor':7000
        },
        {
            'id':5,
            'nome':'Placa de Video',
            'valor':1200
        },
        {
            'id':6,
            'nome':'PS5',
            'valor':4999
        }
    ]

    investimentos_json = json.dumps(lista_de_investimentos)
    Path('investimentos.json').write_text(investimentos_json)

def ler_investimentos_existentes():
    investimentos_json = Path('investimentos.json').read_text()
    investimentos = json.loads(investimentos_json)
    return investimentos

def exibir_investimento_total():
    investimentos = ler_investimentos_existentes()

    total = 0
    for investimento in investimentos:
        total = investimento['valor'] + total

    print(f'O toral investido até o momento foi de: R$ {total}')

def lista_investimentos(exibir_todos = False):
    from tabulate import tabulate

    investimentos = ler_investimentos_existentes()
    lista_de_investimentos = []

    if (exibir_todos == False):
        for investimento in investimentos[:5]:
            lista_de_investimentos.append(
                [investimento['id'], investimento['nome'], investimento['valor']]
            )
    else:
        for investimento in investimentos:
            lista_de_investimentos.append(
                [investimento['id'], investimento['nome'], investimento['valor']]
            )

    print(tabulate(lista_de_investimentos, headers=['id', 'nome', 'valor']))

def apresentar_menu():
    separa_por_linha()
    print('1 - Listar todos os investimentos')
    print('2 - Editar investimento existente')
    print('3 - Excluir um investimento')
    print('4 - Criar investimento')
    opcao = input('Digite uma opção: ')
    separa_por_linha()
    return opcao

def editar_investimento_existente(investimento_id):
    investimentos = ler_investimentos_existentes()
    nome = input('Digite o novo nome: ')
    valor = input('Digite o novo valor: ')
    for investimento in investimentos:
        if (investimento['id'] == int(investimento_id)):
            if (nome != ''):
                investimento.update({'nome': nome})
            if (valor != ''):
                investimento.update({'valor': float(valor)})
            salvar_alteracao(investimentos)
            print(investimento)
            break

def excluir_investimento(investimento_id):
    investimentos = ler_investimentos_existentes()
    for indice, item in enumerate(investimentos):
        if (item['id'] == int(investimento_id)):
            print(f'O investimento {item} foi excluido com sucesso!')
            del investimentos[indice]
            salvar_alteracao(investimentos)
            break

def obter_ultimo_id(investimentos):
    ultimo_investimento = investimentos[-1:]
    ultimo_id = ultimo_investimento[0]
    ultimo_id = ultimo_id['id']
    ultimo_id += 1
    return ultimo_id

def cria_novo_investimento(nome, valor):
    investimentos = ler_investimentos_existentes()
    ultimo_id = obter_ultimo_id(investimentos)
    novo_investimento = {'id': ultimo_id, 'nome': nome, 'valor': float(valor)}
    investimentos.append(novo_investimento)
    salvar_alteracao(investimentos)
    print(f'O investimento {novo_investimento} acaba de ser criado!')
    

if __name__ == '__main__':
    apresenta_programa()
    exibir_investimento_total()
    lista_investimentos()

    while True:
        # playsound('musica.wav', block = False)
        opcao = apresentar_menu()
        if (opcao == '1'): lista_investimentos(exibir_todos = True)
        if (opcao == '2'):
            investimento_id = input('Qual investimento deseja editar: ')
            editar_investimento_existente(investimento_id)
        if (opcao == '3'):
            investimento_id = input('Digite o id do investimento a excluir: ')
            excluir_investimento(investimento_id)
        if (opcao == '4'):
            nome = input('Nome do Investimento: ')
            valor = input('valor do investimento: ')
            cria_novo_investimento(nome, valor)
        if (opcao not in '1234'): break
