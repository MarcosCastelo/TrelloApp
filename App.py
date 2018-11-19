from model.Quadro import *

def main():
    q = Quadro("quadro")
    q.criaLista("lista")
    q.criaCartao("lista", "biribir")
    print(q.listas[0].cartoes)
    print(q.getCartao("biribir", "lista"))

    t = Text()
    print(t.texto)

if __name__ == '__main__':
    main()