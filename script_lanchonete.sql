-- 1. Criar o Banco de Dados
CREATE DATABASE db_lanchonete;

-- (Conecte-se ao banco db_lanchonete criado acima antes de rodar os comandos abaixo)

-- 2. Tabela de Clientes
CREATE TABLE clientes (
    cliente_id SERIAL PRIMARY KEY,
    nome VARCHAR(150) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    telefone VARCHAR(20)
);

-- 3. Tabela de Categorias de Produtos
CREATE TABLE categorias (
    categoria_id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT
);

-- 4. Tabela de Produtos (Cardápio)
CREATE TABLE produtos (
    produto_id SERIAL PRIMARY KEY,
    categoria_id INT REFERENCES categorias(categoria_id),
    nome VARCHAR(150) NOT NULL,
    preco NUMERIC(10, 2) NOT NULL,
    estoque INT NOT NULL
);

-- 5. Tabela de Pedidos
CREATE TABLE pedidos (
    pedido_id SERIAL PRIMARY KEY,
    cliente_id INT REFERENCES clientes(cliente_id),
    data_pedido TIMESTAMP NOT NULL,
    status VARCHAR(50) NOT NULL
);

-- 6. Tabela Associativa de Itens do Pedido
CREATE TABLE itens_pedido (
    item_id SERIAL PRIMARY KEY,
    pedido_id INT REFERENCES pedidos(pedido_id) ON DELETE CASCADE,
    produto_id INT REFERENCES produtos(produto_id),
    quantidade INT NOT NULL,
    preco_unitario NUMERIC(10, 2) NOT NULL
);