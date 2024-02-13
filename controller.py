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
