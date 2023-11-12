from tkinter import *
from tkinter import ttk



class Application():
    def __init__(self):
        self.root = Tk()
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        # criando o Loop
        self.root.mainloop()
    def tela(self):
        self.root.title("Glow Modas")
        self.root.configure(background= '#1e3743')
        self.root.geometry("700x600")
        self.root.resizable(True, True)
        self.root.maxsize(width=800, height=700)
        self.root.minsize(width=500, height=300)
    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bd=4, bg= '#f0f0f0', highlightbackground= '#ffa2e8', highlightthickness=2)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self.frame_2 = Frame(self.root, bd=4, bg='#f0f0f0', highlightbackground= '#ffa2e8', highlightthickness=2)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

    def widgets_frame1(self):

        self.lb_nome_produto = Label(self.frame_1,text="Nome do Produto:")
        self.lb_nome_produto.place(relx=0.01, rely=0.01, relwidth=0.16, relheight=0.14)
        self.entry_nome_produto = Entry(self.frame_1)
        self.entry_nome_produto.place(relx=0.17, rely=0.04, relwidth=0.20, relheight=0.08)
        
        self.lb_tipo_produto = Label(self.frame_1,text="Tipo do Produto:")
        self.lb_tipo_produto.place(relx=0.01, rely=0.12, relwidth=0.16, relheight=0.14)
        self.entry_tipo_produto = Entry(self.frame_1)
        self.entry_tipo_produto.place(relx=0.17, rely=0.15, relwidth=0.20, relheight=0.08)     
        
        self.lb_valor_compra_produto = Label(self.frame_1,text="Valor da Compra:")
        self.lb_valor_compra_produto.place(relx=0.01, rely=0.23, relwidth=0.16, relheight=0.14)
        self.entry_valor_compra_produto = Entry(self.frame_1)
        self.entry_valor_compra_produto.place(relx=0.17, rely=0.26, relwidth=0.20, relheight=0.08)   

        ##IMPORTANTE LEMBRAR
        #QUANTIDADE EM ESTOQUE DEVE SALVAR A QUANTIDADE ANTERIOR POR TIPO E INCREMENTAR CONFORME FOR ADICIONADO MAIS PRODUTOS IGUAIS
        #OBS:Trocar a 'coluna quantidade em estoque' por 'quantidade', e 'quantidade em estoque' será adicionada automaticamente conforme produtos do mesmo tipo serão adicionados.
        self.lb_quantidade = Label(self.frame_1,text="Quantidade:")
        self.lb_quantidade.place(relx=0.01, rely=0.34, relwidth=0.16, relheight=0.14)
        self.entry_quantidade = Entry(self.frame_1)
        self.entry_quantidade.place(relx=0.17, rely=0.37, relwidth=0.05, relheight=0.08)   

        self.lb_data_compra = Label(self.frame_1,text="Data da Compra:")
        self.lb_data_compra.place(relx=0.01, rely=0.45, relwidth=0.16, relheight=0.14)
        self.entry_data_compra = Entry(self.frame_1)
        self.entry_data_compra.place(relx=0.17, rely=0.48, relwidth=0.20, relheight=0.08)   



        self.button_adicionar = Button(self.frame_1, text= 'Adicionar', bg = '#ffa2e8', fg = 'white', font= ("verdana", 10, "bold"))
        self.button_adicionar.place(relx=0.85, rely=0.85, relwidth=0.12, relheight=0.14)
        #self.button_buscar = Button(self.frame_1, text= 'Buscar', bg = '#ffa2e8', fg = 'white', font= ("verdana", 10, "bold"))
        #self.button_buscar.place(relx=0.40, rely=0.08, relwidth=0.12, relheight=0.14)
        #self.button_salvar = Button(self.frame_1, text= 'Salvar', bg = '#008000', fg = 'white', font= ("verdana", 10, "bold"))
        #self.button_salvar.place(relx=0.54, rely=0.08, relwidth=0.12, relheight=0.14)
        #self.button_deletar = Button(self.frame_1, text= 'Deletar', bg = '#ff0000', fg = 'white', font= ("verdana", 10, "bold"))
        #self.button_deletar.place(relx=0.68, rely=0.08, relwidth=0.12, relheight=0.14)


Application()
