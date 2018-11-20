from service.Service import *
import UI

sistema = Service()

def menuLista(lista):
    print(UI.menuLista(lista))
    op = input(UI.operacao())
    while op != "0":
        if op == "1":
            titulo_cartao = input(UI.criarCartao)
            sistema.criarCartao(titulo_cartao)

        print(UI.menuLista(lista))
        op = input(UI.operacao())


def menuQuadro(quadro):
    print(UI.menuQuadro(quadro))
    op = input(UI.operacao())
    while op != "0":
        if op == "1":
            titulo_lista = input(UI.criarLista())
            sistema.criarLista(titulo_lista)
        elif op == "2":
            lista_listas = sistema.listarListas()
            print(UI.listarListas(lista_listas))
            print(UI.fimOperacao())
        elif op == "3":
            pass
        else:
            print(UI.operacaoInvalida())

        print(UI.menuQuadro(quadro))
        op = input(UI.operacao())

def main():
    print(UI.menu())
    op = input(UI.operacao())

    while op != "0":
        if op == "1":
            nome_quadro = input(UI.criarQuadro())
            sistema.criarQuadro(nome_quadro)
            print(UI.fimOperacao())
        elif op == "2":
            lista_quadros = sistema.listarQuadros()
            print(UI.listarQuadros(lista_quadros))
            print(UI.fimOperacao())
        elif op == "3":
            nome_quadro = input(UI.entrarQuadro())
            retorno = sistema.selecionarQuadro(nome_quadro)
            menuQuadro(retorno)
        else:
            print(UI.operacaoInvalida())
        print(UI.menu())
        op = input(UI.operacao())

if __name__ == '__main__':
    main()