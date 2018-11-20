def menu():
    string = "\n1 - Criar um quadro" \
             "\n2 - Listar quadros" \
             "\n3 - Entrar em quadro"
    print(string)


def criarQuadro():
    string = "\n------------------Criação de Quadro---------------------" \
             "\nInsira o título do quadro: "

    print(string)


def listarQuadros(quadros):
    print("\n---------Quadros-----------")
    for quadro in quadros:
        print("\t ->", quadro)


def listarListas(listas):
    print("\n-------------Listas---------------")
    for lista in listas:
        print("\t ->", lista)


def listarCartoes(cartoes):
    print("\n-------------Cartoes---------------")
    for cartao in cartoes:
        print("\t ->", cartao)