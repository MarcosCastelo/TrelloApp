from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button


class UI(App):
    def build(self):
        return Tarefas(['Fazer compras', 'Buscar filho', 'Deixar Grana', 'Pegar Livro','AAAAAAA'])


class Tarefas(ScrollView):
        def __init__(self, tarefas, **kwargs): #keyword arguments
            super().__init__(**kwargs)
            for tarefa in tarefas:
                self.ids.box.add_widget(Button(text=tarefa, font_size=30, size_hint_y=None, height=200))


UI().run()