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
            return "Categoria salva com sucesso!!!"
        else:
            return "A categoria ja existe!!!"
        
x = CategoriaController()
x.cadastrarNovaCategoria("Frios")

