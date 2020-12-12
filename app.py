from utilidades import apresentar_programa

from pathlib import Path
import json


apresentar_programa()

def cria_investimentos_iniciais():
    lista_de_investimentos = [
        {
            'id':'1',
            'nome':'celular',
            'valor':1500
        },
        {
            'id':'2',
            'nome':'geladeira',
            'valor':1300
        },
        {
            'id':'3',
            'nome':'notbook',
            'valor':3500
        },
        {
            'id':'4',
            'nome':'IPhone',
            'valor':7000
        },
        {
            'id':'5',
            'nome':'Placa de Video',
            'valor':1200
        },
        {
            'id':'6',
            'nome':'PS5',
            'valor':4999
        }
    ]

    investimentos_json = json.dumps(lista_de_investimentos)
    Path('investimentos.json').write_text(investimentos_json)

def ler_investimentos_existentes():
    investimentos_json = Path('investimentos.json').read_text()
    investimentos = json.loads(investimentos_json)
    print(investimentos)

ler_investimentos_existentes()