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
        'NATUREZA': 'natureza_pix',
        'VALOR': 'valor_pix',
        'QUANTIDADE': 'quantidade_pix'
    }

    colunas_presentes = [c for c in colunas.keys() if c in df.columns]
    df = df[colunas_presentes].rename(columns=colunas)

    # 3. Tratamento dos dados
    if not df.empty:
        df['valor_pix'] = pd.to_numeric(df['valor_pix'], errors='coerce')
        df['quantidade_pix'] = pd.to_numeric(df['quantidade_pix'], errors='coerce')

        df['valor_pix'] = df['valor_pix'].fillna(df['valor_pix'].median())
        df['quantidade_pix'] = df['quantidade_pix'].fillna(df['quantidade_pix'].median()).astype(int)

        df['data_transacao'] = pd.to_datetime(df['data_transacao'], format='%Y%m')

        df['regiao_pagador'] = df['regiao_pagador'].fillna('Não Informado').str.title()
        df['regiao_receptor'] = df['regiao_receptor'].fillna('Não Informado').str.title()

        df = df.drop_duplicates()
        df = df.dropna(subset=['data_transacao', 'pagador', 'receptor'])
        
        df.to_csv('dados_pix_tratados.csv', index=False, encoding='utf-8-sig', sep=';')
        print("✅ Arquivo 'dados_pix_tratados.csv' gerado com sucesso!")
        
    return df