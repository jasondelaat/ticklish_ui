# Demonstrates how to create a Treeview widget using either a
# MenuSpecification or, for simple trees, by defining the elements
# directly.

from ticklish_ui import *

# Define the menu using MenuSpecification
menu = MenuSpecification()
menu('One', 'Two', 'Three')
menu.One('A', 'B', 'C')
menu.Two('1', '2', '3')
menu.Three('X', 'Y', 'Z')

app = Application(
    'Treevew Example',
    # Create the Treeview using the MenuSpecification.
    [Treeview(menu)],

    # Or create the exact same menu directly.
    [Treeview(
        ('One', ['A', 'B', 'C']),
        ('Two', ['1', '2', '3']),
        ('Three', ['X', 'Y', 'Z'])
    )],
)

(app.get_event_stream('<<TreeviewSelect>>')
 # Calling focus() on the Treeview returns the selected item.
 .map(lambda e: print(e.widget.focus()))
)

app.mainloop()
