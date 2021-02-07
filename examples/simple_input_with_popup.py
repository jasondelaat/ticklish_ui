from ticklish_ui import *

app = Application(
    'Example GUI',

    # .row1
    [Label('Enter some text below:')], 

    # .row2
    [Entry().options(name='user_text')],

    # .row3
    [Button('OK').options(name='ok'), CloseButton('Quit')],
)

def show_text(event):
    text = app.nametowidget('.row2.user_text').get()
    return Toplevel(
        'Your Text',

        # .row1
        [Label(text)],

        # .row2
        [CloseButton('OK')],
    )

(app.get_event_stream('<ButtonRelease-1>')
 .by_name('ok')
 .map(show_text)
)

app.mainloop()
