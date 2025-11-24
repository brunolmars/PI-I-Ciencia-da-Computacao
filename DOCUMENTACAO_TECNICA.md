# ⚙️ Documentação Técnica e Decisões de Engenharia de Dados

Este documento detalha as decisões técnicas, escolhas de arquitetura e regras de limpeza de dados aplicadas no processo de **Extração, Transformação e Carga (ETL)** do projeto SGEF.

---

## 1. Fonte de Dados e Extração (E)

A base de dados é composta por duas fontes principais: dados primários (Formulário) e dados secundários (BCB).

| Fonte                          | Tipo de Dado                    | Decisão de Escolha                                                                                                                                                                          |
| :----------------------------- | :------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Formulário de Pesquisa**     | Comportamental/Demográfico      | Fornece o perfil do público-alvo para análises cruzadas.                                                                                                                                    |
| **API do Banco Central (BCB)** | Macroeconômico/Séries Temporais | A escolha das séries **SELIC**, **IPCA** e **Taxas de Juros** foi feita para garantir que o contexto de investimento (Renda Fixa e Risco) reflita as condições econômicas atuais do Brasil. |

---

## 2. Limpeza e Transformação (T)

A etapa de Limpeza foi executada no notebook `02_Data_Forms.pynb` e seguiu regras estritas de padronização para garantir a qualidade dos dados nas análises.

### 2.1. Padronização de Colunas de Investimento (Sim/Não)

- **Problema:** As colunas `Poupança`, `Tesouro Nacional`, `Renda Fixa`, `Renda Variável` e `Reserva de Valor` continham múltiplas respostas (Ex: "Sim, tenho um pouco", "Sim, invisto nisso").
- **Decisão:** Foi aplicado um mapeamento simples: **Qualquer resposta que contivesse a string "Sim" foi padronizada para 'Sim'**, e qualquer outra resposta (incluindo nulos ou respostas como "Não tenho conhecimento") foi padronizada para **'Não'**.

### 2.2. Tratamento de Colunas de Texto e Nulos

- **Renomeação:** Todas as colunas foram renomeadas para o padrão **snake_case** (Ex: `'Nível de conhecimento'` para `'nivel_conhecimento'`) para facilitar o código Python.
- **Padronização de Texto:** Colunas categóricas (como `'faixa_etaria'` e `'nivel_conhecimento'`) foram limpas com `.str.strip().str.title()` para remover espaços e garantir que as contagens de grupo fossem precisas (Ex: 'iniciante' se torna 'Iniciante').
- **E-mail:** A coluna `'email'` foi padronizada para minúsculas (`.str.lower()`) para evitar duplicidade na contagem de usuários.

---

## 3. Estrutura e Carga (L)

O DataFrame limpo (`df_limpo`) foi modularizado em cinco tabelas para atender ao princípio de **Single Responsibility** (Responsabilidade Única) e facilitar futuras análises específicas. Esta etapa é realizada pelo script `03_estruturar_base_dados.py`.

### 3.1. Estrutura Modular (Esquema de Tabelas)

| Tabela Final              | Conteúdo                                     | Justificativa                                                                   |
| :------------------------ | :------------------------------------------- | :------------------------------------------------------------------------------ |
| **tabela_perfil_pessoal** | Demográficos e Nível de Conhecimento.        | Usada para segmentar o público (Ex: Nível de Conhecimento por Faixa Etária).    |
| **tabela_comportamento**  | Hábitos e Risco (Apostas, Reserva, Decisão). | Usada para analisar tendências comportamentais e propensão ao risco.            |
| **tabela_investimentos**  | Portfólio atual (Sim/Não para 5 classes).    | Usada para correlacionar o portfólio com o perfil e o objetivo financeiro.      |
| **tabela_textos_livres**  | Jornada e Conselho (Textos qualitativos).    | Usada para análise de sentimento, nuvens de palavras e insights não numéricos.  |
| **tabela_bcb_metadados**  | Séries do BCB (SELIC, IPCA, etc.).           | Usada para contextualizar a análise de risco e rentabilidade ao longo do tempo. |

### 3.2. Formato de Saída

Todos os DataFrames finais são salvos no formato **CSV** na pasta `./database` com o separador **ponto e vírgula (`;`)** e codificação **UTF-8**, garantindo a compatibilidade máxima e a preservação de caracteres especiais (acentos).
