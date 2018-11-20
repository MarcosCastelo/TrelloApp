from model.Interface import *
import UI

sistema = Interface()

def menuQuadro(quadro):
    print(UI.menuQuadro(quadro))
    op = input(UI.operacao())
    while op != "0":
        if op == "1":
            titulo_lista = input(UI.criarLista())
            sistema.criarLista(titulo_lista)
        elif op == "2":
            lista_listas = sistema.listarListas()
            print(UI.listarQuadros(lista_listas))
            print(UI.fimOperacao())

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