from supabase import create_client

def load_to_supabase(df):
    if df.empty:
        print("Aviso: DataFrame vazio. Nada será carregado.")
        return

    url = ""
    key = ""
    
    supabase = create_client(url, key)
    dados_para_subir = df.to_dict(orient='records')

    try:
        response = supabase.table("transacoes_pix").insert(dados_para_subir).execute()
        
        print(f"Sucesso! Dados enviados para o Supabase.")
        
    except Exception as e:
        print(f"Erro ao carregar via API Key: {e}")