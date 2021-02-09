# This example demonstrates the use of radiobuttons.
from ticklish_ui import *

app = Application(
    'Radio Button Example',

    #.row1
    # RadioGroup gets a name and a list of text labels.
    [RadioGroup('alpha', ['A', 'B', 'C'])],

    #.row2
    [Button('OK').options(name='ok'), CloseButton('Quit')],
)

def show_choice(e):
    group = app.nametowidget('.row1.alpha')

    # The groups control variable is bound to the attribute 'variable'
    choice = group.variable.get()
    return Toplevel(
        'Your Choice',
        [Label(f'You selected option: {choice}')],
        [CloseButton('OK')]
    )

click = app.get_event_stream('<ButtonRelease-1>')
click.by_name('ok').map(show_choice)

# This handler will execute when any of the radiobuttons is clicked.
# Notice the class name is capitalized!
click.by_class('Alpha').map(lambda e: print(f'Clicked {e.widget.winfo_name()}'))

# But this one only executes when button 'C' is clicked.
click.by_name('radio_C').map(lambda e: print('I have my own handler!'))

app.mainloop()
