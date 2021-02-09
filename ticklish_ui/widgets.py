"""Defines the widgets available is ticklish_ui.

In most cases widgets are wrapped tkinter or tkinter.ttk widgets. Some
widgets, like RadioGroup, are additions intended to make certain tasks
easier: rather than creating individual radio buttons, make a whole
set with a single command.

Widget initialization tries to take sensible minimum arguments to
display that widget. For instance, Labels and Buttons take a text
argument since both, typically, display text; Canvas takes a width and
height; and so on.

All ticklish UIs must start by defining an Application, which is the
root window of the UI, and calling it's mainloop. The minimal ticklish
UI is:

Example - Minimal UI - /examples/minimal_ui.py:
    # The smallest possible ticklish application.
    from ticklish_ui import *

    Application('Window Title').mainloop()

Widgets are added to an Application in rows, each row being given as a
list.  All widgets in a row are automatically packed into a frame and
the frames are named 'rowN' where 'N' is the row number starting at 1.

Example - UI Rows - /examples/ui_rows.py:
    # This example shows how widgets are packed into an application in rows.
    from ticklish_ui import *

    Application(
        'Application Rows',

        # .row1
        [Label('This is the first row.')],

        # .row2
        [Label('This is the second row.'), Label('Still the second row.')],

        # .row3
        [Label('Third row'), CloseButton('Quit')],
    ).mainloop()

In the above example, CloseButton is a ticklish addition which, when
clicked, automatically closes the toplevel window which contains it.

Additional options can be provided by calling the .options() method.

Example - Widget Options - /examples/widget_options.py:
    # The example demonstrates the use of the options method on widgets.

    from ticklish_ui import *

    Application(
        'Options Example',

        # .row1
        [Label('Red text!').options(foreground='red')]
    ).mainloop()

"""
import tkinter as tk
import tkinter.ttk as ttk
import ticklish_ui.events as events

class WidgetFactory:
    """Base class for most non-toplevel widgets.

    When defining an Application users are actually creating
    factories, which store the necessary information to create
    widgets, and not not widgets themselves. The actual widget is
    created later by Application, Toplevel, or other container
    widgets.

    """
    def __init__(self, widget_type):
        super().__init__()
        self.widget_type = widget_type
        self.kwargs = {}

    def options(self, **kwargs):
        """Set additional keyword options on widgets.

        The options are passed along to the underlying widget without
        error checks or modification. If the given options are not
        valid for the underlying widget and error will result when the
        widget is created.

        Arguments:
            kwargs - a keyword argument dictionary

        Returns:
            self

        """
        for key in kwargs:
            self.kwargs[key] = kwargs[key]
        return self

    def create_widget(self, parent):
        """Creates the actual underlying widget.

        Arguments:
            parent - a widget which will contain the widget being created.

        Returns:
            A new widget.

        """
        return self.widget_type(parent, **self.kwargs)

class ContainerFactory(WidgetFactory):
    """Base class for widgets which contain other widgets.

    ContainerFactory differs from WidgetFactory in that it is
    responsible for creating itself and all of it's children.

    """
    def __init__(self, container_type, rows):
        """Initialize the ContainerFactory.

        Arguments:
            container_type - a widget class such as tkinter.ttk.Frame
            rows - a list of lists of WidgetFactory instances

        """
        super().__init__(container_type)
        self.child_rows = rows

    def create_widget(self, parent):
        if self.widget_type:
            container = self.widget_type(parent, **self.kwargs)
        else:
            container = self

        count = 0
        for row in self.child_rows:
            count += 1
            frame = ttk.Frame(container, name=f'row{count}')
            frame.pack(fill=tk.BOTH)
            for factory in row:
                widget = factory.create_widget(frame)
                widget.pack(side=tk.LEFT)
        return container

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

class Button(WidgetFactory):
    """ Wrapper for the tkinter.ttk.Button class. """
    def __init__(self, text):
        """ Initialize the Button.

        Arguments:
            text - the text displayed on the button.
        """
        super().__init__(ttk.Button)
        self.kwargs['text'] = text

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

class CloseButton(Button):
    """Wrapper for the tkinter.ttk.Button class.

    CloseButton is a ticklish addition which closes the toplevel
    window that contains it when clicked.

    """
    def create_widget(self, parent):
        button = super().create_widget(parent)
        button['command'] = lambda: button.winfo_toplevel().destroy()
        return button

class Entry(WidgetFactory):
    """ Wrapper for the tkinter.ttk.Entry class. """
    def __init__(self):
        super().__init__(ttk.Entry)

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

class Label(WidgetFactory):
    """ Wrapper for the tkinter.ttk.Label class. """
    def __init__(self, text):
        """ Initialize the Label.

        Arguments:
            text - the text displayed on the label.
        """
        super().__init__(ttk.Label)
        self.kwargs['text'] = text

class Listbox(WidgetFactory):
    """A wrapper for the tkinter.ttk.Treeview class.

    Listbox always displays its items as flat hierarchy. Each item's
    iid property is set to be the same as its text so a call to the
    widget's focus() method will return the item text.

    """
    def __init__(self, items):
        """ Initialize the Listbox.

        Arguments:
            items - a list of strings to be displayed in the Listbox.
        """
        super().__init__(ttk.Treeview)
        self.items = items

    def create_widget(self, parent):
        tree = super().create_widget(parent)
        for i in range(len(self.items)):
            tree.insert('', i, iid=self.items[i], text=self.items[i])
        tree.pack(side=tk.LEFT)
        return tree

class Radiobutton(WidgetFactory):
    """ Wrapper for the tkinter.ttk.Radiobutton class. """
    def __init__(self, button_text):
        """Initialize the Radiobutton.

        Arugments:
            button_text - a string. The text and value of the
                          radiobutton are set to this value and the
                          name of the radiobutton is set to
                          'radio_{button_text}'

        """
        super().__init__(ttk.Radiobutton)
        self.kwargs['text'] = button_text
        self.kwargs['value'] = button_text
        self.kwargs['name'] = f'radio_{button_text}'

class RadioGroup(Frame):
    """Create a set of radio buttons.

    RadioGroup is a ticklish addition which creates a set of radio
    buttons from a list of strings.

    """
    def __init__(self, group_name, radio_options):
        """Initialize the RadioGroup.

        The frame containing the radio buttons will be given the name
        group_name, each button will be given the name
        radio_{option}, and all radio buttons in the group will be
        assigned group_name capitalized as their class_ option.

        For instance, given group_name = alpha, and
        options = ['A', 'B', 'C']:

        1. The frame will be called alpha
        2. The buttons will be called radio_A, radio_B, and radio_C
        3. All three buttons' class_ option will be Alpha

        Arguments:
            group_name - a string, the name of the group. Radio
                         buttons in this group will have this as as
                         their class_ attribute.

            options - a list of strings. Each string becomes a
                      separate radio button in the group.

        """
        buttons = map(lambda o: Radiobutton(o).options(
            class_=group_name.capitalize()
        ), radio_options)
        super().__init__(buttons)
        self.kwargs['name'] = group_name

    def create_widget(self, parent):
        widget = super().create_widget(parent)
        widget.variable = tk.StringVar()
        for button in widget.winfo_children()[0].winfo_children():
            button.configure(variable=widget.variable)
            tags = list(button.bindtags())
            tags.insert(1, 'TRadiobutton')
            button.bindtags(tags)
        return widget

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
        self.style = ttk.Style()
        self.style.theme_use('aqua')

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
