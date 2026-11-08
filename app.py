from flask import Flask, render_template
import os
import psycopg2
import pandas as pd
from dotenv import load_dotenv

#carregando as variáveis de ambiente do ficheiro .env
load_dotenv()

app = Flask(__name__)

#def para conectar ao PostgreSQL e buscas os dados da View
def buscar_dados_lanchonete():
    try:
        conexao = psycopg2.connect(
            host=os.getenv("DB_HOST", "localhost"),
            database=os.getenv("DB_NAME", "db_lanchonete"),
            user=os.getenv("DB_USER", "postgres"),
            password=os.getenv("DB_PASSWORD") or os.getenv("DB_PASS"),
            port=os.getenv("DB_PORT", "5432")
        )
        #consulta a view que foi criada no banco:
        query = "SELECT * FROM vw_resumo_pedidos;"
        df = pd.read_sql(query, conexao)
        conexao.close()

        #convertendo o DataFrame para um formato de dict para o HTML ler facilmente:
        return df.to_dict(orient="records")
    except Exception as e:
        print(f"Erro ao conectar ao banco: {e}")
        return []

#Rota principal do site:
@app.route("/")
def index():
    pedidos = buscar_dados_lanchonete()
    return render_template("index.html", pedidos = pedidos)

if __name__ == "__main__":
    app.run(debug=True)