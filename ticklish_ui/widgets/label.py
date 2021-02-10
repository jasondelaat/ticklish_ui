"""Defines the ticklish_ui Label widget. """
import tkinter.ttk as ttk
from ticklish_ui.widgets.factories import WidgetFactory

class Label(WidgetFactory):
    """ Wrapper for the tkinter.ttk.Label class. """
    def __init__(self, text):
        """ Initialize the Label.

        Arguments:
            text - the text displayed on the label.
        """
        super().__init__(ttk.Label)
        self.kwargs['text'] = text
