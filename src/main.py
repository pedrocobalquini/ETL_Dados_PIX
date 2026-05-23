from extract import get_link_url
from transform import transform_data
from load import load_to_supabase
from dotenv import load_dotenv

load_dotenv()

def run_etl():
    print("--- Iniciando Pipeline ELT Pix ---")

    dados_brutos = get_link_url()
    
    if dados_brutos:
        print("Transformando dados...")
        df_final = transform_data(dados_brutos)
        if not df_final.empty:
            print("Iniciando no SUPABASE")
            load_to_supabase(df_final)
            print("--- Pipeline finalizada ---")
        else:
            print("Transformação resultou em DataFrame vazio")
    else:
        print("Falha na extração.")

if __name__ == "__main__":
    run_etl()