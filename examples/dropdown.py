# This example demonstrates Dropdown menus.
from ticklish_ui import *

app = Application(
    'Dropdown Example',

    # .row1
    [Dropdown('Select one', [1, 2, 3, 4]).options(name='dd')],

    # .row2
    [Button('OK').options(name='ok'), CloseButton('Quit')]
)

def show_selection(e):
    selection = app.nametowidget('.row1.dd').get()
    return Toplevel(
        'Your Selection',
        [Label(f'You chose {selection}')],
        [CloseButton('OK')]
    )

(app.get_event_stream('<ButtonRelease-1>')
 .by_name('ok')
 .map(show_selection)
)

# When a selection is made the Dropdown generates a <<Selection>>
# virtual event.
(app.get_event_stream('<<Select>>')
 .by_name('dd')
 .map(lambda e: print(e.widget.get()))
)

app.mainloop()
