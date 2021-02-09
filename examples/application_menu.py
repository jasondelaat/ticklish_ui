# This example demonstrates Application menus.
from ticklish_ui import *

app = Application('Application Menus')

app.menubar(
    # Each tuple defines a single toplevel menu

    # This one has a single item.
    ('File', ['Quit']),

    # This one has three.
    ('Background', ['Red', 'Green', 'Blue']),
)

# Bind actions to menu items by specifying the menu-item combo and
# providing a callback.
app.menu_command('File-Quit', lambda app: app.destroy())
app.menu_command(
    'Background-Red', lambda app: app.configure(background='red')
)

app.menu_command(
    'Background-Green', lambda app: app.configure(background='green')
)

app.menu_command(
    'Background-Blue', lambda app: app.configure(background='blue')
)


app.mainloop()
