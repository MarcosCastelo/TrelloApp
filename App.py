from model.Quadro import *

def main():
    q = Quadro("quadro")
    q.criaLista("lista")
    lista = q.getLista("lista")
    lista.adicionaCartao("cartao")


if __name__ == '__main__':
    main()