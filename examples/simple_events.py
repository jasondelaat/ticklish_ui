# This example demonstrates simple use of event streams by creating
# GUI with two buttons and binding multiple events to them.

from ticklish_ui import *

# Create the GUI
app = Application(
    'EventStream Example',
    [Label("I'm a label. Clicking me won't do anything.")],
    [Button('Click me!'), Button('No, me!').options(name='button2')]
)

# Get an event stream of all clicks anywhere in the application
# window.
clicks = app.get_event_stream('<ButtonRelease-1>')

# We can create new streams by filtering and mapping old ones:

# This stream only captures clicks on Button widgets.
any_button = clicks.filter(lambda e: e.widget.winfo_class() == 'TButton')

# And this one captures clicks on the second button only.
button2_only = clicks.filter(lambda e: e.widget.winfo_name() == 'button2')

# Multiple actions can be mapped to a single stream. These actions are
# both performed when either button is clicked.
any_button.map(lambda e: print('Clicked either button'))
any_button.map(lambda e: print('but I don\'t know which one.'))

# But this only happens when the second button is clicked.
button2_only.map(lambda e: print('Clicked "No me!"'))

app.mainloop()
