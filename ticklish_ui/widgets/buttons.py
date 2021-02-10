"""Defines the ticklish_ui Button and CloseButton widgets. """
import tkinter.ttk as ttk
from ticklish_ui.widgets.factories import WidgetFactory

class Button(WidgetFactory):
    """ Wrapper for the tkinter.ttk.Button class. """
    def __init__(self, text):
        """ Initialize the Button.

        Arguments:
            text - the text displayed on the button.
        """
        super().__init__(ttk.Button)
        self.kwargs['text'] = text

class CloseButton(Button):
    """Wrapper for the tkinter.ttk.Button class.

    CloseButton is a ticklish addition which closes the toplevel
    window that contains it when clicked.

    """
    def create_widget(self, parent):
        button = super().create_widget(parent)
        button['command'] = lambda: button.winfo_toplevel().destroy()
        return button
