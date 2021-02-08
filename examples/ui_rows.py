# This example shows how widgets are packed into an application in rows.
from ticklish_ui import *

Application(
    'Application Rows',

    # .row1
    [Label('This is the first row.')],

    # .row2
    [Label('This is the second row.'), Label('Still the second row.')],

    # .row3
    [Label('Third row'), CloseButton('Quit')],
).mainloop()
