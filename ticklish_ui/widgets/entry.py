"""Defines the ticklish_ui Entry widget. """
import tkinter.ttk as ttk
from ticklish_ui.widgets.factories import WidgetFactory

class Entry(WidgetFactory):
    """ Wrapper for the tkinter.ttk.Entry class. """
    def __init__(self):
        super().__init__(ttk.Entry)
