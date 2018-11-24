from service.Service import *
from GUI import Ui
import os

sistema = Service()

def menuLista(lista):
    print(Ui.menuLista(lista))
    op = input(Ui.operacao())
    while op != "0":
        if op == "1":
            titulo_cartao = input(Ui.criarCartao)
            sistema.criarCartao(titulo_cartao)

        print(Ui.menuLista(lista))
        op = input(Ui.operacao())


def menuQuadro(quadro):
    Ui.menuQuadro(quadro)
    op = input()
    while op != "0":
        if op == "1":
            titulo_lista = input()
            sistema.criarLista(titulo_lista)
        elif op == "2":
            cartao = sistema.listarListas()
            print(Ui.listarListas(lista_listas))
            print(Ui.fimOperacao())
        elif op == "3":
            pass
        else:
            print(Ui.operacaoInvalida())

        Ui.menuQuadro(quadro)
        op = input(Ui.operacao())

def menu():
    Ui.menuInicial(sistema.listarQuadros())
    op = input()

    while op != "0":
        if op == "1":
            print("criarQuadro")
            nome_quadro = input()
            sistema.criarQuadro(nome_quadro)
            Ui.exibirQuadros(sistema.listarQuadros())
            
        elif op == "2":
            nome_quadro = input()
            sistema.selecionarQuadro(nome_quadro)
            menuQuadro(nome_quadro)
           
        elif op == "3":
            nome_quadro = input()
            if sistema.removerQuadro(nome_quadro):
                Ui.sucesso()
            else:
                Ui.erro()
        else:
            print(Ui.operacaoInvalida())
        Ui.menuInicial(sistema.listarQuadros())
        op = input()


def main():
    menu()

if __name__ == '__main__':
    main()