# 📖 DICIONÁRIO DE DADOS COMPLETO - SGEF

Este documento detalha as colunas, tipos de dados e as regras de transformação aplicadas nas tabelas de dados fundamentais e nas tabelas de análise agregada geradas pelo projeto.

---

## 1. Tabelas Fundamentais (Base de Dados Estruturada - ETL)

Estas são as 5 tabelas finais geradas pelo processo de ETL (`03_estruturar_base_dados.py`), que modularizam as informações do formulário e os metadados do BCB.

### 1.1. Tabela: `tabela_bcb_metadados` (Dados Macroeconômicos)

| Coluna             | Tipo de Dado | Descrição                                          | Regra de Limpeza/Função                             | Fonte |
| :----------------- | :----------- | :------------------------------------------------- | :-------------------------------------------------- | :---- |
| **Data**           | `datetime`   | Data de referência do indicador.                   | Convertida explicitamente para `datetime`.          | BCB   |
| **Nome_Indicador** | `string`     | Nome completo da série econômica (Ex: Taxa SELIC). | Usada como chave composta para desnormalização.     | BCB   |
| **Area_Analise**   | `string`     | Categoria principal do indicador.                  | Mapeada manualmente (Ex: 'Renda Fixa', 'Inflação'). | BCB   |
| **Valor**          | `float`      | Valor numérico do indicador na data.               | Convertido para `float` para cálculos.              | BCB   |
| **Unidade_Medida** | `string`     | Unidade do valor (Ex: % ao Mês).                   | Mantida para metadados.                             | BCB   |

### 1.2. Tabela: `tabela_perfil_pessoal`

Contém dados demográficos e de autoavaliação. **Chave de Conexão:** Índice Implícito (ID_Resposta).

| Coluna                  | Tipo de Dado | Descrição                                  | Valores/Exemplos                     | Regra de Limpeza/Função                                        |
| :---------------------- | :----------- | :----------------------------------------- | :----------------------------------- | :------------------------------------------------------------- |
| **faixa_etaria**        | `string`     | Idade do respondente.                      | `18 - 25`, `41-60`, `60+`            | Aplicação de **`.str.strip().str.title()`** para padronização. |
| **nivel_conhecimento**  | `string`     | Autoavaliação do conhecimento em finanças. | `Iniciante`, `Avançado`              | Aplicação de **`.str.strip().str.title()`**.                   |
| **objetivo_financeiro** | `string`     | Principal meta de longo/curto prazo.       | `Comprar uma casa`, `Viver de renda` | Padronização de strings.                                       |
| **email**               | `string`     | E-mail do respondente (opcional).          | E-mail padronizado ou `nan`          | Convertido para **`.str.lower()`**.                            |

### 1.3. Tabela: `tabela_comportamento`

Registra o comportamento frente ao risco e planejamento. **Chave de Conexão:** Índice Implícito (ID_Resposta).

| Coluna                 | Tipo de Dado | Descrição                                    | Valores/Exemplos                                      | Regra de Limpeza/Função                  |
| :--------------------- | :----------- | :------------------------------------------- | :---------------------------------------------------- | :--------------------------------------- |
| **participa_apostas**  | `string`     | Participação em jogos de risco/apostas.      | Texto original (Ex: "Sim, mas de forma eventual..."). | `.str.strip().str.title()` para limpeza. |
| **reserva_financeira** | `string`     | Indica se o respondente possui uma reserva.  | `Sim`, `Não`                                          | **Padronizado para Sim/Não**.            |
| **resgate_imediato**   | `string`     | Liquidez da reserva de emergência.           | `Sim`, `Não possuo a reserva`                         | Texto original mantido.                  |
| **decisao_financeira** | `string`     | Tendência ao tomar decisões de investimento. | `Busco equilibrar segurança...`                       | Texto original mantido.                  |

### 1.4. Tabela: `tabela_investimentos`

Detalha o portfólio de investimento (Respostas Sim/Não). **Chave de Conexão:** Índice Implícito (ID_Resposta).

| Coluna             | Tipo de Dado | Descrição                                      | Valores/Formato Final | Regra de Limpeza/Função                                                          |
| :----------------- | :----------- | :--------------------------------------------- | :-------------------- | :------------------------------------------------------------------------------- |
| **poupanca**       | `string`     | Investe em Poupança.                           | `Sim` ou `Não`        | **Padronização Binária:** Uso de **`lambda x: 'Sim' if 'Sim' in x else 'Não'`**. |
| **tesouro**        | `string`     | Investe em Tesouro Nacional.                   | `Sim` ou `Não`        | **Padronização Binária:** Uso de **`lambda x: 'Sim' if 'Sim' in x else 'Não'`**. |
| **renda_fixa**     | `string`     | Investe em Renda Fixa (CDB, LCI, LCA).         | `Sim` ou `Não`        | **Padronização Binária:** Uso de **`lambda x: 'Sim' if 'Sim' in x else 'Não'`**. |
| **renda_variavel** | `string`     | Investe em Renda Variável (Ações, FIIs).       | `Sim` ou `Não`        | **Padronização Binária:** Uso de **`lambda x: 'Sim' if 'Sim' in x else 'Não'`**. |
| **reserva_valor**  | `string`     | Possui reservas de valor (Cripto, Ouro, etc.). | `Sim` ou `Não`        | **Padronização Binária:** Uso de **`lambda x: 'Sim' if 'Sim' in x else 'Não'`**. |

### 1.5. Tabela: `tabela_textos_livres`

Contém as colunas de texto livre para análise qualitativa. **Chave de Conexão:** Índice Implícito (ID_Resposta).

| Coluna                  | Tipo de Dado | Descrição                                              | Regra de Limpeza/Função                            |
| :---------------------- | :----------- | :----------------------------------------------------- | :------------------------------------------------- |
| **jornada_financeira**  | `string`     | Histórico/experiência sobre a jornada de investimento. | Nulos (`NaN`) preenchidos com string vazia (`''`). |
| **conselho_financeiro** | `string`     | Sugestões/conselhos financeiros para outros.           | Nulos (`NaN`) preenchidos com string vazia (`''`). |

---

## 2. Tabelas de Análise Agregada (Resultados de Agregação e Insight)

Estas tabelas são geradas no notebook de análise para criar visualizações e extrair insights do negócio.

### 2.1. Tabela: `tabela_completa` (Resumo Detalhado por Faixa Etária)

| Coluna                                            | Tipo de Dado | Descrição                                                 | Regra de Agregação                          |
| :------------------------------------------------ | :----------- | :-------------------------------------------------------- | :------------------------------------------ |
| **faixa_etaria**                                  | `string`     | Chave de agrupamento.                                     | `groupby` na Faixa Etária.                  |
| **total_pessoas**                                 | `int`        | Total de respondentes na faixa.                           | `count`                                     |
| **nivel_conhecimento_mais_comum**                 | `string`     | Nível de conhecimento mais frequente na faixa.            | Função **`mode()`** (Valor mais frequente). |
| **pessoas_com_reserva**                           | `int`        | Contagem de quem respondeu 'Sim' em `reserva_financeira`. | Soma de 'Sim's.                             |
| **pessoas_que_apostam**                           | `int`        | Contagem de quem respondeu 'Sim' em `participa_apostas`.  | Contagem de strings contendo 'Sim'.         |
| **poupanca, tesouro, renda_fixa, renda_variavel** | `int`        | Contagem de quem investe em cada ativo.                   | Soma de 'Sim's.                             |
| **objetivo_financeiro_mais_comum**                | `string`     | Objetivo mais frequente na faixa.                         | Função **`mode()`** (Valor mais frequente). |

### 2.2. Tabela: `tabela_investimentos` (Investimentos por Nível de Conhecimento)

| Coluna                                                           | Tipo de Dado | Descrição                                     | Regra de Agregação                             |
| :--------------------------------------------------------------- | :----------- | :-------------------------------------------- | :--------------------------------------------- |
| **nivel_conhecimento**                                           | `string`     | Chave de agrupamento.                         | `groupby` no Nível de Conhecimento.            |
| **Poupanca, Tesouro, Renda_Fixa, Renda_Variavel, Reserva_Valor** | `int`        | Número de pessoas que investem em cada ativo. | Contagem de 'Sim' após a padronização binária. |

### 2.3. Tabela: `tabela_faixa` (Distribuição de Perfil)

| Coluna                 | Tipo de Dado | Descrição                                        | Regra de Agregação     |
| :--------------------- | :----------- | :----------------------------------------------- | :--------------------- |
| **faixa_etaria**       | `string`     | Chave de agrupamento.                            | `groupby`              |
| **nivel_conhecimento** | `string`     | Segunda chave de agrupamento.                    | `groupby`              |
| **quantidade**         | `int`        | Contagem total de respondentes nessa combinação. | `size().reset_index()` |

---
