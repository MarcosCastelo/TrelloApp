class Quadro:
    def __init__(self, nome):
        self.nome = nome
        if nome == "":
            self.nome = "Quadro"
        self.listas = list()


    def getNome(self):
        return self.nome


    def temLista(self, lista):
        if lista in self.listas:
            return True

        return False


    def inserirLista(self, lista):
        self.listas.append(lista)


    def removerLista(self, lista):
        if temLista(lista):
            self.listas.remove(lista)
            return True

        return False


    def moverLista(self, lista, index):
        if temLista(lista):
            index_inicial = self.listas.index(lista)
            temp_lista = self.listas[index]
            self.listas[index] = lista
            self.listas[index_inicial] = temp_lista
            return True

        return False


    def getListas(self):
        lista_listas = []
        for lista in self.listas:
            lista_listas.append(lista.getTitulo())

        return lista_listas


    def getLista(self, index):
        self.getListas()[index]


    def getLista(self, titulo):
        for lista in self.getListas():
            if lista.getTitulo() == titulo:
                return lista


    def moverCartao(self, cartao, origem, destino):
        origem.removerCartao(cartao)
        destino.adicionarCartao(cartao)
