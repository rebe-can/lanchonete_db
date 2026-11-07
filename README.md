# Sistema de Gestão de Lanchonete (`db_lanchonete`)

Projeto desenvolvido para fins de estudo e prática de modelagem de dados relacional, administração de bancos de dados PostgreSQL e automação de processos utilizando Python.

---

##  Sobre o Projeto
O sistema simula o controlo e a gestão operacional de uma lanchonete, abrangendo desde a conceção estrutural do modelo de dados até à persistência automatizada de informações a partir de planilhas.

## 🛠️ Tecnologias e Ferramentas Utilizadas
* **Banco de Dados:** PostgreSQL 
* **Linguagem:** Python 3
* **Manipulação de Dados:** Pandas
* **Conexão SQL:** Psycopg2
* **Segurança:** Python-dotenv (`.env` e `.gitignore`)
* **Controle de Versão:** Git e GitHub
* **Ambiente:** VS Code / Git Bash
* 
---

## 🗂️ Estrutura do Repositório

* `script_lanchonete.sql` — Script SQL contendo a criação das tabelas (Categorias, Clientes, Produtos, Pedidos e Itens do Pedido) e as respetivas chaves estrangeiras.
* `popular_dados.py` — Script automatizado em Python que lê todas as abas do Excel e popula o PostgreSQL em lote utilizando `ON CONFLICT DO NOTHING`.
* `lanchonete_dados.xlsx` — Planilha contendo os dados iniciais do negócio estruturados por abas.
* `modelo_conceitual.pdf` — Diagrama conceitual do banco de dados.
* `modelo_logico.pdf` — Diagrama lógico relacional.
* `.gitignore` — Configuração para proteger dados sensíveis.

---

## ⚙️ Como Executar o Projeto Localmente

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/rebe-can/projeto-lanchonete.git](https://github.com/rebe-can/projeto-lanchonete.git)
   cd projeto-lanchonete
