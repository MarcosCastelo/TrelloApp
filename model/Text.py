class Text:
    def __init__(self, texto):
        self.setTexto(texto)

    def __init__(self):
        self.texto = ""

    def setTexto(self, novo_texto):
        self.texto = novo_texto


    def getTexto(self):
        return self.texto


