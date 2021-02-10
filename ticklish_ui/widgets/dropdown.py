"""Defines the ticklish_ui Dropdown widget. """
import tkinter as tk
import tkinter.ttk as ttk
from ticklish_ui.widgets.factories import WidgetFactory

class Dropdown(WidgetFactory):
    """Create a dropdown menu.

    Dropdown is a ticklish addition which handles creating a menu
    button and associated menu in single step.

    """
    def __init__(self, button_text, option_list):
        """Initialize the Dropdown.

        Arguments:
            button_text - a string, the text displayed on the button
                          before a selection is made.
            option_list - a list of strings, the options to be
                          displayed in the dropdown menu.

        """
        super().__init__(ttk.Menubutton)
        self.button_text = button_text
        self.option_list = option_list

    def create_widget(self, parent):
        dropdown = super().create_widget(parent)
        variable = tk.StringVar(value=self.button_text)
        dropdown['textvariable'] = variable
        menu = tk.Menu(dropdown, name=f'{dropdown.winfo_name()}_menu')

        for option in self.option_list:
            menu.add_command(
                label=option, command=_dd_update(dropdown, option)
            )
        dropdown['menu'] = menu
        dropdown.set = variable.set
        dropdown.get = variable.get
        return dropdown

def _dd_update(dropdown, value):
    def command():
        dropdown.set(value)
        dropdown.event_generate('<<Select>>')
    return command
