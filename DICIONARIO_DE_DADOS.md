# 📖 Dicionário de Dados - SGEF (Sistema de Gestão e Educação Financeira)

Este dicionário descreve as colunas, tipos de dados e valores possíveis das tabelas resultantes do processo de ETL (`03_estruturar_base_dados.py`), que modulariza as respostas do formulário e os dados do BCB.

---

## 1. Tabela: `tabela_bcb_metadados`

Esta tabela concentra os indicadores macroeconômicos e de risco extraídos da API do Banco Central do Brasil. É uma tabela desnormalizada que permite a análise temporal de todos os indicadores simultaneamente.

| Coluna             | Tipo de Dado | Descrição                                          | Valores/Exemplos                                                         | Fonte |
| :----------------- | :----------- | :------------------------------------------------- | :----------------------------------------------------------------------- | :---- |
| **Data**           | `datetime`   | Data de referência do indicador (Index temporal).  | `1990-02-01`, `2025-10-01`                                               | BCB   |
| **Nome_Indicador** | `string`     | Nome completo da série econômica.                  | `Taxa SELIC (Meta)`, `Juros Cartão de Crédito`, `IPCA Mensal (Inflação)` | BCB   |
| **Area_Analise**   | `string`     | Categoria principal do indicador.                  | `Renda Fixa`, `Dívida`, `Inflação`, `Risco`                              | BCB   |
| **Valor**          | `float`      | Valor numérico do indicador na data de referência. | `13.75` (SELIC), `0.93` (IPCA)                                           | BCB   |
| **Unidade_Medida** | `string`     | Unidade do valor (Ex: percentual ao mês ou ano).   | `% ao Mês`, `% ao Ano`, `Pontos`                                         | BCB   |
| **Fonte**          | `string`     | Origem da informação (Constante).                  | `Banco Central do Brasil (BCB)`                                          | BCB   |

---

## 2. Tabela: `tabela_perfil_pessoal`

Contém dados demográficos e de autoavaliação dos respondentes.

| Coluna                  | Tipo de Dado | Descrição                                  | Valores/Exemplos                                             | Fonte      |
| :---------------------- | :----------- | :----------------------------------------- | :----------------------------------------------------------- | :--------- |
| **faixa_etaria**        | `string`     | Idade do respondente.                      | `18 - 25`, `26 - 40`, `41 - 60`, `60+`                       | Formulário |
| **nivel_conhecimento**  | `string`     | Autoavaliação do conhecimento em finanças. | `Iniciante`, `Intermediário`, `Avançado`                     | Formulário |
| **objetivo_financeiro** | `string`     | Principal meta de longo/curto prazo.       | `Viver de renda`, `Comprar uma casa`, `Construir patrimônio` | Formulário |
| **email**               | `string`     | E-mail do respondente (opcional).          | E-mail padronizado em minúsculas ou `nan`                    | Formulário |

---

## 3. Tabela: `tabela_comportamento`

Registra o comportamento do respondente frente ao risco e planejamento básico.

| Coluna                 | Tipo de Dado | Descrição                                                                | Valores/Exemplos                                                                                  | Fonte      |
| :--------------------- | :----------- | :----------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------ | :--------- |
| **participa_apostas**  | `string`     | Indica a participação em jogos de risco (apostas).                       | `Sim`, `Não participo desse tipo de jogo`, `Sim, mas de forma eventual...`                        | Formulário |
| **reserva_financeira** | `string`     | Indica se o respondente possui uma reserva financeira.                   | `Sim`, `Não`                                                                                      | Formulário |
| **resgate_imediato**   | `string`     | Avalia se a reserva de emergência está disponível para resgate imediato. | `Sim`, `Não`, `Não possuo a reserva`                                                              | Formulário |
| **decisao_financeira** | `string`     | Tendência do respondente ao tomar decisões de investimento.              | `Prefiro decisões seguras...`, `Busco equilibrar segurança...`, `Estou disposto(a) a aprender...` | Formulário |

---

## 4. Tabela: `tabela_investimentos`

Detalha o portfólio de investimento atual, com respostas padronizadas para facilitar a contagem.

| Coluna             | Tipo de Dado | Descrição                                            | Valores/Exemplos | Fonte      |
| :----------------- | :----------- | :--------------------------------------------------- | :--------------- | :--------- |
| **poupanca**       | `string`     | Investe em Poupança.                                 | `Sim`, `Não`     | Formulário |
| **tesouro**        | `string`     | Investe em Tesouro Nacional.                         | `Sim`, `Não`     | Formulário |
| **renda_fixa**     | `string`     | Investe em Renda Fixa (CDB, LCI, LCA, etc.).         | `Sim`, `Não`     | Formulário |
| **renda_variavel** | `string`     | Investe em Renda Variável (Ações, FIIs, etc.).       | `Sim`, `Não`     | Formulário |
| **reserva_valor**  | `string`     | Possui reservas de valor (Criptomoedas, Ouro, etc.). | `Sim`, `Não`     | Formulário |

---

## 5. Tabela: `tabela_textos_livres`

Contém as colunas de texto livre para análise qualitativa, nuvens de palavras ou análise de sentimento.

| Coluna                  | Tipo de Dado | Descrição                                                 | Valores/Exemplos                                                                    | Fonte      |
| :---------------------- | :----------- | :-------------------------------------------------------- | :---------------------------------------------------------------------------------- | :--------- |
| **jornada_financeira**  | `string`     | Histórico/experiência sobre a jornada de investimento.    | `Aprendi que cada pequena economia faz diferença.`, `Pretendo criar uma reserva...` | Formulário |
| **conselho_financeiro** | `string`     | Sugestões/conselhos financeiros para outros investidores. | `Diversifique seus investimentos...`, `Comece a poupar cedo...`                     | Formulário |
