#importando as bibliotecas necessárias
import os
from dotenv import load_dotenv
import pandas as pd
import psycopg2

load_dotenv()

#configurações de conexão com o PostgreSQL
DB_HOST = "localhost"
DB_NAME = "db_lanchonete"
DB_USER = "postgres"
DB_PASS = os.getenv("DB_PASS")  
DB_PORT = "5432"


def popular_dados():
  arquivo_excel = "lanchonete_dados.xlsx"
  print("Lendo todas as abas da planilha...")

  #carregando todas as abas da planilha do excel
  df_categorias = pd.read_excel(arquivo_excel, sheet_name="categorias")
  df_clientes = pd.read_excel(arquivo_excel, sheet_name="clientes")
  df_produtos = pd.read_excel(arquivo_excel, sheet_name="produtos")
  df_pedidos = pd.read_excel(arquivo_excel, sheet_name="pedidos")
  df_itens = pd.read_excel(arquivo_excel, sheet_name="itens_pedido")

  try:
    conexao = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        port=DB_PORT,
    )
    cursor = conexao.cursor()
    print("Conexão com o PostgreSQL estabelecida com sucesso!")

    # 1 CATEGORIAS 
    print("Populando categorias...")
    for _, row in df_categorias.iterrows():
      cursor.execute(
          """
                INSERT INTO categorias (categoria_id, nome, descricao) 
                VALUES (%s, %s, %s)
                ON CONFLICT (categoria_id) DO NOTHING;
            """,
          (int(row["categoria_id"]), str(row["nome"]), str(row["descricao"])),
      )

    # 2.CLIENTES 
    print("Populando clientes...")
    for _, row in df_clientes.iterrows():
      cursor.execute(
          """
                INSERT INTO clientes (cliente_id, nome, email, telefone) 
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (cliente_id) DO NOTHING;
            """,
          (
              int(row["cliente_id"]),
              str(row["nome"]),
              str(row["email"]),
              str(row["telefone"]),
          ),
      )

    # 3 PRODUTOS 
    print("Populando produtos...")
    for _, row in df_produtos.iterrows():
      cursor.execute(
          """
                INSERT INTO produtos (produto_id, categoria_id, nome, preco, estoque) 
                VALUES (%s, %s, %s, %s, %s)
                ON CONFLICT (produto_id) DO NOTHING;
            """,
          (
              int(row["produto_id"]),
              int(row["categoria_id"]),
              str(row["nome"]),
              float(row["preco"]),
              int(row["estoque"]),
          ),
      )

    # 4 PEDIDOS 
    print("Populando pedidos...")
    for _, row in df_pedidos.iterrows():
      cursor.execute(
          """
                INSERT INTO pedidos (pedido_id, cliente_id, data_pedido, status) 
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (pedido_id) DO NOTHING;
            """,
          (
              int(row["pedido_id"]),
              int(row["cliente_id"]),
              str(row["data_pedido"]),
              str(row["status"]),
          ),
      )

    # 5 ITENS DO PEDIDO 
    print("Populando itens do pedido...")
    for _, row in df_itens.iterrows():
      cursor.execute(
          """
                INSERT INTO itens_pedido (item_id, pedido_id, produto_id, quantidade, preco_unitario) 
                VALUES (%s, %s, %s, %s, %s)
                ON CONFLICT (item_id) DO NOTHING;
            """,
          (
              int(row["item_id"]),
              int(row["pedido_id"]),
              int(row["produto_id"]),
              int(row["quantidade"]),
              float(row["preco_unitario"]),
          ),
      )

    # efetiva todas as alterações no banco
    conexao.commit()
    print("Sucesso! Planilha inteira importada para o PostgreSQL! 🚀")

  except Exception as e:
    print(f"Ocorreu um erro durante a importação: {e}")
    if "conexao" in locals():
      conexao.rollback()

  finally:
    if "cursor" in locals():
      cursor.close()
    if "conexao" in locals():
      conexao.close()


if __name__ == "__main__":
  popular_dados()