from model.Interface import *

def main():
    sistema = Interface()
    sistema.criarQuadro("Projeto X")
    sistema.criarLista("Pendencias")
    print(sistema.quadros[0].listas[0].titulo)


if __name__ == '__main__':
    main()