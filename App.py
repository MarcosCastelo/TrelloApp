from model.Quadro import *

def main():
    q = Quadro("quadro")
    q.criaLista("lista")
    q.criaCartao("lista", "biribir")
    print(q.listas[0].cartoes[0].getTitulo())
    print(q.getCartao("biribir", "lista").getTitulo())
    q.criaLista("lista2")
    q.moverCartao("biribir", "lista", "lista2")

    print(q.listas[0].cartoes)

if __name__ == '__main__':
    main()