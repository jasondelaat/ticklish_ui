# This example demonstrates the use of Combobox
from ticklish_ui import *

app = Application(
    'Combobox Example',

    # .row1
    [Label('Enter a color or select from the available choices.')],


    # .row2
    [Combobox('red', 'green', 'blue').options(name='color')],

    # .row3
    [Button('OK').options(name='ok'), CloseButton('Quit')],
)

def set_color(e):
    combobox = app.nametowidget('.row2.color')
    color = combobox.get()

    # If the color isn't already in the dropdown options, add it.
    if combobox.current() < 0:
        combobox['values'] = (*combobox['values'], color)
    app.style.configure('.', foreground=color)

submit = app.get_event_stream('<ButtonRelease-1>').by_name('ok')
submit.map(set_color)

app.mainloop()
