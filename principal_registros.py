import tkinter as tk
from tkinter import ttk
import def_registros as def_registros



class PrincipalDB:
    def __init__(self, win):
        self.objBD = def_registros.AppBD()
        # Componentes
        self.lbCodigo=tk.Label(win, text='Codigo: ')
        self.lblData = tk.Label(win, text='Data de Registro: ')
        self.lblNome=tk.Label(win, text='Nome do Aluno: ')
        self.lblTurma=tk.Label(win, text='Turma: ')

        self.txtCodigo=tk.Entry(bd=3)
        self.txtData = tk.Entry()
        self.txtNome=tk.Entry()
        self.txtTurma=tk.Entry()


        self.btnCadastrar=tk.Button(win, text='Cadastrar', command=self.fcadastrarProduto)
        self.btnAtualizar=tk.Button(win, text='Atualizar', command=self.fAtualizarProduto)
        self.btnExcluir=tk.Button(win, text='Excluir', command=self.fExcluirProduto)
        self.btnLimpar=tk.Button(win, text='Limpar', command=self.fLimparTela)
        self.btnBuscar=tk.Button(win, text='Buscar', command=self.fBuscarProduto)


        self.dadosColunas = ("Codigo", "Data", "Nome", "Turma")
        self.treeRegistro = ttk.Treeview(win, columns=self.dadosColunas, selectmode='browse')
        self.verscrlbar = ttk.Scrollbar(win, orient='vertical', command=self.treeRegistro.yview)
        self.verscrlbar.pack(side='right', fill='x')
        self.treeRegistro.configure(yscrollcommand=self.verscrlbar.set)
        self.treeRegistro.heading("Codigo", text="Código")
        self.treeRegistro.heading("Data", text="Data de Registro")
        self.treeRegistro.heading("Nome", text="Nome do Aluno")
        self.treeRegistro.heading("Turma", text="Turma")

        self.treeRegistro.column("Codigo", minwidth=0, width=100)
        self.treeRegistro.column("Data", minwidth=0, width=100)
        self.treeRegistro.column("Nome", minwidth=0, width=100)
        self.treeRegistro.column("Turma", minwidth=0, width=100)

        self.treeRegistro.pack(padx=10, pady=10)
        self.treeRegistro.bind("<<TreeviewSelect>>", self.apresentarRegistrosSelecionados)

        #Posicionamento dos componentes na janela
        self.lbCodigo.place(x=100, y=50)
        self.txtCodigo.place(x=250, y=50)

        self.lblData.place(x=100, y=100)
        self.txtData.place(x=250, y=100)

        self.lblNome.place(x=100, y=150)
        self.txtNome.place(x=250, y=150)

        self.lblTurma.place(x=400, y=50)
        self.txtTurma.place(x=550, y=50)


        self.btnCadastrar.place(x=100, y=200)
        self.btnAtualizar.place(x=200, y=200)
        self.btnExcluir.place(x=300, y=200)
        self.btnLimpar.place(x=400, y=200)
        self.btnBuscar.place(x=500, y=200)

        self.treeRegistro.place(x=100, y=300)
        self.verscrlbar.place(x=805, y=300, height=225)
        self.carregarDadosIniciais()

    def apresentarRegistrosSelecionados(self, event):
        self.fLimparTela()
        for selection in self.treeRegistro.selection():
            item = self.treeRegistro.item(selection)
            codigo,data,nome,turma = item["values"][0:4]
            self.txtCodigo.insert(0, codigo)
            self.txtData.insert(0, data)
            self.txtNome.insert(0, nome)
            self.txtTurma.insert(0, turma)

    def carregarDadosIniciais(self):
        try:
            self.id = 0
            self.iid = 0
            registro = self.objBD.selecionarDados()
            print("***************** dados disponiveis no BD *******************")
            for item in registro:
                codigo = item[0]
                data = item[1]
                nome = item[2]
                turma = item[3]
                print("código = ", codigo)
                print("Data = ", data)
                print("Nome = ", nome)
                print("Turma = ", turma, "\n")

                self.treeRegistro.insert('', 'end', iid=self.iid, values=(codigo, data, nome, turma))
                self.iid = self.iid + 1
                self.id = self.id + 1
                print("Dados da base")
        except:
            print('Ainda não existem dados para carregar')

    def fLerCampos(self):
        try:
            print("******************** dados disponiveis *********************")
            codigo = int(self.txtCodigo.get())
            print('codigo', codigo)
            data = self.txtData.get()
            print('data', data)
            nome = self.txtNome.get()
            print('nome', nome)
            turma = self.txtTurma.get()
            print('turma', turma)
            print("Leitura os dados com sucesso")
        except:
            print('Não foi possivel ler os dados')
        return codigo, data, nome, turma

    def fcadastrarProduto(self):
        try:
            print("****************** dados disponiveis **************************")
            codigo, data, nome, turma = self.fLerCampos()
            self.objBD.inserirDados(codigo, data, nome, turma)
            self.treeRegistro.insert('', 'end', iid=self.iid, values=(codigo, data, nome, turma))
            self.iid = self.iid + 1
            self.id = self.id + 1
            self.fLimparTela()
            print('Produto cadastrado com sucesso')
        except:
            print("Não foi possivel fazer o cadastro")

    def fAtualizarProduto(self):
        try:
            print("****************** dados disponiveis ********************")
            codigo , data, nome, turma = self.fLerCampos()
            self.objBD.atualizarDados(codigo, data, nome, turma)
            # Rcarregar dados na tela
            self.treeRegistro.delete(*self.treeRegistro.get_children())
            self.carregarDadosIniciais()
            self.fLimparTela()
            print('O produto foi atualizado com sucesso')
        except:
            print('Não foi possivel fazer a atualização')

    def fExcluirProduto(self):
        try:
            print("**************** dados disponiveis *******************&")
            codigo, data, nome, turma = self.fLerCampos()
            self.objBD.excluirDados(codigo)
            # Recarregar dados na tela
            self.treeRegistro.delete(*self.treeRegistro.get_children())
            self.carregarDadosIniciais()
            self.fLimparTela()
            print('O produto foi excluido com sucesso')
        except:
            print('Não foi possivel fazer a exclusão do produto')

    def fLimparTela(self):
        try:
            print("**************** dados disponiveis ********************")
            self.txtCodigo.delete(0, tk.END)
            self.txtData.delete(0, tk.END)
            self.txtNome.delete(0, tk.END)
            self.txtTurma.delete(0, tk.END)
            print('Campos limpos')
        except:
            print('Não foi possivel limpar os campos')

    def fBuscarProduto(self):
        try:
            self.treeRegistro.delete(*self.treeRegistro.get_children())
            print("**************** dados disponiveis *******************")
            registro = self.objBD.buscarDados(self.txtCodigo.get())
            self.treeRegistro.insert('', 'end', iid=self.iid, values=registro)
            self.iid = self.iid + 1
            self.id = self.id + 1
        except Exception as e:
            print(e)

janela = tk.Tk()
principal = PrincipalDB(janela)
janela.title('Bem vindo ao Gerenciador de Biblioteca')
janela.geometry("820x600+10+10")
janela.mainloop()