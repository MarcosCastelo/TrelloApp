class Cartao:
    def __init__(self, titulo):
        self.titulo = titulo


    def getTitulo(self):
        return self.titulo


    def __repr__(self):
        return self.getTitulo()