# This example demonstrates more complex Application menus.  Recreates
# a portion of the Firefox 'View' menu.  Only 'File-Quit' and
# 'View-Toolbars-Bookmarks Toolbar-Always Show' do anything, the rest
# of the menu entries are just for show.
from ticklish_ui import *

app = Application('Application Menus')

menu = MenuSpecification()
menu('File', 'Edit', 'View')
menu.File('Quit')
menu.Edit('Cut', 'Copy', 'Paste')
menu.View('Toolbars', 'Sidebars')
menu.View.Toolbars('Bookmarks Toolbar', 'Customize')

# Since 'Bookmarks Toolbar' contains a space we use indexing instead
# of the dot operator.
menu.View.Toolbars['Bookmarks Toolbar']('Always Show', 'Never Show')
menu.View.Sidebars('Bookmarks', 'History')

app.menubar(menu)

# Bind actions to menu items by specifying the menu-item combo and
# providing a callback.
app.menu_command('File-Quit', lambda app: app.destroy())

# Nested menus work the same way, just specify the full 'path' to the
# menu item you want to bind.
app.menu_command(
    'View-Toolbars-Bookmarks Toolbar-Always Show',
    lambda app: print('Always showing bookmarks toolbar.')
)

app.mainloop()
