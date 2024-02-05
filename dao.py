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
                cls.categorias= arqcategorias.readlines()
            cls.categorias = list(map(lambda x: x.replace("\n", ""), cls.categorias))

            return cls.arq_categorias

        except FileExistsError:
            print("O arquivo de categorias não existe!!!")
            #return "O arquivo de categorias não existe!!!"
        
