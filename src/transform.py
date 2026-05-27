import pandas as pd

def transform_data(json_data):
    if not json_data or 'value' not in json_data or len(json_data['value']) == 0:
        print("Aviso: Nenhum dado recebido da API para este período.")
        return pd.DataFrame() 

    df = pd.DataFrame(json_data['value'])
    colunas = {
        'AnoMes': 'data_transacao',
        'PAG_PFPJ': 'pagador',
        'REC_PFPJ': 'receptor',
        'PAG_REGIAO': 'regiao_pagador',
        'REC_REGIAO': 'regiao_receptor',
        'PAG_IDADE': 'idade_pagador',
        'REC_IDADE': 'idade_receptor',
        'FORMAINICIACAO': 'forma_iniciacao',
        'NATUREZA': 'natureza_pix',
        'FINALIDADE': 'finalidade',
        'VALOR': 'valor_pix',
        'QUANTIDADE': 'quantidade_pix'
    }

    colunas_presentes = [c for c in colunas.keys() if c in df.columns]
    df = df[colunas_presentes].rename(columns=colunas)

    if not df.empty:
        df = df.drop_duplicates()
        df = df.dropna()
        
        df['valor_pix'] = df['valor_pix'].fillna(df['valor_pix'].median())
        df['quantidade_pix'] = df['quantidade_pix'].fillna(df['quantidade_pix'].median()).astype(int)

        df['pagador'] = df['pagador'].fillna('Pagador Desconhecido')
        df['receptor'] = df['receptor'].fillna('Receptor Desconhecido')
        df['regiao_pagador'] = df['regiao_pagador'].fillna('Regiao do pagador Desconhecido')
        df['regiao_receptor'] = df['regiao_receptor'].fillna('Regiao do receptor Desconhecido')
        df['natureza_pix'] = df['natureza_pix'].fillna('Natureza do pix Desconhecida')
        df['finalidade'] = df['finalidade'].fillna('Finalidade do pix Desconhecida')

        df['data_transacao'] = pd.to_datetime(df['data_transacao'], format='%Y%m')
        df['data_transacao'] = df['data_transacao'].dt.strftime('%Y-%m-%d')
        
    return df