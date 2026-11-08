# Sistema de Gestão de Lanchonete (`db_lanchonete`) 🇧🇷 ☺️

Projeto desenvolvido para fins de estudo e prática de modelagem de dados relacional, administração de bancos de dados PostgreSQL, automação de processos utilizando Python e desenvolvimento web com **Flask**.

## Sobre o Projeto
O sistema simula o controle e a gestão operacional de uma lanchonete, abrangendo desde a concepção estrutural do modelo de dados, persistência automatizada de informações a partir de planilhas, até um **dashboard web interativo** construído em Flask com estilização moderna em CSS. c:

## 🛠️ Tecnologias e Ferramentas Utilizadas
* **Banco de Dados:** PostgreSQL (com Views em SQL)
* **Back-end & Web:** Python 3, Flask
* **Front-end:** HTML5, CSS3 (com folha de estilos externa)
* **Manipulação de Dados:** Pandas
* **Conexão SQL:** Psycopg2
* **Segurança:** Python-dotenv (`.env` e `.gitignore`)
* **Controle de Versão:** Git e GitHub
* **Ambiente:** VS Code / Git Bash
* 
---

## 📂 Estrutura do Repositório

* `app.py` — Aplicação principal em Flask responsável por conectar ao banco, buscar os dados da View e renderizar o dashboard.
* `static/style.css` — Folha de estilos CSS externa para o design moderno do dashboard.
* `templates/index.html` — Estrutura HTML da página web integrada com Jinja2.
* `script_lanchonete.sql` — Script SQL contendo a criação das tabelas (Categorias, Clientes, Produtos, Pedidos e Itens do Pedido) e as respectivas chaves estrangeiras.
* `popular_dados.py` — Script automatizado em Python que lê a planilha e popula o PostgreSQL em lote.
* `lanchonete_dados.xlsx` — Planilha contendo os dados iniciais do negócio estruturados por abas.
* `modelo_conceitual.pdf` — Diagrama conceitual do banco de dados.
* `modelo_logico.pdf` — Diagrama lógico relacional.
* `.gitignore` — Configuração para proteger dados sensíveis (incluindo o arquivo `.env`).
---

## ⚙️ Como Executar o Projeto Localmente

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/rebe-can/projeto-lanchonete.git](https://github.com/rebe-can/projeto-lanchonete.git)
   cd projeto-lanchonete
