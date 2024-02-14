from datetime import datetime

class Categoria:
    def __init__(self, categorias):
        self.categoria = categorias

class Produtos:
    def __init__(self, nome, preco, categoria):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria

class Estoque:
    def __init__(self, produto: Produtos, qtd_produto):
         self.produto = produto
         self.qtd_produto = qtd_produto

class Venda:
    def __init__(self, iten_vendidos: Produtos, vendedor, comprador, qtd_vendida, data = datetime.now().strftime("%d/%m/%Y")):
        self.iten_vendidos = iten_vendidos
        self.vendedor = vendedor
        self.comprador = comprador
        self.qtd_vendida = qtd_vendida
        self.data = data

class Fornecedor:
    def __init__(self, nome_empresa, cnpj_empresa, telefone_contato, categoria: Categoria):
        self.nome_empresa = nome_empresa
        self.cnpj_empresa = cnpj_empresa
        self.telefone_contato = telefone_contato
        self.categoria = categoria

class Pessoa:
    def __init__(self, nome, endereco, cpf, email, telefone):
        self.nome = nome
        self.endereco = endereco
        self.cpf = cpf
        self.email = email
        self.telefone = telefone

class Funcionario(Pessoa):
    def __init__(self, clt, nome, endereco, cpf, email, telefone):
        self.clt = clt
        super(Funcionario, self).__init__(nome, telefone, cpf, email, endereco)
