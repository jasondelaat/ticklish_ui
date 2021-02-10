"""Defines the ticklish_ui Frame and LabelFrame widgets. """
import tkinter.ttk as ttk
from ticklish_ui.widgets.factories import ContainerFactory

class Frame(ContainerFactory):
    """ Wrapper for the tkinter.ttk.Frame class. """
    def __init__(self, *rows):
        """Initialize the Frame.

        Arguments:
            *rows - any number of rows given as lists of ticklish widgets.
        """
        super().__init__(ttk.Frame, rows)

class LabelFrame(ContainerFactory):
    """ Wrapper for the tkinter.ttk.LabelFrame class. """
    def __init__(self, label_text, *rows):
        """ Initialize the LabelFrame.

        Arguments:
            label_text - the text displayed on the LabelFrame.
            *rows - any number of rows given as lists of ticklish widgets.
        """
        super().__init__(ttk.LabelFrame, rows)
        self.kwargs['text'] = label_text
