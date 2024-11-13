CREATE TABLE produtos_db (id SERIAL PRIMARY KEY, nome VARCHAR(100) NOT NULL, preco DECIMAL(10, 2) NOT NULL, codigo_barra VARCHAR(13) UNIQUE NOT NULL);


INSERT INTO produtos (nome, preco, codigo_barra) VALUES ('Produto Exemplo', 29.99, '7891234567890');

SELECT * FROM produtos;

SELECT * FROM produtos WHERE codigo_barra = '7891234567890';


UPDATE produtos SET preco = 34.99 WHERE codigo_barra = '7891234567890';

DELETE FROM produtos WHERE codigo_barra = '7891234567890';