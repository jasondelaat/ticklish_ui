"""Defines the ticklish_ui Toplevel widget. """
import tkinter as tk
from ticklish_ui.widgets.factories import ContainerFactory

class Toplevel(ContainerFactory, tk.Toplevel):
    """ Wrapper for the tkinter.Toplevel class. """
    def __init__(self, title, *rows):
        """Initialize the Toplevel window.

        Arguments:
            title - a string, the name of the window displayed in the
                    titlebar.
            *rows - any number of rows given as lists of ticklish widgets.

        """
        super().__init__(None, rows)
        self.create_widget(None)
        self.title(title)
