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

    try:
        response = supabase.table("transacoes_pix").insert(dados_para_subir).execute()
        
        print(f"Sucesso! Dados enviados para o Supabase.")
        
    except Exception as e:
        print(f"Erro ao carregar via API Key: {e}")