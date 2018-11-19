class Quadro:
    def __init__(self):
        self.listas = list()


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