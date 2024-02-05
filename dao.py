from model import *

class CategoriaDao:
    @classmethod
    def salvar_categoria(cls, categorias: Categoria):
        with open("Categorias.txt", "a") as arqcategorias:
            arqcategorias.writelines(categorias)
            arqcategorias.writelines("\n")
    
    @classmethod
    def ler_categoria(cls):
        try:
            with open("Categorias.txt", "r") as arqcategorias:
                cls.categorias = arqcategorias.readlines()
            
            cls.categorias = list(map(lambda x: x.replace("\n", ""), cls.categorias))
            
            categori = []

            for i in cls.categorias:
                categori.append(Categoria(i))

            return categori

        except FileExistsError:
            return "O arquivo de categorias não existe!!!"

class VendasDao:
    @classmethod
    def salvar_vendas(cls, vendas: Venda):
        with open("Vendas.txt", "a") as arqvendas:
            arqvendas.writelines(vendas.itens_vendidos.nome + "|" + vendas.itens_vendidos.preco + "|"
                                 + vendas.itens_vendidos.categoria + "|" + str(vendas.qtd_vendida) + "|"
                                 + vendas.vendedor + "|" + vendas.comprador + "|" + vendas.data + "|")
            arqvendas.writelines("\n")
    @classmethod
    def ler_vendas(cls):
        try:
            with open("Vendas.txt", "r") as arqvendas:
                cls.vendas = arqvendas.readlines()
            cls.vendas = list(map(lambda x: x.replace("\n", ""), cls.vendas))
            
            vend = []

            for i in cls.vendas:
                vend.append(Categoria(i))

            return vend

        except FileExistsError:
            return "O arquivo de vendas não existe!!!"

x = Produtos ("Banana", "Banana da Terra", "5", "frutas")
y = Venda(x, "3", "sara", "daniel")
VendasDao.ler_vendas()











"""class ProdutosDao:
    @classmethod
    def salvar_produtos(cls, produtos: Produtos):
        with open("Produtos.txt", "a") as arqprodutos:
            arqprodutos.writelines(produtos.produto + "|" + produtos.nome + "|"
                                 + str(produtos.preco) + "|" + produtos.categoria + "|")
            arqprodutos.writelines("\n")

    @classmethod
    def ler_produtos(cls):
        try:
            with open("Produtos.txt", "r") as arqprodutos:
                cls.produtos = arqprodutos.readlines()
            cls.produtos = list(map(lambda x: x.replace("\n", ""), cls.produtos))
            
            produt = []

            for i in cls.produtos:
                produt.append(Produtos(i))

            return produt

        except FileExistsError:
            return "O arquivo de produtos não existe!!!"

ProdutosDao.salvar_produtos("Agua", "Agua sem gas", "0.99", "bebidas")
ProdutosDao.salvar_produtos("Coca Cola", "Coca Cola sem açucar", "8.99", "Bebidas")
ProdutosDao.salvar_produtos("Vinho", "Vinho tinto", "21.99", "Bebidas")
ProdutosDao.ler_produtos()"""
