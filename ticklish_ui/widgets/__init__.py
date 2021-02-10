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
from ticklish_ui.widgets.widgets import *
