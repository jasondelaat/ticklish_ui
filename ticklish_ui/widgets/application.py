"""Defines the ticklish_ui Application root widget. """
import tkinter as tk
import tkinter.ttk as ttk
import ticklish_ui.events as events
from ticklish_ui.widgets.factories import ContainerFactory

class Application(ContainerFactory, tk.Tk):
    """The root window for all ticklish UIs.

    This class wraps the tkinter.Tk class so every ticklish UI must
    contain exactly one instance of Application.

    """
    def __init__(self, title, *rows):
        """Initialize the Application.

        Arguments:
            title - a string, the name of the window displayed in the
                    titlebar.
            *rows - any number of rows given as lists of ticklish widgets.

        """
        super().__init__(None, rows)
        self.create_widget(None)
        self.title(title)
        self.style = ttk.Style()
        self.style.theme_use('aqua')

    def get_event_stream(self, event_sequence):
        """Bind an event stream to the Application.

        See Stream and EventStream for how to use streams to implement
        UI functionality.

        Arguments:
            event_sequence - a string specifying the event to
                             bind. See the tkinter documentation for
                             how to specify event sequences.

        Returns:
            An EventStream object.

        """
        stream = events.EventStream()
        self.bind_all(event_sequence, stream.insert)
        return stream

    def menubar(self, *menus):
        """Define the application menus.

        Arguments:
            *menus - any number of menu definitions. Each menu
                     definition is given as a 2-tuple. The first
                     element is the menu name, the second element is a
                     list of strings defining the items in the menu.

        """
        menubar = tk.Menu(self, name='menubar')
        self['menu'] = menubar
        for menu_label, items in menus:
            menu = tk.Menu(menubar)
            menubar.add_cascade(label=menu_label, menu=menu)
            for item in items:
                menu.add_command(
                    label=item, command=_menu_update(self, menu_label, item)
                )

    def menu_command(self, menu_selector, callback):
        """Bind a command to a menu item.

        Arguments:
            menu_selector - a string of the form {Menu}-{Item}. For
                            instance, given a menu Background with
                            entries Red, Green and Blue, the
                            menu_selector to bind a command to Red
                            would be 'Background-Red'
            callback - a function to call when the given menu item is
                       selected. The callback takes the root window as
                       input so the application can be manipulated in
                       any way the user requires.

        """
        (self.get_event_stream(f'<<Menu-{menu_selector}>>')
         .map(lambda e: callback(self))
        )

def _menu_update(root, label, item):
    def command():
        root.event_generate(f'<<Menu-{label}-{item}>>')
    return command
