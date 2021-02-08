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
    def __init__(self):
        super().__init__()
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

        This method must be overridden in subclasses.

        Arguments:
            parent - a widget which will contain the widget being created.

        Returns:
            A new widget.

        """
        raise NotImplementedError()

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
        super().__init__()
        self.container_type = container_type
        self.child_rows = rows

    def create_widget(self, parent):
        if self.container_type:
            container = self.container_type(parent, **self.kwargs)
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

class Button(WidgetFactory):
    """ Wrapper for the tkinter.ttk.Button class. """
    def __init__(self, text):
        """ Initialize the Button.

        Arguments:
            text - the text displayed on the button.
        """
        super().__init__()
        self.kwargs['text'] = text

    def create_widget(self, parent):
        return ttk.Button(parent, **self.kwargs)

class Canvas(WidgetFactory):
    """ Wrapper for the tkinter.Canvas class. """
    def __init__(self, width, height):
        """Initialize the Canvas.

        Arguments:
            width - an int
            height - an int

        """
        super().__init__()
        self.kwargs['width'] = width
        self.kwargs['height'] = height

    def create_widget(self, parent):
        return tk.Canvas(parent, **self.kwargs)

class CloseButton(WidgetFactory):
    """Wrapper for the tkinter.ttk.Button class.

    CloseButton is a ticklish addition which closes the toplevel
    window that contains it when clicked.

    """
    def __init__(self, text):
        """ Initialize the CloseButton.

        Arguments:
            text - the text displayed on the button.
        """
        super().__init__()
        self.kwargs['text'] = text

    def create_widget(self, parent):
        button = ttk.Button(parent, **self.kwargs)
        button['command'] = lambda: button.winfo_toplevel().destroy()
        return button

class Entry(WidgetFactory):
    """ Wrapper for the tkinter.ttk.Entry class. """
    def create_widget(self, parent):
        return ttk.Entry(parent, **self.kwargs)

class Label(WidgetFactory):
    """ Wrapper for the tkinter.ttk.Label class. """
    def __init__(self, text):
        """ Initialize the Label.

        Arguments:
            text - the text displayed on the label.
        """
        super().__init__()
        self.kwargs['text'] = text

    def create_widget(self, parent):
        return ttk.Label(parent, **self.kwargs)

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
        super().__init__()
        self.items = items

    def create_widget(self, parent):
        tree = ttk.Treeview(parent, **self.kwargs)
        for i in range(len(self.items)):
            tree.insert('', i, iid=self.items[i], text=self.items[i])
        tree.pack(side=tk.LEFT)
        return tree

class RadioGroup(WidgetFactory):
    """Create a set of radio buttons.

    RadioGroup is a ticklish addition which creates a set of radio
    buttons from a list of strings.

    """
    def __init__(self, group_name, options):
        """Initialize the RadioGroup.

        The frame containing the radio buttons will be given the name
        radiogroup_{group_name}, each button will be given the name
        radio_{option}, and all radio buttons in the group will be
        assigned the group name as their class_ option.

        For instance, given group_name = Alpha, and
        options = ['A', 'B', 'C']:

        1. The frame will be called radiogroup_Alpha
        2. The buttons will be called radio_A, radio_B, and radio_C
        3. All three buttons' class_ option will be Alpha

        Arguments:
            group_name - a string, the name of the group. Radio
                         buttons in this group will have this as as
                         their class_ attribute.

            options - a list of strings. Each string becomes a
                      separate radio button in the group.

        """
        super().__init__()
        self.kwargs['name'] = f'radiogroup_{group_name}'
        self.group_name = group_name
        self.radio_options = options

    def create_widget(self, parent):
        group = ttk.Frame(parent, **self.kwargs)
        group.pack(fill=tk.BOTH)
        control = tk.StringVar()
        for option in self.radio_options:
            button = ttk.Radiobutton(
                group, value=option, text=option, variable=control,
                class_=self.group_name, name=f'radio_{option}'
            )
            tags = list(button.bindtags())
            tags.insert(1, 'TRadiobutton')
            button.bindtags(tags)
            button.pack(side=tk.LEFT)
        control.set(self.radio_options[0])
        group.variable = control
        return group

class Toplevel(tk.Toplevel):
    """ Wrapper for the tkinter.Toplevel class. """
    def __init__(self, title, *rows):
        """Initialize the Toplevel window.

        Arguments:
            title - a string, the name of the window displayed in the
                    titlebar.
            *rows - any number of rows given as lists of ticklish widgets.

        """
        super().__init__()
        self.title(title)
        self.style = ttk.Style()
        self.style.theme_use('aqua')
        count = 0
        for row in rows:
            count += 1
            frame = ttk.Frame(self, name=f'row{count}')
            frame.pack(fill=tk.BOTH)
            for factory in row:
                widget = factory.create_widget(frame)
                widget.pack(side=tk.LEFT)
