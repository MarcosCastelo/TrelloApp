def operacao():
    return "Digite a operacao: "


def menu():
    string = "\n1 - Criar um quadro" \
             "\n2 - Listar quadros" \
             "\n3 - Entrar em quadro" \
             "\n0 - Sair"
    return string


def menuQuadro(quadro):
    string = "--------------"+quadro+"-------------" \
             "\n1 - Criar Lista" \
             "\n2 - Listar Listas" \
             "\n3 - Apagar Lista" \
             "\n4 - Sair"

    return string

def criarQuadro():
    string = "\n------------------Criação de Quadro---------------------" \
             "\nInsira o título do quadro: "

    return string


def listarQuadros(quadros):
    string = "\n---------Quadros-----------"
    for quadro in quadros:
        string += ("\n\t ->" + quadro)

    return string


def entrarQuadro():
    return "Digite o nome do quadro que deseja entrar: "


def criarLista():
    string = "\n------------------Criação de Lista---------------------" \
             "\nInsira o título da lista: "

    return string


def listarListas(listas):
    string = "\n-------------Listas---------------"
    for lista in listas:
        string += ("\n\t ->" + lista)

    return string

def listarCartoes(cartoes):
    string = "\n-------------Cartoes---------------"
    for cartao in cartoes:
        string += ("\n\t ->", cartao)

def operacaoInvalida():
    return "Operação Invalida"


def fimOperacao():
    return "\n--------------------------\n"