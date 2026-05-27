from supabase import create_client
import os

def load_to_supabase(df):
    if df.empty:
        print("Aviso: DataFrame vazio. Nada será carregado.")
        return

    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")
    supabase = create_client(url, key)

    dados_para_subir = df.to_dict(orient='records')

    CHAVE_CONFLITO = (
            "data_transacao,pagador,receptor,"
            "regiao_pagador,regiao_receptor,"
            "idade_pagador,idade_receptor,"
            "forma_iniciacao,natureza_pix,finalidade"
        )

    try:
        response = (
            supabase.table("transacoes_pix")
            .upsert(dados_para_subir, on_conflict=CHAVE_CONFLITO)
            .execute()
        )
        print("Sucesso! Dados enviados para o Supabase.")

    except Exception as e:
        print(f"Erro ao carregar via API Key: {e}")