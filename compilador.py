from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
Config.set('kivy','window_icon','icon.png')
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.label import Label
from kivy.properties import BooleanProperty
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
import os
import lexicalAnalyzer
import sintacticAnalyzer
import semanticAnalyzer
import  sys
import pyperclip
from graphviz import Source, render
import graphviz
import time

import pydot
from subprocess import check_call
#from IPython.display import Image, display


class SelectableRecycleGridLayout(FocusBehavior, LayoutSelectionBehavior,
                                RecycleGridLayout):
    ''' Adds selection and focus behaviour to the view. '''

class SelectableLabel(RecycleDataViewBehavior, Label):
    ''' Add selection support to the Label '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        return super(SelectableLabel, self).refresh_view_attrs(
            rv, index, data)

"""background_image = None
insert_image = None
class CustomLayout(GridLayout):
    background_image = ObjectProperty(Image(source="icon.png", anim_delay=.1))
    insert_image = ObjectProperty(None)

class RV(RecycleView):
    def __init__(self, **kwargs):
        dataTable = ("Tipo", "Token", "No. linea", "No. caracter")
        super(RV, self).__init__(**kwargs)
        #table = ObjectProperty(None)
        self.data = [{'text': str(x)} for x in dataTable]"""

class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)

class SaveDialog(FloatLayout):
    save = ObjectProperty(None)
    text_input = ObjectProperty(None)
    cancel = ObjectProperty(None)

class Test(TabbedPanel):
    #code_input = ObjectProperty()

    loadfile = ObjectProperty(None)
    savefile = ObjectProperty(None)
    text_input = ObjectProperty(None)
    text_error = ObjectProperty(None)
    table_out = ObjectProperty(None)
    text_graph = ObjectProperty(None)
    text_grammar = ObjectProperty(None)
    insert_image = ObjectProperty(Image(source="icon.png", anim_delay=.1))
    button_refresh = ObjectProperty(None)
    #image = Image(source="graphviztree.gv.png")

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def show_save(self):
        content = SaveDialog(save=self.save, cancel=self.dismiss_popup)
        self._popup = Popup(title="Save file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def earase_code(self):

        #self.show_save()
        self.text_input.text = ""
        self.text_error.text = ""
        self.text_error.background_color = [1, 1, 1, .7]
        self.table_out.data = ''
        self.text_graph.text = ''
        self.insert_image.source = "icon.png"

    def load(self, path, filename):
        with open(os.path.join(path, filename[0])) as stream:
            self.text_input.text = stream.read()

        self.dismiss_popup()

    def save(self, path, filename):
        with open(os.path.join(path, filename), 'w') as stream:
            stream.write(self.text_input.text)

        self.dismiss_popup()

    def compile_code(self):
        if len(self.text_input.text) > 0:
            semanticAnalyzer.txt = " "
            semanticAnalyzer.cont = 0
            semanticAnalyzer.asm = " "
            #print(self.text_input.text) # Imprime en consola el contenido.

            with open('tokens.txt', 'w') as tokens:
                tokens.write(self.text_input.text)

            try:
                file = "tokens.txt"

                list = lexicalAnalyzer.test(file)
                self.text_error.background_color = [0.2, 1, 0.2, 1]
                self.text_error.text = "Exito: Se compilo correctamente."

                self.table_out.data = [{'text': str(x)} for x in list]

                sintacticAnalyzer.test(file)

                with open('graphviztree.gv','r') as graph:
                    result = graph.read()
                    self.text_graph.text = result

                with open('parser.out','r') as grammar:
                    result = grammar.read()
                    self.text_grammar.text = result

                os.environ["PATH"] += os.pathsep + 'C:\\release\\bin'
                graphviz.render('dot', 'png', 'graphviztree.gv')

                self.insert_image.source = "graphviztree.gv.png"
                self.insert_image.reload()
            except lexicalAnalyzer.LexicalError as error:
                self.text_error.text = "Error: " + str(error.args)
                self.text_error.background_color = [1, 0.2, 0.2, 1]
                self.table_out.data = ''
                self.text_graph.text = ''
                self.insert_image.source = "icon.png"
            except sintacticAnalyzer.SintaxlError as error:
                self.text_error.text = str(error.args)
                self.text_error.background_color = [1, 0.2, 0.2, 1]
                self.table_out.data = ''
                self.text_graph.text = ''
                self.insert_image.source = "icon.png"
        else:
            self.text_error.text = "Error: No hay nada escrito."
            self.text_error.background_color = [1, 0.2, 0.2, 1]
            #self.text_error.foreground = "blue"

    def error_code(self):
        #self.text_error.text = "Algo"
        pass

    def addToClipBoard(self):
        pyperclip.copy(self.text_graph.text)
        spam = pyperclip.paste()

"""    def refresh(self):
        self.insert_image.source = "graphviztree.gv.png"

        os.remove("graphviztree.gv.png")
        os.environ["PATH"] += os.pathsep + 'C:\\release\\bin'
        graphviz.render('dot', 'png', 'graphviztree.gv')

        self.insert_image.reload()"""

class CompIoTApp(App):
    def build(self):
        return Test()

Factory.register('Root', cls=Test)
Factory.register('LoadDialog', cls=LoadDialog)
Factory.register('SaveDialog', cls=SaveDialog)

if __name__ == '__main__':
    CompIoTApp().run()