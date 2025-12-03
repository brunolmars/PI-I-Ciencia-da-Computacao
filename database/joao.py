# ...existing code...
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker

sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = [12, 6]
plt.rcParams['font.size'] = 11

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_DIR = os.path.join(BASE_DIR, "csv_joao")
print(f"[INFO] BASE_DIR: {BASE_DIR}")
print(f"[INFO] CSV_DIR: {CSV_DIR} | exists={os.path.isdir(CSV_DIR)}")

def norm_cols(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = (
        df.columns.astype(str)
        .str.replace('\ufeff', '', regex=False)
        .str.strip()
        .str.lower()
        .str.normalize('NFKD')
        .str.encode('ascii', errors='ignore').str.decode('ascii')
        .str.replace(r'\W+', '_', regex=True)
        .str.strip('_')
    )
    return df

def read_csv(path: str, seps=(';', ','), encs=('utf-8-sig', 'latin-1')):
    for sep in seps:
        for enc in encs:
            try:
                df = pd.read_csv(path, sep=sep, encoding=enc)
                return norm_cols(df)
            except Exception:
                pass
    raise ValueError(f"Falha ao ler {path}")

def fmt_moeda_axis_mi():
    return ticker.FuncFormatter(lambda x, p: f'R$ {x/1e6:.0f} Mi')

# 1) BCB macro (série 29038) -> grafico_1_bcb_macro.png
def plot_bcb_macro():
    path = os.path.join(CSV_DIR, "bcdata.sgs.29038.csv")
    if not os.path.isfile(path):
        print(f"[WARN] BCB CSV não encontrado: {path}")
        return
    df = read_csv(path, seps=(';', ','))

    col_data = next((c for c in df.columns if 'data' in c), None)
    col_val  = next((c for c in df.columns if 'valor' in c or 'value' in c), None)
    if not col_data or not col_val: return

    vals = df[col_val].astype(str).str.replace(',', '.').str.replace(' ', '')
    df['_valor'] = pd.to_numeric(vals, errors='coerce')
    df['_data']  = pd.to_datetime(df[col_data], dayfirst=True, errors='coerce')
    df = df.dropna(subset=['_data','_valor']).sort_values('_data')

    plt.figure(figsize=(10,5))
    plt.plot(df['_data'], df['_valor'], color='#0d6efd', linewidth=3)
    plt.title('Endividamento das Famílias vs Renda (BCB 29038)')
    plt.ylabel('% da renda comprometida')
    plt.grid(True, linestyle='--', alpha=0.4)
    plt.fill_between(df['_data'], df['_valor'], color='#0d6efd', alpha=0.12)
    out = os.path.join(BASE_DIR, "grafico_1_bcb_macro.png")
    plt.savefig(out, bbox_inches='tight')
    print(f"[OK] Salvo: {out}")
    plt.close()

# 2) Desenrola por estado (Top 10) -> grafico_2_desenrola_estados.png
#    dataset: database/csv_joao/dados_desenrola.csv
def plot_desenrola_estados():
    path = os.path.join(CSV_DIR, "dados_desenrola.csv")
    if not os.path.isfile(path):
        print(f"[WARN] Desenrola CSV não encontrado: {path}")
        return
    df = read_csv(path, seps=(';', ','))

    # colunas esperadas pelo seu CSV: DATA_BASE;TIPO_DESENROLA;UNIDADE_FEDERACAO;...;NUMERO_OPERACOES;VOLUME_OPERACOES
    col_uf   = next((c for c in df.columns if c in ('unidade_federacao','uf') or 'unidade_federacao' in c or 'uf' in c), None)
    col_vol  = next((c for c in df.columns if 'volume_operacoes' in c or 'valor' in c or 'montante' in c or 'total' in c), None)
    if not col_uf or not col_vol: return

    df['_valor'] = pd.to_numeric(
        df[col_vol].astype(str).str.replace('R$','').str.replace('.','').str.replace(',','.'),
        errors='coerce'
    ).fillna(0)

    top = (
        df.groupby(col_uf)['_valor']
          .sum().sort_values(ascending=False).head(10).reset_index()
    )
    plt.figure(figsize=(12,6))
    sns.barplot(data=top, x='_valor', y=col_uf, palette='Blues_r')
    plt.title('Desenrola: Volume Renegociado por Estado (Top 10)')
    plt.xlabel('Valor Renegociado (R$)')
    plt.gca().xaxis.set_major_formatter(fmt_moeda_axis_mi())
    out = os.path.join(BASE_DIR, "grafico_2_desenrola_estados.png")
    plt.savefig(out, bbox_inches='tight')
    print(f"[OK] Salvo: {out}")
    plt.close()

# 3) Perfil do devedor (PF vs PJ) a partir de DEVEDORES CSV -> grafico_3_perfil_devedor.png
def plot_perfil_devedor():
    # tente encontrar um CSV com “devedores” na pasta csv_joao
    cand = None
    for name in os.listdir(CSV_DIR):
        if 'devedores' in name.lower() and name.lower().endswith('.csv'):
            cand = os.path.join(CSV_DIR, name)
            break
    if not cand or not os.path.isfile(cand):
        print(f"[WARN] CSV de devedores não encontrado em {CSV_DIR}")
        return

    df = read_csv(cand, seps=(';', ','))
    col_tipo = next((c for c in df.columns if ('tipo_de_pessoa' in c) or ('tipo' in c and 'pessoa' in c)), None)
    if not col_tipo: return

    s = df[col_tipo].astype(str).str.lower()
    pf = s.str.contains('pessoa f', na=False).sum()
    pj = s.str.contains('pessoa j', na=False).sum()
    perf = pd.DataFrame({'tipo': ['Pessoa Física','Pessoa Jurídica'], 'qtd': [pf, pj]})

    plt.figure(figsize=(10,6))
    sns.barplot(data=perf, x='tipo', y='qtd', palette=['#0d6efd','#20c997'])
    plt.title('Perfil do Devedor (PF vs PJ)')
    plt.ylabel('Quantidade de Registros')
    out = os.path.join(BASE_DIR, "grafico_3_perfil_devedor.png")
    plt.savefig(out, bbox_inches='tight')
    print(f"[OK] Salvo: {out}")
    plt.close()

# 4) Evolução da dívida ativa por ano (soma) -> grafico_4_evolucao_divida.png
def plot_evolucao_divida():
    # usa o mesmo arquivo “devedores”
    cand = None
    for name in os.listdir(CSV_DIR):
        if 'devedores' in name.lower() and name.lower().endswith('.csv'):
            cand = os.path.join(CSV_DIR, name)
            break
    if not cand or not os.path.isfile(cand):
        print(f"[WARN] CSV de devedores não encontrado para evolução em {CSV_DIR}")
        return

    df = read_csv(cand, seps=(';', ','))
    col_saldo = next((c for c in df.columns if 'saldo' in c or 'honor' in c or 'valor' in c), None)
    col_data  = next((c for c in df.columns if 'data_da_inscricao' in c or 'data_inscricao' in c or 'inscricao' in c), None)
    if not col_saldo or not col_data: return

    df['_val'] = pd.to_numeric(
        df[col_saldo].astype(str).str.replace('R$','').str.replace('.','').str.replace(',','.'),
        errors='coerce'
    )
    # formato comum: dd/mm/aaaa
    df['_dt'] = pd.to_datetime(df[col_data].astype(str), dayfirst=True, errors='coerce')
    df['_ano'] = df['_dt'].dt.year
    by_year = df.dropna(subset=['_ano']) \
                .groupby('_ano')['_val'].sum().reset_index()

    plt.figure(figsize=(12,6))
    sns.barplot(data=by_year, x='_ano', y='_val', color='#6f42c1')
    plt.title('Evolução da Dívida Ativa (Soma por Ano de Inscrição)')
    plt.xlabel('Ano')
    plt.ylabel('Valor (R$)')
    plt.gca().yaxis.set_major_formatter(fmt_moeda_axis_mi())
    plt.xticks(rotation=45)
    out = os.path.join(BASE_DIR, "grafico_4_evolucao_divida.png")
    plt.savefig(out, bbox_inches='tight')
    print(f"[OK] Salvo: {out}")
    plt.close()

# 5) Cartão de Crédito (Cadastro Positivo) -> grafico_5_cartao_credito.png
def plot_cartao_credito():
    # tenta localizar arquivo com "cartao" na pasta csv_joao
    cand = None
    for name in os.listdir(CSV_DIR):
        nl = name.lower()
        if 'cartao' in nl and nl.endswith('.csv'):
            cand = os.path.join(CSV_DIR, name)
            break
    if not cand or not os.path.isfile(cand):
        print(f"[WARN] CSV de cartão de crédito não encontrado em {CSV_DIR}")
        return

    df = read_csv(cand, seps=(';', ','))
    # tentativa de colunas: data_base, modalidade, quantidade, valor
    col_data = next((c for c in df.columns if 'data_base' in c or 'data' in c), None)
    col_mod  = next((c for c in df.columns if 'modalidade' in c or 'produto' in c), None)
    col_qtd  = next((c for c in df.columns if 'qtd' in c or 'quant' in c or 'numero' in c), None)
    col_val  = next((c for c in df.columns if 'valor' in c or 'montante' in c or 'total' in c), None)

    # valor
    if col_val:
        df['_valor'] = pd.to_numeric(
            df[col_val].astype(str).str.replace('R$','').str.replace('.','').str.replace(',','.'),
            errors='coerce'
        ).fillna(0)
    else:
        df['_valor'] = 0
    # data
    if col_data:
        # aceita AAAAMM ou dd/mm/aaaa
        df['_dt'] = pd.to_datetime(df[col_data].astype(str), errors='coerce')
        mask_na = df['_dt'].isna()
        if mask_na.any():
            df.loc[mask_na, '_dt'] = pd.to_datetime(df.loc[mask_na, col_data].astype(str), format='%Y%m', errors='coerce')
    else:
        df['_dt'] = pd.NaT

    # agregação por mês
    df['_mes'] = df['_dt'].dt.to_period('M').astype(str)
    by_month = df.dropna(subset=['_mes']).groupby('_mes')['_valor'].sum().reset_index()

    plt.figure(figsize=(12,6))
    sns.lineplot(data=by_month, x='_mes', y='_valor', marker='o', color='#dc3545')
    plt.title('Cartão de Crédito: Valor Positivo (Linha do Tempo)')
    plt.ylabel('Valor (R$)')
    plt.gca().yaxis.set_major_formatter(fmt_moeda_axis_mi())
    plt.xticks(rotation=45)
    out = os.path.join(BASE_DIR, 'grafico_5_cartao_credito.png')
    plt.savefig(out, bbox_inches='tight')
    print(f"[OK] Salvo: {out}")
    plt.close()

# 6) Empréstimo Pessoal (Cadastro Positivo) -> grafico_6_emprestimo_pessoal.png
def plot_emprestimo_pessoal():
    cand = None
    for name in os.listdir(CSV_DIR):
        nl = name.lower()
        if 'emprestimo_pessoal' in nl and nl.endswith('.csv'):
            cand = os.path.join(CSV_DIR, name)
            break
        if 'emprestimo' in nl and 'pessoal' in nl and nl.endswith('.csv'):
            cand = os.path.join(CSV_DIR, name)
            break
    if not cand or not os.path.isfile(cand):
        print(f"[WARN] CSV de empréstimo pessoal não encontrado em {CSV_DIR}")
        return

    df = read_csv(cand, seps=(';', ','))
    col_data = next((c for c in df.columns if 'data_base' in c or 'data' in c), None)
    col_val  = next((c for c in df.columns if 'valor' in c or 'montante' in c or 'total' in c or 'volume' in c), None)

    if col_val:
        df['_valor'] = pd.to_numeric(
            df[col_val].astype(str).str.replace('R$','').str.replace('.','').str.replace(',','.'),
            errors='coerce'
        ).fillna(0)
    else:
        df['_valor'] = 0

    if col_data:
        df['_dt'] = pd.to_datetime(df[col_data].astype(str), errors='coerce')
        mask_na = df['_dt'].isna()
        if mask_na.any():
            df.loc[mask_na, '_dt'] = pd.to_datetime(df.loc[mask_na, col_data].astype(str), format='%Y%m', errors='coerce')
    else:
        df['_dt'] = pd.NaT

    df['_mes'] = df['_dt'].dt.to_period('M').astype(str)
    by_month = df.dropna(subset=['_mes']).groupby('_mes')['_valor'].sum().reset_index()

    plt.figure(figsize=(12,6))
    sns.lineplot(data=by_month, x='_mes', y='_valor', marker='o', color='#20c997')
    plt.title('Empréstimo Pessoal: Valor Positivo (Linha do Tempo)')
    plt.ylabel('Valor (R$)')
    plt.gca().yaxis.set_major_formatter(fmt_moeda_axis_mi())
    plt.xticks(rotation=45)
    out = os.path.join(BASE_DIR, 'grafico_6_emprestimo_pessoal.png')
    plt.savefig(out, bbox_inches='tight')
    print(f"[OK] Salvo: {out}")
    plt.close()

def main():
    print("Gerando gráficos a partir de CSVs em:", CSV_DIR)
    plot_bcb_macro()
    plot_desenrola_estados()
    plot_perfil_devedor()
    plot_evolucao_divida()
    plot_cartao_credito()
    plot_emprestimo_pessoal()
    print("Concluído. Arquivos salvos em:", BASE_DIR)
    print("- grafico_1_bcb_macro.png")
    print("- grafico_2_desenrola_estados.png")
    print("- grafico_3_perfil_devedor.png")
    print("- grafico_4_evolucao_divida.png")
    print("- grafico_5_cartao_credito.png")
    print("- grafico_6_emprestimo_pessoal.png")

if __name__ == "__main__":
    main()
# ...existing code...