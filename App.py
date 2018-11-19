from model.Lista import *

def main():
    l = Lista("l")
    l.adicionarCartao("c")
    for i in l.cartoes:
        print(i.titulo)

    print(l.arquivarCartao("c"))

if __name__ == '__main__':
    main()