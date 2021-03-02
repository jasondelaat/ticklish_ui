# Demonstrates the Separator widget.

from ticklish_ui import *

app = Application(
    'Separator Example',
    # .row1
    [Label('Label 1'), Separator(), Label('Label 2')],
    # .row2
    [Separator('horizontal')],
    # .row3
    [Label('Label 1'), Separator(), Label('Label 2')],
    
)

app.mainloop()
