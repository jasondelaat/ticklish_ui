"""A thin(-ish) wrapper around tkinter.

The ticklish_ui package is allows users to define GUI applications
declaratively and decouples event binding from GUI creation.

While ticklish is mostly just a wrapper around tkinter widgets some
'quality of life' additions have been made. Two examples:

    RadioGroup - automatically creates radio buttons from a list of
                 names so you don't have to create them all manually

    CloseButton - a button which automatically closes the toplevel
                  window that contains it.

ticklish uses themed tkinter widgets (ttk) when possible and falls
back to the base tkinter widget set otherwise.

Example:
    from ticklish_ui import *

    app = Application(
        'Example GUI',

        # .row1
        [Label('Enter some text below:')],

        # .row2
        [Entry().options(name='user_text')],

        # .row3
        [Button('OK').options(name='ok'), CloseButton('Quit')],
    )

    def show_text(event):
        text = app.nametowidget('.row2.user_text').get()
        return Toplevel(
            'Your Text',

            # .row1
            [Label(text)],

            # .row2
            [CloseButton('OK')],
        )

    (app.get_event_stream('<ButtonRelease-1>')
    .by_name('ok')
    .map(show_text)
    )

    app.mainloop()

"""
from ticklish_ui.widgets import *
from ticklish_ui.events import *
