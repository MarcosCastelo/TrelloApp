from model.Interface import *
import UI

sistema = Interface()

def menuQuadro(operacao):

    if operacao == "1":
        pass

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
            print("\t", UI.listarListas(retorno[0], retorno[1]))
        else:
            print(UI.operacaoInvalida())
        print(UI.menu())
        op = input(UI.operacao())

if __name__ == '__main__':
    main()