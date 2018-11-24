class Cartao:
    def __init__(self, titulo):
        self.titulo = titulo
        self.etiquetas = list()
        self.descricao = ""
        self.comentarios = list()


    def getTitulo(self):
        return self.titulo


    def adicionarEtiqueta(self, etiqueta):
        self.etiquetas.append(etiqueta)


    def adicionarDescricao(self, descricao):
        self.descricao = descricao


    def adicionarComentario(self, comentario):
        self.comentarios.append(comentario)


    def removerEtiqueta(self, etiqueta):
        if etiqueta in self.etiquetas:
            self.etiquetas.remove(etiqueta)
            return True

        return False


    def removerComentario(self, comentario):
        if comentario in self.comentarios:
            self.comentario.remove(comentario)
            return True

        return False


       

