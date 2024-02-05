from datetime import datetime

class Categoria:
    def __init__(self, categoria):
        self.categoria = categoria

class Produtos:
    def __init__(self, produto, nome, preco, categoria: Categoria):
        self.produto = produto
        self.nome = nome
        self.preco = preco
        self.categoria = categoria

class Estoque:
    def __init__(self, produto: Produtos, qtd_produto, id):
         self.produto = produto
         self.qtd_produto = qtd_produto
         self.peso = id

class Venda:
    def __init__(self, itens_vendidos: Produtos, qtd_vendida, vendedor, comprador, data = datetime.now().strftime("%d/%m/%Y")):
        self.itens_vendidos = itens_vendidos
        self.qtd_vendida = qtd_vendida
        self.vendedor = vendedor
        self.comprador = comprador
        self.data = data

class Fornecedor:
    def __init__(self, nome_empresa, cnpj_empresa, telefone_contato, categoria):
        self.nome_empresa = nome_empresa
        self.cnpj_empresa = cnpj_empresa
        self.telefone_contato = telefone_contato
        self.categoria = categoria

class Pessoa:
    def __init__(self, nome, endereco, cpf, email, telefone):
        self.nome = nome
        self.idade = endereco
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
    
class Cliente(Pessoa):
    def __init__(self, nome, endereco, cpf, email, telefone, idade):
        self.idade = idade
        super().__init__(nome, endereco, cpf, email, telefone)

class Funcionario(Pessoa):
    def __init__(self, nome, endereco, cpf, email, telefone, clt):
        self.clt = clt
        super().__init__(nome, endereco, cpf, email, telefone)

