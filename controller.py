from dao import *
from model import *

class CategoriaController:
    def cadastrarNovaCategoria(self, novacategoria):
        existe_categoria = False
        x = CategoriaDao.ler_categoria()
        for i in x:
            if i.categoria == novacategoria:
                existe_categoria = True
        
        if not existe_categoria:
            CategoriaDao.salvar_categoria(novacategoria)
            return ("Categoria salva com sucesso!!!")
        else:
            return ("A categoria ja existe!!!")
        
#x = CategoriaController()
#x.cadastrarNovaCategoria("Carnes")

    def removerCategoria(self, remover_categoria):
        x = CategoriaDao.ler_categoria()
        list_categoria = list(filter(lambda x: x.categoria == remover_categoria, x))
            
        if len(list_categoria) <= 0:
                return "A categoria que pretende exlcuir não existe!!!"
        else:
            for i in range(len(x)):
                if x[i].categoria == remover_categoria:
                    del x[i]
                    break
            print ("Categoria removida com sucesso!!!")
            #TODO: COLOCAR SEM CATEGORIA NO ESTOQUE

            with open("Categorias.txt", "w") as arqcategorias:
                for i in x:
                    arqcategorias.writelines(i.categoria)
                    arqcategorias.writelines("\n")

    def alterarCategoria(self, alterar_categoria, categoria_alterada):
        x = CategoriaDao.ler_categoria()

        list_categoria = list(filter(lambda x: x.categoria == alterar_categoria, x))

        if len(list_categoria) > 0:
            list_categorias = list(filter(lambda x: x.categoria == categoria_alterada, x))

            if len(list_categorias) == 0:
                x = list(map(lambda x: Categoria(categoria_alterada) if(x.categoria == alterar_categoria) else(x), x))
                print("Alteração realizada com sucesso!!!")
                #TODO: ALTERAR A CATEGORIA NO ESTOQUE

            else:
                print("Categoria ja existente!!!")

        else:
            print("Categoria inexistente para alteração")

        with open("Categorias.txt", "w") as arqcategorias:
                for i in x:
                    arqcategorias.writelines(i.categoria)
                    arqcategorias.writelines("\n")

#a = CategoriaController()
#a.alterarCategoria("Frios", "Frios")

    def mostrarCategorias(self):

        categoria = CategoriaDao.ler_categoria()

        if len(categoria) == 0:
            print("Não ha categorias para mostrar!!!")
            
        else:
            for i in categoria:
                print(f"Categorias: {i.categoria}")

#a = CategoriaController()
#a.mostrarCategorias()

class EstoqueController:
    def cadastrarProduto(self, nome, preco, categoria, qtd_produto):
        x = EstoqueDao.ler_estoque()
        y = CategoriaDao.ler_categoria()
        list_categoria = list(filter(lambda x: x.categoria == categoria, y))
        list_estoque = list(filter(lambda x: x.produto.nome == nome, x))

        if len(list_categoria) > 0:
            if len(list_estoque) == 0:
                produto = Produtos(nome, preco, categoria)
                EstoqueDao.salvar_estoque(produto, qtd_produto)
                print("Produto cadastrado com sucesso!!!")

            else:
                print("Este produto ja existe no estoque!!!")
        
        else:
            print("Essa categoria não existe!!!")

a = EstoqueController()
a.cadastrarProduto("Banana", "5", "Frutas", 2)
