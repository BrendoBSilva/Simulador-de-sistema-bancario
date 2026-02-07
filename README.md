Sistema Bancário com Pipeline 

Visão Geral
Este projeto simula um **sistema bancário analítico**, integrando **SQL, Python e análise de dados**, com foco em **inadimplência, score de crédito e risco financeiro**.  
O objetivo é demonstrar, de forma prática, como dados bancários podem ser organizados, processados e analisados em uma **pipeline real de dados**, seguindo para uma análise dos mesmos via Power BI.

---

Objetivos do Projeto
- Criar uma base bancária estruturada em SQL
- Processar dados financeiros via Python
- Identificar clientes inadimplentes
- Calcular métricas de risco e score de crédito
- Exportar dados para análise e visualização
- Demonstrar raciocínio analítico aplicado ao setor bancário

---

Arquitetura da Solução (Pipeline)

MySQL (Workbench)
↓
Python (ETL + Regras de Negócio)
↓
CSV Analítico
↓
Power BI / Análises


---

Modelagem SQL
O banco de dados foi criado no **MySQL Workbench**, contendo tabelas que simulam um ambiente bancário real, como:

- Clientes
- Operações financeiras
- Empréstimos
- Inadimplência

Pipeline em Python
O Python foi utilizado para consumir os dados do banco, aplicar regras de negócio e gerar datasets analíticos.

### Principais funcionalidades:
- Conexão com banco MySQL
- Extração de dados via SQL
- Identificação de inadimplência
- Cálculo de score de crédito
- Classificação de risco (baixo, médio, alto)
- Exportação de dados para CSV

Arquivos principais:
banco.py
pipeline.py
export_csv.py


---

Métricas Calculadas
- Total de clientes
- Taxa de inadimplência
- Valor em risco
- Score de crédito
- Classificação de risco por cliente

Essas métricas permitem **análises estratégicas e suporte à tomada de decisão**.

---

Estrutura do Projeto

Sistema_Bancario/
├── banco.sql
├── banco.py
├── pipeline.py
├── export_csv.py
├── dataset.csv

├── README.md
└── .gitignore

<img width="1108" height="658" alt="Representação pdf e mais 5 páginas - Perfil 1 — Microsoft​ Edge 06_02_2026 21_09_28" src="https://github.com/user-attachments/assets/e43d7b8b-e8c3-46a7-b189-e7cc9c55a72a" />



