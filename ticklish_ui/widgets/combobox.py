"""Defines the ticklish_ui Combobox widget. """
import tkinter.ttk as ttk
from ticklish_ui.widgets.factories import WidgetFactory

class Combobox(WidgetFactory):
    """ Wrapper for the tkinter.ttk.Combobox class. """
    def __init__(self, *values):
        """Initialize the Combobox window.

        Arguments:
            *values - any number of strings which are the initial
                      values in the combobox's dropdown.

        """
        super().__init__(ttk.Combobox)
        self.kwargs['values'] = values
