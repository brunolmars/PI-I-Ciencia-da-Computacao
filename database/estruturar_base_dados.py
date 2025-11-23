import os
import sys
import pandas as pd

script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)
PASTA_DATABASE = os.path.join(project_root, 'database')
os.makedirs(PASTA_DATABASE, exist_ok=True)
print(f"Diretório de saída: {PASTA_DATABASE}")

caminho_csv = os.path.join(PASTA_DATABASE, 'respostas_formulario.csv')
print(f"Tentando carregar: {caminho_csv}")


df = None
for sep, enc in [(';','utf-8-sig'), (',','utf-8-sig'), (';','latin-1')]:
    try:
        df = pd.read_csv(caminho_csv, sep=sep, encoding=enc)
        print(f"Lido com sep='{sep}' enc='{enc}'")
        break
    except FileNotFoundError:
        print("ERRO: arquivo não encontrado:", caminho_csv)
        sys.exit(1)
    except Exception:
        df = None

if df is None:
    print("ERRO: não foi possível ler o CSV. Verifique separador/encoding.")
    sys.exit(1)

print("\n--- primeiras linhas ---")
print(df.head().to_string(index=False))
print("\n--- colunas originais ---")
print(list(df.columns))


df.columns = (
    df.columns
    .astype(str)
    .str.replace('\ufeff', '', regex=False)
    .str.strip()
    .str.lower()
    .str.normalize('NFKD')  
    .str.encode('ascii', errors='ignore').str.decode('ascii')
    .str.replace(r'\W+', '_', regex=True)
    .str.strip('_')
)

print("\n--- colunas normalizadas ---")
print(list(df.columns))


colunas_perfil = ['faixa_etaria', 'nivel_conhecimento', 'objetivo_financeiro', 'email']
colunas_comportamento = ['participa_apostas', 'reserva_financeira', 'resgate_imediato', 'decisao_financeira']
colunas_investimentos = ['poupanca', 'tesouro', 'renda_fixa', 'renda_variavel', 'reserva_valor']
colunas_textos = ['jornada_financeira', 'conselho_financeiro']

def selecionar_colunas(df, lista):
    existentes = [c for c in lista if c in df.columns]
    faltantes = [c for c in lista if c not in df.columns]
    if faltantes:
        print(f"Aviso: colunas ausentes e serão ignoradas: {faltantes}")
    if not existentes:
        print(f"Aviso: nenhuma das colunas esperadas {lista} encontrada.")
        return df.iloc[0:0].copy()
    return df[existentes].copy()

tabela_perfil_pessoal = selecionar_colunas(df, colunas_perfil)
tabela_comportamento = selecionar_colunas(df, colunas_comportamento)
tabela_investimentos = selecionar_colunas(df, colunas_investimentos)
tabela_textos_livres = selecionar_colunas(df, colunas_textos)

tabelas_para_salvar = {
    'tabela_perfil_pessoal': tabela_perfil_pessoal,
    'tabela_comportamento': tabela_comportamento,
    'tabela_investimentos': tabela_investimentos,
    'tabela_textos_livres': tabela_textos_livres
}

for nome, df_salvar in tabelas_para_salvar.items():
    caminho_arquivo = os.path.join(PASTA_DATABASE, f'{nome}.csv')
    if df_salvar.empty:
        print(f"Pulado: {nome}.csv (vazio) — não será salvo.")
       
        continue
    df_salvar.to_csv(caminho_arquivo, index=False, sep=';', encoding='utf-8')
    print(f"💾 {nome}.csv salvo ({len(df_salvar)} linhas) em {caminho_arquivo}")

print("✅ Finalizado.")