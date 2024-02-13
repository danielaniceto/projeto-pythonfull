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
#x.cadastrarNovaCategoria("Frutas")

    def removerCategoria(self, remover_categoria):
        x = CategoriaDao.ler_categoria()
        list_categoria = list(filter(lambda x: x.categorias == remover_categoria, x))
        
        if len(list_categoria) <= 0:
                return "A categoria que pretende exlcuir não existe!!!"
        else:
            for i in range(len(x)):
                if x[i].categorias == remover_categoria:
                    del x[i]
                    break
            print ("Categoria removida com sucesso!!!")

            with open("Categorias.txt", "w") as arqcategorias:
                for i in x:
                    arqcategorias.writelines(i.categorias)
                    arqcategorias.writelines("\n")

    def alterarCategoria(self, alterar_categoria, categoria_alterada):
        x = CategoriaDao.ler_categoria()

        list_categoria = list(filter(lambda x: x.categoria == alterar_categoria, x))

        if len(list_categoria) > 0:
            list_categorias = list(filter(lambda x: x.categoria == categoria_alterada, x))

            if len(list_categorias) == 0:
                x = list(map(lambda x: Categoria(categoria_alterada) if(x.categoria == alterar_categoria) else(x), x))
                print("Alteração realizada com sucesso!!!")

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
