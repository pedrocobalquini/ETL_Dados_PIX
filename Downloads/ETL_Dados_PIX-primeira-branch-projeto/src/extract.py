import requests
from datetime import datetime
import pandas as pd

def obter_mes_ano_atual():
    data_atual = datetime.now()
    data_nova = data_atual - pd.DateOffset(months=3)
    return data_nova.strftime('%Y%m')

def get_link_url():
    data_alvo = obter_mes_ano_atual()
    
    url = (
        f"https://olinda.bcb.gov.br/olinda/servico/Pix_DadosAbertos/versao/v1/odata/"
        f"EstatisticasTransacoesPix(Database=@Database)?@Database='{data_alvo}'"
        "&$top=5000&$format=json"
        "&$select=AnoMes,PAG_PFPJ,REC_PFPJ,PAG_REGIAO,REC_REGIAO,"
        "PAG_IDADE,REC_IDADE,FORMAINICIACAO,NATUREZA,FINALIDADE,VALOR,QUANTIDADE"
    )
    
    response = requests.get(url)
    return response.json()