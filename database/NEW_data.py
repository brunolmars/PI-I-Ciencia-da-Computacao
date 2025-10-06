import requests
import json
from datetime import datetime


NEWS_API_KEY = '7967f5ae0e844b66b422b7c15fde6644'

# Parâmetros da busca para notícias de educação financeira e investimento em português
parametros = {
    'q': 'educação financeira E investimento', 
    'language': 'pt',                        
    'sortBy': 'publishedAt',                 
    'apiKey': NEWS_API_KEY                   
}


URL_BASE = 'https://newsapi.org/v2/everything'


try:
    print("Buscando notícias...")
    
    resposta = requests.get(URL_BASE, params=parametros)
    
    
    resposta.raise_for_status() 
    
    
    dados = resposta.json()
    
    
    artigos = dados.get('articles', [])
    
    print(f"\n--- Resultados Encontrados: {len(artigos)} artigos ---")

    
    for i, artigo in enumerate(artigos[:10]): 
        
        titulo = artigo.get('title')
        fonte = artigo.get('source', {}).get('name')
        data_publicacao = artigo.get('publishedAt')
        link_completo = artigo.get('url')
        
        
        if data_publicacao:
             
            data_formatada = datetime.fromisoformat(data_publicacao.replace('Z', '+00:00')).strftime('%d/%m/%Y %H:%M')
        else:
             data_formatada = "Data indisponível"

        print(f"\nArtigo {i+1}:")
        print(f"  Título: {titulo}")
        print(f"  Fonte: {fonte} | Publicado em: {data_formatada}")
        print(f"  Link: {link_completo}")
        print("-" * 30)

    
    
except requests.exceptions.HTTPError as errh:
    print(f"Erro HTTP: {errh}")
except requests.exceptions.RequestException as err:
    print(f"Ocorreu um erro na requisição: {err}")