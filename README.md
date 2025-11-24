# 🚀 SGEF (Sistema de Gestão e Educação Financeira): A Chave para Seus Investimentos

![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
![Versão](https://img.shields.io/badge/versão-1.0-blue)
![Contribuições](https://img.shields.io/badge/contribuições-bem--vindas-brightgreen)
![Feito com](https://img.shields.io/badge/Feito%20com-Love-red)
![Tecnologias](https://img.shields.io/badge/Tecnologias-Python%20%7C%20HTML%20%7C%20Bootstrap-blueviolet)

## Curso: Ciência da Computação

## Instituição: Centro Universitário de Brasília (UniCEUB)

## Projeto Integrador I

---

## 💡 Sobre o Projeto

O **Projeto Integrador - Educação Financeira** nasceu com um propósito claro: **democratizar o acesso ao conhecimento sobre investimentos**.

Este projeto visa auxiliar qualquer pessoa a aprender sobre o mercado financeiro de forma **clara, prática e 100% acessível**. Aqui, desmistificamos a ideia de que investir é complexo ou exclusivo para especialistas, provando que é um hábito que pode transformar sua vida financeira.

Você encontrará materiais, ferramentas e exemplos focados em:

- **Renda Variável:**
      - **Bolsa de Valores (Ações)**
      - **Fundos de Investimento Imobiliário (FIIs)**
- **Renda Fixa e Títulos Públicos:**
      - **Tesouro Direto** (Selic, Prefixado e IPCA+)
      - **Renda Fixa Privada** (CDBs, LCIs, LCAs, Debêntures, etc.)

---

## 💻 Tecnologias Utilizadas

Este projeto foi desenvolvido utilizando as seguintes tecnologias, incluindo as bibliotecas de Data Science e Análise de Dados:

| Categoria                | Tecnologia            | Descrição                                                                                                        |
| :----------------------- | :-------------------- | :--------------------------------------------------------------------------------------------------------------- |
| **Backend/Lógica**       | **Python**            | Lógica do simulador e scripts de **Análise e Engenharia de Dados (ETL)**.                                        |
| **Análise de Dados**     | **Pandas / Seaborn**  | Manipulação, limpeza de dados e criação de gráficos analíticos.                                                  |
| **Frontend/Estrutura**   | **HTML5**             | Estrutura fundamental das páginas web.                                                                           |
| **Frontend/Design**      | **Bootstrap**         | Framework para um design responsivo, moderno e padronizado.                                                      |

---

## 💾 Arquitetura e Fluxo de Dados (ETL)

O projeto segue um fluxo de trabalho claro de **Extração, Transformação e Carga (ETL)**, que combina dados macroeconômicos e comportamentais para gerar insights.

### 1. Fontes de Dados

- **API do Banco Central do Brasil (BCB):** Extração de indicadores macroeconômicos (SELIC, IPCA) para contextualizar o ambiente de investimento.
- **Formulário de Pesquisa (CSV):** Dados primários sobre o perfil, conhecimento, objetivos e comportamento de investimento do público.

### 2. Base de Dados Estruturada e Dicionário

O processo de Engenharia de Dados resulta em uma base de dados modularizada, que é o principal entregável técnico.

Para detalhes completos sobre as colunas, seus tipos e valores em cada tabela (`tabela_bcb_metadados`, `tabela_perfil_pessoal`, etc.), consulte o documento:

➡️ **[DICIONÁRIO DE DADOS COMPLETO](./DICIONARIO_DE_DADOS.md)**

---

## 📈 Análise de Dados e Insights Gerados

Os scripts analíticos são utilizados para responder perguntas-chave sobre o público:

1.  **Adoção de Risco:** Existe uma correlação entre **Faixa Etária** e a **participação em Renda Variável** ou **Apostas**?
2.  **Educação vs. Prática:** Qual a relação entre o **Nível de Conhecimento** autodeclarado e a posse de uma **Reserva de Emergência**?
3.  **Metas vs. Perfil:** Como o **Objetivo Financeiro** (Ex: Viver de Renda) se alinha com a **Decisão Financeira** (Ex: Preferência por segurança ou por assumir novos riscos)?

---

## 📁 Estrutura do Repositório (Scripts)

Os scripts de Python que guiam o fluxo de ETL e análise estão localizados em `./scripts/` e devem ser executados na seguinte ordem:

| Script                          | Função Principal                                                                                            |
| :------------------------------ | :---------------------------------------------------------------------------------------------------------- |
| `01_BCB_Data.pynb`              | Extrai e limpa os dados macroeconômicos do BCB.                                                             |
| `02_Data_Forms.pynb`            | Realiza a limpeza (`Sim`/`Não`, padronização de texto) e gera as análises e gráficos do formulário.         |
| `03_estruturar_base_dados.py`   | Cria a Base Estruturada (modulariza o `df_limpo` em tabelas) e salva o entregável final.                    |

---

---

## 📄 Documentação Técnica e Decisões de Projeto

Para uma visão detalhada das escolhas de Engenharia de Dados, o tratamento de dados faltantes, a padronização das respostas e a justificativa para a escolha das séries do Banco Central (BCB), consulte o documento de documentação técnica:

➡️ **[DOCUMENTAÇÃO TÉCNICA COMPLETA](./DOCUMENTACAO_TECNICA.md)**

## ❓ A Motivação

Muitas pessoas evitam investir por medo, falta de informação de qualidade ou por acreditarem em mitos financeiros. Acreditamos que a **educação financeira** é a ferramenta mais poderosa para construir um futuro seguro.

Nossos pilares:

- **Combate à Desinformação:** Oferecer conteúdo de qualidade e acessível.
- **Fuga das Dívidas:** Ajudar a criar bons hábitos e sair do endividamento.
- **Investimento Seguro:** Mostrar que é possível começar com pouco e construir patrimônio com segurança.
- **Liberdade Financeira:** Incentivar uma mentalidade de longo prazo, focada em independência.

---

## 🎯 Objetivos Principais

O que queremos entregar e ensinar:

- **Fundamentos do Mercado:** Ensinar os conceitos básicos e avançados do mercado financeiro.
- **Estratégias para Todos:** Apresentar estratégias de investimento adequadas para diferentes perfis (conservador, moderado e agressivo).
- **Prática e Simulação:** Oferecer simuladores e exemplos práticos para acelerar e facilitar o aprendizado.
- **Mentalidade Financeira:** Incentivar a educação como ferramenta de liberdade e independência duradoura.

---

## 👥 Contribuidores e Equipe

Agradecemos a dedicação e o esforço de todos os membros da equipe que tornaram este projeto possível.

| Membro                                | Função               | GitHub                                                  |
| :------------------------------------ | :------------------- | :------------------------------------------------------ |
| **Bruno de Lima Marques**             | Gerente de Projeto   | [`bruno.lmars`](https://github.com/bruno.lmars)         |
| **Caue Muniz Anastacio**              | Pesquisador          | [`Catadordegames`](https://github.com/Catadordegames)   |
| **Davi Pereira Araújo**               | QA/Tester            | [`Ovomexid0`](https://github.com/Ovomexid0)             |
| **joão pedro nunes gomes da silva**   | Desenvolvedor        | [`joaosilva07`](https://github.com/joaosilva07)         |
| **Luisa de Moura Zimmer**             | Designer             | [`lulumishi`](https://github.com/lulumishi)             |

---

## 🤝 Quer Contribuir?

Se você tem interesse em melhorar ou expandir este projeto, sua contribuição é muito bem-vinda!

- Sinta-se à vontade para abrir **Issues** para relatar bugs ou sugerir novas funcionalidades.
- Para submeter correções ou novas implementações, por favor, faça um **Pull Request**.
