from ticklish_ui import *

app = Application(
    'Theme Browser',
    # .row1
    [Label('Select a theme:')],

    # .row2
    [],

    # .row3
    [CloseButton('Quit')],
)

# Since we need access to the app.style object to get the available
# theme names, the Listbox is created after the Application and
# inserted into row 2 with an explicit call to create_widget().
(Listbox(app.style.theme_names())
 .options(name='theme_selector')
 .create_widget(app.nametowidget('.row2'))
)

def change_theme(e):
    toplevel = e.widget.winfo_toplevel()
    theme = e.widget.focus()
    toplevel.style.theme_use(theme)

click = app.get_event_stream('<Button-1>')

(click
 .by_name('theme_selector')
 .map(change_theme)
)

app.mainloop()
