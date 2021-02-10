from ticklish_ui import *

# Define the layout.  An application can have any number of rows and
# rows can contain any number of widgets.
app = Application(
    'ticklish_ui_example',
    
    # .row1
    [Label('Enter some text below')],
    
    # .row2
    [Entry().options(name='entry')],

    # .row3
    [Button('OK').options(name='ok'), CloseButton('Quit')]
)

def print_input(event):
    entry = app.nametowidget('.row2.entry')
    print(entry.get())

# click captures all click events anywhere in the application.
click = app.get_event_stream('<ButtonRelease-1>')

# An event stream can then be filtered and bound to some action(s)
(click
 # Here we filter by the name of the widget clicked.
 .by_name('ok') 

 # And then map/bind an action to that event.
 .map(print_input)
)

app.mainloop()
