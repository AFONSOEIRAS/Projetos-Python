import sqlite3

con = sqlite3.connect("glow_modas.db")
cur = con.cursor()

# Criar a tabela Produto
cur.execute("""CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_produto TEXT NOT NULL,
    tipo_produto TEXT NOT NULL,
    valor_compra_produto REAL NOT NULL,
    quantidade_estoque REAL NOT NULL,
    data_compra TEXT NOT NULL
);""")
#OBS: TALVEZ quantidade_estoque SEJA UMA NOVA TABELA


# Criar a tabela Venda
cur.execute("""CREATE TABLE IF NOT EXISTS vendas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_Produto INTEGER NOT NULL,
    valor_venda_produto REAL NOT NULL,
    data_venda TEXT NOT NULL,
    FOREIGN KEY (id_Produto)
    REFERENCES produto (id)   
);""")
#ADICIONAR MAIS DADOS POR EXEMPLO DATA DA VENDA

# Dados do produto
nome_produto = 'Cropped Cinza'
tipo_produto = 'Cropped'
valor_compra_produto = 9.99
quantidade_estoque = 5
data_compra = '2023-11-06'

id_produto = 1
valor_venda_produto = 19.99
data_venda = '2023-11-07'


#Inserir um novo registro na tabela
cur.execute("INSERT INTO produtos (nome_produto, tipo_produto, valor_compra_produto, quantidade_estoque, data_compra) VALUES (?, ?, ?, ?)", (nome_produto, tipo_produto, valor_compra_produto, quantidade_estoque, data_compra))

cur.execute("INSERT INTO vendas (id_produto, valor_venda_produto, data_venda) VALUES (?, ?, ?)", (id_produto, valor_venda_produto, data_venda))
cur.execute("INSERT INTO vendas (id_produto, valor_venda_produto, data_venda) VALUES (?, ?, ?)", (id_produto, valor_venda_produto, '2023-11-08'))

# to select all column we will use 
query_select_produtos = '''SELECT * FROM produtos'''
obj_query_select_produtos = cur.execute(query_select_produtos) 
list_produtos = obj_query_select_produtos.fetchall()
print("All the data") 
for row in list_produtos: 
  print(row) 


query_select_vendas = '''SELECT * FROM vendas'''
obj_query_select_vendas = cur.execute(query_select_vendas) 
list_vendas = obj_query_select_vendas.fetchall()
print("All the data") 
for row in list_vendas: 
  print(row) 



data_limite = '2023-11-08'
query_select_vendas = '''SELECT * FROM vendas WHERE data_venda >= ?'''
obj_query_select_vendas = cur.execute("SELECT * FROM vendas WHERE data_venda >= ?", (data_limite,))
list_vendas = obj_query_select_vendas.fetchall()
print("LOOP DATAS FILTRADAS") 
for row in list_vendas: 
  print(row) 

# Salvar as alterações no banco de dados
con.commit()

# Fechar a conexão com o banco de dados
con.close()
