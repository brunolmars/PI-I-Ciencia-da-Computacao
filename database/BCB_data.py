import requests
from datetime import date 



# --- 1. BUSCA POR INADIMPLÊNCIA (CÓDIGO 1441) ---

CODIGO_INADIMPLENCIA = 1441 
NOME_SERIE = "Inadimplência PF - Recursos Livres"

URL_BCB = f'https://api.bcb.gov.br/dados/serie/bcdata.sgs.{CODIGO_INADIMPLENCIA}/dados?format=json'


def buscar_dados_bcb():
    try:
        
        print(f"Buscando dados da série {CODIGO_INADIMPLENCIA} ({NOME_SERIE}) no BCB...")
        
        resposta = requests.get(URL_BCB)
        resposta.raise_for_status()
        
        
        dados_serie = resposta.json()
        
        
        if dados_serie:
            
            
            ultimos_valores = dados_serie[-5:] 
            
            
            
            ultimo = ultimos_valores[-1]
            print(f"Último valor de {NOME_SERIE} (data {ultimo['data']}): {ultimo['valor']}%")
            
            
            
            
           
            return ultimos_valores 

        else:
            print(f"Nenhum dado encontrado para a série {CODIGO_INADIMPLENCIA}.")
            return [] 

    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar dados do BCB: {e}")
        return []

dados_inadimplencia = buscar_dados_bcb()


# --- 2. BUSCA POR JUROS DO CHEQUE ESPECIAL (CÓDIGO 25471) ---

CHEQUE_ESPECIAL = 25471
URL_BCB_CHEQUE_ESPECIAL = f'https://api.bcb.gov.br/dados/serie/bcdata.sgs.{CHEQUE_ESPECIAL}/dados?format=json'

def buscarDadoChequeEspecial():

    try:
        print(f"Buscando dados de serie {CHEQUE_ESPECIAL} (taxa de juros cheque especial) no BCB")

        resposta = requests.get(URL_BCB_CHEQUE_ESPECIAL)
        resposta.raise_for_status()

        dados_series = resposta.json()

        if dados_series:

            ultimos_valorres = dados_series[-5:]
            
            

            
            ultimo = ultimos_valorres[-1] 
            print(f"Último dado retirado do BCB (Data: {ultimo['data']}): {ultimo['valor']}% ao mês")

            return ultimos_valorres 
        
        else:
            print(f"Nenhum dado encontrado para a série {CHEQUE_ESPECIAL}.")
            return []
    
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar dados do BCB: {e}")
        return []
    
dados_ChequeEspecial = buscarDadoChequeEspecial()


# --- 3. BUSCA POR IPCA (INFLAÇÃO - CÓDIGO 433) ---

O_INIMIGO = 433

URL_BCB_IPCA = f'https://api.bcb.gov.br/dados/serie/bcdata.sgs.{O_INIMIGO}/dados?format=json'

def buscar_INIMIGO():
    try:
        print(f"Buscando dados de serie {O_INIMIGO} (IPCA Mensal) no BCB") 

        resposta = requests.get(URL_BCB_IPCA)
        resposta.raise_for_status()

        dados_series = resposta.json()
        
        if dados_series:

            ultimos_valores = dados_series[-5:]
            
            
            ultimo = ultimos_valores[-1] 
            print(f"Último dado retirado do BCB (Data: {ultimo['data']}): {ultimo['valor']}% (Inflação)")

            return ultimos_valores
        
        else:
            print(f"Nenhum dado encontrado para a série {O_INIMIGO}.")
            return []
            
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar dados do BCB: {e}")
        return []
    
dados_IPCA = buscar_INIMIGO()

#--- 4.Busca cartão de credito ---


CARTÃO_DE_CREDITO = 25473

URL_BCB_CARTAO_DE_CREDITO = f'https://api.bcb.gov.br/dados/serie/bcdata.sgs.{CARTÃO_DE_CREDITO}/dados?format=json'

def buscar_cartão_de_credito_juros():
    try:
        print(f"Buscando dados de series{CARTÃO_DE_CREDITO}(juros anuais do cartões de credito)")

        resposta = requests.get(URL_BCB_CARTAO_DE_CREDITO)
        resposta.raise_for_status()

        dados_serie = resposta.json()
        
        if dados_serie:
            ultimo_dado = dados_serie[-1]

            print(f"Último dado retirado do BCB (Data: {ultimo_dado['data']}): {ultimo_dado['valor']}% (Juros anuais)")

    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar dados do BCB: {e}")
        return []
    
dados_cartão_de_credito = buscar_cartão_de_credito_juros()


#--- 5. Busca Emprestimo cosignado ------

EMPRESTIMO_CONSIGNADO = 25477

URL_BCB_EMPRESTIMO_CONSIGNADO =f'https://api.bcb.gov.br/dados/serie/bcdata.sgs.{EMPRESTIMO_CONSIGNADO}/dados?format=json'


def busca_jurosEmprestimoCosignado():
    try:
        print(f"Buscando dados de serie{EMPRESTIMO_CONSIGNADO}(Juros emprestimo consignado)")

        resposta = requests.get(URL_BCB_EMPRESTIMO_CONSIGNADO)
        resposta.raise_for_status()

        dados_de_serie = resposta.json()

        if dados_de_serie:


            ultimo_dado = dados_de_serie[-1]

            print(f"Último dado retirado do BCB (Data: {ultimo_dado['data']}): {ultimo_dado['valor']}% (Juros mensais)")

            return dados_de_serie
        
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar dados do BCB: {e}")
        return []
    
dados_EmprestimoConsignado = busca_jurosEmprestimoCosignado()