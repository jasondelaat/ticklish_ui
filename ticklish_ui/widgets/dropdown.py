"""Defines the ticklish_ui Dropdown widget. """
from ticklish_ui.widgets.combobox import Combobox

class Dropdown(Combobox):
    """Create a dropdown menu.

    Dropdown is a ticklish addition which handles creating a menu
    button and associated menu in single step.

    """
    def __init__(self, *options):
        """Initialize the Dropdown.

        Arguments:
            button_text - a string, the text displayed on the button
                          before a selection is made.
            option_list - a list of strings, the options to be
                          displayed in the dropdown menu.

        """
        super().__init__(*options)
        self.initial_state = options[0]

    def create_widget(self, parent):
        dropdown = super().create_widget(parent)
        dropdown.state(['readonly'])
        dropdown.set(self.initial_state)
        return dropdown
