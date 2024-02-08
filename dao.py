from model import *

class CategoriaDao:
    @classmethod
    def salvar_categoria(cls, categorias):
        with open("Categorias.txt", "a") as arqcategorias:
            arqcategorias.writelines(categorias)
            arqcategorias.writelines("\n")
    
    @classmethod
    def ler_categoria(cls):
        try:
            with open("Categorias.txt", "r") as arqcategorias:
                cls.categorias = arqcategorias.readlines()
            
            cls.categorias = list(map(lambda x: x.replace("\n", ""), cls.categorias))
            
            list_categoria = []

            for i in cls.categorias:
                list_categoria.append(Categoria(i))

            return list_categoria

        except FileExistsError:
            return "O arquivo de categorias não existe!!!"

class VendasDao:
    @classmethod
    def salvar_vendas(cls, vendas: Venda):
        with open("Vendas.txt", "a") as arqvendas:
            arqvendas.writelines(vendas.iten_vendidos.nome +
                                     "|" + vendas.iten_vendidos.preco +
                                     "|" + vendas.iten_vendidos.categoria +
                                     "|" + vendas.vendedor + 
                                     "|" + vendas.comprador +
                                     "|" + str(vendas.qtd_vendida) +
                                     "|" + vendas.data)
            
            arqvendas.writelines("\n")

    @classmethod
    def ler_vendas(cls):
        try:
            with open("Vendas.txt", "r") as arqvendas:
                cls.vendas = arqvendas.readlines()

            cls.vendas = list(map(lambda x: x.replace("\n", ""), cls.vendas))
            cls.vendas = list(map(lambda x: x.split("|"), cls.vendas))
            #print(cls.vendas)

            list_venda = []

            for i in cls.vendas:
                list_venda.append(Venda(Produtos(i[0], i[1], i[2]), i[3], i[4], i[5], i[6]))


            return list_venda

        except FileExistsError:
            return "O arquivo de vendas não existe!!!"

class EstoqueDao:
    @classmethod
    def salvar_estoque(cls, estoques: Estoque):
        with open("Estoque.txt", "a") as arqestoque:
            arqestoque.writelines (      estoques.produto.nome +
                                   "|"+  estoques.produto.preco +
                                   "|" + estoques.produto.categoria + 
                                   "|" + estoques.qtd_produto)
            
            arqestoque.writelines("\n")

    @classmethod
    def ler_estoque(cls):
        try:
            with open("Estoque.txt", "r") as arqestoques:
                cls.estoques = arqestoques.readlines()

            cls.estoques = list(map(lambda x: x.replace("\n", ""), cls.estoques))
            cls.estoquess = list(map(lambda x: x.split("|"), cls.estoques))
            #print(cls.estoques)

            list_estoque = []
            if len(cls.estoques) > 0:
                for i in cls.estoques:
                    list_estoque.append(Estoque(Produtos(i[0], i[1], i[2]), i[3]))

            return list_estoque

        except FileExistsError:
            return "O arquivo de estoque não existe!!!!"

class FornecedoresDao:
    @classmethod
    def salvar_fornecedor(cls, fornecedores: Fornecedor):
        with open("Fornecedores.txt", "a") as arqfornecedor:
            arqfornecedor.writelines (   fornecedores.nome_empresa +
                                   "|" + fornecedores.cnpj_empresa +
                                   "|" + fornecedores.telefone_contato + 
                                   "|" + fornecedores.categoria)
            
            arqfornecedor.writelines("\n")

    @classmethod
    def ler_fornecedor(cls):
        try:
            with open("Fornecedores.txt", "r") as arqfornecedor:
                cls.fornecedores = arqfornecedor.readlines()

            cls.fornecedores = list(map(lambda x: x.replace("\n", ""), cls.fornecedores))
            cls.fornecedores = list(map(lambda x: x.split("|"), cls.fornecedores))
            #print(cls.fornecedores)

            list_fornecedor = []

            for i in cls.fornecedores:
                    list_fornecedor.append(Fornecedor(i[0], i[1], i[2]), i[3])

            return list_fornecedor

        except FileExistsError:
            return "O arquivo de fornecedores não existe!!!!"

class PessoaDao:
    @classmethod
    def salvar_pessoa(cls, clientes: Pessoa):
        with open("Clientes.txt", "a") as arqpessoa:
            arqpessoa.writelines (       clientes.nome +
                                   "|" + clientes.endereco +
                                   "|" + clientes.cpf + 
                                   "|" + clientes.email +
                                   "|" + clientes.telefone)
            
            arqpessoa.writelines("\n")

    @classmethod
    def ler_pessoa(cls):
        try:
            with open("Clientes.txt", "r") as arqcliente:
                cls.clientes = arqcliente.readlines()

            cls.clientes = list(map(lambda x: x.replace("\n", ""), cls.clientes))
            cls.clientes = list(map(lambda x: x.split("|"), cls.clientes))
            #print(cls.clientes)

            list_cliente = []

            for i in cls.clientes:
                    list_cliente.append(Pessoa(i[0], i[1], i[2]), i[3], i[4])

            return list_cliente

        except FileExistsError:
            return "O arquivo de clientes não existe!!!!"

class FunicionarioDao:
    @classmethod
    def salvar_funcionario(cls, funcionarios: Funcionario):
        with open("Funcionarios.txt", "a") as arqfuncionario:
            arqfuncionario.writelines (  funcionarios.nome +
                                   "|" + funcionarios.endereco +
                                   "|" + funcionarios.cpf + 
                                   "|" + funcionarios.email +
                                   "|" + funcionarios.telefone + 
                                   "|" + funcionarios.clt)
            
            arqfuncionario.writelines("\n")
    
    @classmethod
    def ler_funcionario(cls):
        try:
            with open("Funcionarios.txt", "r") as arqfuncionario:
                cls.funcionarios = arqfuncionario.readlines()

            cls.funcionarios = list(map(lambda x: x.replace("\n", ""), cls.funcionarios))
            cls.funcionarios = list(map(lambda x: x.split("|"), cls.funcionarios))
            #print(cls.clientes)

            list_funcionario = []

            for i in cls.clientes:
                    list_funcionario.append(Pessoa(i[0], i[1], i[2]), i[3], i[4], i[5])

            return list_funcionario

        except FileExistsError:
            return "O arquivo de clientes não existe!!!!"
