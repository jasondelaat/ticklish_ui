# This example demonstrates the use of checkbuttons with CheckGroup.
from ticklish_ui import *

app = Application(
    'CheckGroup Example',

    # .row1
    # CheckGroup can take multiple rows of buttons.
    [CheckGroup('alpha',
                # .row1
                ['A', 'B', 'C', 'D', 'E'],
                # .row2
                ['F', 'G', 'H', 'I', 'J'])
    ],

    # .row2
    [Button('OK').options(name='ok'), CloseButton('Quit')],
    
)

# Checks to see which buttons have been selected and reports the
# results in a new Toplevel window.
def show_selections(e):
    first_group = app.nametowidget('.row1.alpha.row1').winfo_children()
    second_group = app.nametowidget('.row1.alpha.row2').winfo_children()
    all_buttons = first_group + second_group

    # The get and set methods of the control variable have been bound
    # directly to the buttons themselves.
    checked = filter(lambda cb: cb.get() == 1, all_buttons)
    selected = ", ".join(map(lambda cb: cb['text'], checked))
    return Toplevel(
        'Checkbutton Selections',
        [Label(f'You selected options: {selected}')],
        [CloseButton('OK')]
    )

click = app.get_event_stream('<ButtonRelease-1>')

(click
 .by_name('ok')
 .map(show_selections)
)

# We can bind events to all buttons by class (notice capitalization!)
(click
 .by_class('Alpha')
 .map(lambda e: print('Clicked one of the checkbuttons.'))
)

# Or even bind individual buttons.
(click
 .by_name('check_J')
 .map(lambda e: print('Clicked J.'))
)

app.mainloop()
