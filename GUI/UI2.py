from kivy.app import App
from service.Storage import *
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition, SlideTransition
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.lang.builder import Builder

Builder.load_file('ui.kv')
Window.clearcolor = .45, .45, .45, 1

storage = Storage()
storage.inserirListas('Projeto', ['todo', 'doing'])
storage.inserirListas('BLA', ['1', '2', '3'])


class Geral():
	def mudar_tela(self, nome_tela, tipo_transicao='Slide', direcao='left'):
		if (tipo_transicao == 'Slide'):
			self.manager.transition = SlideTransition()
		else:
			self.manager.transition = NoTransition()
		self.manager.transition.direction = direcao
		self.manager.current = nome_tela

class Listas(Screen,Geral):
	def atualizar(self, nome_quadro):
		listas = storage.buscaListas(nome_quadro)
		self.ids.listas.clear_widgets()
		for lista in listas:
			print(listas)
			self.ids.listas.add_widget(Lista(text=lista))
			self.ids.listas.add_widget(Cartao(text=lista))

class Lista(BoxLayout):
	def __init__(self,text,**kwargs):
		super().__init__(**kwargs)
		self.ids.label.text = text
		self.remove_widget(self.children[0])
        

class Quadros(Screen, Geral):
	pass

class Cartao(BoxLayout):
	def __init__(self,text,**kwargs):
		super().__init__(**kwargs)
		self.ids.label.text = text
		self.remove_widget(self.children[1])
		


class Menu(Screen, Geral):
	pass

gerenciador = ScreenManager()
gerenciador.add_widget(Listas(name='listas'))
gerenciador.add_widget(Quadros(name='quadros'))

gerenciador.current = 'quadros'

class Quadros(Screen, Geral):
	pass

class UI(App):
	title = 'Editor de Imagens'
	def build(self):
		return gerenciador

UI().run()