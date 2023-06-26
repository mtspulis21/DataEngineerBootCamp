from faker import Faker
import json
fake = Faker(['pt_BR','pt_BR','pt_BR','pt_BR'])


# modelo tabela de vendas
# data da venda - nome_cliente - cnpj_cliente - uf_cliente - valor_venda

def criar_tabela_vendas(num_vendas):
    tab_vendas = []
    
    for x in range(num_vendas):
        data = {
            'id_venda': x,
            'data_venda': str(fake.date_between(start_date='-1y')),
            'nome_cliente':str(fake.company()),
            'cnpj_cliente':str(fake.cnpj()),
            'uf_cliente':str(fake.estado_sigla()),
            'valor_venda':float(fake.pricetag().replace('R$','').replace('.','').replace(',','.')),
        }
        tab_vendas.append(data)
    
    return tab_vendas

vendas = criar_tabela_vendas(50)

import pandas as pd

df = pd.DataFrame(vendas)
df

df.to_csv('vendas_faker.csv')