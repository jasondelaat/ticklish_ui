# Demonstrates the Notebook widget.

from ticklish_ui import *

def make_frame(n):
    return Frame(
        # .row1
        [Text(f'Some text in tab {n}')]
    ).options(name=f'tab{n}')

app = Application(
    'Notebook Example',
    # .row1
    [Notebook(
        {'Tab 1' : make_frame(1),
         'Tab 2' : make_frame(2),
         'Tab 3' : make_frame(3),
         'Tab 4' : Frame([Label('We can also define tabs inline.')])
        }
    ).options(name='notebook')]
)

t5 = Frame([Label('Or add them later')])

nb = app.nametowidget('.row1.notebook')
nb.add(t5.create_widget(nb), text='Tab 5')

app.mainloop()
