from declare_ui import *

app = Application(
    'Theme Browser',
    # .row1
    [Label('Select a theme:')],

    # .row2
    [],

    # .row3
    [CloseButton('Quit')],
)

(Listbox(app.style.theme_names())
 .options(name='theme_selector')
 (app.nametowidget('.row2'))
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
