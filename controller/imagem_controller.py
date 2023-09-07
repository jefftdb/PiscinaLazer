from model.entity.imagem import Imagem

class Imagem_modal():
    def __init__(self) -> None:        

        imagem1 = Imagem(0,'img/1.jpg')
        imagem2 = Imagem(1,'img/2.jpg')
        imagem3 = Imagem(2,'img/3.jpg')

        todasAsImagens = [imagem1,imagem2,imagem3]
        self.todasAsImagens = todasAsImagens
