from tkinter import *
from tkinter import messagebox
import sqlite3




class Application():
    def __init__(self): 
        self.root = Tk()
        self._tela()
        self._frames_da_tela()
        self._widgets_frame1()
        # criando o Loop
        self.root.mainloop()
       

    def  _start_database(self):
        self.con = sqlite3.connect("glow_modas.db")
        self.cur = self.con.cursor()

        self.cur.execute("""CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_produto TEXT NOT NULL,
        tipo_produto TEXT NOT NULL,
        valor_compra_produto REAL NOT NULL,
        quantidade INTEGER NOT NULL,
        data_compra TEXT NOT NULL
        );""")

        self.cur.execute("""CREATE TABLE IF NOT EXISTS vendas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_Produto INTEGER NOT NULL,
        valor_venda_produto REAL NOT NULL,
        data_venda TEXT NOT NULL,
        FOREIGN KEY (id_Produto)
        REFERENCES produto (id)   
        );""")
        
    def _tela(self):
        self.root.title("Glow Modas")
        self.root.configure(background= '#333333')
        self.root.geometry("700x600")
        self.root.resizable(True, True)
        self.root.maxsize(width=800, height=700)
        self.root.minsize(width=500, height=300)

    def _frames_da_tela(self):
        self.frame_1 = Frame(self.root, bd=4, bg= '#f0f0f0', highlightbackground= '#ffa2e8', highlightthickness=2)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self.frame_2 = Frame(self.root, bd=4, bg='#f0f0f0', highlightbackground= '#ffa2e8', highlightthickness=2)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

    def _widgets_frame1(self):
        
        self.nome_produto = StringVar()
        self.lb_nome_produto = Label(self.frame_1,text="Nome do Produto:")
        self.lb_nome_produto.place(relx=0.01, rely=0.01, relwidth=0.16, relheight=0.14)
        self.entry_nome_produto = Entry(self.frame_1, textvariable=self.nome_produto)
        self.entry_nome_produto.place(relx=0.21, rely=0.04, relwidth=0.20, relheight=0.08)
        
        self.tipo_produto = StringVar()
        self.lb_tipo_produto = Label(self.frame_1,text="Tipo do Produto:")
        self.lb_tipo_produto.place(relx=0.01, rely=0.12, relwidth=0.14, relheight=0.14)
        self.entry_tipo_produto = Entry(self.frame_1,textvariable=self.tipo_produto)
        self.entry_tipo_produto.place(relx=0.21, rely=0.15, relwidth=0.20, relheight=0.08) 

        self.valor_compra_produto = StringVar()
        self.lb_valor_compra_produto = Label(self.frame_1,text="Valor da Compra (R$):")
        self.lb_valor_compra_produto.place(relx=0.01, rely=0.23, relwidth=0.18, relheight=0.14)
        self.entry_valor_compra_produto = Entry(self.frame_1, textvariable=self.valor_compra_produto)
        self.entry_valor_compra_produto.place(relx=0.21, rely=0.26, relwidth=0.20, relheight=0.08)   

        ##IMPORTANTE LEMBRAR
        #QUANTIDADE EM ESTOQUE DEVE SALVAR A QUANTIDADE ANTERIOR POR TIPO E INCREMENTAR CONFORME FOR ADICIONADO MAIS PRODUTOS IGUAIS
        #OBS:Trocar a 'coluna quantidade em estoque' por 'quantidade', e 'quantidade em estoque' será adicionada automaticamente conforme produtos do mesmo tipo serão adicionados.
        self.quantidade = StringVar()
        self.lb_quantidade = Label(self.frame_1,text="Quantidade:")
        self.lb_quantidade.place(relx=0.01, rely=0.34, relwidth=0.10, relheight=0.14)
        self.entry_quantidade = Entry(self.frame_1, textvariable=self.quantidade)
        self.entry_quantidade.place(relx=0.21, rely=0.37, relwidth=0.05, relheight=0.08)   
        
        self.data_compra = StringVar()
        self.lb_data_compra = Label(self.frame_1,text="Data da Compra:")
        self.lb_data_compra.place(relx=0.01, rely=0.45, relwidth=0.14, relheight=0.14)
        self.entry_data_compra = Entry(self.frame_1,textvariable=self.data_compra)
        self.entry_data_compra.place(relx=0.21, rely=0.48, relwidth=0.20, relheight=0.08)  

        
        self.button_adicionar = Button(self.frame_1, text= 'Adicionar', bg = '#ffa2e8', fg = '#333333', font= ("verdana", 10, "bold"), command=self._adicionar_dados_banco)
        self.button_adicionar.place(relx=0.85, rely=0.85, relwidth=0.12, relheight=0.14)
        #self.button_buscar = Button(self.frame_1, text= 'Buscar', bg = '#ffa2e8', fg = 'white', font= ("verdana", 10, "bold"))
        #self.button_buscar.place(relx=0.40, rely=0.08, relwidth=0.12, relheight=0.14)
        #self.button_salvar = Button(self.frame_1, text= 'Salvar', bg = '#008000', fg = 'white', font= ("verdana", 10, "bold"))
        #self.button_salvar.place(relx=0.54, rely=0.08, relwidth=0.12, relheight=0.14)
        #self.button_deletar = Button(self.frame_1, text= 'Deletar', bg = '#ff0000', fg = 'white', font= ("verdana", 10, "bold"))
        #self.button_deletar.place(relx=0.68, rely=0.08, relwidth=0.12, relheight=0.14)


    def _adicionar_dados_banco(self, *args):
        
        self._start_database()


        try:
            #ADICIONAR VALIDAÇÕES PARA SE O TIPO DE DADOS ESTÁ CORRETO
            nome_produto_insert_database = str(self.nome_produto.get())
            tipo_produto_insert_database= str(self.tipo_produto.get())
            
            #Validação para se o valor da compra é numérico ou não 
            try:
                is_float = isinstance(float(self.valor_compra_produto.get()), float)
            except ValueError:
                is_float = False

            if is_float:
                valor_compra_produto_insert_database= float(self.valor_compra_produto.get())
            else:
                raise ValueError("Valor de compra do produto não é numérico!")    


            #Validação para se o valor da compra é numérico ou não 
            try:
                is_int = isinstance(int(self.quantidade.get()), int)
            except ValueError:
                is_int = False
            
            if is_int:
                quantidade_insert_database= int(self.quantidade.get())
            else:
                raise ValueError("Quantidade não é inteiro!")    
            
            #IMPORTANTE
            #ADICIONAR VALIDAÇÃO PARA DATA E FAZER CONVERSÃO DE UMA DATA INTERIDA NO FORMADO dd/MM/yyyy PARA O FORMATO yyyy-MM-dd
            data_compra_insert_database = str(self.data_compra.get())

            self.cur.execute("INSERT INTO produtos (nome_produto, tipo_produto, valor_compra_produto, quantidade, data_compra) VALUES (?, ?, ?, ?,?)", (nome_produto_insert_database, tipo_produto_insert_database, valor_compra_produto_insert_database, quantidade_insert_database, data_compra_insert_database))
        
            print("Nome Produto: " + str(self.nome_produto.get()))
            print("Tipo Produto: " + str(self.tipo_produto.get()))
            print("Valor Compra: " +str(self.valor_compra_produto.get()))
            print("Quantidade: "+ str(self.quantidade.get()))
            print("Data da Compra:"+ str(self.data_compra.get()))
            #to select all column we will use 
            query_select_produtos = '''SELECT * FROM produtos'''
            obj_query_select_produtos = self.cur.execute(query_select_produtos) 
            list_produtos = obj_query_select_produtos.fetchall()
            print("All the data") 
            for row in list_produtos: 
                print(row) 


            # Salvar as alterações no banco de dados
            self.con.commit()
            # Fechar a conexão com o banco de dados
            self.con.close()
        
        except Exception as e:
            # Exibe uma tela de erro personalizada
            messagebox.showerror("Erro:", e)


 



Application()
