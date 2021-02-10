"""Defines the ticklish_ui Canvas widget. """
import tkinter as tk
from ticklish_ui.widgets.factories import WidgetFactory

class Canvas(WidgetFactory):
    """ Wrapper for the tkinter.Canvas class. """
    def __init__(self, width, height):
        """Initialize the Canvas.

        Arguments:
            width - an int
            height - an int

        """
        super().__init__(tk.Canvas)
        self.kwargs['width'] = width
        self.kwargs['height'] = height
