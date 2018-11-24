def menuInicial(quadros):
	print("Quadros:")
	print(fimOperacao())
	exibirQuadros(quadros)

	print("\n------------TrelloApp--------------")
	print("1 - Criar Quadro")
	print("2 - Acessar Quadro")
	print("3 - Remover Quadro\n\n")


def menuQuadro(quadro):
	print("---------------"+quadro+"--------------")
	print("1 - Criar Lista")
	print("2 - Acessar Cartão")
	print("3 - Mover Lista")
	print("4 - Mover Cartão")
	print("5 - Remover Lista\n\n")




def menuCartao():
	print("1 - Adicionar Comentario")
	print("2 - Excluir Comentario")
	print("3 - Adicionar Etiqueta")
	print("4 - Remover Etiqueta")


def exibirQuadros(quadros):
	for quadro in quadros:
		print("\t -0-", quadro)


def exibirLista(lista, cartoes):
	print("\t->",lista)
	for cartao in cartoes:
		print("\t #", cartao)

def fimOperacao():
	return "----------------------------------\n"


def erro():
	print("Erro de Operacao")


def sucesso():
	print("Operacao realizada com sucesso")