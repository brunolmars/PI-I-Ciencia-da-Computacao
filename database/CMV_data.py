import pandas as pd
import requests
from io import BytesIO
import zipfile


ANO = '2024'
URL_DADOS_CVM = f'http://dados.cvm.gov.br/dados/FI/DADOS/CAD/inf_cadastral_fi_{ANO}.zip'



def processar_dados_fundos_cvm():
    try:
        print(f"Baixando e processando dados cadastrais de fundos da CVM do ano {ANO}...")
        
        resposta = requests.get(URL_DADOS_CVM)
        resposta.raise_for_status()
        
        arquivo_zip = zipfile.ZipFile(BytesIO(resposta.content))
        
        
        nome_csv = f'inf_cadastral_fi_{ANO}.csv' 

        with arquivo_zip.open(nome_csv) as csv_file:
            
            dados_fundos = pd.read_csv(csv_file, sep=';', encoding='latin1') 
        
        print(f"Sucesso! {len(dados_fundos)} fundos encontrados.")
        
        print("\n--- Exemplo de 5 Fundos Encontrados ---")
        print(dados_fundos[['DENOM_SOCIAL', 'CNPJ_FUNDO', 'DT_REG']].head()) 
        
        return dados_fundos 

    except requests.exceptions.RequestException as e:
        print(f"Erro ao baixar dados da CVM: {e}. Verifique o link: {URL_DADOS_CVM}")
        return None
    

dados_cmv = processar_dados_fundos_cvm()